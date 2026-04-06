import random
import time
from colorama import init, Fore, Back, Style

name = input(f'{Fore.BLUE}Назови своего героя: ')
stat = []
stat.append(name)

print("Загрузка ", end="", flush=True)

for i in range(50):  
    time.sleep(0.1)  
    progress = "=" * (i // 2) + ">"
    print(f"\rЗагрузка [{progress:<25}]", end="", flush=True)

print()
num = random.randint(5, 10)

if num > 8:
    print(f'ОГО. Да тебе крупно повезло, ведь... \n Твой баланс целых {num} монет:\n Сейчас твоя задача прокачать статы своего персонажа\n Хп:?\n Сила:?\n Интелект:?\n Трать свои монеты рационально!')
elif 7 <= num < 9:
     print(f'ТЫ богаче 80% всех игроков, ведь... \n Твой баланс {num} монет:\n Сейчас твоя задача прокачать статы своего персонажа\n Хп:?\n Сила:?\n Интелект:?\n Трать свои монеты рационально!')
else:
     print(f'Тебе не повезло брат, ведь... \n Твой баланс всего {num} монет:\n Сейчас твоя задача прокачать статы своего персонажа\n Хп:?\n Сила:?\n Интелект:?\n Трать свои монеты рационально!')



print("Загрузка ", end="", flush=True)

for i in range(50):  
    time.sleep(0.1)  
    progress = "=" * (i // 2) + ">"
    print(f"\rЗагрузка [{progress:<25}]", end="", flush=True)

print()
print(f'Итак тебе предстоит ответственная миссия, тебе нужно прокачать своего персонажа, от этого зависит вся игра.\nНапоминаю, твой баланс {num} монет.')

while num > 0:
     a = int(input('Выбирай что будешь прокачивать (1-3): '))

     if a == 1:
          hp = int(input('ХП: '))
          if hp > num:
               print(f'{Fore.RED}Недостаточно средств.\nВаш баланс {num} монет.')
          else:
               print(f'ХП: +{hp}\nУ тебя осталось {num - hp}')
               stat.append(hp)
     if a == 2:
          num = num - hp
          st = int(input('СИЛА: '))
          if st > num:
               print(f'{Fore.RED}Недостаточно средств.\nВаш баланс {num} монет.')
          else:
               print(f'ХП: +{st}\nУ тебя осталось {num - st}')
               stat.append(st)
     if a == 3:
          num = num - st
          inte = int(input('ИНТЕЛЕКТ: '))
          if inte > num:
               print(f'{Fore.RED}Недостаточно средств.\nВаш баланс {num} монет.')
          else:
               print(f'ХП: +{inte}\nУ тебя осталось {num - inte}')
               stat.append(inte)
     if a == 0 or a > 3:
          print(f'{Fore.RED}Ошибка')
          continue
     if num == 0:
          break
     
print('Итак ты завершил начальную прокачку своего юнита.')

for i in range(50):  
    time.sleep(0.1)  
    progress = "=" * (i // 2) + ">"
    print(f"\rЗагрузка [{progress:<25}]", end="", flush=True)

print('Теперь тебе необходимо сражаться с другими юнитами, дабы прокачать своего.\nВ конце тебя будет ждать финальный босс...')
q = input('Напиши (1) чтобы продолжить: ')

if q < 1 or q > 1:
     print(f'{Fore.RED}Ошибка')
elif q == 1:
     for i in range(50):  
          time.sleep(0.1)  
          progress = "=" * (i // 2) + ">"
          print(f"\rЗагрузка [{progress:<25}]", end="", flush=True)
     stat1 = *stat, sep='\n'
     print(f'Идет подбор противника...\nСтаты твоего юнита\n{stat1}')
     for i in range(100):  
          time.sleep(0.1)  
          rogress = "=" * (i // 2) + ">"
          print(f"\rЗагрузка [{progress:<25}]", end="", flush=True)


