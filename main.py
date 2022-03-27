import matplotlib.pyplot as plt
from csv import DictReader

with open('owid_covid_dataset.csv', 'r') as csv:
    csvdict = DictReader(csv)
    rows = list(filter(lambda x: x['location'] == 'Brazil', csvdict))
    
    fig, ax = plt.subplots()
    valid_rows = [(rows[i]["new_deaths"], rows[i]["date"][2:7]) for i in range(0, len(rows), 30) if rows[i]["date"] and rows[i]["new_deaths"]]
    # ax.hist([float(i["new_deaths"]) // 10 for i in valid_rows], rwidth=0.5)
    ax.plot([i[1] for i in valid_rows], [int(float(i[0])) for i in valid_rows])
    ax.set(xlabel="Data (ano-mês)", ylabel="Novas mortes", title="Visualização de novas mortes-mês")

    plt.show()

