# Geoguessr Location Generator


This simple Python script generates a random list of locations for use in creating a map in the Geoguessr game.

The program works by randomly generating a pair of latitude/longitude coordinates, querying that location against the Google Maps Street View API to check if it exists, and saving each valid location in a CSV file. This file can then be imported into Geoguessr when creating a custom map.

### Google Maps API
For more information on the Google Maps API, visit:
https://developers.google.com/maps/documentation/streetview/overview

### Geoguessr
For more information on Geoguessr and to play, vist:
https://www.geoguessr.com
