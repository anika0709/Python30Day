# The file that we run always has a __name__ variable with a value of "__main__". That is simply how Python tells us that we ran that file.

# Any file that doesn't have a __name__ equal to "__main__" was imported.

def get_user_age():
    return int(input("Enter your age: "))

if __name__ == "__main__":
    get_user_age()