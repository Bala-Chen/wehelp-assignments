import requests
import json
import csv

json_file = requests.get("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json",verify=False)

list_of_dicts = json_file.json()
main_data = list_of_dicts["result"]["results"]
all_list=[]
for i in range(len(main_data)):
    one_list =[]
    stitle = main_data[i]["stitle"]
    district = main_data[i]["address"][5:8]
    longitude = main_data[i]["longitude"]
    latitude = main_data[i]["latitude"]
    img = main_data[i]["file"].split("https://")[1]
    print(stitle,district,longitude,latitude,"https://"+img)
    one_list.append(stitle)
    one_list.append(district)
    one_list.append(longitude)
    one_list.append(latitude)
    one_list.append("https://" + img)
    all_list.append(one_list)
    
with open("week-3.csv","w",newline="",encoding="utf-8-sig") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["景點名稱","區域","經度","緯度","圖檔網址"])
    writer.writerows(all_list)
