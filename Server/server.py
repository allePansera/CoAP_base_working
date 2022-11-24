import logging, asyncio, aiocoap.resource as resource, aiocoap
from Resources.Actuator.FanResource import CoreFanResource
from Resources.Sensor.TemperatureSensorResource import CoreTemperatureSensorResource

logging.basicConfig(level=logging.INFO)
logging.getLogger("coap-server").setLevel(logging.INFO)

def main():
    # Resource tree creation
    root = resource.Site()
    # define ids
    fanID, fanDescription = "urn:demo-smartfan-0001", "fan-Toshiba"
    sensorID, sensorDescription = "urn:demo-smartsensor-000A", "sensor-Mitsubishi"
    # Add WellKnownCore Resource to support the standard Resource Discovery
    root.add_resource(['.well-known', 'core'], resource.WKCResource(root.get_resources_as_linkheader, impl_info=None))
    root.add_resource(['temperature'], CoreTemperatureSensorResource(sensorID, sensorDescription))
    root.add_resource(['fan'], CoreFanResource(fanID, fanDescription))
    asyncio.Task(aiocoap.Context.create_server_context(root, bind=('127.0.0.1', 5683)))
    asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    main()