import logging, asyncio, aiocoap
from aiocoap import *

logging.basicConfig(level=logging.INFO)


async def main():
    protocol = await Context.create_client_context()

    # getting temperature
    request = Message(code=aiocoap.GET, uri='coap://127.0.0.1:5683/temperature')
    try:
        response = await protocol.request(request).response
    except Exception as e:
        print('Failed to fetch resource:')
        print(e)
    else:
        print("Getting temperature")
        response_string = response.payload.decode("utf-8")
        print('Result: %s\nPayload: %r\nPayload String: %s' % (response.code, response.payload, response_string))

    # getting fan
    request = Message(code=aiocoap.GET, uri='coap://127.0.0.1:5683/fan')
    try:
        response = await protocol.request(request).response
    except Exception as e:
        print('Failed to fetch resource:')
        print(e)
    else:
        print("Getting fan status")
        response_string = response.payload.decode("utf-8")
        print('Result: %s\nPayload: %r\nPayload String: %s' % (response.code, response.payload, response_string))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())