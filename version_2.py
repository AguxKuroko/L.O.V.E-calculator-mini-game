print("Welcome to the Love Calculator!")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

names = name1 + "" + name2
names = names.lower()

t = names.count("t")
r = names.count("r")
u = names.count("u")
e = names.count("e")

part_1 = t + r + u + e

l = names.count("l")
o = names.count("o")
v = names.count("v")
e = names.count("e")

part_2 = l + o + v + e

final_name = str(part_1) + str(part_2)
final_name_int = int(final_name)

print(final_name)

if (final_name_int < 10) or (final_name_int > 90):
    print(f"Your score is {final_name}, you go together like coke and mentos.")

elif (final_name_int >= 40) and (final_name_int <= 50):
    print(f"Your score is {final_name}, you are alright together.")

else:
    print(f"Your score is {final_name}.")
