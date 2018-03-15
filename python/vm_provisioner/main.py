# A Python script for provisioning VM's
# A little imractical as it requires the subprocess module as a pre-req,
# and honestly this should just be all written in bash.
# Class structure is purely for modularity/clarity.
#
# Just provide an ordered iterable of functions to the setup() function
# Each function should return a boolean based on whether or not it succeeded
# The functions will be run in order, and the script will fall through if any fail
#
# With minor modification, one could add a "optional" flag to the functions, allowing the
# script to continue on a failed function

import subprocess
import os
import time

def run_command(command, check=subprocess.check_call):
    spl = command.split(" ")
    output = check(spl)

    return output

def get_environment_var(key, prompt_if_missing=False):
    if key in os.environ:
        return os.environ[key]
    elif prompt_if_missing:
        return raw_input("Please provide a value for '{}'".format(key))

    return ''

class Git():
    @staticmethod
    def get_folder_name_from_url(url):
        return url.split(".git")[0].split("/")[-1]

    @staticmethod
    def generate_ssh_keys():
        keygen_command = "ssh-keygen -t rsa -b 4096 -C {email} -N  -f ~/.ssh/id_rsa -q"

        email = get_environment_var('GIT_EMAIL')

        if email == '':
            email = raw_input('Please provide an email for your ssh keys (optional): ')

        creation_succeeded = run_command(keygen_command.format(email=email)) == 0

        if creation_succeeded:
            cat_command = "cat ~/.ssh/id_rsa.pub"
            print("Your public rsa key will be printed into console, please visit https://github.com/settings/keys and add it to your account")
            print("")
            print(run_command(cat_command, subprocess.check_output))
            print("")

            raw_input("Press any key to continue.. (don't continue until you've added your key, everything after this relies on this step)")
            return True

        print("FAILURE: Unable to generate SSH keys")
        return False

    def setup_repository(self):
        mkdir_command = "mkdir ~/Code"
        repository = get_environment_var("REPO_SSH_URL")
        folder_name = self.get_folder_name_from_url(repository)
        clone_command = "git clone {} ~/Code/{}".format(repository, folder_name)

        run_command(mkdir_command)

        clone_succeeded = run_command(clone_command) == 0

        if clone_succeeded:
            return True

        print("FAILURE: Unable to clone the GitHub project")
        return False

class AWS():
    @staticmethod
    def is_installed():
        check = subprocess.Popen(('aws', 'help'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        check.communicate()
        return check.returncode == 0

    def configure(self):
        if self.is_installed():
            command = "aws configure --profile gazelle".split(" ")

            access_key_id = get_environment_var('AWS_ACCESS_KEY_ID', True)
            secret_access_key = get_environment_var('AWS_SECRET_ACCESS_KEY', True)
            default_region_name = get_environment_var('AWS_DEFAULT_REGION_NAME', True)
            default_output_format = get_environment_var('AWS_DEFAULT_OUTPUT_FORMAT', True)

            configuration_input = [
                access_key_id,
                secret_access_key,
                default_region_name,
                default_output_format
            ]

            process = subprocess.Popen(command, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, bufsize=1)
            for config in configuration_input:
                process.stdin.write("{}\n".format(config))
                # There's a slight delay in the CLI between prompts - not ideal but it works
                time.sleep(0.5)

            _outs, _errs = process.communicate()

            return process.returncode == 0

        print("FAILURE: awscli is not properly installed")
        return False

def setup(commands):
    for command in commands:
        if not command():
            print("Failed on '{}' - script halting".format(command.__name__))
            return False
    return True

if __name__ == "__main__":

    vm_setup = [
        Git().generate_ssh_keys,
        Git().setup_repository,
        AWS().configure
    ]
    vagrant_setup = [ AWS().configure ]

    if setup(vm_setup):
        print("Setup script complete.")
    else:
        print("Script failure.")

