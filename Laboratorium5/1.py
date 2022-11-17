values = [10, 20, 30]
keys = ["ten", "twenty", "thirty"]
print("1", list(zip(keys, values)))

z_1 = dict(zip(keys, values))

print("2", z_1)
z_1 = {}
for i in range(len(values)):
    z_1[keys[i]] = values[i]
print("3", z_1)

z_2 = dict(thirty = 33, fourty = 40, fifty = 50)
print("4", z_2)

z_3 = z_1.copy()
z_3.update(z_2)

print("5", z_3)


