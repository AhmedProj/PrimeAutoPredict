# PrimeAutoPredict

Project devoted to the developement of a deep learning model to predict the total claims payments by the insurance company. The project includes as well its deployment for production.


The goal is to compute a yearly third party premium (material + bodily injury) for the 36,311 contracts of the
pricing dataset, for 2011.

## Démarche
To achieve this, we'll develop four models:

1- Model for material cost estimation.

2- Model for bodily injury cost estimation.

3- Model for material incident frequency prediction.

4- Model for bodily injury occurrence frequency prediction.

## Prérequis
La présence de [Python](https://www.python.org/) sur la machine est requise.

## Configuration de l'Environnement

Après avoir cloné ce projet, vous devez exécuter les commandes suivantes :

```bash
$ cd PrimeAutoPredict
$ pip install -r requirements.txt
```
## Dossiers

1. **Creation_Dataset**
   - `nomdufichier.csv`: fichier csv contenant nos données
     
2. **Data_Exploration**
   - `nomdufihcier.ipynb` : Notebook pour l'exploration des données.
   - `nomdufihcier.ipynb` :  Notebook pour les analyses statistiques des données.

3. **Data_Preprocessing**
   - `nomdufihcier.ipynb`: Notebook pour le prétraitement des données.

## Contributors
