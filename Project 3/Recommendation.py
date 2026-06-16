# AI Recommendation System - Project 3

# Sample dataset
items = {
    "Interstellar": ["space", "sci-fi", "time", "drama"],
    "Avengers": ["action", "superhero", "marvel", "fight"],
    "Inception": ["dream", "sci-fi", "mind", "thriller"],
    "Titanic": ["romance", "drama", "ship", "love"],
    "The Matrix": ["sci-fi", "action", "ai", "simulation"],
    "Harry Potter": ["magic", "fantasy", "school", "adventure"]
}

# Take user input
user_input = input("Enter your interests (comma separated): ")

# Convert input into list
user_preferences = [x.strip().lower() for x in user_input.split(",")]

# Function to calculate similarity score
def get_score(item_tags, user_prefs):
    score = 0
    for tag in item_tags:
        if tag in user_prefs:
            score += 1
    return score

# Generate recommendations
recommendations = []

for item, tags in items.items():
    score = get_score(tags, user_preferences)
    if score > 0:
        recommendations.append((item, score))

# Sort based on score (highest first)
recommendations.sort(key=lambda x: x[1], reverse=True)

# Output results
print("\nRecommended Items for You:\n")

if recommendations:
    for item, score in recommendations:
        print(f"{item} (match score: {score})")
else:
    print("No good match found. Try different interests!")