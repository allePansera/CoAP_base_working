import logging

import aiocoap, aiocoap.resource as resource, aiocoap.numbers as numbers
import time
from kpn_senml import *
from Model.Sensor.TemperatureSensor import TemperatureSensor

class CoreTemperatureSensorResource(resource.Resource):
    """This class defines the Sensor Resource under CoRE link format"""

    def __init__(self, sensorID, sensorDescription):
        super().__init__()
        self.sensorID, self.sensorDescription = sensorID, sensorDescription
        # defines the attribute interface
        self.if_ = "core.s"
        # defines content type attribute
        self.ct = numbers.media_types_rev['application/senml+json'] #->40
        # defines resource type attribute
        self.rt = "it.unimore.device.temperature"
        self.sensor = TemperatureSensor(id=self.sensorID, description=self.sensorDescription)

    def buildSenMLJson(self):
        """This method allows the generation of the SenML repr. of a temperature resource"""
        pack = SenmlPack(self.sensorID)
        print("Temperature creation")
        temp = SenmlRecord("temperature",
                           unit=SenmlUnits.SENML_UNIT_DEGREES_CELSIUS, # defines u attribute
                           value=self.sensor.value, # defines v attribute
                           time=int(time.time())) # defines t attribute
        pack.add(temp)
        print("Temperature build")
        return pack.to_json()

    async def render_get(self, request):
        self.sensor.generateRandom()
        payload = self.buildSenMLJson()
        return aiocoap.Message(content_format=self.ct,
                               payload=payload.encode('utf-8'))

