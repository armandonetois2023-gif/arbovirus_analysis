import pandas as pd
from analysis.analysis import  ArbovirusAnalysis

df = pd.read_csv("data/processed/data.csv")
analysis = ArbovirusAnalysis(df)

analysis.plot_symptom_frequency()
analysis.plot_severity()
analysis.plot_gender_comparison()
analysis.plot_age_analysis()
