def convert(hour, minute):
    period = "AM"
    if hour >= 12:
        period = "PM"
    if hour == 0:
        hour = 12
    elif hour > 12:
        hour -= 12
    return "{:02d}:{:02d} {}".format(hour, minute, period)
 
for _ in range(int(input())):
    hour, minute = map(int, input().split(":"))
    print(convert(hour,minute))
