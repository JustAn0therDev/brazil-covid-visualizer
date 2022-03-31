import matplotlib.pyplot as plt
from csv import DictReader
from dataset_manager import update_csv_dataset

print("Updating dataset...")
update_csv_dataset()

with open('owid_covid_dataset.csv', 'r') as csv:
    csvdict = DictReader(csv)

    rows = list(filter(lambda x: x['location'] == 'Brazil', csvdict))
    
    fig, ax = plt.subplots()
    valid_rows = [(rows[i]["new_deaths"], rows[i]["date"][2:7]) for i in range(0, len(rows), 30) if rows[i]["date"] and rows[i]["new_deaths"]]
    dates = [int(float(i[0])) for i in valid_rows]
    new_deaths = [i[1] for i in valid_rows]
    ax.plot(new_deaths, dates)
    ax.set(xlabel="Data (ano-mês)", ylabel="Novas mortes", title="Visualização de novas mortes-mês")

    plt.show()

