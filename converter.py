"""Master converter file containing all conversion logic"""

# TODO:
# - finish creating all the convert methods
# - find volume of duck
# - print duck emojis
# - make flask app and endpoints
# - make ui
# - add other conversions not in the unitconvert module?



from unitconvert.digitalunits import DigitalUnit
from unitconvert.lengthunits import LengthUnit
from unitconvert.timeunits import TimeUnit
from unitconvert.volumeunits import VolumeUnit
from unitconvert.massunits import MassUnit
from unitconvert.temperatureunits import TemperatureUnit

class Converter:

    def convert_length(self, amount, unit):

        inches = LengthUnit(amount, unit, 'in').doconvert()
        return inches/23

    def convert_height(self, amount, unit):

        inches = LengthUnit(amount, unit, 'in').doconvert()
        return inches/4.5

    def convert_weight(self, amount, unit):

        lbs = MassUnit(amount, unit, 'lb').doconvert()
        return lbs/2.55

    # TODO
    def convert_volume(self, amount, unit):

        lbs = VolumeUnit(amount, unit, 'lb').doconvert()
        return lbs/2.55

    def convert_temp(self, amount, unit):

        temp = TemperatureUnit(amount, unit, 'F').doconvert()
        return temp/107.5
