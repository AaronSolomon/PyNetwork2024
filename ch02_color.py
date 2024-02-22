fgRed = '\033[31m'
endColor = '\033[0m'
fgGreen = '\033[32m'
bgGreen = '\033[42m'

print(fgRed, "Good", endColor, "morning")

print(fgGreen, "Good", endColor+bgGreen, "afternoon", endColor)
