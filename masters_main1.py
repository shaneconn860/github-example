#print("Enter grade of first student (first test): ")
#print("second test: "")
#x = int(input())
results = ' '

finished = False
while not finished:
  print("Next student (first test): ")
  x = int(input())
  print("second test: ")
  z = int(input())
  y = x + z
  if y != 51:
    if 0 <= y <= 49:
        print("Fail")
        results += "Fail "
    elif 50 <= y <= 69:
        print("Pass")
        results += "Pass "
    else:
        print("Distinction")
        results += "Distinction "
    #x = y


  elif y == 51:
      finished = True
      print(results)
