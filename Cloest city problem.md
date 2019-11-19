# Closest cities

The closest pair problem is a "classic" algorithm for beginning coders. (The closest pair of points problem or closest pair problem is a problem of computational geometry: given n points in metric space, find a pair of points with the smallest distance between them). It has real life significance in many applications. Consider: where are the closest shops? where is the closest hospital?

## RECOMMENDED PRIOR UNDERSTANDING

* Concept of latitude and longitude coordinate system
* Basic trigonometry

## TASK ONE

Given two sets of coordinates, use the haversine formula to determine the distance between them.

The haversine formula determines the great-circle distance between two points on a sphere given their longitudes and latitudes. Where

* d  =  the distance between the two points (along the surface of the sphere),
* r  =  the radius of the sphere,
* φ1  =  latitude of point 1
* φ2  =  latitude of point 2,
* λ1  =  longitude of point 1,
* λ2  =  longitude of point 2.

Then, the distance between those two points is

![](assets/haversine.svg)

NOTE

* You may assume the radius of the earth is 6373 kilometers.
* You will likely need to import your Math library.
* Most programming languages use radians by default so you will need to convert your degree based coordinates to radians using the appropriate function in your Math library.

## TASK TWO

* Download the `cities.csv` file from https://github.com/paulbaumgarten/data-sets
* Load all the coordinates from the CSV file into your program
* Prompt the user for two city names
* Find the distance between the two given cities

## TASK THREE

Given an input of one city name, find the closest other city to it from the data in the CSV file in Task Two.

## REMEMBER

* Your program must include appropriate prompts for the entry of data.
* Error messages and other output need to be set out clearly.
* All variables, constants and other identifiers must have meaningful names.

