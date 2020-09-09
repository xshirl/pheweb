import json
import requests

# data.json from http://pheweb.sph.umich.edu/api/top_hits.json
with open('data.json') as o:
    data = json.loads(o.read())
# converts data.json to json object


# phenocodes gives the codes of the phenotype
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
# creates array of urls to request from

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
            # appends nearest gene to genes array
        for gene in genes:
            if gene not in unique_genes:
                unique_genes.append(gene)
        genes_array.append(unique_genes)
        # creates array of unique genes
    except:
        pass


# creates dictionary with phenotype as key and array of nearest genes as value
genes = dict(zip(phenotypes, genes_array))

# creates json file of associated phenotypes and genes
f = open("associations.json", "w")
f.write(json.dumps(genes))
f.close()

# converts to gmt file
with open("associations.gmt", "w") as f:
    with open("associations.json") as o:
        a = json.loads(o.read())
        for key, value in a.items():
            f.write(key + "\t\t")
            for v in value:
                f.write(v + " ")
            f.write("\n")
