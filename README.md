# Défi Reinforcement Learning (RL)

## Description  
Ce projet explore différentes techniques d’apprentissage par renforcement (RL) telles que l’itération par valeurs, le Q-learning et le Deep Q-learning. L'objectif principal est de développer des agents capables de naviguer efficacement dans des environnements variés comme GridWorld et Pac-Man.

## Contenu du Projet  

### 1. **Itération par valeurs**  
- Implémentation d'un agent dans `valueIterationAgents.py` permettant de :  
  - Calculer les valeurs des états via l'itération par valeurs.  
  - Sélectionner les meilleures actions à partir des valeurs d'état.  
  - Évaluer des politiques optimales, par exemple pour traverser des ponts risqués ou privilégier des sorties proches.  
- Ajustement des paramètres tels que le facteur de dépréciation (`discount`) et le bruit (`noise`) pour affiner les politiques.  

### 2. **Q-learning**  
- Développement d'un agent dans `qlearningAgents.py` capable d'apprendre par essais et erreurs :  
  - Calcul et mise à jour des Q-values.  
  - Gestion du compromis exploration/exploitation avec une stratégie ε-Greedy.  
- Validation sur des grilles (`BridgeGrid`, `DiscountGrid`) avec des épisodes contrôlés.

### 3. **Application Pac-Man**  
- Utilisation de `PacmanQAgent` pour entraîner Pac-Man :  
  - Entraînement sur 2000 épisodes suivi de tests avec un objectif de taux de victoire supérieur à 80 %.  
  - Expérimentation sur des grilles simples (`smallGrid`) et complexes (`mediumGrid`) avec ajustement des hyperparamètres.  

### 4. **Q-learning Approximatif**  
- Implémentation d'un agent utilisant des fonctions caractéristiques (`featureExtractors.py`) :  
  - Extraction de caractéristiques avec `IdentityExtractor` et `SimpleExtractor`.  
  - Optimisation des politiques sur des grilles plus grandes (`mediumClassic`).  
- Ajout de nouvelles caractéristiques encourageant Pac-Man à manger des fantômes effrayés.  

### 5. **Deep Q-learning**  
- Approche avec un réseau de neurones profond pour approximer les Q-values :  
  - Structure avec couches convolutives et entièrement connectées.  
  - Optimisation des hyperparamètres (`learning rate`, `discount factor`, `batch size`).  
- Gain de performance et réduction du temps de calcul sur des environnements complexes.  
- Analyse des comportements problématiques de Pac-Man en fin de partie.  

## Instructions d'Exécution  
### GridWorld  
```bash
python gridworld.py -a value -i 100 -g BridgeGrid --discount 0.9 --noise 0.01
python gridworld.py -a q -k 100
```
### Pacman 
```bash
python pacman.py -p PacmanQAgent -x 2000 -n 2010 -l smallGrid
python pacman.py -p ApproximateQAgent -x 50 -n 60 -l mediumClassic
```

# Auteurs 
Nicolas Melaerts
Manu Mathey-Prévot

