import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import base64
from io import BytesIO
from django.shortcuts import render

# Function to convert plots to base64 format
def get_base64_image():
    buffer = BytesIO()
    plt.savefig(buffer, format="png", bbox_inches="tight")
    plt.close()
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return image_base64

def home(request):
    """Generate plots and pass them to the template."""

    # Load dataset
    df = pd.read_csv("data/zomato.csv", encoding="latin-1")

    # **1️⃣ Histogram: Distribution of Restaurant Ratings**
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Aggregate rating'], bins=20, kde=True, color='blue')
    plt.title('Distribution of Restaurant Ratings', fontsize=16)
    plt.xlabel('Aggregate Rating', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    rating_chart = get_base64_image()

    # **2️⃣ Bar Chart: Top 10 Most Common Cuisines**
    cuisines = df['Cuisines'].dropna().str.split(', ').explode()
    cuisine_counts = cuisines.value_counts().head(10)

    plt.figure(figsize=(12, 6))
    sns.barplot(x=cuisine_counts.values, y=cuisine_counts.index, hue=cuisine_counts.index, palette="viridis", legend=False)
    plt.title('Top 10 Most Common Cuisines', fontsize=16)
    plt.xlabel('Number of Restaurants', fontsize=14)
    plt.ylabel('Cuisine Type', fontsize=14)
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    cuisine_chart = get_base64_image()

    # **3️⃣ Pie Chart: Price Range Distribution**
    price_range_counts = df['Price range'].value_counts().sort_index()

    plt.figure(figsize=(8, 8))
    plt.pie(price_range_counts, labels=price_range_counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
    plt.title('Distribution of Restaurants by Price Range', fontsize=16)
    price_chart = get_base64_image()

    # **4️⃣ Scatter Plot: Aggregate Rating vs. Votes**
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Aggregate rating', y='Votes', data=df, alpha=0.6, color='orange')
    plt.title('Aggregate Rating vs. Votes', fontsize=16)
    plt.xlabel('Aggregate Rating', fontsize=14)
    plt.ylabel('Votes', fontsize=14)
    plt.grid(axis='both', linestyle='--', alpha=0.7)
    rating_vs_votes_chart = get_base64_image()

    # **5️⃣ Bar Chart: Top 10 Cities with Most Restaurants**
    top_cities = df['City'].value_counts().head(10)

    plt.figure(figsize=(12, 6))
    sns.barplot(y=top_cities.index, x=top_cities.values, hue=top_cities.index, palette="viridis", legend=False)
    plt.title('Top 10 Cities by Number of Restaurants', fontsize=16)
    plt.xlabel('Number of Restaurants', fontsize=14)
    plt.ylabel('City', fontsize=14)
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    top_cities_chart = get_base64_image()

    # **6️⃣ Heatmap: Correlation Matrix**
    numeric_cols = ['Average Cost for two', 'Price range', 'Aggregate rating', 'Votes']
    correlation_matrix = df[numeric_cols].corr()

    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Correlation Matrix', fontsize=16)
    correlation_chart = get_base64_image()

    # **7️⃣ Box Plot: Price Range vs. Average Cost for Two**
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Price range', y='Average Cost for two', data=df, hue='Price range', palette='coolwarm', legend=False)
    plt.title('Price Range vs. Average Cost for Two', fontsize=16)
    plt.xlabel('Price Range', fontsize=14)
    plt.ylabel('Average Cost for Two', fontsize=14)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    price_vs_cost_chart = get_base64_image()

    # **8️⃣ Bar Chart: Top 10 Localities by Restaurant Count**
    top_locations = df['Locality'].value_counts().head(10)

    plt.figure(figsize=(12, 6))
    sns.barplot(y=top_locations.index, x=top_locations.values, hue=top_locations.index, palette="crest", legend=False)
    plt.title('Top 10 Localities by Number of Restaurants', fontsize=16)
    plt.xlabel('Number of Restaurants', fontsize=14)
    plt.ylabel('Locality', fontsize=14)
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    top_localities_chart = get_base64_image()

    # **9️⃣ Pie Chart: Online Delivery Availability**
    delivery_counts = df['Has Online delivery'].value_counts()

    plt.figure(figsize=(8, 8))
    plt.pie(delivery_counts, labels=['Yes', 'No'], autopct='%1.1f%%', startangle=140, colors=['#4CAF50', '#FFC107'])
    plt.title('Online Delivery Availability', fontsize=16)
    online_delivery_chart = get_base64_image()

    # Pass images to the template
    return render(request, "analysis/home.html", {
        "rating_chart": rating_chart,
        "cuisine_chart": cuisine_chart,
        "price_chart": price_chart,
        "rating_vs_votes_chart": rating_vs_votes_chart,
        "top_cities_chart": top_cities_chart,
        "correlation_chart": correlation_chart,
        "price_vs_cost_chart": price_vs_cost_chart,
        "top_localities_chart": top_localities_chart,
        "online_delivery_chart": online_delivery_chart
    })
