#=== COSMIC CALCULATOR ===

#Welcome, Explorer!

#1. Calculate light travel time
#2. Convert kilometers to astronomical units
#3. Explore planetary gravity
#4. Exit


print("Welcome, Explorer!")
print("We have summer travel packages for Earthlings to the following destinations: ")
print("Mars")
print("Jupiter")
print("Saturn")

destination = input("Where would you like to travel? ")

print("You chose ", destination)
Confirmation = input("Are you sure you want to travel to " + destination + "? (yes/no) ")

while Confirmation.lower() != "yes" and Confirmation.lower() != "no":
    print("Invalid choice.")
    Confirmation = input("Please respond with 'yes' or 'no': ")

if Confirmation.lower() == "yes":
    print("Great! Let's check our available packages.")
    
    if destination.lower() == "mars":
        distance_km = 225_000_000  # Average distance from Earth to Mars in kilometers
        light_speed_km_per_s = 299_792  # Speed of light in kilometers per second
        travel_time_seconds = distance_km / light_speed_km_per_s
        travel_time_minutes = travel_time_seconds / 60
        travel_time_hours = travel_time_minutes / 60
        print(f"The light travel time to Mars is approximately {travel_time_hours:.2f} hours.")

    elif destination.lower() == "jupiter":
        distance_km = 778_500_000  # Average distance from Earth to Jupiter in kilometers
        light_speed_km_per_s = 299_792  # Speed of light in kilometers per second
        travel_time_seconds = distance_km / light_speed_km_per_s
        travel_time_minutes = travel_time_seconds / 60
        travel_time_hours = travel_time_minutes / 60
        print(f"The light travel time to Jupiter is approximately {travel_time_hours:.2f} hours.")

    elif destination.lower() == "saturn":
        distance_km = 1_432_000_000  # Average distance from Earth to Saturn in kilometers
        light_speed_km_per_s = 299_792  # Speed of light in kilometers per second
        travel_time_seconds = distance_km / light_speed_km_per_s
        travel_time_minutes = travel_time_seconds / 60
        travel_time_hours = travel_time_minutes / 60
        print(f"The light travel time to Saturn is approximately {travel_time_hours:.2f} hours.")


    else: 
        print("Sorry, we currently do not have travel packages to that destination. Please choose from Mars, Jupiter, or Saturn.")

elif Confirmation.lower() == "no":
    print("No worries! Feel free to explore our other destinations.")
#else: 
    print("Invalid input. Please respond with 'yes' or 'no'.")