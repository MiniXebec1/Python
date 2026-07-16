user=input('Number Greater than 10: ')
if user == 'yes':
    greater_than_10 = True
    print(greater_than_10)
else:
    print('Number is not greater than 10')

temperature = int(input('Enter the temperature in Celsius: '))
if temperature < 20:
    outfit='jacket'
    print("It is cold today.")
    print("You should wear a", outfit)
else:
    outfit='t-shirt'
    print("It is warm today.")
    print("You should wear a", outfit)

user_input = input('Is it raining? (yes/no): ')
if user_input=='yes':
    print("You should take an umbrella.")
else:
    print("No need for an umbrella today.")

wind_speed = int(input('Enter the wind speed in km/h: '))
if wind_speed > 30:
    print("It is windy today.")
    print("Wear a windbreaker over your", outfit)
else:
    print("The wind speed is moderate today.")

has_puddles = input('Are there puddles on the ground? (yes/no): ')
if has_puddles == 'yes':
    shoes = "boots"
    print("The ground is wet.")
    print("Wear", shoes, "to keep your feet dry.")
else:
    shoes = "sneakers"
    print("The ground is dry.")
    print("You can wear", shoes, "today.")

print("\nWeather check complete!\n")
print("=====WEATHER OUTFIT PICKER=====")
print("Temperature:", temperature, "°C")
print("Outfit Chosen:", outfit)
print("Raining:", user_input)
print("Windbreaker Needed:", "Yes" if wind_speed > 30 else "No")
print("Shoes Chosen:", shoes)
print("=================================")


