import json
with open("associations.gmt", "w") as f:
    with open("associations.json") as o:
        a = json.loads(o.read())
        for i in a:
            f.write(i["phenotype"] + "/t/t")
        for j in i["genes"]:
            f.write(j + " ")
            
    