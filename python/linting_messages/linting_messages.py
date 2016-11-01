# -*- coding: utf-8 -*-
import subprocess


class CheckLinting():
    def __init__(self):
        self.ESLINT_COMMAND = "eslint ."

        self.lint_errors = {}

        print("Initialized")

        self.main()

    def main(self):
        output = self.getLintingOutput()
        self.parseLintingOutput(output)

        for k, v in self.lint_errors.iteritems():
            print("{}//{}".format(k, v))

    def formatError(self, error):
        split = error.split("  ")
        error_info = [x for x in split if x != '']
        err_str = "{} // {}".format(error_info[2], error_info[3])

        return err_str

    def addError(self, error):
        self.lint_errors[error] = self.lint_errors.get(error, 0) + 1

    def getLintingOutput(self):
        print("Getting linting output... ")
        command = self.ESLINT_COMMAND.split(" ")

        p = subprocess.Popen(command, stdout=subprocess.PIPE)

        (output, err) = p.communicate()

        p.wait()

        print("Finished getting output")
        return output

    def lineIsError(self, line):
        if line is None:
            return False

        elif line == "":
            return False

        elif line[0] == "/":
            return False

        elif "✖" in line:
            return False

        return True

    def parseLintingOutput(self, output):
        # Split the output and shave off the first few lines
        output = output.split("\n")[2:]

        for line in output:
            if self.lineIsError(line):
                self.addError(self.formatError(line))


if __name__ == "__main__":
    CheckLinting()
