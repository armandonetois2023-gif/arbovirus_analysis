import pandas as pd

def transform(data):
    rows = []
    for record in data:
        for symptom, value in record["symptoms"].items():            
            rows.append({
                "gender": record["gender"],
                "age": (record["year"] - int(record["born_year"])) if (isinstance(record["born_year"], str)) else -1,
                "year": record["year"],
                "evolution": record["evolution"],
                "symptom": symptom,
                "present":  1 if value == "1" else 2
            })
    df = pd.DataFrame(rows)
    return df