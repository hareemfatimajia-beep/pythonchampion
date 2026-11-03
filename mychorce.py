total_chores = 4
count = total_chores
print(f" You have {count} choers to finish today\n")

completed_count = 0
chores_nums = 1

while chores_nums <= total_chores:

    if chores_nums == 1: next_chore = "Make your bed"
    elif chores_nums == 2: next_chore = "Feed the pet"
    elif chores_nums == 3: next_chore = "Take out the trash"
    else: next_chore ="Wash the dishes"

    answer = input(f"Have you finished: {next_chore} (yes\ no):")


    if answer == "yes":
        completed_count += 1
        chores_nums +=1 
        print("Great job! Chore completed.")
    else:
        print("Okay, finish it and check again!")

    print("Chorce remaning :", total_chores - completed_count)
    print()

test_value = 0 
safety_counter = 0
while test_value <= 0:
    print("This condition never changes, so this would run forever!")
    safety_counter += 1
    if safety_counter == 3:
        print("Stopping here on purpose - a real infinite loop never stops on its own!")
        break
    