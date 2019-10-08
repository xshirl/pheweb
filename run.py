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



associations = []
genes_array = []

for url in sites:
    try:
        print(url)
        response = requests.get(url)
        json_data = response.json()
        genes = []
        unique_genes = []
        for variant in json_data["unbinned_variants"]:
            gene = variant["nearest_genes"]
            genes.append(gene)
        for gene in genes:
            if gene not in unique_genes:
                unique_genes.append(gene)
        genes_array.append(unique_genes)
    except:
        pass


genes = dict(zip(phenotypes, genes_array))

f = open("associations.json", "w")
f.write(json.dumps(genes))
f.close()
   




