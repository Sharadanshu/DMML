import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Create interaction matrix (same as Step 4)
data = {
    "user_id": ["U1", "U1", "U2", "U2", "U3"],
    "product_id": ["P1", "P2", "P1", "P3", "P2"],
    "interaction_score": [4, 1, 1, 1, 3]
}

df = pd.DataFrame(data)

interaction_matrix = df.pivot(
    index="user_id",
    columns="product_id",
    values="interaction_score"
).fillna(0)

# Step 2: Compute user-user similarity
similarity_matrix = cosine_similarity(interaction_matrix)

similarity_df = pd.DataFrame(
    similarity_matrix,
    index=interaction_matrix.index,
    columns=interaction_matrix.index
)

print("User Similarity Matrix:")
print(similarity_df)

# Step 3: Recommend products for a target user
target_user = "U2"

# Similar users sorted by similarity score
similar_users = similarity_df[target_user].sort_values(ascending=False)

# Exclude the target user itself
similar_users = similar_users.drop(target_user)

# Products already interacted by target user
user_products = interaction_matrix.loc[target_user]
seen_products = user_products[user_products > 0].index.tolist()

# Collect candidate products from similar users
recommendations = {}

for user, score in similar_users.items():
    user_items = interaction_matrix.loc[user]
    for item, interaction in user_items.items():
        if item not in seen_products and interaction > 0:
            recommendations[item] = recommendations.get(item, 0) + score * interaction

print(f"\nRecommended products for {target_user}:")
for item, score in sorted(recommendations.items(), key=lambda x: x[1], reverse=True):
    print(item, round(score, 3))
