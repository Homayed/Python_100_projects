#with open("weather_data.csv","r") as data_file:
#    content = data_file.readlines()
#    print(content)

#import csv
#
#with open("weather_data.csv") as data_file:
#    data = csv.reader(data_file)
#    print(data)
#    temparature = []
#    for row in data:
#        print(row)
#        if row[1]!= 'temp':
#            temparature.append(int(row[1]))
#    print(temparature)

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
count = 0

l = data["Primary Fur Color"]
m = l.tolist()
gray = 0
cinnamon = 0
black = 0
for item in m:
    if item == "Gray":
        gray += 1
    if item == "Black":
        black += 1
    if item == "Cinnamon":
        cinnamon += 1

final_data = {
    "Fur Color":["gray", "black" ,"cinnamon"],
    "Count":[gray,black,cinnamon],
}
data1 = pandas.DataFrame(final_data)

data1.to_csv("new_data.csv")






