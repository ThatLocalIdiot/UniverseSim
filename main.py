import random
upQuark = 1
downQuark = 0
electron = -1
x = []
y = []
z = []
index = 0

def checkMovement(i, list):
  if i == upQuark:
    if 0 <= index+1 < len(x):
      if x[index+1] == upQuark:
        print(list[index], x[index+1])
      if x[index-1] == upQuark:
        print(list[index], x[index+1])
    if 0 <= index+1 < len(y):
      if y[index+1] == upQuark:
        print(list[index], y[index+1])
      if y[index-1] == upQuark:
        print(list[index], y[index-1])
    if 0 <= index+1 < len(z):
      if z[index+1] == upQuark:
        print(list[index], z[index+1])
      if z[index-1] == upQuark:
        print(list[index], z[index-1])
    if 0 <= index+1 < len(x):
      if x[index+1] == downQuark:
        print(list[index], x[index+1])
      if x[index-1] == downQuark:
        print(list[index], x[index+1])
    if 0 <= index+1 < len(y):
      if y[index+1] == downQuark:
        print(list[index], y[index+1])
      if y[index-1] == downQuark:
        print(list[index], y[index-1])
    if 0 <= index+1 < len(z):
      if z[index+1] == downQuark:
        print(list[index], z[index+1])
      if z[index-1] == downQuark:
        print(list[index], z[index-1])
    if 0 <= index+1 < len(x):
      if x[index+1] == electron:
        print(list[index], x[index+1])
      if x[index-1] == electron:
        print(list[index], x[index+1])
    if 0 <= index+1 < len(y):
      if y[index+1] == electron:
        print(list[index], y[index+1])
      if y[index-1] == electron:
        print(x[index], y[index-1])
    if 0 <= index+1 < len(z):
      if z[index+1] == electron:
        print(list[index], z[index+1])
      if z[index-1] == electron:
        print(list[index], z[index-1])
  if i == downQuark:
    if 0 <= index+1 < len(x):
      if x[index+1] == upQuark:
        print(list[index], x[index+1])
      if x[index-1] == upQuark:
        print(list[index], x[index+1])
    if 0 <= index+1 < len(y):
      if y[index+1] == upQuark:
        print(list[index], y[index+1])
      if y[index-1] == upQuark:
        print(list[index], y[index-1])
    if 0 <= index+1 < len(z):
      if z[index+1] == upQuark:
        print(list[index], z[index+1])
      if z[index-1] == upQuark:
        print(list[index], z[index-1])
    if 0 <= index+1 < len(x):
      if x[index+1] == downQuark:
        print(list[index], x[index+1])
      if x[index-1] == downQuark:
        print(list[index], x[index+1])
    if 0 <= index+1 < len(y):
      if y[index+1] == downQuark:
        print(list[index], y[index+1])
      if y[index-1] == downQuark:
        print(list[index], y[index-1])
    if 0 <= index+1 < len(z):
      if z[index+1] == downQuark:
        print(list[index], z[index+1])
      if z[index-1] == downQuark:
        print(list[index], z[index-1])
    if 0 <= index+1 < len(x):
      if x[index+1] == electron:
        print(list[index], x[index+1])
      if x[index-1] == electron:
        print(list[index], x[index+1])
    if 0 <= index+1 < len(y):
      if y[index+1] == electron:
        print(list[index], y[index+1])
      if y[index-1] == electron:
        print(x[index], y[index-1])
    if 0 <= index+1 < len(z):
      if z[index+1] == electron:
        print(list[index], z[index+1])
      if z[index-1] == electron:
        print(list[index], z[index-1]) 
  if i == electron:
    if 0 <= index+1 < len(x):
      if x[index+1] == upQuark:
        print(list[index], x[index+1])
      if x[index-1] == upQuark:
        print(list[index], x[index+1])
    if 0 <= index+1 < len(y):
      if y[index+1] == upQuark:
        print(list[index], y[index+1])
      if y[index-1] == upQuark:
        print(list[index], y[index-1])
    if 0 <= index+1 < len(z):
      if z[index+1] == upQuark:
        print(list[index], z[index+1])
      if z[index-1] == upQuark:
        print(list[index], z[index-1])
    if 0 <= index+1 < len(x):
      if x[index+1] == downQuark:
        print(list[index], x[index+1])
      if x[index-1] == downQuark:
        print(list[index], x[index+1])
    if 0 <= index+1 < len(y):
      if y[index+1] == downQuark:
        print(list[index], y[index+1])
      if y[index-1] == downQuark:
        print(list[index], y[index-1])
    if 0 <= index+1 < len(z):
      if z[index+1] == downQuark:
        print(list[index], z[index+1])
      if z[index-1] == downQuark:
        print(list[index], z[index-1])
    if 0 <= index+1 < len(x):
      if x[index+1] == electron:
        print(list[index], x[index+1])
      if x[index-1] == electron:
        print(list[index], x[index+1])
    if 0 <= index+1 < len(y):
      if y[index+1] == electron:
        print(list[index], y[index+1])
      if y[index-1] == electron:
        print(x[index], y[index-1])
    if 0 <= index+1 < len(z):
      if z[index+1] == electron:
        print(list[index], z[index+1])
      if z[index-1] == electron:
        print(list[index], z[index-1])
  return
def updateUniverse(i, list):
  checkMovement(i, list)

for i in range(0, 10):
  x.append(random.randint(-1, 1))
  y.append(random.randint(-1, 1))
  z.append(random.randint(-1, 1))
  
while True:
  for i in x:
    updateUniverse(x[index], x)
    index += 1
  index = 0
  for i in y:
    updateUniverse(y[index], y)
    index += 1
  index = 0
  for i in z:
    updateUniverse(z[index], z)
    index += 1
  index = 0
  break

print(x, y, z)