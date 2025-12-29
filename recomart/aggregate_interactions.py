import pandas as pd

# Load data with interaction scores
df = pd.read_csv("data/interactions.csv")

interaction_map = {
    "view": 1,
    "purchase": 3
}

df["interaction_score"] = df["event_type"].map(interaction_map)

# Aggregate interactions: one row per user-product
agg_df = (
    df.groupby(["user_id", "product_id"], as_index=False)
      .agg({"interaction_score": "sum"})
)

print(agg_df)
