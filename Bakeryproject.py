# Aly Batch
# 10.14.19
# Hartwick Bakery

cookies = []
candy = []


def cookie_input():
    for choco in range(0, 6):
        value = int(input(f"Monthly Sale for month {choco+1}:"))
        cookies.append(value)


def candy_input():
    for trix in range(0, 6):
        value = int(input(f"Monthly Sale for month {trix+1}:"))
        candy.append(value)


print("Here we are going to input the monthly sales we have had for cookies sold at the Hartwick Bakery.")
print("Please enter the values for each month and then press enter each time you do. This will bring you to the next line.")
cookie_input()
print("**********")

print("Now let's do the same thing for candy sales.")
candy_input()

def cookie_average():
    print(sum(cookies)/ len(cookies))

def candy_average():
    print(sum(candy) / len(candy))

def cookie_max():
    print(max(cookies))

def cookie_min():
    print(min(cookies))

def most_popular():
    if sum(candy) > sum(cookies):
        return'cookies'
    elif sum(candy) < sum(cookies):
        return 'cookies'
    else:
        return'equal'


