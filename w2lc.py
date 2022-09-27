import yaml
import os
from scipy.spatial.transform import Rotation as R

path = os.getcwd()
os.makedirs(os.path.join(path, "out"), exist_ok=True)

for root, dirs, files in os.walk(path):
    for fn in files:
        if fn.endswith(("w2l.yml")):
            fp = os.path.join(root, fn)
            fn = fn.replace(".yml","")

            with open(fp, 'r') as file:
                data = yaml.safe_load(file)
                if "entities" in data["templates"][fn]:
                    for i in data["templates"][fn]["entities"]:
                        if "transform" in i and "template" in i:
                            pos = i["transform"]["pos"]
                            rot = i["transform"]["rot"]
                            scale = i["transform"]["scale"]
                            ent = i["template"]
                            with open(ent.replace("/", "-") + ".csv","a+") as f:
                                f.write("" + str(pos[0]) + " " + str(pos[1]) + " " + str(pos[2]) + " " + str(round(rot[0]), 2) + " " + str(round(rot[1]), 2) + " " + str(round(rot[2]), 2) + " " + str((sum(scale) / len(scale))) + "\n")
                            
                if "BlockData" in data["templates"][fn]["sectorData"]:
                    for i in data["templates"][fn]["sectorData"]["BlockData"]:
                        if "meshIndex" in data["templates"][fn]["sectorData"]["BlockData"][i] and "position" in data["templates"][fn]["sectorData"]["BlockData"][i] and "rotationMatrix" in data["templates"][fn]["sectorData"]["BlockData"][i]:
                            posX = data["templates"][fn]["sectorData"]["BlockData"][i]["position"]["X"]
                            posY = data["templates"][fn]["sectorData"]["BlockData"][i]["position"]["Y"]
                            posZ = data["templates"][fn]["sectorData"]["BlockData"][i]["position"]["Z"]
                            rot = data["templates"][fn]["sectorData"]["BlockData"][i]["rotationMatrix"]
                            mesh = data["templates"][fn]["sectorData"]["Resources"][data["templates"][fn]["sectorData"]["BlockData"][i]["meshIndex"]]["pathHash"]

                            r = R.from_matrix([[rot["ax"], rot["ay"], rot["az"]], [rot["bx"], rot["by"], rot["bz"]], [rot["cx"], rot["cy"], rot["cz"]]])
                            r = r.as_euler('xyz', degrees=True)

                            with open(os.path.join(os.getcwd(), "out", mesh.replace("/", "-")) + ".csv","a+") as f:
                                f.write("" + str(posX) + " " + str(posY) + " " + str(posZ) + " " + str(round(r[0], 2)) + " " + str(round(r[1], 2)) + " " + str(round(r[2], 2)) + " " + "1" + "\n")