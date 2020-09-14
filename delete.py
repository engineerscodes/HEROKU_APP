import os
from threading import Timer
from datetime import datetime, timedelta
def remove():
 if os.path.exists("data.csv"):
    os.remove("data.csv")
    return True
 return False

if __name__ == '__main__':
    remove()

