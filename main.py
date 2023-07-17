from getpass import getpass as input

print("epic battle between capulet and montague")
print("pick between R, P or S")
capulet = input("select your move, capulet: ")
montague = input("select your move, montague: ")

if capulet == "R" and montague == "S":
  print("aaaanddddd capulet wins this round!")
elif capulet == "R" and montague == "R":
  print("and all families survive! tis a tie")
elif capulet == "R" and montague == "P":
  print("aaandddd montague strikes win")
elif capulet == "P" and montague == "S":
  print("aaannnddd montague cuts the paper! congrats montague")
elif capulet == "P" and montague == "P":
  print("looks like both families survive and need a shirt because tis a tie!")
elif capulet == "S" and montague == "S":
  print("we may need another fight because tis another draw!")
else:
  print("hmm looks like something is wrong! check if you used 'R', 'P', or 'S'!")
