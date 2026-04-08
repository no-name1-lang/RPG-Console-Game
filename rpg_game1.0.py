import random
import time

name = input('Name your character: ')
statistics = []
statistics.append(name)

print("Loading ", end="", flush=True)

for i in range(50):  
    time.sleep(0.1)  
    progress = "=" * (i // 2) + ">"
    print(f"\rLoading [{progress:<25}]", end="", flush=True)

print()
money = random.randint(5, 10)

if money > 8:
    print(f'OMG. Youre really lucky, because... \n Your balance is as follows {money} money:\n Now your task is to upgrade your characters stats.\n Health:?\n Power:?\n Intelligence:?\n Spend your coins wisely!')
elif 7 <= money < 9:
     print(f'You are richer than 80% of all players, because... \n Your balance is {money} money:\n Now your task is to upgrade your characters stats.\n Health:?\n Power:?\n Intelligence:?\n Spend your coins wisely!')
else:
     print(f'Youre out of luck... \n Your balance is {money} money:\n Now your task is to upgrade your characters stats.\n Health:?\n Power:?\n Intelligence:?\n Spend your coins wisely!')



print("Loading ", end="", flush=True)

for i in range(50):  
    time.sleep(0.1)  
    progress = "=" * (i // 2) + ">"
    print(f"\rLoading [{progress:<25}]", end="", flush=True)

print()
print(f'So you have a responsible mission, you need to level up your character, the whole game depends on it.\nI remind you, your balance {money} money.')

while money > 0:
     a = int(input('Choose what youre going to upgrade (1-3): '))

     if a == 1:
          Health = int(input('Health: '))
          if Health > money:
               print(f'Insufficient funds.\nYour balance is {money} money.')
          else:
               print(f'Health: +{Health}\nDo you have any left {money - Health}')
               statistics.append(Health)
     if a == 2:
          money = money - Health
          Power = int(input('Power: '))
          if Power > money:
               print(f'Insufficient funds.\nYour balance is {money} money.')
          else:
               print(f'Health: +{Power}\nDo you have any left {money - Power}')
               statistics.append(Power)
     if a == 3:
          money = money - Power
          Intelligence = int(input('Intelligence: '))
          if Intelligence > money:
               print(f'Insufficient funds.\nYour balance is {money} money.')
          else:
               print(f'Health: +{Intelligence}\nDo you have any left {money - Intelligence}')
               statistics.append(Intelligence)
     if a == 0 or a > 3:
          print(f'Error')
          continue
     if money == 0:
          break
     
print('So youve completed the initial leveling of your unit.')

for i in range(50):  
    time.sleep(0.1)  
    progress = "=" * (i // 2) + ">"
    print(f"\rLoading [{progress:<25}]", end="", flush=True)

print('Now you need to fight other units in order to level up your own.\nAt the end, the final boss will be waiting for you...')
q = input('Write (1) to continue: ')

if q < 1 or q > 1:
     print('Error')
elif q == 1:
     for i in range(50):  
          time.sleep(0.1)  
          progress = "=" * (i // 2) + ">"
          print(f"\rLoading [{progress:<25}]", end="", flush=True)
     statistics1 = *statistics, sep='\n'
     print(f'An opponent is being selected...\nYour units Stats\n{statistics1}')
     for i in range(100):  
          time.sleep(0.1)  
          rogress = "=" * (i // 2) + ">"
          print(f"\rLoading [{progress:<25}]", end="", flush=True)