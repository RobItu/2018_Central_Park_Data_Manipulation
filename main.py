import pandas
#
# data = pandas.read_csv("weather_data.csv")
#
# temp_list = data["temp"].to_list()
#
# monday_temp = data[data.day == "Monday"]
# fa = (int(monday_temp.temp)*(9/5))+32
# print(fa)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_colors = data["Primary Fur Color"]
Gray = data[squirrel_colors == "Black"]

dic = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [2473, 392, 103]
}

new_data = pandas.DataFrame(dic)
new_data.to_csv("new_data.csv")