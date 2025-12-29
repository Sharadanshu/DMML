import pandas as pd

# Load aggregated interaction data
data = {
    "user_id": ["U1", "U1", "U2", "U2", "U3"],
    "product_id": ["P1", "P2", "P1", "P3", "P2"],
    "interaction_score": [4, 1, 1, 1, 3]
}

df = pd.DataFrame(data)

# Create user-item interaction matrix
interaction_matrix = df.pivot(
    index="user_id",
    columns="product_id",
    values="interaction_score"
).fillna(0)

print(interaction_matrix)
