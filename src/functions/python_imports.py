from datetime import datetime
from time import *
from os import *


now = datetime.today().strftime('%Y-%m-%d')
ctime = datetime.today().strftime('%H:%M:%S')
print(f"current date is : {now}")
sleep(2)
print(f"current time is : {ctime}")


current_dir = path.dirname(path.abspath(__file__))
print(f"current dir : {current_dir}")

root_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))
print(f"current dir : {root_dir}")





