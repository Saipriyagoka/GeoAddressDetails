import requests
from dicttoxml import dicttoxml
from fastapi import FastAPI, Request, Depends, Response

from utils.validation import *
from config import settings

app = FastAPI()

@app.post("/getAddressDetails", dependencies=[Depends(validate_input)])
async def get_address_details(request: Request):
    try:
        input_payload = await request.json()
        
        response_obj = {}

        url = 'https://maps.googleapis.com/maps/api/geocode/json'

        params = {'key': settings.API_KEY,
                  'address': input_payload['address']}

        response = requests.get(url, params)

        if response.status_code == 200 and response.json().get('status', '') == 'OK':
            if response.json().get('results', []):
                result = response.json()['results'][0]
                response_obj['address'] = result.get('formatted_address', '')
                response_obj['coordinates'] = result.get('geometry', {}).get('location', {})

        if input_payload.get('output_format', 'json') == 'xml':
            return Response(content=dicttoxml(response_obj), media_type="application/xml")

        return response_obj

    except Exception as error:
        print(error)
        return 'Something went wrong, we are checking it.'