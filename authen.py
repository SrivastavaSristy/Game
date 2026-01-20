def auth_user(name, level, coins, db):
    if not name or not level or not coins:
        print("Enter all rrequired details")
    if name  not in db:
        db[name] = {"name":name, "level": level,"coins":coins }
        print(f"user is: {name} tyagi")     

def login(name, level, coins, db):
    if name not in db:
        return "Login failed: user not found"

    return f"Login successful: Welcome {name}"   

# changes 
        
