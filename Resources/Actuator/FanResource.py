import aiocoap, aiocoap.resource as resource, aiocoap.numbers as numbers
import time
from kpn_senml import *
from aiocoap.numbers.codes import Code
from Model.Actuator.Fan import Fan


class CoreFanResource(resource.Resource):
    """This class defines the Fan Resource under CoRE link format"""

    def __init__(self, actuatorID, actuatorDescription):
        super().__init__()
        self.actuatorID, self.actuatorDescription = actuatorID, actuatorDescription
        # defines interface actuator
        self.if_ = "core.a"
        # defines content type actuatore
        self.ct = numbers.media_types_rev['application/senml+json'] # -> 40
        # defines resource type attribute
        self.rt = "it.unimore.device.actuator"
        self.fan = Fan(id=self.actuatorID, description=self.actuatorDescription)

    def buildSenMLJson(self):
        """This method allows the generation of the SenML repr. of a fan resource"""
        pack = SenmlPack(self.actuatorID)
        temp = SenmlRecord("fan",
                           unit="RPM", # there is no available common unit
                           value=self.fan.rpm,
                           time=int(time.time()))
        pack.add(temp)
        return pack.to_json()

    async def render_get(self, request):
        payload = self.buildSenMLJson()
        return aiocoap.Message(content_format=self.ct,
                               payload=payload.encode('utf-8'))

    async def render_post(self, request):
        """This methods handle a change of status of fan"""
        self.fan.changeStatus()
        return aiocoap.Message(code=Code.CHANGED, payload=f"{str(self.fan.status)};{self.fan.rpm}".encode())

    async def render_put(self, request):
        """This methods allow to set RPM values of a FAN updating status"""
        payload = request.payload.decode('utf-8')
        # check if given data is castable to int or float otherwise fan is turned off
        try:
            # if the value is acceptable i update fan status
            rpm = int(payload)
            if rpm <= 0:
                raise Exception()
            self.fan.updateRPM(rpm)
        except Exception as e:
            self.fan.updateRPM(0)
            return aiocoap.Message(code=Code.BAD_REQUEST,payload="Error: wrong payload format".encode())

        return aiocoap.Message(code=Code.CHANGED, payload=f"{str(self.fan.status)};{self.fan.rpm}".encode())