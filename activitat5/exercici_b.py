import pandas as pd
import matplotlib.pyplot as plt

def str_to_float(string):
    remove_braquets = string.split("[")[0]
    return remove_braquets.replace(",", "")
# 1 funció que mostri per pantalla, el total de població per ciutat.
def get_population(file):
    df = pd.read_csv(file, usecols=["City", "Population"])[:10]
    df["Population"] = df["Population"].apply(str_to_float)
    print(df)
    return df
# 1 funció que mostri per pantalla, la densitat per KM2 per ciutat.
def get_density_km(file):
    df = pd.read_csv(file, usecols=["City","Density (/km²)"])[:10]
    print(df)
    return df
# 1 funció que mostri per pantalla, la densitat per M2 per ciutat.
def get_density_m(file):
    df = pd.read_csv(file, usecols=["City","Density (/mi²)"])[:10]
    print(df)
    return df

def add_graf(window, position, data, target):
    # Add a subplot to the window
    graf = window.add_subplot(2, 2, position)
    
    # Extracting the required data
    list_data = data[target].tolist()
    locations = data["City"].tolist()

    # Create the pie chart on the subplot
    graf.pie(list_data, labels=locations, autopct="%1.1f%%")
    

# 1 funció main la qual truqui a les 3 funcions i mostri, utilitzant matplotlib, 1 gràfica circular per cada funció mostrant els resultats. (Cal que la gràfica tingui llegenda i cal mostrar el % en cada “quesito”). Si veieu que en aquest format, la llegenda es sobreposa, agafeu una mostra des del main.
def main():
    file = "./List of world cities by population density.csv"
    window = plt.figure()
    population = get_population(file)
    density_km = get_density_km(file)
    density_m = get_density_m(file)
    add_graf(window, 1, population, "Population")
    add_graf(window, 2, density_km, "Density (/km²)")
    add_graf(window, 3, density_m, "Density (/mi²)")
    plt.show()