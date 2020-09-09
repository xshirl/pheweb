# PheWeb
http://pheweb.sph.umich.edu/top_hits

This project aims to create a gmt file containing the phenotypes of diseases and the associated nearest genes of the disease.

API: http://pheweb.sph.umich.edu/api/manhattan/pheno/<phenocode>.json

To run:
```
python run.py
```
1. Goes through all the API requests for all the phenotypes.
2. Creates a genes array with all the nearest genes for each disease phenotype.
3. Creates a json file associating phenotypes with genes.
4. Creates a gmt file of phenotypes and associated nearest genes.