def format_itineraries(itineraries):
    result = []
    
    for index, (traveler_name, origin, destination) in enumerate(itineraries, start=1):
    
        itinerary = f"itinerary {index}: {traveler_name} - from {origin} to {destination}"
        result.append(itinerary)
    
    return "\n".join(result)


itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
formatted_itineraries = format_itineraries(itineraries)
print(formatted_itineraries)