import screen_brightness_control as pct

print(pct.get_brightness())

level = input("Enter brightness level: ")

pct.set_brightness(level)

print(pct.get_brightness())