# syntax:

# if condition:

# code

# elif condition:

# code

# else:

# code(fallback)

#smart school day planner::

# Smart School Day Planner - Topic 1

day = input("Enter today's day: ").strip().capitalize()

if day in ("Saturday", "Sunday"):
	print("Day type : Weekend - enjoy your free time!")
elif day == "Monday":
	print("Day type : First day of the week.")
elif day == "Friday":
	print("Day type : Last school day.")
elif day in ("Tuesday", "Wednesday", "Thursday"):
	print("Day type : Regular school day.")
else:
	print("Day type : Day not recognised.")
	
    
# Topic 2 - AND operator

weather=input("How is the weather? ")

homework=input("Do you have homework? ")

if weather == "sunny" and homework == "no":
	print("After school: Head to the park!")
else:
	print("Do ur Homework")
	
    
# Topic 3 - OR operator
	
weather=input("How is the weather? ")

if weather == "rainy" or weather == "cloudy":
	print("Weather tip : Pack your umbrella!")
else:
	print('go to Home ')
	
    # Topic 4 - NOT operator
	
homework = input("Do you have homework? ")

day = input("What day of the week is it? ")

if not (homework == "yes"):
	print("Homework : Not done yet. Finish it before going out!")

# not-equal operator

if day != "Saturday":
	print("It is a school week day.")
	
# Topic 5 -- Combining AND + OR + NOT together

if weather == "rainy" and not (homework == "yes"):
	print("Best plan : Stay in, finish homework, then watch your favourite show.")
elif weather == "sunny" and homework == "yes" and not (day in ("Saturday", "Sunday")):
	print("Best plan : All set for a great school day - you are prepared!")
elif day in ("Saturday", "Sunday") and weather == "sunny":
	print("Best plan : Perfect weekend weather - head outside and have fun!")
else:
	print("Best plan : Take it one step at a time - you have got this!")

print()

print("Plan complete! Have a wonderful day!")

