##Given a variable `a` (containing any value), re-assign the value `"N/A"` if `a` is `None`,
# and leave `a` unchanged otherwise. Use an `if...else...` statement.

a=100
if a is None:
    a='N/A'
    print(a)
else:
    print(a)

a='N/A' if a is None else a
print(a)

#Given an credit score `score`, assign a string value to another variable `rating` based on the following scale:



credit_score = 820
if credit_score <= 580:
    print('POOR')
elif credit_score >= 580 and credit_score <= 670:
    print('Fair',credit_score)
elif credit_score >= 670 and credit_score <= 740:
    print('Good')
elif credit_score >= 740 and credit_score <= 800:
    print('Very Good')
else:
    print('EXCELLENT')
print(credit_score)


seconds_in_minute = 60
seconds_in_hour = 60 * seconds_in_minute
seconds_in_day = 24 * seconds_in_hour
seconds_in_week = 7 * seconds_in_day

s = 'FfEeDdCcBbAa'
reversed_s=s[::-1]
print(reversed_s)

t1 = 1, 2, 3, 4, 5, 6
t2 = 7, 8, 9, 10
t3 = 11, 12, 13, 14, 15, 16, 17

l1=list(t1)
l2=list(t2)
l3=list(t3)


l1[::2] = [0, 0, 0]
print(l1)
l2[::2] = [0, 0]
print(l2)
l3[::2] = [0, 0, 0, 0]
print(l3)

s = 'Π, ύ, θ, ω, ν'
chars = s.split()
print(chars)


m=3
n=4

for row in range(1,m+1):
    for col in range(1,n+1):
        print(f'{row}*{col}={row*col}')
    print('_'*15)

