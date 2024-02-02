from detoxify import Detoxify

# Charger le modèle Detoxify

toxicity_model = Detoxify('multilingual')

def analyze_toxicity(comments):
    toxicity_scores = toxicity_model.predict(comments)
    return toxicity_scores['toxicity']