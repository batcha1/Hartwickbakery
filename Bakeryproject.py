# Aly Batch
# 10.14.19
# Hartwick Bakery

cookies = []  # These are the varibles for cookies and candy.
candy = []


def cookie_input():  # This is my function for cookie input using an abbreviation of choco for chocolate chip
    for choco in range(0, 6):
        value = int(input(f"Monthly Sale for month {choco + 1}:"))
        cookies.append(value)


def candy_input():  # This is my function for cookie input using an abbreviation of trix for trix candy
    for trix in range(0, 6):
        value = int(input(f"Monthly Sale for month {trix + 1}:"))
        candy.append(value)


def cookie_average():  # This is my function to find the cookie averages.
    print(round(sum(cookies) / len(cookies)))


def candy_average():  # Ths is my function to find the candy averages.
    print(round(sum(candy) / len(candy)))


def cookie_max():  # This is my function to find the maximum number of cookie sales
    print(max(cookies))


def cookie_min():  # This is my function to find minimum number of cookie sales
    print(min(cookies))


def candy_max():
    print(max(candy))


# Both of these functions are the same as the one above but for candy instead.
def candy_min():
    print(min(candy))


def most_popular():  # This is my function to find the most popular out of cookies and candy
    if sum(candy) > sum(cookies):
        return 'Candy'
    elif sum(candy) < sum(cookies):
        return 'Cookies'
    else:
        return 'Equal'


# This is where my code actually begins.
print("Here we are going to input the monthly sales we have had for cookies sold at the Hartwick Bakery.")
print(
    "Please enter the values for each month and then press enter each time you do. This will bring you to the next line.")
cookie_input()
print("**********")

print("Now let's do the same thing for candy sales.")
candy_input()
print("************")
print("Here are the averages for the of both cookies and candy.")
print("Cookies:")
cookie_average()
print("Candy")
candy_average()

print("**********")
print("Now we need to know the maximum and minimum cookie and candy sales that have happened at the Hartwick Bakery.")
print("Cookie Max and Min:")
cookie_max()
cookie_min()
print("Candy Max and Min:")
candy_max()
candy_min()

print("*******")
print("Now we can find out which of the two sales is the most popular!")
print(most_popular())
