def pattern(arr):
  output = []
  prod = 1
  for i in arr:
    prod = prod*i
  for j in range(len(arr)):
    output.append(prod/arr[j])
  return output
a = []
n = int(input('Enter the number of elements in the array'))
s = input('Enter the array elements:')
s = (s.split(' '))
for i in range(n):
  a.append(int(s[i]))
output = pattern(a)
print(output)
