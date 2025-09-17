a = [12,23,7,9,30,45,28,50]
b = [x for x in a if x % 2 == 0]
c = [x for x in a if x % 2 != 0]
d = [x for x in a if x > 25]

print("Pāra skaitļi:", b)
print("Nepāra skaitļi:", c)
print("Skaitļi, kas ir lielāki par 25:", d) 