def is_empty(value):
    try:
        return len(value) == 0
    except TypeError:
        return False

if __name__ == "__main__":
    print ("This is from main module")
else:
    print ("This is from imported module")