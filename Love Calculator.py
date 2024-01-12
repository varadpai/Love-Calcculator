print("Welcome to love calculator")
name1 = input("What is the name of first person?")
name2 = input("What is the name of second person?")
combined_name = name1+name2
lower_names = combined_name.lower()
t = lower_names.count('t')
r = lower_names.count('r')
u = lower_names.count('u')
e = lower_names.count('e')

true = t + r + u + e

l = lower_names.count('l')
o = lower_names.count('o')
v = lower_names.count('v')
e = lower_names.count('e')

love = l + o + v + e
final_string = int(str(true) + str(love))

if (final_string < 10) or (final_string > 90):
    print(f"Your love score is {final_string}, you go with each other like coke and mentos")
elif (final_string >= 40) and (final_string <= 50):
    print(f"Your love score is {final_string}, you are alright together")
else:
    print(f"Your love score is {final_string}")