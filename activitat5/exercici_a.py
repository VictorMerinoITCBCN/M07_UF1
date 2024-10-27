import pandas as pd
import matplotlib.pyplot as plt

def get_locations(df,limit=-1):
    return df.drop_duplicates(subset="location")["location"][:limit].tolist()

#1 funció que mostri per pantalla, la quantitat de casos total per mes per país (agafar 10 països) (agafar 4 mesos).
def get_cases_amount(file):
    # Leer el archivo CSV
    df = pd.read_csv(file, usecols=["location", "date", "new_cases"])

    # Guardar en una lista las 10 primeres ubicacions
    locations = get_locations(df,10)

    # Transformar la columna date a datetime
    df["date"] = pd.to_datetime(df["date"])

    # Filtrar els casos per les 10 ubicacions y els primeros 4 mesos
    cases = df[(df["location"].isin(locations)) & (df["date"].dt.month <= 4)]

    # Afegir una columna per el mes
    cases = cases.assign(month=cases["date"].dt.month)

    # Agrupar por location y mes, sumand els casos
    return cases.groupby(['location', 'month'])['new_cases'].sum().reset_index()

#1 funció que mostri per pantalla, les morts totals per mes per país (agafar 10 països) (agafar 4 mesos) del 2021.
def get_death_amount(file):
    df = pd.read_csv(file, usecols=["location", "date", "new_deaths"])

    locations = get_locations(df,10)
    df["date"] = pd.to_datetime(df["date"])

    deaths = df[(df["location"].isin(locations)) & (df["date"].dt.month <= 4)]

    deaths = deaths.assign(month=deaths["date"].dt.month)

    return deaths.groupby(["location","month"])["new_deaths"].sum().reset_index()

#1 funció que mostri per pantalla la “reproduction_rate” per mes per país (agafar 10 països) (agafar 4 mesos).
def get_reprodution_rate(file):
    df = pd.read_csv(file, usecols=["location", "date", "reproduction_rate"])

    locations = get_locations(df,10)
    df["date"] = pd.to_datetime(df["date"])

    repro = df[(df["location"].isin(locations)) & (df["date"].dt.month <= 4)]

    repro = repro.assign(month=repro["date"].dt.month)

    return repro.groupby(["location","month"])["reproduction_rate"].mean().reset_index()

def add_graf(window, position, data, target, title, label):
    graf = window.add_subplot(2,2,position) #Afegeix una nova grafica

    months = ["gener", "febrer", "març", "abril"]

    data_by_location = data[target].to_numpy().reshape(10,4) #Transforma el dataframe a una matriu 10x4


    locations = get_locations(data,10) #Obte el nom de les ubicacions

    #Recorre la matriu i afegeix a la grafica els valors de cada ubicació
    for i in range(data_by_location.shape[0]):
        graf.plot(months, data_by_location[i], label=f'{locations[i]}')

    #Afegeix el titol i les llegendes
    graf.set_title(title)
    graf.set_xlabel("Mes")
    graf.set_ylabel(label)
    graf.legend()

def add_cases_graf(window):
    file = "./df_covid19_countries.csv"
    data = get_cases_amount(file)

    add_graf(window, 1, data, "new_cases", "Casos per mes", "casos")

def add_death_graf(window):
    file = "./df_covid19_countries.csv"
    data = get_death_amount(file)

    add_graf(window, 2, data, "new_deaths", "Morts per mes", "morts")    

def add_reproduction_graf(window):
    file = "./df_covid19_countries.csv"
    data = get_reprodution_rate(file)

    add_graf(window, 3, data, "reproduction_rate", "Reproducció per mes", "rati reproducció")

#1 funció main la qual truqui a les 3 funcions i mostri, utilitzant matplotlib, 1 gràfica de línies per cada funció mostrant els resultats. (Cal que la gràfica tingui llegenda)
def main():
    window = plt.figure()
    add_cases_graf(window)
    add_death_graf(window)
    add_reproduction_graf(window)
    plt.show()
    

