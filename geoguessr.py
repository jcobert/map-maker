import requests, random

API_Key = "INSERT YOUR GOOGLE MAPS API KEY HERE"
url = "https://maps.googleapis.com/maps/api/streetview/metadata?"

def generate_location():
    latitude = round(random.uniform(-90, 90), 6)
    longitude = round(random.uniform(-180, 180), 6)
    coordinates = f"{latitude},{longitude}"
    return coordinates

def query_map(location):
    query_url = f"{url}location={location}&key={API_Key}"
    response = requests.get(query_url, headers={"Accept": "application/json"})
    data = response.json()
    status_code = data["status"]
    return status_code

def collect_locations(count):
    values = ""
    i = 0
    while i < count:
        loc = generate_location()
        if query_map(loc) == "OK":
            values += loc + ','
            i+=1
    return values

csv = open("locs.csv", "w")
csv.write(collect_locations(5))
csv.close()








   