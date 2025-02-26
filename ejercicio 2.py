
var = 222

for i in range(var):
    i = i + 1
    division = var / i
    print(division)
    if '.0' in str(division):
        es_primo = False
        break
    else:
        es_primo = True


print()