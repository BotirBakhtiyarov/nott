import os
import time
#cwd = os.getcwd()

#print('could not execute')
os.system('start cmd /c "dir"')
time.sleep(5)
print('could not execute')
os.system('start  cmd /k "dir"')
