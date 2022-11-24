import logging, asyncio, link_header
from aiocoap.numbers.codes import Code
from aiocoap import *

logging.basicConfig(level=logging.INFO)


async def main():
    protocol = await Context.create_client_context()
    # resource discovery requests
    request = Message(code=Code.GET, uri='coap://127.0.0.1:5683/.well-known/core')

    try:
        # getting response
        response = await protocol.request(request).response
    except Exception as e:
        print('Failed to fetch resource:')
        print(e)
    else:
        # fetching response
        response_string = response.payload.decode("utf-8")
        print(response_string)
        links_headers = link_header.parse(response_string)
        # printing response
        for link in links_headers.links:
            print('Href: %s\nAttributes: %s' % (link.href, link.attr_pairs))

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())