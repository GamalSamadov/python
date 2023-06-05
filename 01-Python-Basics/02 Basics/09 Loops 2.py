# Contutinue
x = 0
while x < 100:
    x += 1
    if x % 2 != 0:
        print(x, end=' ')
    else:
        continue  # Skip this iteretion

print()
print('=' * 50)

# Break
x = 1
while True:
    print(x, end=' ')
    x += 2
    if x > 100:
        break
        print('The end')  # Dosn't print this code
print('The end')  # Will Print it

print('=' * 50)

# Else
x = 1
while x < 100:
    print(x, end=' ')
    x += 2
else:
    print('The end')

print('=' * 50)
print()

# Multiple Loop, loop in loop
for i in range(1, 21):
    for j in range(1, 21):
        print(f"{i} x {j} = {i * j}")
    print('_' * 10)

print()
print('=' * 50)
print()

for i in range(4):
    for j in range(4):
        if i == j: break
        print(i, j)

print()
print('=' * 50)
print()

for i in range(4):
    for j in range(4):
        if i == j: continue
        print(i, '*', j, '=', i * j)
