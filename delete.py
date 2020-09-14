import os
'''TO GET DATA DAILY DATA OF COVID and REMOVE OLDER ONCES'''
def remove():
 if os.path.exists("data.csv"):
    os.remove("data.csv")
    return True
 return False

if __name__ == '__main__':
    remove()

