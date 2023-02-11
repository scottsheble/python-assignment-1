tuition = 8000
print("Year\t", "Current Tuition")
for i in range(1,6):
    tuition += tuition * .03
    print(i, '\t', format(tuition, '12,.2f'))