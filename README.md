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
     
1. **Data_Exploration**
   - `Data_Exploration.ipynb` : Notebook pour l'exploration des données.
   - `Statistical_Analysis.ipynb` :  Notebook pour les analyses statistiques des données.
     
2. **Data_Preprocessing**
   - `Data_Preprocessing.ipynb` : Notebook pour le prétraitement des données.

3. **Recherche_modeles**
   - `README.md`: explication du dossier
   - `Frequence_Corporelle_classification.ipynb`: Notebook pour prédire la fréquence corporelle.
   - `Frequence_Materielle_classification.ipynb`: Notebook pour prédire la fréquence materielle.

5. **Models**
   - `Frequence_Corporelle.ipynb`: Notebook pour prédire la fréquence corporelle.
   - `Frequence_Materielle.ipynb`: Notebook pour prédire la fréquence materielle.
   - `Cout_Corporel.ipynb`: Notebook pour prédire le cout corporelle.
   - `Cout_Materiel.ipynb`: Notebook pour prédire le cout materielle.

6. **Prediction_Calcul_Prime**
   - `Prime_Modeling.ipynb`: Notebook final pour calculer la prime à prédire.
     
7. **CNN**
   - `nomdufichier.ipynb`: Notebook pour ...

8. **csv**
   - `training.csv`: Dataset.
   - `training_clean.csv`: Dataset noettoyé.
   -  `pricing.csv`
     
## Contributors

