import pandas as pd
import sqlite3
import os

# Step 1: Extract
file_path = "C:/Users/ad/covid_etl_project/movies.csv"
if not os.path.exists(file_path):
    raise FileNotFoundError(f"❌ File not found at {file_path}")

df = pd.read_csv(file_path)
print("🧾 Available columns:", df.columns.tolist())

# Step 2: Transform
df = df.dropna()

# ✅ Use correct column name
df['year'] = pd.to_numeric(df['year'], errors='coerce')
df = df.dropna(subset=['year'])
df['year'] = df['year'].astype(int)

# ✅ Clean genre - take first genre
df['genre'] = df['genre'].apply(lambda x: x.split(',')[0].strip())

# ✅ Clean gross column
df['gross'] = df['gross'].replace(r'[\$,]', '', regex=True).astype(float)

# ✅ Save cleaned CSV
clean_csv_path = "C:/Users/ad/covid_etl_project/clean_movies.csv"
df.to_csv(clean_csv_path, index=False)

# Step 3: Load to SQLite
db_path = "C:/Users/ad/covid_etl_project/imdb_etl.db"

# ✅ Delete corrupted DB if it exists
if os.path.exists(db_path):
    os.remove(db_path)

# ✅ Create new DB and insert data
conn = sqlite3.connect(db_path)
df.to_sql("imdb_movies", conn, if_exists="replace", index=False)
conn.close()

print("✅ ETL process complete. Data saved to:")
print(f"    • Clean CSV: {clean_csv_path}")
print(f"    • SQLite DB: {db_path}")
