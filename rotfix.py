import os

path = os.getcwd()

for root, dirs, files in os.walk(path):
    for name in files:
        if name.endswith(("w2l.yml")):
            state = -1
            lines = ""
            filename = os.path.join(root, name)

            with open(filename) as file:
                for line in file:
                    if "rotationMatrix:" in line:
                        state = 0
                    elif state == 4:
                        line = line.replace("by:", "bx:")
                    elif state == 5:
                        line = line.replace("bz:", "by:")
                    elif state == 6:
                        line = line.replace("by:", "bz:")
                    elif state == 7:
                        line = line.replace("cz:", "cx:")
                        state = -1

                    if state >= 0:
                        state += 1

                    lines += line

            with open(filename, 'w') as file:
                        file.write(lines)
                        file.close()