import logging, asyncio, aiocoap
from aiocoap import *

logging.basicConfig(level=logging.INFO)


async def main():
    protocol = await Context.create_client_context()

    # creating the request to set specific fan rpm
    request = Message(code=aiocoap.PUT, uri='coap://127.0.0.1:5683/fan', payload=str(150).encode())
    try:
        # sending message...
        response = await protocol.request(request).response
    except Exception as e:
        print('Failed to fetch resource:')
        print(e)
    else:
        print("Fan update...")
        response_string = response.payload.decode("utf-8")
        print('Result: %s\nPayload: %r\nPayload String: %s' % (response.code, response.payload, response_string))

    # creating the request to update fan status using post over specific resource
    request = Message(code=aiocoap.POST, uri='coap://127.0.0.1:5683/fan')
    try:
        # sending message...
        response = await protocol.request(request).response
    except Exception as e:
        print('Failed to fetch resource:')
        print(e)
    else:
        print("Fan state changed...")
        response_string = response.payload.decode("utf-8")
        print('Result: %s\nPayload: %r\nPayload String: %s' % (response.code, response.payload, response_string))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())