import pandas as pd
# https://goheels.com/sports/mens-basketball/roster

player = {"Last Name": ["Bacot", "Davis", "Cadeau"],
            "First Name": ["Armando", "RJ", "Elliot"],
            "height": [83, 72, 73],
            "weight": [240, 180, 180]
            }
data = pd.DataFrame(player)
print(data)
