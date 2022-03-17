import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_colors = data["Primary Fur Color"]
Gray = data[squirrel_colors == "Black"]

dic = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [2473, 392, 103]
}

new_data = pandas.DataFrame(dic)
new_data.to_csv("new_data.csv")
