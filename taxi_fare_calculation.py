def calculate_fare(trips):
    base_fare = 50
    fare_per_km = 10
    total_fare = 0
    trip_fares = []
    
    for i, distance in enumerate(trips):
        trip_fare = base_fare + distance * fare_per_km
        trip_fares.append(trip_fare)
        print(f"Trip {i + 1}: ${trip_fare}")
        total_fare += trip_fare
    
    print(f"Total Fare: ${total_fare}")

trips = [5, 10, 3]
calculate_fare(trips)
