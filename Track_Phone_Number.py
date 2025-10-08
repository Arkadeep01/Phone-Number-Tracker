import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import folium
from opencage.geocoder import OpenCageGeocode
from phone_number import number
import os
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())
KEY = os.getenv("GEO_CODER_API_KEY")

check_number = phonenumbers.parse(str(number))

# Getting Location
number_location = geocoder.description_for_number(check_number, "en")
print(number_location)

# Getting Service Provider
service_provider = carrier.name_for_number(check_number, "en")
print(service_provider)

# Getting Time Zones
time_zones = timezone.time_zones_for_number(check_number)
print(time_zones)

# Getting Exact Location
geocoder = OpenCageGeocode(KEY)
query = str(number_location)

if query:
    results = geocoder.geocode(query)
    if results:
        lat = results[0]['geometry']['lat']
        lng = results[0]['geometry']['lng']
        print(f"Approximate coordinates of {number_location}: {lat}, {lng}")
    else:
        print("Geocoding failed — no results found.")
else:
    print("No region found for this number.")

# Generating Map
map_location = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=number_location).add_to((map_location))
map_location.save("Location.html")