import random
cards_art=['''
 _________
|A        |
|@   *    |
|   / \   |
|  /_@_\  |
|    !    |
|   ~ ~  @|
|        V|
 ~~~~~~~~~
''','''
 _________
|K |/|\|  |
|@ \- -/  |
| ! |-|   |
|  % I %  |
|   |-| ! |
|  /- -\ @|
|  |\|/| X|
 ~~~~~~~~~
''','''
 _________
|Q |~~~|  |
|@ \- -/  |
| o |-|   |
|  I % I  |
|   |-| o |
|  /- -\ @|
|  |___| Q|
 ~~~~~~~~~
''','''
 ________
|J /~~|_  |
|@ ! -\   |
|  \ -!   |
|  '.\*.  |
|   I- \  |
|   \- I @|
|  ~|__/ P|
 ~~~~~~~~~
''','''
 _________
|10@   @  |
|@   @    |
|  @   @  |
|         |
|  @   @  |
|    @   @|
|  @   @0l|
 ~~~~~~~~~
''','''
 _________
|9 @   @  |
|@        |
|  @   @  |
|    @    |
|  @   @  |
|        @|
|  @   @ 6|
 ~~~~~~~~~
''','''
 _________
|8 @   @  |
|@        |
|  @   @  |
|         |
|  @   @  |
|        @|
|  @   @ 8|
 ~~~~~~~~~
''','''
 _________   
|7        |
|@ @   @  |
|    @    |
|  @   @  |
|         |
|  @   @ @|
|        L|
 ~~~~~~~~~
''','''
 _________
|6        |
|@ @   @  |
|         |
|  @   @  |
|         |
|  @   @ @|
|        9|
 ~~~~~~~~~
''','''
 _________
|5        |
|@        |
|  @   @  |
|    @    |
|  @   @  |
|        @|
|        S|
 ~~~~~~~~~
''','''
 _________
|4        |
|@        |
|  @   @  |
|         |
|  @   @  |
|        @|
|        b|
 ~~~~~~~~~
''','''
 _________
|3        |
|@   @    |
|         |
|    @    |
|         |
|    @   @|
|        E|
 ~~~~~~~~~
''','''
 ________
|2        |
|@        |
|    @    |
|         |
|    @    |
|        @|
|        Z|
 ~~~~~~~~~
''']





logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_/
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def asking():
   ask=input("\nPlease type 'S' if you want to STAND otherwise type 'H' to HIT :  " ).lower()   
   if ask=="h":
      hit()
   elif ask=="s":
      stand()
   else:
      asking()     
def losing():
     print(f"\ndealers deck is {dealer} and its sum is {sum(dealer)}")
     print(f"\nyour deck is {player} and its sum is {sum(player)}")
     print("\nyou lose\n")
def winning(): 
     print(f"\ndealers deck is {dealer} and its sum is {sum(dealer)}")
     print(f"\nyour deck is {player} and its sum is {sum(player)}")
     print("\nyou win\n")   
def tie():  
   print(f"\ndealers deck is {dealer} and its sum is {sum(dealer)}")
   print(f"\nyour deck is {player} and its sum is {sum(player)}")
   print("\ntie\n")   
def stand():
   while sum(dealer)<=16:
      x=random.choice(cards)
      dealer.append(x) 
   if sum(player)>21  :
      losing()
   elif sum(dealer)>21 :
      winning()   
   elif sum(dealer)<sum(player) :
      winning()
   elif sum(player)<sum(dealer) :  
      losing() 
   else:
      tie()                            
def hit():
    
    y=random.choice(cards)
    player.append(y)

    if sum(player)>21:
       if player.count(11)==1:
          player[player.index(11)]=1      
          if sum(player)>21 :
             losing()
          else:
             print(f"\ndealers deck is [{dealer[0]}] ")
             print(f"\nyour deck is {player} and its sum is {sum(player)}")             
             asking()
       else:
          losing()
    elif sum(player)<=21:
       print(f"\ndealers deck is [{dealer[0]}] ")
       print(f"\nyour deck is {player} and its sum is {sum(player)}")
       asking()            
while 5<8:
   print(logo)
   cards=[11,10,10,10,10,9,8,7,6,5,4,3,2]
   dealer=random.choices(cards,k=2)
   player=random.choices(cards,k=2)
   #print(cards_art[cards.index(player[0])] + cards_art[cards.index(player[1])])
   m=input("\ndo you want to play blackjack if YES type 'Y' otherwise type 'N' :  ").lower()  
   if m=="y":
      print(f"\ndealers deck is [{dealer[0]}]{cards_art[cards.index(dealer[0])]} ")
      print(f"\nyour deck is {player} and its sum is {sum(player)}")
      asking()
   elif m=="n":
      print("\ngood bye!!\n")
      break
   else:
      m







       





    








      

