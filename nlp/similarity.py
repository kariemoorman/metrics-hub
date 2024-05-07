import numpy as np

def euclidean_distance(v1, v2):
    """Calculate the Euclidean distance between two vectors."""
    return np.linalg.norm(np.array(v1) - np.array(v2))

def dot_product(v1, v2): 
    """Calculate the dot product of two vectors."""
    return np.dot(v1,v2)

def cosine_similarity(v1, v2):
    """Calculate the cosine similarity between two vectors."""
    dot_product = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    similarity = dot_product / (norm_v1 * norm_v2)
    return similarity

# Example usage:
v1 = [50.23, 45.44, 47.01, 65.10, 80.71]
v2 = [10.41, 65.11, 67.31, 25.17, 70.81]

dotproduct = dot_product(v1, v2)
print("Dot Product:", dotproduct)

euclideandistance = euclidean_distance(v1, v2)
print("Euclidean Distance:", euclideandistance)

cosinesimilarity = cosine_similarity(v1, v2)
print("Cosine Similarity:", cosinesimilarity)
