Secret_num = float(12)
Guss = ""
Gusses = 0
Guss_limit = 5
print("WELCOME TO A GUESSING GAME")

while Guss != Secret_num and Gusses != Guss_limit:
    Guss = input("please enter a number:")
    if not Guss.isdigit():
        print("wrong, please number only")

        continue
    Guss = int(Guss)
    Gusses += 1

    if Guss == Secret_num and Guss != Guss_limit:
     print("yor guss is correct")
     break
    else:
     print("your guess is incorrect")


    if Guss == Guss_limit:
        print("sorry! you are out of gusses")

        break


















