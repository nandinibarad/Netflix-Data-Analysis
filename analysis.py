import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


# Folder Paths

base_path = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(base_path, "data", "netflix_titles.csv")
charts_path = os.path.join(base_path, "charts")

# Create charts folder if not exists
os.makedirs(charts_path, exist_ok=True)

# Load Dataset

df = pd.read_csv(file_path)

# Fill missing text values
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].fillna("Unknown")

# Style
sns.set_style("whitegrid")


# 1. Movies vs Shows

if 'type' in df.columns:
    plt.figure(figsize=(7,5))
    sns.countplot(x='type', data=df)
    plt.title("Movies vs Shows")
    plt.tight_layout()
    plt.savefig(os.path.join(charts_path, "movies_vs_shows.png"), dpi=300)
    plt.show()


# 2. IMDB Score Distribution

if 'imdb_score' in df.columns:
    plt.figure(figsize=(8,5))
    df['imdb_score'].dropna().hist(bins=10)
    plt.title("IMDB Score Distribution")
    plt.xlabel("IMDB Score")
    plt.tight_layout()
    plt.savefig(os.path.join(charts_path, "imdb_score_distribution.png"), dpi=300)
    plt.show()


# 3. Release Year Count

if 'release_year' in df.columns:
    plt.figure(figsize=(10,5))
    df['release_year'].value_counts().head(10).plot(kind='bar')
    plt.title("Top Release Years")
    plt.tight_layout()
    plt.savefig(os.path.join(charts_path, "release_years.png"), dpi=300)
    plt.show()

print("Project Run Successfully ✅")
