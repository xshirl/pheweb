import json
import requests


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


url = "http://pheweb.sph.umich.edu/pheno/"

sites = []
for code in phenocodes:
    site = url + str(code)
    sites.append(site)


all_genes = {}

for url in sites:
    try:
        response = requests.get(url)
        json_data = response.json()
        for variant in json_data["unbinned_variants"]:
            gene = variant["nearest_genes"]
            genes.append(gene)
            print(genes)
        for phenotype in phenotypes:
            all_genes["phenotype"] = phenotype
            all_genes["genes"] = genes
    except Exception:
        pass

print(all_genes)

with open('data2.json') as f:
    data2 = json.loads(f.read())
    
# genes = []
# unique_genes = []
# for variant in data2["unbinned_variants"]:
#     gene = variant["nearest_genes"]
#     genes.append(gene)

# for gene in genes:
#     if gene not in unique_genes:
#         unique_genes.append(gene)

