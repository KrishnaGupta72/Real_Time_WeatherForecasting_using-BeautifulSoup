from bs4 import BeautifulSoup
#requests module will allow you to send HTTP/1.1 requests using Python. With it, you can add content like headers, form data, multipart files, and parameters via simple Python libraries. It also allows you to access the response data of Python in the same way
import requests
#csv module implements classes to read and write tabular data in CSV format
import csv
city=str(input("Enter the name of the city you want the weather forecast for:"))
result=requests.get("https://www.weather-forecast.com/locations/"+city+"/forecasts/latest").text
soup = BeautifulSoup(result,'lxml')
w_desc=[]

for weather in soup.find_all('td', class_='b-forecast__table-description-cell--js'):
    desc = weather.find('p', class_='b-forecast__table-description-content').text
    w_desc.append(desc)

alist=[]
for i in soup.find_all('tbody', class_="b-metar-table__body")[0]:
    alist.append((i).encode('utf-8'))
city_weather_info=alist[0]
soup1 = BeautifulSoup(city_weather_info,'lxml')

station=soup1.find('td', class_="b-metar-table__weather-station")
# print(station.text)

temp=soup1.find('span', class_="temp")
tem=temp.text
tem=tem + ' C'

wind=soup1.find('div', class_="b-metar-table__wind-text")
# print(wind.text)

cloud_visi=soup1.find('div', class_="b-metar-table__additionally-container")
# print(cloud_visi.text)

#Writing all product(Printer) information into a csv file.
with open("Weather_Forcast.csv", "a", newline='') as file:
    # Defines column names into a csv file.
    field_names = ['Weather Today days', 'Weather days', '10 Day Weather days', 'Weather_Station_Info', 'Temperature', 'Wind', 'Cloud_Visibility']
    writer = csv.DictWriter(file, fieldnames=field_names)
    writer.writeheader()

    # Writing all information in a row.
    writer.writerow(
        {
            'Weather Today days': w_desc[0],
            'Weather days': w_desc[1],
            '10 Day Weather days': w_desc[2],
            'Weather_Station_Info': station.text,
            'Temperature': tem,
            'Wind': wind.text,
            'Cloud_Visibility': cloud_visi.text
        }
    )
