import json
with open("associations.gmt", "w") as f:
    with open("associations.json") as o:
        a = json.loads(o.read())
        for key, value in a.items():
            f.write(key + "\t\t")
            for v in value:
                f.write(v + " ")
            f.write("\n")
        # print(a)
        # for i in a:
        #     f.write(i["phenotype"] + "\t\t")
        # for j in i["genes"]:
        #     f.write(j + " ")
            
    