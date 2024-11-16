import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.ensemble import IsolationForest
from sklearn.metrics.pairwise import cosine_similarity

# Function to compute similarity using LSA (Latent Semantic Analysis)
def compute_similarity(uploaded_content, existing_contents):
    # Use TF-IDF vectorization to capture term frequencies
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform([uploaded_content] + existing_contents)
    
    # Apply LSA (TruncatedSVD) to reduce dimensionality
    lsa_model = TruncatedSVD(n_components=100)  # Set the number of topics
    lsa_matrix = lsa_model.fit_transform(tfidf_matrix)
    
    # Calculate cosine similarity
    similarity_matrix = cosine_similarity(lsa_matrix[0:1], lsa_matrix[1:])
    return np.max(similarity_matrix)

# Example anomaly detection using Isolation Forest
def detect_anomaly(file_features):
    # Features could include: file size, timestamp hour, etc.
    # Anomalies are detected based on how the feature values deviate from the norm
    
    # Using Isolation Forest for anomaly detection
    model = IsolationForest(contamination=0.05)  # 5% of the data is expected to be anomalous
    features = np.array(file_features).reshape(1, -1)  # Reshape for single prediction
    
    # Predict anomaly (1: normal, -1: anomalous)
    prediction = model.fit_predict(features)
    
    # If prediction is -1, it's an anomaly
    return prediction[0] == -1
