import pandas as pd
from cleaning import clean_comment
from analysis import analyze_toxicity
from loading import load_data_to_mongodb

def process_data():
    # Load data from CSV
    csv_file_path = 'posts_data.csv'
    df = pd.read_csv(csv_file_path)

    # # Clean comments
    df['cleaned_comments'] = df['comments'].apply(clean_comment)
    df['cleaned_comments'] = df['cleaned_comments'].apply(lambda comments: ' '.join(map(str, comments)))
    df['cleaned_comments']=df['cleaned_comments'].astype(str)
    # # Analyze toxicity
    print('starting analysis of toxicity...')
    df['toxicity_scores'] = df['cleaned_comments'].apply(analyze_toxicity)

    return df.to_dict(orient="records")
