i = 0
s = 0

while i <= 63:
    wheats = 2 ** i
    s = s + wheats
    i = i + 1

print("舍罕王应该给达依尔", s, "粒麦子！")
