def check_option(option: str) -> bool:
    if option == "a" or option == "b":
        return True
    else:
        print("\n>>>Wrong choice\n")
        return False
    
    
def check_option_a(option_a: str) -> bool:
    try:
        if int(option_a) < 1 or int(option_a) > 4:
            print("\n>>>Wrong choice\n")
            return False
        else:
            return True
    except Exception:
        print(">>>>>wrong\n")
        return False
    

def check_option_c(option_c: str) -> bool:
    try:
        if int(option_c) < 1 or int(option_c) > 5:
            print("\n>>>Wrong choice\n")
            return False
        else:
            return True
    except Exception:
        print(">>>>>wrong\n")
        return False


