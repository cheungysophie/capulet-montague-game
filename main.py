from getpass import getpass as input

print("epic battle between capulet and montague")
print("pick between R, P or S")

capScore = 0
monScore = 0

while True:
  if capScore == 3:
    print("cap win")
    break
  elif monScore == 3:
    print("mon win")
    break
  else:
    capulet = input("select your move, capulet: ")
    montague = input("select your move, montague: ")
    if (capulet == "R" and montague == "S") or (capulet == "P" and montague == "R") or (capulet == "S" and montague == "P"):
      print("aanddddd capulet wins this round!")
      capScore += 1
      continue
    elif (capulet == "R" and montague == "P") or (capulet == "P" and montague == "S") or (capulet == "S" and montague == "R"):
      print("andddd montague strikes win")
      monScore += 1
      continue
    elif (capulet == "P" and montague == "P") or (capulet == "S" and montague == "S") or (capulet == "R" and montague == "R"):
      print("looks like both families survive and need a shirt because tis a tie!")
      continue
    else:
      print("hmm something is wrong! check if you used 'R', 'P', or 'S'!")
      continue 
print("lets hope the star-crossed lovers get to reunite in another world")
