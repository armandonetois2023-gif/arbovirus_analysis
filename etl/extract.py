from data.raw.fatch_data_apidadosabertos import fatch_data

def extract(params):
    response = fatch_data(params["type_disease"], params["year"], params["limit"], params["offset"])
    if not (isinstance(response, int)):
        lines = []
        for record in response:
            lines.append(
                {"disease": params["type_disease"], "dt_notific": record["dt_notific"], "year": params["year"], "gender": record["cs_sexo"], "pregnant": record["cs_gestant"], "race": record["cs_raca"] , 
                 "education": record["cs_escol_n"], "r_sorotype": record["resul_soro"], "sorotype": record["sorotipo"], "evolution": record["evolucao"], "dt_death": record["dt_obito"], 
                 "born_year": record["ano_nasc"],
                 "symptoms": {"fever": record["febre"],  "myalgia": record["mialgia"], "headache": record["cefaleia"], "rash": record["exantema"], "vomit": record["vomito"],  "nausea": record["nausea"],
                 "back_pain": record["dor_costas"],  "conjunctivitis": record["conjuntvit"],  "arthritis": record["artrite"], "arthralgia": record["artralgia"], "petechiae": record["petequia_n"], 
                 "leukopenia": record["leucopenia"], "lasso_test": record["laco"], "orbital_pain": record["dor_retro"]},
                 "conditions": {"diabetes": record["diabetes"], "hematological": record["hematolog"], "liver_diseases": record["hepatopat"], "kidney_disease": record["renal"], 
                 "high_pressure": record["hipertensa"], "autoimmune_diseases": record["auto_imune"]}
                 })
        return lines
    return response