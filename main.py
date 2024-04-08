import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])

monday = data[data.day=="Monday"]

monday_temp = monday.temp[0]

monday_temp_f = monday_temp * 9/5 + 32

print(monday_temp_f)
