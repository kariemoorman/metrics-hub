#include <iostream>
#include <vector>
#include <cmath>

// double: data type used to represent floating-point numbers with double precision; used to store decimal numbers with higher range and precision compared to "float" data type.

// dotProduct Function: Calculate the cumulative sum of the product of i-th value of two vectors (i.e., dot product).
// Dot Product: scalar value that represents the similarity between two vectors (numerator of cosine similarity).
double dotProduct(const std::vector<double>& v1, const std::vector<double>& v2) {
    double result = 0.0;
    for (size_t i = 0; i < v1.size(); ++i) {
        result += v1[i] * v2[i];
    }
    return result;
}


// magnitude Function: Calculate the square root of the cumulative sum of squares of each element within a vector.
// Magnitude: Euclidean Norm of a vector; a measure of its length in a multidimensional space (used in denominator of cosine similarity).
double magnitude(const std::vector<double>& v) {
    double result = 0.0;
    for (int x : v) {
        result += x * x;
    }
    return std::sqrt(result);
}

// cosineSimilarity Function: Calculate the dot product of two vectors divided by the magnitudes (i.e., Euclidean norms) of the two vectors.
double cosineSimilarity(const std::vector<double>& v1, const std::vector<double>& v2) {
    double dot = dotProduct(v1, v2);
    double mag1 = magnitude(v1);
    double mag2 = magnitude(v2);
    return dot / (mag1 * mag2);
}

// euclideanDistance Function: Calculate the squared difference between two elements in two respective vectors.
double euclideanDistance(const std::vector<double>& v1, const std::vector<double>& v2) {
    if (v1.size() != v2.size()) {
        std::cerr << "Error: Vectors do not share same dimensionality." << std::endl;
        return 0.0;
    }
    double sum = 0.0;
    for(size_t i=0; i < v1.size(); ++i) {
        double diff = v1[i] - v2[i];
        sum += diff * diff;
    }
    return std::sqrt(sum);
}

int main() {
    // Create two vectors: v1 and v2
    std::vector<double> v1;
    v1 = {50.23, 45.44, 47.01, 65.10, 80.71};

    std::vector<double> v2;
    v2 = {10.41, 65.11, 67.31, 25.17, 70.81};

    // Calculate dot product 
    double dotproduct = dotProduct(v1, v2);

    // Print dot product
    std::cout << "Dot Product: " << dotproduct << std::endl;
    
    // Calculate cosine similarity
    double similarity = cosineSimilarity(v1, v2);

    // Print the cosine similarity
    std::cout << "Cosine Similarity: " << similarity << std::endl;

    // Calculate euclidean distance 
    double eucdistance = euclideanDistance(v1, v2);

    // Print euclidean distance 
    std::cout << "Euclidean Distance: " << eucdistance << std::endl;
    
    return 0;
}

// Compile: g++ -std=c++11 -o ./similarity cosine_similarity.cpp
// Run: ./similarity
