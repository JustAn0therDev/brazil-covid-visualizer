import requests

def update_csv_dataset():
    csv_data_url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
    response = requests.get(csv_data_url)

    with open('owid_covid_dataset.csv', 'w') as csv:
        csv.write(response.text)
