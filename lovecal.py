#this is a love calculator to check whether you love is true or not
print("The Love calculator is calculation your score...")

#name input
name1 = input("What is your name?\n").lower()
name2 = input("What is their name?\n").lower()

#concatinating the name
true_name = name1 + name2
love_name = name1 + name2


#count letters from name
letter_t = true_name.count("t")
letter_r = true_name.count("r")
letter_u = true_name.count("u")
letter_e = true_name.count("e")
letter_l = love_name.count("l")
letter_o = love_name.count("o")
letter_v = love_name.count("v")


#adding letters
score1 = letter_t + letter_r + letter_u + letter_e
score2 = letter_l + letter_o + letter_v + letter_e

#final Score
final_score = str(score1) + str(score2)
love_score = int(final_score)

#printing output based on condition
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")


print(final_score)