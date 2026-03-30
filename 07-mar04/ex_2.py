def divisor():
    print("_" * 30 + "\n")
    print("*" * 30)
    print("_" * 30 + "\n")

# divisor()

def tests(function):
    print(f"Function: {function.__name__}")
    print("True - ", function("alice"))
    print("False - uppercase -", function("Alice"))
    print("False - starts with digit -", function("4alice"))
    print("False - too short -", function("ab"))
    print("False - too long -", function("abdsgfdsgdsgdsgfg"))

def is_valid_username(username):
    if len(username) >= 4:
        if len(username) <= 16:
                if username.isalnum():
                     if username[0].isalpha():
                        if username.islower():
                            return True
        return False

divisor()
tests(is_valid_username)

def is_valid_username_2(username):
     return (len(username) >= 4
             and len(username) <= 16
             and username.isalnum()
             and username[0].isalpha()
             and username.islower())

divisor()
tests(is_valid_username_2)



def is_valid_username_3(username):
     if len(username) < 4:
        return False
        if len(username) > 16:
         return False
     if not username.isalnum():
        return False
     if not username[0].isalpha():
        return False
     if not username.islower():
        return False
     
     return True

divisor()
tests(is_valid_username_3)

