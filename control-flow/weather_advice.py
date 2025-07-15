# This script will ask the user about the current weather conditions and provide clothing recommendations based on the input.

weather = input("What's the weather like today? (sunny/rainy/cold):").strip().lower()
recommedations = ""

if weather == "sunny":
    recommedations = "Wear a t-shirt and sunglasses."
elif weather == "rainy":
    recommedations = "Don't forget your umbrella and a raincoat."
elif weather == "cold":
    recommedations = "Make sure to wear a warm coat and a scarf."
else:
    recommedations = "Sorry, I don't have recommendations for this weather."

print(recommedations)
