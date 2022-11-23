import os

url_geo = "https://static.data.gouv.fr/resources/contours-des-communes-de-france-simplifie-avec-regions-et-departement-doutre-mer-rapproches/20220219-095144/a-com2022.json"
path_target_geo = os.path.join(os.path.dirname(os.path.realpath(__file__)),"..","data","commf2020.json")

url_db="https://data.enedis.fr/explore/dataset/consommation-annuelle-residentielle-par-adresse/download/?format=csv&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B"
path_target_db = os.path.join(os.path.dirname(os.path.realpath(__file__)),"..","data","conso.csv")
