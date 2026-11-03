#=== COSMIC CALCULATOR ===

#Welcome, Explorer!

#1. Calculate light travel time
#2. Convert kilometers to astronomical units
#3. Explore planetary gravity
#4. Exit

def calculate_light_time(distance_km):
    light_speed_km_per_s = 299_792  # Speed of light in kilometers per second
    travel_time_seconds = distance_km / light_speed_km_per_s
    travel_time_hours = travel_time_seconds / 3600
    return travel_time_hours


def show_destinations():
    print("Welcome, Explorer!")
    print("We have summer travel packages for Earthlings!")
    print("Mars")
    print("Jupiter")
    print("Saturn")


def confirm_destination(confirmation):
    while confirmation.lower() not in ("yes", "no"):
        print("Invalid choice.")
        confirmation = input("Please respond with 'yes' or 'no': ")

    return confirmation


def main():
    show_destinations()
    destination = input("Where would you like to travel? ")

    print("You chose ", destination)
    confirmation = input("Are you sure you want to travel to " + destination + "? (yes/no) ")

    confirmation = confirm_destination(confirmation)

    if confirmation.lower() == "yes":
        print("Great! Let's check our available packages.")
        
        if destination.lower() == "mars":
            distance_km = 225_000_000  # Average distance from Earth to Mars in kilometers
            travel_time_hours = calculate_light_time(distance_km)
            print(f"The light travel time to Mars is approximately {travel_time_hours:.2f} hours.")

        elif destination.lower() == "jupiter":
            distance_km = 778_500_000  # Average distance from Earth to Jupiter in kilometers
            travel_time_hours = calculate_light_time(distance_km)
            print(f"The light travel time to Jupiter is approximately {travel_time_hours:.2f} hours.")

        elif destination.lower() == "saturn":
            distance_km = 1_432_000_000  # Average distance from Earth to Saturn in kilometers
            travel_time_hours = calculate_light_time(distance_km)
            print(f"The light travel time to Saturn is approximately {travel_time_hours:.2f} hours.")


        else: 
            print("Sorry, we currently do not have travel packages to that destination. Please choose from Mars, Jupiter, or Saturn.")

    elif confirmation.lower() == "no":
        print("No worries! Feel free to explore our other destinations.")

#else: 
#   print("Invalid input. Please respond with 'yes' or 'no'.")]

if __name__ == "__main__":
    main()