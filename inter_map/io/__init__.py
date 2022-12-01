import os

url_geo = "https://www.data.gouv.fr/fr/datasets/r/90b9341a-e1f7-4d75-a73c-bbc010c7feeb"
path_target_geo = os.path.join(os.path.dirname(os.path.realpath(__file__)),"..","data","departements.json")

url_db="https://data.enedis.fr/explore/dataset/consommation-annuelle-residentielle-par-adresse/download/?format=csv&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B"
path_target_db = os.path.join(os.path.dirname(os.path.realpath(__file__)),"..","data","conso.csv")
