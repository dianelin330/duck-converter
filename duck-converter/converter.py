"""Master converter class containing all conversion logic"""

# TODO:
# X finish creating all the convert methods
# X find volume of duck
# - print duck emojis
# - make flask app and endpoints
# - make ui
# - add other conversions not in the unitconvert module?
import emoji

from unitconvert.massunits import MassUnit
from unitconvert.timeunits import TimeUnit
from unitconvert.lengthunits import LengthUnit
from unitconvert.volumeunits import VolumeUnit
from unitconvert.digitalunits import DigitalUnit
from unitconvert.temperatureunits import TemperatureUnit

class Converter:
    """All measurements are averaged from stats found on the internet
    and are based off of the Mallard, the most common duck species"""

    def convert_mass(self, amount, unit):

        lbs = MassUnit(amount, unit, 'lb').doconvert()
        return lbs/2.55


    def convert_time(self, amount, unit):
        """Returns time divided by average life span"""

        years = TimeUnit(amount, unit, 'yr').doconvert()
        return years/7.5


    def convert_length(self, amount, unit):

        inches = LengthUnit(amount, unit, 'in').doconvert()
        return inches/23


    def convert_height(self, amount, unit):

        inches = LengthUnit(amount, unit, 'in').doconvert()
        return inches/4.5


    def convert_volume(self, amount, unit):
        """Assumes average length of 23 and length of 4.5
        Average width was estimated to be about 3 inches"""
        sqinches = VolumeUnit(amount, unit, 'in3').doconvert()
        return sqinches/310.5


    def convert_storage(self, amount, unit):
        """This is calculated based on the following equation:
        150 lbs = average human weight
        55 TB = average human brain capacity
        2.55 lbs = average duck weight

        55/150 = x/2.55
        x = 0.934999, or TB of average duck brain
        """
        tb = DigitalUnit(amount, unit, 'TB').doconvert()
        return tb/0.934999


    def convert_temp(self, amount, unit):

        temp = TemperatureUnit(amount, unit, 'F').doconvert()
        return temp/107.5

