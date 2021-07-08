import pickle as p
def countrec():
   count = 0
   f = open()
   while True:
      try:
         t = p.load(f)
         if t[2] > 75:
            count = count + 1
            print(t)
      except EOFError:
         print("EOF reached !!")
         break
   print("Number student with per  greater than 75%", count)
countrec()