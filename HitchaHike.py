from colorama import Fore, Style, init
import time
import random
import itertools
def rainbow_text(text):
    colors = [
        "\033[31m",
        "\033[33m",
        "\033[32m",
        "\033[36m",
        "\033[34m",
        "\033[35m",
    ]
    colored_chars = [f"{color}{char}" for char, color in zip(text, itertools.cycle(colors))]
    print("".join(colored_chars))
init(autoreset=True)
again="y"
while again=="y":
  level=input("(d)emon mode, (h)ard mode, (n)ormal mode, (e)asy mode, or (b)aby mode? Press (i) for more info.  ")
  if level=="i":
    print("Baby: 125 hp, 250-500 miles\nEasy: 125 hp, 500-750 miles\nNormal: 100 hp, 500-750 miles\nHard:75 hp, 750-1000 miles\nDemon: 50 hp, 750-1250 miles")
    level=input("(d)emon mode, (h)ard mode, (n)ormal mode, (e)asy mode, or (b)aby mode? Press (i) for more info. ")
    if level=="d":
      health=50
      distance=random.randint(1000,1250)
    if level=="h":
      health=75
      distance=random.randint(750,1000)
    if level=="n":
      health=100
      distance=random.randint(500,750)
    if level=="e":
      health=125
      distance=random.randint(500,750)
    if level=="b":
      health=125
      distance=random.randint(250,500)
  if level=="d":
    health=50
    distance=random.randint(1000,1250)
  if level=="h":
    health=75
    distance=random.randint(750,1000)
  if level=="n":
    health=100
    distance=random.randint(500,750)
  if level=="e":
    health=125
    distance=random.randint(500,750)
  if level=="b":
    health=125
    distance=random.randint(250,500)
  print("You have ",health,"health.")
  print (Fore.CYAN+"You are on a bus ride to the city of Portville")
  time.sleep(0.5)
  print(Fore.CYAN+"Soon the bus crashes on the side of the street and you find yourself the only survivor.")
  time.sleep(1)
  print(Fore.CYAN+"You take out your phone and check the distance from your home. It shows that you are ",distance," miles away.")
  time.sleep(1)
  print(Fore.CYAN+"Because of the second amendment, you have one revolver inside your pocket with 6 ammunition.")
  ammo=6
  while distance>0 and health>0:
    hitchhike=random.randint(1,3)
  
    if hitchhike==1:
      print(Fore.CYAN+"A car comes over and the person inside asks if you want to hitchhike.")
      mood=random.randint(0,6)
      time.sleep(1)
      hyon=input(Fore.YELLOW+"Hitchhike? (y)es or (n)o?: ")
      if hyon not in ['y', 'n']:
        print(Fore.RED + "Invalid input. Please type 'y' or 'n'.")
        continue
      if hyon=='y':
        print(Fore.CYAN+"Boarding car...")
        if mood <=2:
          time.sleep(2)
          print(Fore.RED+"OH NO THE DRIVER IS DANGEROUS")
          time.sleep(0.1)
          risk=input(Fore.YELLOW+"Do you want to try to fight him? (y)es or (n)o: ")
          dmg=random.randint(5,50)
          if risk=="y":
            yourdmg=random.randint(5,25)
            if yourdmg>=dmg:
              health-=2
              print(Fore.GREEN+"Luckily, you manage to fight your way out of the situation and run. You manage to get away losing only 2hp. Your health is ",health,".")
            if yourdmg<dmg:
              print(Fore.RED+"He is stronger than you and you cannot defeat him.")
              print(Fore.RED+"He attacks you dealing",dmg)
              health-=dmg
          if risk=="n":
            print(Fore.RED+"He attacks you dealing",dmg)
            time.sleep(0.5)
            health-=dmg
             
        if mood >2:
          time.sleep(2)
          print(Fore.GREEN+"The driver is safe\nHe takes you on his car")
          distance-=(random.randint(50,250))
          if distance<0:
            print(Fore.CYAN+"You arrive in Portville")
          else:
            print(Fore.YELLOW+"You are now",distance,"miles away from your destination")
      if hyon=='n':
        print(Fore.YELLOW+"You decided to be safe and not go on the car... You are ",distance, " miles from your destination.")
    else:
      encounter=random.randint(1,3)
      time.sleep(2)
      print(Fore.CYAN+"You have no luck finding cars that are willing to hitchhike")
      option=int(input(Fore.YELLOW+"Do you want to \n(1)Walk a distance\n(2)Search the area for ammo or food\n(3)Check your health\n(4)Check distance left\n: "))
      time.sleep(1)
      if option not in [1, 2, 3, 4]:
        print(Fore.RED + "Invalid input. Please type 1 or 2.")
        continue
      if encounter==1:
          zombies=random.randint(1,5)
          print(Fore.RED+"You encounter",zombies,"zombies")
          if ammo>=zombies:
            time.sleep(1)
            print(Fore.GREEN+"You use your revolver and kill the zombies")
            ammo-=zombies
            print(Fore.YELLOW+"You have",ammo,"ammo left from killing the zombies")
          else:
            time.sleep(1)
            print(Fore.RED+"The zombies attack you, and you dont have enough ammo to kill them!")
            health-=random.randint(20,30)
            if health>0:
              print(Fore.YELLOW+"You now have",health,"health left.")
      if option==1:
        distance-=random.randint(10,20)
        time.sleep(0.5)
        if distance<0:
          print(Fore.CYAN+"You arrive in portville")
        else:
          print(Fore.YELLOW+"You walk for a while, you now have",distance,"miles left.")
      if option==2:
        earn=0
        luckammo=random.randint(0,3)  
        if luckammo==1:  
          gain=random.randint(1,5)
          ammo+=gain
          time.sleep(0.5)
          earn+=1
          print(Fore.YELLOW+"You got",gain,"ammo now you have",ammo,"ammo")
        luckbread=random.randint(0,3)
        if luckbread==2:
          print(Fore.YELLOW+"You find some bread.")
          earn+=1
          keepbread=input(Fore.YELLOW+"Eat? (y)es or (n)o?:")
          if keepbread not in ['y', 'n']:
            print(Fore.RED + "Invalid input. Please type 'y' or 'n'.")
            continue
          if keepbread=="y":
            health=health+3
            print(Fore.GREEN+"You eat the bread and you gain 3 health. Your health is ", health,".")
        luckmeat=random.randint(0,3)
        if luckmeat==3:
          print(Fore.YELLOW+"You find some meat BE CAREFUL IT HAS CHANCE OF POISONING YOU!!!.")
          earn+=1
          keepmeat=input(Fore.YELLOW+"Eat? (y)es or (n)o?:")
          if keepmeat not in ['y', 'n']:
            print(Fore.RED + "Invalid input. Please type 'y' or 'n'.")
            continue
          if keepmeat=="y":
            randmeat=random.randint(1,3)
            if randmeat==1:
              health=health-2
              if health>0:
                print(Fore.RED+"Oh no! It's poisonous! You lose 2 hp. Your health is ", health,".")
              else:
                print(Fore.RED+"Oh no! It's poisonous! You lose 2 hp.")
            if randmeat==2:
              health=health+5
              print(Fore.GREEN+"You eat it and gain 5 hp. Your health is ", health,".")
            if randmeat==3:
              health=health+10
              print(Fore.GREEN+"You eat it. It tastes great and gain 10 hp. Your health is ", health,".")
        if earn==0:
          print(Fore.YELLOW+"You found nothing...")
      if option==3:
        time.sleep(1.5)
        print(Fore.YELLOW+"You have",health,"health left")
      if option==4:
        print(Fore.YELLOW+"You check your phone for the distance remaining till you reach portville...")
        time.sleep(1.5)
        print(Fore.YELLOW+"You still have",distance,"miles left on your journey.")
  if health<=0:
    print(Fore.RED+"GG you died")
    again=input("Play again? (y) or (n). ")
  else:
    rainbow_text("CONGRATS YOU'RE SAFE BACK HOME!!!")
    again=input("Play again? (y) or (n). ")
