import pandas as pd

# Load raw interaction data
df = pd.read_csv("data/interactions.csv")

# Define interaction weights
interaction_map = {
    "view": 1,
    "purchase": 3
}

# Convert event_type to numeric score
df["interaction_score"] = df["event_type"].map(interaction_map)

print(df)
