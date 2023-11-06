from main import Bulb

bulb = Bulb()
#Test case-1
def test_bulb_isOff():
    assert bulb.getStatus() == "Bulb is not glowing"

def test_bulb_isOn():
    bulb.isOn()
    assert bulb.getStatus() == "Bulb is glowing"



