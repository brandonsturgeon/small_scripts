# Grep Copy

look_for = "110"

opened_file = open("ips.txt", "rb")
read_file = opened_file.read().split("\n")
opened_file.close()

for x in read_file:
    if look_for in x:
        print x

