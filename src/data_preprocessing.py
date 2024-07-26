# Data Preprocessing Script

import pandas as pd

def load_data(true_path, false_path):
    true_df = pd.read_csv(true_path)
    false_df = pd.read_csv(false_path)
    true_df['label'] = 1
    false_df['label'] = 0
    return pd.concat([true_df, false_df], ignore_index=True)

def clean_data(df):
    # Add your cleaning steps here (e.g., remove nulls, duplicates)
    df.dropna(inplace=True)
    return df

def save_processed_data(df, path):
    df.to_csv(path, index=False)

if __name__ == "__main__":
    true_path = 'data/raw/True.csv'
    false_path = 'data/raw/Fake.csv'
    processed_path = 'data/processed/combined.csv'
    
    df = load_data(true_path, false_path)
    df = clean_data(df)
    save_processed_data(df, processed_path)
