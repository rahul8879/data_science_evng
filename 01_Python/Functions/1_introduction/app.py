

list_of_user =["Rahul", "Anjali", "Priya", "Amit"]
def test(a, b):
    '''This function returns the greater of two numbers'''
    if a > b:
        print("a is greater")
        return a
    else:
        return b
    

def test2(x, y=10):
    '''This function returns the sum of two numbers, with a default value for y'''
    return x + y


def test3(name="Guest"):
    print("Hello", name)


def add_user(user_name):
    list_of_user.append(user_name)
    return list_of_user

def login(user_name):
    if user_name in list_of_user:
        return True
    else:
        return False
    
def compute_hcf(x, y):
    """This function returns the HCF of two numbers"""
    hcf = 1
    for i in range(1, min(x, y) + 1):
        if x % i == 0 and y % i == 0:
            hcf = i
    return hcf


