# name = "Kenneth Daniely"
# print(name.upper())

# name = "KENNETH DANIELY"
# print(name.lower())

# name = "kenneth daniely"
# print(name.title())

# famous_person = "Albert Einstein"
# famous_quote = (f'{famous_person} once said, "A person who never made a mistake never tried anything new')
# print(famous_quote)

# name = "  Kenneth\t Daniely\n  "
# print(name.strip())


# add = 5+3
# sub = 16-8
# multi = 4*2
# div = 16/2
# print(f"Your results for add, sub, multi, and div are\n add = {add}\n sub = {sub}\n multi = {multi}\n div = {div}\n")
# print(add)
# print(sub)
# print(multi)
# print(div)


# fav_num = 7
# print(f"Your favorite number is {fav_num}")


# Heist total.
heist_money = input("Enter how much money was stolen.\n$ ")

# Robber count input
robbers_count = input("How many robbers took part in the crimne?\n")
if int(robbers_count) <= 1:
	print("No one gets the money. Oh well.")
elif int(robbers_count) == 1:
	robber_1 = input("Enter the name of the first robber:\n ")
elif int(robbers_count) >= 2:
	robber_2 = input("Enter the name of the second robber:\n ")
elif int(robbers_count) >= 3:
	robber_3 = input("Enter the name of the third robber:\n ")
elif int(robbers_count) >= 4:
	robber_4 = input("Enter the name of the fourth robber:\n ")
elif int(robbers_count) <= 5:
	robber_5 = input("Enter the name of the fifth robber:\n ")
else:
	print("That's it?")


# Robber information to be entered.
# robber_1 = input("Enter the name of the first robber:\n ")
# robber_2 = input("Enter the name of the second robber:\n ")
# robber_3 = input("Enter the name of the third robber:\n ")
# robber_4 = input("Enter the name of the fourth robber:\n ")
# robber_5 = input("Enter the name of the fifth robber:\n ")

# Calculation of the money to be spilt up.
heist_split = int(heist_money) / 5

# Format messaging for the robbery messages.
split_1 = f"{robber_1}'s cut will be {heist_split}"
split_2 = f"{robber_2}'s cut will be {heist_split}"
split_3 = f"{robber_3}'s cut will be {heist_split}"
split_4 = f"{robber_4}'s cut will be {heist_split}"
split_5 = f"{robber_5}'s cut will be {heist_split}"

# Result messages of the money split.
print(f"{split_1}\n,{split_2}\n,{split_3}\n,{split_4}\n,{split_5}\n.")

