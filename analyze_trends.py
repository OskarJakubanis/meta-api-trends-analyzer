import pandas as pd

PROCESSED_DATA_DIR = "data/processed"
OUTPUT_DIR = "outputs"

def analyze_github_trends():
    df = pd.read_csv(f"{PROCESSED_DATA_DIR}/github_repos.csv")
    
    # Przykład uproszczony: liczymy top 3 repo pod względem gwiazdek (stars)
    top_stars = df.sort_values(by="stars", ascending=False).head(3)
    
    # Można tu dodać logikę porównywania z poprzednim okresem, np. wzrost gwiazdek
    # Wtedy potrzebne byłyby historyczne dane, by wyliczyć delta (zmianę)
    
    return top_stars

def main():
    top_repos = analyze_github_trends()
    print("Top 3 repo wg gwiazdek:")
    print(top_repos[["repo_name", "owner", "stars"]])

if __name__ == "__main__":
    main()
