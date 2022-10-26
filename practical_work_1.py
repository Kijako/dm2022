import pandas as pd
import re
from math import log
import numpy as np


df_review = pd.read_json("D:/ESILV/Annee_5/Vietnam/cours/Data_mining_2/archive/yelp_academic_dataset_review.json", lines=True, nrows=1000)


df_review["text_split"] = (
    df_review["text"].astype(str).apply(lambda x: x.lower().replace(",", "").replace("'", " ").replace("!", "").replace("?", "").replace(".", "").replace(";", "").replace("(", "").replace(")", ""))
)
df_review["text_split"] = df_review["text_split"].astype(str).apply(lambda x: re.sub(" +", " ", x))
df_review["text_split"] = df_review["text_split"].astype(str).apply(lambda x: re.split(" ", x))

df_review["explod"] = df_review["text_split"]
df_review = df_review.explode("explod").reset_index(drop=True)
df_review["count_by_text"] = 1


# df_review[df_review['business_id']=='x4XdNhp0Xn8lOivzc77J-g'].iloc[3]['text']


df_review["text_split"] = df_review["text_split"].astype(str)
df_review = df_review.groupby(["text", "explod", "text_split", "review_id", "user_id", "business_id", "stars", "useful", "funny", "cool", "date"]).agg({"count_by_text": "sum"}).reset_index(drop=False)


df_review = df_review.groupby(["business_id", "explod"]).aggregate({"count_by_text": "sum", "review_id": "count"}).reset_index(drop=False)


df_review["IDF"] = np.log(df_review["review_id"] / df_review["count_by_text"])
# df_review['IDF'] = np.log(1000/df_review['count_by_text'])


df_review = df_review.sort_values(["business_id", "IDF"], ascending=False).groupby("business_id").head(5)


df_review = df_review.groupby("business_id").aggregate({"explod": lambda x: x.tolist(), "IDF": lambda x: x.tolist()}).reset_index(drop=False)
# df_review["scores"] = df_review.apply(dict(zip(df_review["explod"], df_review["IDF"])))

print(df_review)

# df_review["scores"] = df_review.apply(lambda x: dict(zip(df_review["business_id"], df_review["IDF"]), axis=1))


# df_review[df_review["IDF"] > 0]
# df_review[df_review['review_id']>1]
# df_review[df_review[('count_by_text'>1) & ('count_by_text'>1)]
