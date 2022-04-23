from audioop import add
from distutils.log import error
from fastapi import Request, HTTPException
from json.decoder import JSONDecodeError

async def validate_input(request: Request):
    #import pdb;pdb.set_trace()
    try:
        input_payload = await request.json()
    except JSONDecodeError as e:
        raise HTTPException(status_code=400, detail="Invalid JSON")

    address = input_payload.get('address', '')
    output_format = input_payload.get('output_format', '')

    if not address:
        raise HTTPException(status_code=400, detail="Please provide the Address details")
    if not output_format:
        raise HTTPException(status_code=400, detail="Please provide the output_format")
    if output_format not in ['json', 'xml']:
        raise HTTPException(status_code=400, detail="Please provide the output_format as 'json'/'xml' ")
