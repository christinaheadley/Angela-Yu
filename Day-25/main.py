# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

# print(row):
# ['day', 'temp', 'condition']
# ['Monday', '12', 'Sunny']
# ['Tuesday', '14', 'Rain']
# ['Wednesday', '15', 'Rain']
# ['Thursday', '14', 'Cloudy']
# ['Friday', '21', 'Sunny']
# ['Saturday', '22', 'Sunny']
# ['Sunday', '24', 'Sunny']
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         print(temperatures)
# don't know why mine prints out multiple rows while Angela's only prints final row

import pandas
import statistics
data = pandas.read_csv("weather_data.csv")
# print(type(data["temp"]))
# # print(data["temp"])
temp_list = data["temp"].to_list()
# print(temp_list)
#
# print(type(data))
# data_dict = data.to_dict()
# print(data_dict)
#
# ave_temp = statistics.mean(temp_list)
# print(f"Average temperature: {ave_temp}")
#
max_temp = max(temp_list)
# print(f"Max temperature: {max_temp}")
#
# # To print column data:     **both ways are case sensitive**
# print(data["condition"])
# # OR
# print(data.condition)
# print(data.day)
#
# Get data in row
print(data[data.day == "Monday"])
monday = data[data.day == "Monday"]
print(f"Type: {type(monday)}")
print(monday.day)
print(data[data.temp == max_temp])
#
# # get monday's temp in fahrenheit:
# print(monday.temp)
# print((monday.temp * 9 / 5) + 32)
# print((24 * 9 / 5) + 32)

# create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "Carlos", "Jo"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict) #initilize class with contents of parens
# # print(data)
# data.to_csv("new_data.csv")

# create csv called squirrel counts. tally number of squirrels in each color
# build new dataframe with fur color and total count
# Primary Fur Color

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data["Primary Fur Color"])
fur_color = data["Primary Fur Color"]
gray = data[fur_color == "Gray"]
red = data[fur_color == "Cinnamon"]
black = data[fur_color == "Black"]

squirrel_dict = {
    "fur color": ["Gray", "Cinnamon", "Black"],
    "total": [len(gray), len(red), len(black)]
}
data = pandas.DataFrame(squirrel_dict)
data.to_csv("squirrel_counts.csv")
# df.loc[df[‘Color’] == ‘Green’]
# print(len(gray))
# print(len(red))
# print(len(black))
# .to_list())
