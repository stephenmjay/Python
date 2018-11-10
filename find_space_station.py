import urllib.request
import json
import turtle
import time

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read().decode('UTF-8'))
print("People in Space: ", result["number"])
people = result["people"]
for person in people:
    print(person["name"], "in", person["craft"])

url = "http://api.open-notify.org/iss-now.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read().decode('UTF-8'))

location = result["iss_position"]
lat = float(location["latitude"])
lon = float(location["longitude"])
print("Latitude:", lat)
print("Longitude:", lon)

screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic("map.png")

screen.register_shape("iss.gif")
iss = turtle.Turtle()
iss.shape("iss.gif")
iss.setheading(90)
iss.penup()
iss.goto(lon, lat)

# Space Center, Houston
lat = 29.5502
lon = -95.097

location = turtle.Turtle()
location.penup()
location.color("yellow")
location.goto(lon, lat)
location.dot(5)
location.hideturtle()

url = "http://api.open-notify.org/iss-pass.json"
url = url + "?lat=" + str(lat) + "&lon=" + str(lon)
response = urllib.request.urlopen(url)
result = json.loads(response.read().decode('UTF-8'))
over = result['response'][0]['risetime']

style = ('Arial', 6, 'bold')
location.write(time.ctime(over), font=style)

# Winnipeg
lat = 49.895136
lon = -97.138374

location = turtle.Turtle()
location.penup()
location.color("orange")
location.goto(lon, lat)
location.dot(5)
location.hideturtle()

url = "http://api.open-notify.org/iss-pass.json"
url = url + "?lat=" + str(lat) + "&lon=" + str(lon)
response = urllib.request.urlopen(url)
result = json.loads(response.read().decode('UTF-8'))
over = ""
for stamp in result['response']:
    over += time.ctime(stamp['risetime']) + "\n"

style = ('Arial', 6, 'bold')
location.write(over, font=style)
