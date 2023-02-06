import art 
import game_data
print(art.logo)
info=game_data.data
import random 
def picker(info):
  l1=random.choice(info)
  info.remove(l1)
  l2=random.choice(info)
  info.remove(l2)
  return l1,l2
def compare(c1,c2):
  if c1['follower_count']>c2['follower_count']:
    return 'higher'
  elif c1['follower_count']<c2['follower_count']:
    return 'lower'
  else:
    return 'same'
lost=False
score=0
while not lost:
  c1,c2=picker(info)
  val=compare(c1,c2)
  n1=c1['name']
  n2=c2['name']
  guess=input((f"does {n1} have higher or lower followers than {n2}?: "))
  if guess==val:
    score+=1
    print(f"score:{score}")
  elif val=='same':
    score+=1
    print(f"score:{score}")
  else:
    lost=True
    print(f'game over! you scored:{score}')
