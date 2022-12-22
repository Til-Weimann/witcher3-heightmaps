import os

path = os.getcwd()

for f in os.listdir(path):
    if f.endswith(".txt"):
        with open(os.path.join(path, f)) as data:
            treetype = "none"
            c = 0
            out = ""
            for line in data.readlines():
                if "Treetype" in line:
                    p = os.path.join(path, "o", treetype.replace("/","\\") + ".txt")
                    os.makedirs(p.rsplit("\\",1)[0], exist_ok=True)
                    with open(p,"a+") as outfile:
                        outfile.write(out)
                        out = ""
                    treetype = line.split(" ")[-1].split("\\")[-1].replace(".srt","").replace("\n","")
                elif "PositionX (Float) : " in line:
                    c = 6
                if c > 0:
                    out += line.replace(" ","")
                    c -= 1
            with open(os.path.join(path, "o", treetype + ".txt"),"a+") as outfile:
                outfile.write(out)
