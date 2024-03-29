import os

cwd = os.getcwd()
wcc_path = 'G:\\Witcher 3\\_modTools\\Witcher 3 Mod Tools\\bin\\x64\\'
w3c_path = 'D:\\SteamLibrary2\\steamapps\\common\\The Witcher 3\\content\\'

os.makedirs(os.path.join(cwd, "fbx"), exist_ok=True)

ucdict = {}

for root, dirs, files in os.walk(os.path.join(cwd, "csv")):
    for fn in files:
        if fn.endswith(("w2mesh.csv")):
            os.makedirs(os.path.join(cwd, "tmpdir"), exist_ok=True)
            fp = os.path.join(root, fn).replace(".csv","")
            target_path = root.replace(os.path.join(cwd, "csv"),"")[1:]
            os.chdir(wcc_path)
            if target_path not in ucdict:
                print("Uncooking " + target_path)
                cmd_uc = 'wcc_lite.exe uncook -indir="' + w3c_path.replace('\\','\\\\') + '" -outdir="' + os.path.join(cwd, "tmpdir").replace('\\','\\\\') + '" -targetdir=' + target_path + ' -imgfmt="tga"'
                os.system(cmd_uc)
                ucdict[target_path] = True
            print("Exporting " + fn.replace(".csv",""))
            os.makedirs(os.path.join(cwd, "fbx", target_path), exist_ok=True)
            cmd_ep = 'wcc_lite.exe export -depot="' + os.path.join(cwd, "tmpdir") + '" -file=' + target_path + "\\" + fn.replace(".csv","") + ' -out="' + os.path.join(cwd, "fbx", target_path, fn.replace("w2mesh.csv", "fbx")) + '"'
            os.system(cmd_ep)
            if not os.path.exists(os.path.join(cwd, "fbx", target_path, fn.replace("w2mesh.csv", "fbx"))):
                print("Error")
                with open(os.path.join(cwd, "missing.txt"),"a+") as f: # + cmd_uc + "\n" + cmd_ep + "\n"
                    f.write("[F]  " + os.path.join(target_path, fn.replace(".csv", "")) + "\n")
                    f.close()
            else:
                with open(os.path.join(cwd, "missing.txt"),"a+") as f:
                    f.write("[ ]  " + os.path.join(target_path, fn.replace(".csv", "")) + "\n")
                    f.close()
