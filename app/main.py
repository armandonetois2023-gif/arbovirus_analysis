from etl.extract import extract
from etl.transform import transform
from etl.load import load
import random

arbovirus = ["dengue", "chikungunya", "zikavirus"]
disease = random.choice(arbovirus)
year = random.randint(2000, 2026)

data = extract({"type_disease":  disease, "year": year, "limit": 20, "offset": 0})
if (len(data) > 0):
    df = transform(data)
    load(df, "data/processed/data.csv")
else:
    print("The request returned empty!")