import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Mock dataset
data = {
    'City': ['Paris', 'New York', 'Tokyo', 'Sydney', 'Cairo'],
    'Description': [
        'art culture history',
        'business nightlife fashion',
        'technology culture modern',
        'beaches wildlife adventure',
        'history culture ancient'
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Feature extraction using TF-IDF
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(df['Description'])

# Function to recommend cities
def recommend_city(city, df, tfidf_matrix):
    # Find the index of the city in the dataframe
    city_index = df.index[df['City'] == city].tolist()[0]

    # Compute cosine similarity between this city and all others
    cosine_similarities = cosine_similarity(tfidf_matrix[city_index], tfidf_matrix).flatten()

    # Get the top 5 similar cities, excluding the city itself
    similar_cities_indices = cosine_similarities.argsort()[-2:-7:-1]
    
    # Fetch the city names
    recommended_cities = df['City'].iloc[similar_cities_indices]

    return recommended_cities

# Test the system
city_to_recommend = 'Paris'
recommended_cities = recommend_city(city_to_recommend, df, tfidf_matrix)
print(f"Cities recommended based on your interest in {city_to_recommend}:")
print(recommended_cities)
