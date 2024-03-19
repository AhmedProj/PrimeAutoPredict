# PrimeAutoPredict

Projet dédié au développement d'un modèle Machine Learning pour prédire le total des paiements de sinistres par la compagnie d'assurance. Le projet comprend également son déploiement pour la production.

L'objectif premier était de calculer une prime annuelle tiers (matériels + dommages corporels) pour les 36 311 contrats du jeu de données de tarification, pour 2011.

Cependant nous nous concentrerons plutôt sur la prédiction la Prime Annuelle Materielle

## Démarche
Pour y parvenir, nous développerons quatre modèles :

1- Modèle pour l'estimation du coût matériel.

2- Modèle pour l'estimation du coût des dommages corporels.

3- Modèle pour la prédiction de la fréquence des incidents matériels.

4- Modèle pour la prédiction de la fréquence des occurrences de dommages corporels.


Puis nous calculons la Prime predite  = Fréquence predite * Coût moyen​ predit ​


## Prérequis
La présence de [Python](https://www.python.org/) sur la machine est requise.

## Configuration de l'Environnement

Après avoir cloné ce projet  vous devez exécuter les commandes suivantes pour pouvoir tester les notebooks:

```bash
$ cd PrimeAutoPredict
$ pip install -r requirements.txt
```
ET pour visuliser l'interface graphique crée :
```bash
$ cd Application
$ streamlit run appli.py
```

### Image Docker

En se plaçanat dans le dossier Application, vous pouvez créer l'image docker de notre application et lancer un conteneur par la suite pour pouvoir visualiser le site via le port 8501.
```bash
$ docker build -t application .   
$ docker run --name site -d -p 8501:8501 application
```
## Dossiers

1. **Application**
   - Dossier permettant de déployer notre solution 
     
2. **CNN**
   - `cnn-insurance.ipynb`: Notebook pour entrainer un model CNN pour prédire le niveaux de dommage dans images de voiture
   - `model_functions.py`: fonctions utilisées pour faire marcher CNN
   - `test-destructed.jpg`: image hors dataset pour tester le model
     
3. **Notebooks**

 * **Data_Exploration**
      - `Statistiques_Initiales.ipynb`: Notebook pour les analyses statistiques des données.
 * **Data Preprocessing**
   - `Data_preprocessing.ipynb` : Notebook pour le prétraitement des données.
   - `Etude_Frequence_corporels.ipynb` : Notebook pour l'étude de la fréquence des dommages corporels.
   - `Etude_Frequence_materiel.ipynb` : Notebook pour l'étude de la fréquence des incidents matériels.
   - `Predicting_bodily_claims_costs.ipynb` : Notebook pour prédire les coûts des dommages corporels.
   - `Predicting_material_claims_costs.ipynb` : Notebook pour prédire les coûts matériels.

4. **Models**
   - `model_couts_corporels.joblib`: Notebook pour prédire le cout corporelle sous format Joblib pour mise en production.
   - `model_couts_materiels.joblib`: .Notebook pour prédire le cout materielle sous format Joblib pour mise en production.
   - `model_frequence_corporel.joblib`:Notebook pour prédire la fréquence corporelle sous format Joblib pour mise en production.
   - `model_frequence_materiell.joblib`: Notebook pour prédire la fréquence materielle sous format Joblib pour mise en production.
   - `Code_final_prime.ipynb`: Ce notebook réunit nos meilleurs models permet de calculer la prime prime annuelle à prédire destinée à couvrir les dommages matériel


5. **data**
   - `training.csv`: Dataset.
   - `training_clean.csv`: Dataset nettoyé.
     
## Contributors

*Boughanja Yosra
*Bitton Yona
*Haddad Nesrine
*Ouassou Ahmed
*Solis Lerma Daniel
