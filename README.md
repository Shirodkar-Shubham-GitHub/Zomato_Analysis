# Zomato Analysis

## Introduction
The Zomato dataset provides comprehensive information about restaurants, including details such as location, cuisine types, cost for two, ratings, and online delivery availability. This dataset offers valuable insights into consumer preferences, restaurant trends, and geographical distribution of dining establishments. By analyzing this data, we can uncover patterns in dining habits, restaurant density, and the factors influencing popularity. This analysis is especially useful for businesses aiming to optimize their services and for customers seeking better dining experiences. The live version of the application is available [here](https://shubhamshirodkar990.pythonanywhere.com/).

## Dataset Description
The Zomato dataset comprises detailed information about restaurants across various cities, including features such as restaurant names, locations, cuisines offered, average cost for two, ratings, votes, and delivery options. It also includes temporal data like review timestamps and operational details like online delivery availability. This structured dataset is ideal for analyzing trends in the food industry, geographical restaurant distribution, and customer preferences, enabling data-driven decision-making and strategic insights.

## Objective
The objective of analyzing the Zomato dataset is to explore restaurant trends, customer preferences, and geographical patterns in the food industry. By leveraging this data, we aim to identify key insights such as top-rated locations, popular cuisines, cost variations, and delivery trends. This analysis will provide actionable recommendations for stakeholders, including restaurant owners, food delivery services, and customers, to make informed decisions and enhance the dining experience.

## Tools and Technologies Used
* **Python**: For data manipulation, analysis, and visualization.
* **Django**: A high-level Python web framework used for building scalable and secure web applications.
* **Pandas**: To clean, preprocess, and analyze the dataset efficiently.
* **NumPy**: For numerical operations and handling large datasets.
* **Matplotlib**: To create static visualizations and charts.
* **Seaborn**: For advanced and aesthetically pleasing visualizations.
* **Jupyter Notebook**: As the development environment for interactive data analysis.

## Installation
 #### 1. Clone the Repository:
    git clone https://github.com/Shirodkar-Shubham-GitHub/Zomato_Analysis
    cd Zomato_Analysis
 #### 2. Create a Virtual Environment:
    python -m venv my_env
    my_env\Scripts\activate
 #### 3. Install Dependencies:
    pip install -r requirements.txt
 #### 4. Run the Development Server:
    python manage.py runserver

## Data Preprocessing
1. **Loading the Dataset**:
   * The dataset was loaded into a Pandas DataFrame for analysis and manipulation.
2. **Handling Missing Values**:
   * Columns with a significant number of missing values were identified.
   * Missing values in numerical columns (e.g., Average Cost for two, Votes) were replaced with appropriate measures such as the mean or median.
   * Missing values in categorical columns (e.g., Cuisines, Location) were either filled with the mode or left as-is if not critical to the analysis.
3. **Removing Duplicates**:
   * Duplicate entries in the dataset were identified and removed to ensure data integrity.
4. **Outlier Detection and Handling**:
   * Outliers in columns like Average Cost for two and Votes were identified using statistical methods (e.g., IQR) and either capped or removed to prevent skewed results.
5. **Feature Engineering**:
   * Aggregated columns were created (e.g., Total Ratings = Ratings * Votes) for more meaningful insights.

## Exploratory Data Analysis (EDA)
**1. Distribution of Restaurant Ratings**
* **Insights**:
  * Ratings tend to cluster around higher values, indicating restaurants generally receive favorable ratings.
  * Few restaurants have ratings below 2.0.
* **Visualization**:
  * A histogram is used to visualize the distribution of restaurant ratings.

**2. Top 10 Most Common Cuisines**
* **Insights**:
  * North Indian, Chinese, and Fast Food are the most common cuisines offered.
* **Visualization**:
  * A bar chart shows the most popular cuisines.

**3. Distribution of Restaurants by Price Range**
* **Insights**:
  * Most restaurants fall within the budget-friendly categories (price range 1 and 2).
* **Visualization**:
  * A pie chart to show the proportion of restaurants in different price ranges.

**4. Relationship Between Restaurant Ratings and Number of Votes**
* **Insights**:
  * Restaurants with higher ratings tend to have more votes, indicating customer engagement correlates with quality.
* **Visualization**:
  * A scatter plot to explore the correlation between aggregate ratings and votes.

**5. Cities Dominating in Terms of Restaurant Counts**
* **Insights**:
  * Major cities like New Delhi, Gurgaon and Noida dominate in terms of the number of restaurants.
* **Visualization**:
  * A bar chart showing the top 10 cities by restaurant count.

**6. Overall Relationship Between Numeric Variables**
* **Insights**:
  * Strong correlation between votes and ratings.
  * Weak correlation between cost and other variables.
* **Visualization**:
  * A heatmap to display correlations between numerical variables.

**7. Comparing the Average Cost Across Different Price Ranges**
* **Insights**:
  * Higher price ranges naturally have a higher average cost, with significant variation in range 4.
* **Visualization**:
  * A boxplot showing the cost distribution across price ranges.
 
**8. Top 10 Localities by Number of Restaurants**
* **Insights**:
  * High concentration of restaurants in specific localities reflects popular dining areas.
* **Visualization**:
  * A bar chart showing the top 10 localities.

**9. Commonly Used Delivery Services**
* **Insights**:
  * A majority of restaurants offer online delivery, aligning with the growing trend of food delivery services.
* **Visualization**:
  * A pie chart or bar chart to show the availability of online delivery.

## Deployment
   This project was deployed on PythonAnywhere. Follow the platform's instructions to deploy your Django application.
   
## Conclusion
The Zomato dataset analysis reveals key insights into the restaurant industry, including customer preferences, pricing trends, and geographical distribution. Popular cuisines like North Indian, Chinese, and Fast Food dominate, while cities such as New Delhi, Gurgaon and noida lead in restaurant density. Most restaurants cater to budget-friendly price ranges, with premium options showing greater cost variation. A strong correlation between ratings and votes highlights the importance of quality in customer engagement. The rise of online delivery services reflects changing consumer habits, emphasizing the shift toward convenience and digital platforms. These findings offer actionable insights for businesses to optimize their strategies and enhance customer satisfaction.
