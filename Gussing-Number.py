import random
import time
winningNumber =  random.randint(1,100)
# print(winningNumber)

print('''

   ____                       _                     _   _                       _                   
  / ___|  _   _   ___   ___  (_)  _ __     __ _    | \ | |  _   _   _ __ ___   | |__     ___   _ __ 
 | |  _  | | | | / __| / __| | | | '_ \   / _` |   |  \| | | | | | | '_ ` _ \  | '_ \   / _ \ | '__|
 | |_| | | |_| | \__ \ \__ \ | | | | | | | (_| |   | |\  | | |_| | | | | | | | | |_) | |  __/ | |   
  \____|  \__,_| |___/ |___/ |_| |_| |_|  \__, |   |_| \_|  \__,_| |_| |_| |_| |_.__/   \___| |_|   
                                          |___/                                                     

''')
count = 1
try:
    print('\t\t\t\t:: Note - Enter only integer values ::')
    time.sleep(2)
    print("\nHere we goo...")
    time.sleep(1)
    user = int(input("\nGusse a number Betweeen 1 to 100 : "))
    while(True):
        if(winningNumber==user):
            print(f'You Winn, and you gusses this number in {count} itmes ')
            break
        else:
            if(user>winningNumber):
                print("Too High")
            else:
                print('Too Low')
        count += 1
        user = int(input('Try Again : ')) 
except:
    print('\nInvaild Input !!')


