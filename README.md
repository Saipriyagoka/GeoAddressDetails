# GeoAddressDetails

## Endpoints:

### getAddressDetails

#### Method: POST

#### Input:

{
    "address": "# 3582,13 G Main Road, 4th Cross Rd, Indiranagar, Bengaluru, Karnataka 560008",
    "output_format": "json"
}

#### Expected Output: 

{
    "address": "3582, 13th G Main Rd, Channakesahava Nagar, HAL 2nd Stage, Doopanahalli, Indiranagar, Bengaluru, Karnataka 560008, India",
    "coordinates": {
        "lat": 12.9658286,
        "lng": 77.63948169999999
    }
}
