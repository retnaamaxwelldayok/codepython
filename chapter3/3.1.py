passes = 0
failures = 0
for students in range(10):
    result = int(input("Enter result (1 = pass, 2 = failure): "))
    while 1 < result > 2:
        if 1 != result != 2:
            result = int(input("Please enter (1 = pass, 2 = failure) no dey whine me: "))
    if result == 1:
        passes = passes + 1
    elif result == 2:
        failures = failures + 1

print("Passed: ", passes)
print("Failed: ", failures)

if passes > 8:
    print("Bonus to instructor")
