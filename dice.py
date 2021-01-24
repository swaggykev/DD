import random

def d4():
  rand = random.randint(1,4)
  return rand
  
def d6():
  rand = random.randint(1,6)
  return rand

def d8():
  rand = random.randint(1,8)
  return rand

def d10():
  rand = random.randint(1,10)
  return rand

def d12():
  rand = random.randint(1,12)
  return rand

def d20():
  rand = random.randint(1,20)
  return rand

def d100():
  rand = random.randint(1,100)
  return rand

def total(die,times,addition):
  randtotal = 0
  for x in range(times):
    if die == 'd4':
      randtotal = randtotal + d4()
    elif die == 'd6':
      randtotal = randtotal + d6()
    elif die == 'd8':
      randtotal = randtotal + d8()
    elif die == 'd10':
      randtotal = randtotal + d10()
    elif die == 'd12':
      randtotal = randtotal + d12()
    elif die == 'd20':
      randtotal = randtotal + d20()
    elif die =='d100':
      randtotal = randtotal + d100()
  randtotal = randtotal + addition
  return randtotal
