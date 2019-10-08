import requests 

site2 = "http://pheweb.sph.umich.edu/api/manhattan/pheno/782.6.json"
# response = ur.urlopen(site)
# data3 = response.read()
# print(data3)
resp = requests.get(site2)
data3 = resp.json()
print(data3)