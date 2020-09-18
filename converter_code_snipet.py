price = [ 1.08,  2.5 , 60.  , 90.  , 60.  , 12.5 ]
a = [2350, 2400, 2100, 2800, 2100,  400]

print(len(price))
print(len(a))

r = []

print('Maximum Buy:\t\t', max(price))
print('Minimum Buy:\t\t', min(price))

for i in range(0, len(price)):
    r.append(price[i]/a[i])
   
print('List of rent:\t\t', r)

# print(sum(r))
print('Total Properties:\t', len(r))
print('Average Buy/sq ft.:\t',sum(r)/len(r))
