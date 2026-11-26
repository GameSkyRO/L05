def check_password(pw):
    print(pw)
    if (len(pw) < 10): 
      print("Password must have at least 10 characters")
    return len(pw) >= 10