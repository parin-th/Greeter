import datetime as dt

now = dt.datetime.now()
gmt_hour = now.hour

# Calculate EST by subtracting 4 hours from GMT
est_hour = gmt_hour - 4

# Calculate DST (Daylight Saving Time) hour by subtracting 1 more hour
dst_hour = est_hour - 1

if dst_hour < 1: 
    dst_hour = dst_hour + 24

name = input("Hello! What is your name? ")

if dst_hour < 12:
    print("Good Morning, " + name)
elif 12 < dst_hour < 18:
    print("Good Afternoon, " + name)
else:
    print("Good Night, " + name)
