from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
import re
import string

stop_words = set(stopwords.words("french"))
stemmer = SnowballStemmer("french")

def clean_comment(text):
    # Suppression des émoticônes
    text = re.sub(r'[\U00010000-\U0010ffff]', '', text)
    # Enlève la ponctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    # Enlève les chiffres
    text = ''.join([i for i in text if not i.isdigit()])
    # Tokenisation
    words = word_tokenize(text, language='french')
    # Suppression des stopwords
    filtered_words = [word.lower() for word in words if word.lower() not in stop_words]
    # Stemming (racinisation)
    stemmed_words = [stemmer.stem(word) for word in filtered_words]
    # Reconstruction du texte nettoyé
    cleaned_comment = " ".join(stemmed_words)
    
    
    return cleaned_comment