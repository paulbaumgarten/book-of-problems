# Closest cities

The closest pair problem is a "classic" algorithm for beginning coders. (The closest pair of points problem or closest pair problem is a problem of computational geometry: given n points in metric space, find a pair of points with the smallest distance between them). It has real life significance in many applications. Consider: where are the closest shops? where is the closest hospital?

## RECOMMENDED PRIOR UNDERSTANDING

## RECOMMENDED PACKAGES

## RECOMMENDED RESOURCES

## TASK ONE

| Example input                         | Example output                        |
| ------------------------------------- | ------------------------------------- |
|                                       |                                       |
|                                       |                                       |
|                                       |                                       |

## TASK TWO

## TASK THREE

## REMEMBER

* Your program must include appropriate prompts for the entry of data.
* Error messages and other output need to be set out clearly.
* All variables, constants and other identifiers must have meaningful names.

## ATTRIBUTION/CREDIT

Your task:

* Derive an algorithm based on the Haversine formula (use your 7 step process). 
* Use the your algorithm to find the distance from our classroom to each city. 
* Generate a list in sorted order of every location, from closest to most distant.

Assumptions provided:

* The radius of the earth is 6373 km.
* The coordinates of my classroom @ ISL are: `{"lat": 46.542816, "lng":6.637191}`

Location data: Use any of the following...

* [City information dataset 1](https://github.com/paulbaumgarten/data-sets) - 660 records (good starting point)
* [City information dataset 2](https://github.com/bahar/WorldCityLocations) - ~10 thousand records
* [City information dataset 3](https://github.com/lutangar/cities.json) - ~4 million records!

You will likely need to check the documentation for the math functionality you will require for your programming language:

* [Javascript Math library reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math)
* [Python Math library reference](https://docs.python.org/3/library/math.html)
* [Java Math library reference](https://docs.oracle.com/javase/8/docs/api/java/lang/Math.html)

The haversine formula determines the great-circle distance between two points on a sphere given their longitudes and latitudes.

It holds that where:

* `d` -  the distance between the two points (along the surface of the sphere),
* `r` -  the radius of the sphere,
* `φ1` - latitude of point 1 
* `φ2` - latitude of point 2,
* `λ1` - longitude of point 1,
* `λ2` - longitude of point 2.

then d =

![](img/haversine.svg)
