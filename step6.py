a = int(input('add you result:'))
b = int(input('add you aim:'))
result_days = 1
result_km = a
while result_km < b:
        a = a + 0.1 * a
        result_days += 1
        result_km = result_km + a
print(f"you will you aim on  %.d " % result_days)