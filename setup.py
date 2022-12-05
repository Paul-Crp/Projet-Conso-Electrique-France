from setuptools import setup
from Prediction import __version__ as current_version

setup(
    name="potemodule",
    version=current_version,
    description="Prediction of electricity consumption in France for 8/12/2022",
    url="https://github.com/Paul-Crp/Projet-Conso-Electrique-France.git",
    author="Crespin Paul, Lamrini Oualid, Renoir Thamara, Sinibaldi Emma",
    author_email="paul.crespin@etu.umontpellier.fr, oualid.lamrini@etu.umontpellier.fr, thamara.renoir@etu.umontpellier.fr, emma.sinibaldi.@etu.umontpellier.fr",
    license="MIT",
    packages=["potemodule", "potemodule.intermap", "potemodule.Prediction"],
    zip_safe=False,
)
