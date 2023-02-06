import art 
import game_data
import os
print(art.logo)
info=game_data.data
import random 
def picker(info):
  l1=random.choice(info)
  info.remove(l1)
  l2=random.choice(info)
  info.remove(l2)
  return l1,l2
def positions(info,l2):
  nl1=l2
  nl2=random.choice(info)
  info.remove(nl2)
  return nl1,nl2
def compare(c1,c2):
  if c1['follower_count']>c2['follower_count']:
    return 'higher'
  elif c1['follower_count']<c2['follower_count']:
    return 'lower'
  else:
    return 'same'
lost=False
score=0  
c1,c2=picker(info)
while not lost:
  val=compare(c1,c2)
  n1=c1['name']
  n2=c2['name']
  guess=input((f"does {n1} have higher or lower followers than {n2}?: "))
  os.system('cls')
  if guess==val:
    score+=1
    print(f"score:{score}")
  elif val=='same':
    score+=1
    print(f"score:{score}")
  else:
    lost=True
    print(f'game over! you scored:{score}')
  c1,c2=positions(info,c2)
  
