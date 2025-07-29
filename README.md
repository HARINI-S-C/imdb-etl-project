# 🎬 IMDb Movies ETL and Data Visualization Project

This project performs an **ETL (Extract, Transform, Load)** process on a dataset of IMDb movies, followed by **data visualization** using Python libraries like `pandas`, `matplotlib`, and `seaborn`. The goal is to clean, transform, store, and analyze IMDb movie data to extract meaningful insights.

---

## 🧠 Project Concept

The aim of this project is to build a **mini data pipeline** and visualization system using open-source tools. The pipeline processes raw movie data, cleans and transforms it, stores it in a structured database (SQLite), and produces insightful visualizations like:

- Feature correlation heatmaps  
- Distributions of numerical values (e.g., gross revenue, year)  
- Box plots to compare numerical data across genres  

This project is beginner-friendly and suitable for those learning **ETL, data cleaning, and visualization** techniques in Python.

---

## 📁 Folder Structure
imdb_etl_project/
│
├── imdb_etl.py # ETL script: Extracts, transforms, and loads data
├── visualization.py # Visualization script using matplotlib & seaborn
├── movies.csv # Raw IMDb movie dataset (input)
├── clean_movies.csv # Cleaned dataset after transformation (output)
├── imdb_etl.db # SQLite database storing the final table (output)
└── README.md # Project documentation


## 🔁 ETL Pipeline (imdb_etl.py)

### ✔️ Process Overview:
1. **Extract**  
   - Reads the raw IMDb data from `movies.csv`.

2. **Transform**
   - Removes rows with missing values.
   - Parses and converts the `year` column to integers.
   - Cleans the `gross` column by removing currency symbols and converting to float.
   - Extracts the first genre if multiple genres are present.

3. **Load**
   - Saves the cleaned data to `clean_movies.csv`.
   - Loads the cleaned data into a SQLite database as a table named `imdb_movies`.

### 📌 Output:
- `clean_movies.csv`
- `imdb_etl.db` (SQLite file)

---

## 📊 Data Visualization (visualization.py)

This script reads the cleaned CSV and generates the following plots:

### ✅ Outputs:
- 🔗 **Correlation Heatmap** (`correlation_heatmap.png`)  
- 📈 **Histograms** of all numeric columns  
- 📦 **Boxplots** grouped by a categorical column (e.g., `genre`) *(optional)*

---

## ▶️ How to Run

### 🐍 1. Install Dependencies

Ensure Python 3 is installed. Then, install the required libraries:
- Python 3.x
- pandas
- matplotlib
- seaborn
- sqlite3 (standard library)

### 1.Run the ETL pipeline
python imdb_etl.py

### 2.Generate Visualizations
python visualization.py

