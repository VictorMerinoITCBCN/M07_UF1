import pandas as pd
import matplotlib.pyplot as plt

# (Caldrà agafar els següents 10 ID’s com a mostres:  3,13,34,56,70,85,110,120,210,400).
def get_mobile(file, id):
    df = pd.read_csv(file)
    return df.loc[df["id"] == id]

# 1 funció que mostri per pantalla, el clock speed segons  l’ID del mòbil.
def get_clock_speed(file, id):
    return get_mobile(file, id)["clock_speed"].tolist()[0]

# 1 funció que mostri per pantalla, els megapixels segons l’ID del mòbil.
def get_mpx(file, id):
    return get_mobile(file, id)["fc"].tolist()[0]

# 1 funciño que mostri per pantalla, la battery power segons l’ID del mòbil.
def get_batery(file, id):
    return get_mobile(file, id)["battery_power"].tolist()[0]
# 1 funció main la qual truqui a les 3 funcions i mostri, utilitzant matplotlib, 1 gràfica barres per cada funció mostrant els resultats. (Cal que la gràfica tingui llegenda)
def main():
    file = "./mobiles.csv"
    ids = [3,13,34,56,70,85,110,120,210,400]
    clock_speeds = list([get_clock_speed(file, id) for id in ids])
    mpxs = list([get_mpx(file, id) for id in ids])
    baterys = list([get_batery(file, id) for id in ids])
    colors = ['blue', 'green', 'red', 'orange', 'purple', 'cyan', 'magenta', 'yellow', 'black', 'brown']

    window = plt.figure()
    graf1 = window.add_subplot(3,1,1)
    graf2 = window.add_subplot(3,1,2)
    graf3 = window.add_subplot(3,1,3)

    graf1.bar(ids, clock_speeds, width=10, color=colors, label=ids)
    graf2.bar(ids, mpxs, width=10, color=colors, label=ids)
    graf3.bar(ids, baterys, width=10, color=colors, label=ids)

    graf1.legend()
    graf2.legend()
    graf3.legend()
    plt.show()