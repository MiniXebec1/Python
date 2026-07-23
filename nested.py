# Custom Ride Builder

# File : ride_builder.py

# Lesson: SPCM2L1 — Nested Conditional Statements (Jr)

print("====================================")

print(" Welcome to Ride Builder! ")

print("====================================")

print()

print("Step 1: Pick your vehicle")

print(" 1 - Bike")

print(" 2 - Car")

print()

choice = int(input("Enter 1 or 2: "))

print()

if choice == 1:
    print("Step 2: Pick your bike type")
    print(" 1 - Kawasaki Ninja H2R")
    print(" 2 - Bullet")
    bike_type = int(input("Enter 1 or 2: "))
    if bike_type == 1:
        print("You picked Kawasaki Ninja H2R! Fast and furious!")
        print("Top Speed: 400 km/h")
        print("Best for: Speed lovers")
    else:
        print("You picked Bullet! Classic and reliable!")
        print("Top Speed: 120 km/h")
        print("Best for: City cruising")
elif choice == 2:
    print("Step 2: Pick your car type")
    print(" 1 - Hyundai Getz")
    print(" 2 - Toyota RAV4 GX")
    car_type = int(input("Enter 1 or 2: "))
    if car_type == 1:
        print("You picked Hyundai Getz! Perfect and practical for daily commutes!")
        print("Top Speed: 160 km/h")
        print("Best for: Everyday use")
    elif car_type == 2:
        print("You picked Toyota RAV4 GX! Luxury and comfort on the road!")
        print("Top Speed: 180 km/h")
        print("Best for: Luxury and comfort")