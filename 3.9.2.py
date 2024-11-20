SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60

h1 = int(input("enter the hours (first interval): "))
m1 = int(input("enter the minutes (first interval): "))
s1 = int(input("enter the seconds (first interval): "))

h2 = int(input("enter the hours (second interval): "))
m2 = int(input("enter the minutes (second interval): "))
s2 = int(input("enter the seconds (second interval): "))

result1 = h1 * SECONDS_PER_HOUR + m1 * SECONDS_PER_MINUTE + s1

result2 = h2 * SECONDS_PER_HOUR + m2 * SECONDS_PER_MINUTE + s2

total = result1 + result2

hours = int(total / SECONDS_PER_HOUR)
minutes = (total % SECONDS_PER_HOUR) // SECONDS_PER_MINUTE
seconds =  total - hour * SECONDS_PER_HOUR + minutes * SECONDS_PER_MINUTE

print('the solution is: ' hours ', hours,' minutes' minutes and ' seconds 'seconds')

