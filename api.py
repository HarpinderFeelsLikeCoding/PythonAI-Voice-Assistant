import enum
from typing import Annotated
from livekit.agents import llm
import logging

logger = logging.getLogger("temperature-control")
logger.setLevel(logging.INFO)

class Zone(enum.Enum):
    LIVING_ROOM="living_room"
    BEDROOM="bedroom"
    KITCHEN="kitchen"
    BATHROOM="bathroom"
    OFFICE="office"

class AssisstantFnc(llm.FunctionContext):
    def __init__(self) -> None:
        super().__init__()

        self._temperature={
            Zone.LIVING_ROOM: 22,
            Zone.BEDROOM: 20,
            Zone.KITCHEN: 19,
            Zone.BATHROOM: 22,
            Zone.OFFICE: 21
        }
        
    @llm.ai_callable(description="get the ttemperature in a specfic room")

    def get_temperature(self, zone:Annotated[Zone,llm.TypeInfo(description="the specific zone")]):
        logger.info("get temp - zone %s", zone)
        temp = self._temperature[Zone(zone)]
        return f"The temperature in the ${zone} is ${temp}C"
    
    @llm.ai_callable(description="set temperature in a specfic room")
    def set_temperature(self, zone:Annotated[Zone,llm.TypeInfo(description="the temperature to be set")], temp:Annotated[int, llm.TypeInfo(description="the specific temperature")]):
        logger.info("set temp = zone %s, temp: %s", zone, temp)
        self._temperature[Zone(zone)] = temp
        return f"the temperature in the {zone} is now {temp}C"