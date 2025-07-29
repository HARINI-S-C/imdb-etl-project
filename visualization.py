import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------ 1. Load CSV Dynamically ------------
def load_csv(filename="data.csv"):
    folder = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(folder, filename)
    try:
        df = pd.read_csv(path)
        print(f"✅ Loaded data from: {path}")
        return df
    except FileNotFoundError:
        print(f"❌ File not found at: {path}")
        exit()

# ------------ 2. Describe Data --------------------
def describe_data(df):
    print("📊 Columns:", df.columns.tolist())
    print("🔎 Preview:\n", df.head())
    print("📈 Summary:\n", df.describe())

# ------------ 3. Correlation Heatmap --------------
def plot_correlation(df, filename="correlation_heatmap.png"):
    numeric_df = df.select_dtypes(include="number")
    if numeric_df.empty:
        print("⚠️ No numeric data for correlation.")
        return
    plt.figure(figsize=(10, 8))
    sns.heatmap(numeric_df.corr(), annot=True, fmt=".2f", cmap="coolwarm", square=True)
    plt.title("🔗 Feature Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()

# ------------ 4. Distributions --------------------
def plot_distributions(df, filename_prefix="dist_"):
    numeric_cols = df.select_dtypes(include="number").columns
    for col in numeric_cols:
        plt.figure(figsize=(7, 4))
        sns.histplot(df[col], kde=True, bins=30, color='teal')
        plt.title(f"📊 Distribution of {col}")
        plt.tight_layout()
        plt.savefig(f"{filename_prefix}{col}.png")
        plt.show()

# ------------ 5. Category Boxplots ----------------
def plot_boxplots(df, category_col, filename_prefix="boxplot_"):
    numeric_cols = df.select_dtypes(include="number").columns
    if category_col not in df.columns:
        print(f"⚠️ '{category_col}' not found in data.")
        return
    for col in numeric_cols:
        plt.figure(figsize=(8, 6))
        sns.boxplot(x=df[category_col], y=df[col])
        plt.title(f"🎓 {col} by {category_col}")
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.savefig(f"{filename_prefix}{col}_by_{category_col}.png")
        plt.show()

# ------------ 6. Master Execution ----------------
def main():
    df = load_csv("clean_movies.csv")  # 👈 Update filename if needed
    describe_data(df)

    # Create output directory
    os.makedirs("charts", exist_ok=True)
    os.chdir("charts")

    plot_correlation(df)
    plot_distributions(df)
    # plot_boxplots(df, category_col="education_level")  # 👈 Update this column name as needed

if __name__ == "__main__":
    main()
