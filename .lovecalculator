
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


name1 = name1.lower()
name2 = name2.lower()

love_score1 = 0
love_score2 = 0
love_score3 = 0
love_score4 = 0
love_score5 = 0
love_score6 = 0
love_score7 = 0
love_score8 = 0

love_part_1 = 0
love_part_2 = 0

if name1.count("t") or name2.count("t"):
    love_score1 = name1.count("t") + name2.count("t")

if name1.count("r") or name2.count("r"):
   love_score2 = name1.count("r") + name2.count("r")
    
if name1.count("u") or name2.count("u"):
    love_score3 = name1.count("u") + name2.count("u")
    
if name1.count("e") or name2.count("e"):
    love_score4 = name1.count("e") + name2.count("e")

love_part_1 = love_score1 + love_score2 + love_score3 + love_score4

if name1.count("l") or name2.count("l"):
    love_score5 = name1.count("l") + name2.count("l")
    
if name1.count("o") or name2.count("o"):
    love_score6 = name1.count("o") + name2.count("o")
    
if name1.count("v") or name2.count("v"):
    love_score7 = name1.count("v") + name2.count("v")
    
if name1.count("e") or name2.count("e"):
    love_score8 = name1.count("e") + name2.count("e")
    
love_part_2 = love_score5 + love_score6 + love_score7 + love_score8
love_part_2 = str(love_part_2)
love_part_1 = str(love_part_1)
love_part_final = love_part_1 + love_part_2
love_part_final_int = int(love_part_final)

if love_part_final_int < 10 or love_part_final_int > 90:
    print(f"Your score is {love_part_final}, you go together like coke and mentos.")
    
elif love_part_final_int >=40 and love_part_final_int <= 50:
    print(f"Your score is {love_part_final}, you are alright together.")
     
else:
    print(f"Your score is {love_part_final}.")
