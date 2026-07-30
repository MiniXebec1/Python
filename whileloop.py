#while loop: infinite loop , true loop

# syntax: while condition:
#loop code

total_chores = 4
original_count = total_chores
print(f"You have {original_count} chores to finish today.")

completed_count = 0
chore_num = 1
while chore_num <= total_chores:
    if chore_num == 1: next_chore = "Make your bed"
    elif chore_num == 2: next_chore = "Feed the pet"
    elif chore_num == 3: next_chore = "Take out the trash"
    else: next_chore = "Wash the dishes"
    answer = input(f"Have you completed chore {next_chore}? (yes/no): ")
    if answer=="yes":
        completed_count += 1
        chore_num += 1
    else:
        print("Okay, finish it and check again later.")
        print("Chores remaining: ", total_chores - completed_count)
        print()
        print("====ALL CHORES COMPLETED====")
        print("You have completed all your chores for today!")
        print("Now let's safely peek at an infinite loop....")
 



test_value=0
safety_counter=0
while test_value <= 0:
    print("This condition never changes, so this would run forever")
    safety_counter += 1
    if safety_counter == 3:
        print("Stopping here on purpose- a real infinite loop would never stop on its own")
        print("\n==== CHORE CHECKLIST SUMMARY ====")
        break
print("Chores assigned today:", original_count)
print("Chores completed today:", completed_count)
print("Chores remaining today:", total_chores - completed_count)
print("=====================================")
