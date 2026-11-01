
#weight = mass * gravity

gravityearth = 9.81
gravitymars = 3.71
gravityjupiter = 24.79
gravitysaturn = 10.44

# to choose a planet.
mass = float(input("Hey dude, what is your body mass in kilograms? "))
planet = input("On which planet are you? (Earth/Mars/Jupiter/Saturn) ").strip().lower()

if planet == "earth":
    weight = mass * gravityearth
elif planet == "mars":
    weight = mass * gravitymars
elif planet == "jupiter":
    weight = mass * gravityjupiter
elif planet == "saturn":
    weight = mass * gravitysaturn
else:
    print("Invalid planet selection.")
    exit()

print(f"Your weight on {planet.capitalize()} is: {weight:.2f} Newtons")
