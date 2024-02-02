## Analyse de Commentaires avec FastAPI

# Analyse de Commentaires avec FastAPI

## Aperçu

L'application d'Analyse de Commentaires avec FastAPI permet d'effectuer les tâches suivantes :

1. **Nettoyer les Commentaires :** L'application offre une fonctionnalité pour nettoyer les commentaires en supprimant tout élément indésirable ou mise en forme.

2. **Analyse de Toxicité :** Elle utilise le modèle Detoxify (https://github.com/unitaryai/detoxify) pour analyser la toxicité des commentaires.

3. **Chargement des Données dans MongoDB :** Les commentaires nettoyés et analysés sont chargés dans une base de données MongoDB pour un stockage et une récupération ultérieurs.

4. **Conteneurisation avec Docker :** L'application FastAPI est conteneurisée avec Docker pour une déployment facile et une reproductibilité.

## Fonctionnalités

- **Nettoyer les Commentaires :** Une route est disponible pour nettoyer les commentaires, en supprimant tout élément indésirable ou formatage.

- **Analyse de Toxicité :** Le modèle Detoxify est utilisé pour analyser la toxicité des commentaires, fournissant des informations sur un contenu potentiellement nocif.

- **Intégration MongoDB :** Les commentaires nettoyés et analysés sont stockés dans une base de données MongoDB pour un stockage persistant.

- **Framework FastAPI :** Exploitation du framework FastAPI pour un développement d'API efficace, rapide et sûr.

- **Conteneurisation Docker :** L'application est conteneurisée avec Docker, assurant une cohérence sur différentes plateformes.

## Prérequis

- Python 3.x
- FastAPI
- Detoxify
- MongoDB
- Docker

## Installation

### 1. Cloner le dépôt :

```bash
git clone https://github.com/votre_nom/fastapi-comment-analysis.git
cd fastapi-comment-analysis


2. Installer les dépendances :
bash
Copy code
pip install -r requirements.txt
3. Configurer MongoDB :
Assurez-vous que MongoDB est installé et en cours d'exécution. Mettez à jour les détails de connexion MongoDB dans l'application FastAPI ou utilisez des variables d'environnement.

Utilisation

Exécuter l'application FastAPI :
bash
Copy code
uvicorn main:app --reload
Accéder à la documentation FastAPI :
Ouvrez votre navigateur et accédez à http://127.0.0.1:8000/docs pour interagir avec l'API en utilisant Swagger.
Nettoyer les Commentaires :
Utilisez le point de terminaison API fourni pour nettoyer les commentaires.
Analyse de Toxicité :
Utilisez le modèle Detoxify pour l'analyse de toxicité via la route API dédiée.
Chargement des Données dans MongoDB :
Les commentaires nettoyés et analysés sont automatiquement chargés dans la base de données MongoDB.
Conteneurisation avec Docker

Construire l'image Docker :
bash
Copy code
docker build -t fastapi-comment-analysis .
Exécuter le conteneur Docker :
bash
Copy code
docker run -p 8000:8000 fastapi-comment-analysis
L'application FastAPI sera accessible à l'adresse http://127.0.0.1:8000.
