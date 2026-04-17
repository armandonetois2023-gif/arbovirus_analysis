import pandas as pd
import matplotlib.pyplot as plt

class ArbovirusAnalysis:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
    
    def symptom_frenquecy(self):
        result = (self.df.groupby("symptom")["present"]).sum().sort_values(ascending=False)
        return result

    def plot_symptom_frequency(self):
        data = self.symptom_frenquecy()
        
        plt.figure()
        data.plot(kind="barh")
        plt.title("Most Common Symptoms")
        plt.xlabel("Number of Cases")
        plt.ylabel("Symptoms")
        plt.tight_layout()
        plt.show()
    
    def symptoms_by_severity(self, severe_velue=9):
        severe_df = self.df[self.df["evolution"] == severe_velue]
        
        result = (severe_df.groupby("symptom")["present"].mean().sort_values(ascending=False))
        return result
    
    def plot_severity(self):
        data = self.symptoms_by_severity()
        
        plt.figure()
        data.plot(kind="barh")
        plt.title("Symptoms in Severe Cases (Probability)")
        plt.xlabel("Probability")
        plt.tight_layout()
        plt.show()
    
    def symptoms_by_gender(self):
        result = self.df.pivot_table(index="symptom", columns="gender", values="present", aggfunc="mean")
        return result
        
    def plot_gender_comparison(self):
        data = self.symptoms_by_gender()
        
        plt.figure()
        data.plot(kind="bar")
        plt.title("Symptoms by Gender")
        plt.ylabel("Probability")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        
    def add_age_groups(self):
        self.df["age_group"] = pd.cut(self.df["age"], bins=[0, 18, 40, 60, 100], lables=["0 - 18", "19-40", "41-60", "60+"])
        
    def symptoms_by_age(self):
        self.add_age_groups()
        
        result = self.df.pivot_table(index="symptom", columns="age_group", values="present", aggfunc="mean")
        return result
        
    def plot_age_analysis(self):
        data = self.symptoms_by_gender()
        
        plt.figure()
        plt.title("Symptoms by Age Group")
        plt.ylabel("Probability")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()