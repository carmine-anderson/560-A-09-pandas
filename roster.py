import pandas as pd
# https://goheels.com/sports/mens-basketball/roster

player = {"Last Name": ["Bacot", "Davis", "Cadeau", "High", "Ryan", "Trimble", "Wojcik", "Washington", "Lebo", "Landry"],
            "First Name": ["Armando", "RJ", "Elliot", "Zayden", "Cormac", "Seth", "Paxson", "Jalen", "Creighton", "Rob"],
            "height": [83, 72, 73, 80, 74, 75, 78, 74, 72, 70],
            "weight": [240, 180, 180, 200, 210, 185, 184, 205, 190, 215]
            }
data = pd.DataFrame(player)

data["bmi"] = ((data["weight"]/2.025) / ((data["height"]/39.37)**2)).round(2)

print(data)

data.to_csv("bmi.csv")