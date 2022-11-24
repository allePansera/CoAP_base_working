class Fan:
    """The class defines Fan resource"""
    def __init__(self, id="", description="", rpm=0, status=0, jsonSerialized = None):
        self.id = id
        self.description = description
        self.rpm = rpm
        self.status = status
        if jsonSerialized is not None:
            self.__dict__ = jsonSerialized

    def changeStatus(self):
        """This method changes status, rpm are set to 0"""
        if self.status == 0:
            self.status = 1
        elif self.status == 1:
            self.status = 0
        self.rpm = 0

    def updateRPM(self,rpm):
        """This method allow to set correctly the rpm setting correctly the status.
        If wrong value is given fan is turned off setting rpm to 0"""
        if rpm <= 0:
            self.rpm = 0
            self.status = 0
        else:
            self.status = 1
            self.rpm = rpm