import json
import requests
import urllib.request as ur

with open('data.json') as o:
    data = json.loads(o.read())


f = open("pheweb.gmt", "w")
for json_data in data:
    f.write(str(json_data["phenostring"]) + '\t\t' + str(json_data["nearest_genes"]) + "\n")


phenocodes = []
phenotypes = []

for json_data in data:
    phenocodes.append(json_data["phenocode"])
    phenotypes.append(json_data["phenostring"])


url = "http://pheweb.sph.umich.edu/api/manhattan/pheno/{}.json"

sites = []
for code in phenocodes:
    site = url.format(code)
    sites.append(site)

site2 = "http://pheweb.sph.umich.edu/api/manhattan/pheno/782.6.json"
# response = ur.urlopen(site)
# data3 = response.read()
# print(data3)
# resp = requests.get(site2)
# data3 = resp.json()
# genes = []
# for variant in data3["unbinned_variants"]:
#     gene = variant["nearest_genes"]
#     genes.append(gene)
# print(genes)

all_genes = {}
genes = []
unique_genes = []
associations = []
for url in sites:
    try:
        print(url)
        response = requests.get(url)
        json_data = response.json()
        for variant in json_data["unbinned_variants"]:
            gene = variant["nearest_genes"]
            genes.append(gene)
        for gene in genes:
            if gene not in unique_genes:
                unique_genes.append(gene)
        for phenotype in phenotypes:
            all_genes["phenotype"] = phenotype
            all_genes["genes"] = unique_genes
        associations.append(all_genes)
        f = open("associations.json", "w")
        f.write(json.dumps(associations))
        f.close()
    except Exception:
        pass

# print(all_genes)

# with open('data2.json') as f:
#     data2 = json.loads(f.read())
    
# genes = []
# unique_genes = []
# for variant in data2["unbinned_variants"]:
#     gene = variant["nearest_genes"]
#     genes.append(gene)


