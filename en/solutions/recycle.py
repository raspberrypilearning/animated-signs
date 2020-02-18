from sense_hat import SenseHat
import time

s = SenseHat()
green = (0, 255, 0)
nothing = (0, 0, 0)

def one_arrow():
    G = green
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, G, O, O,
    O, O, O, O, O, O, G, G,
    O, O, O, O, O, O, G, G,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def two_arrows():
    G = green
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, G, O, O,
    O, O, O, O, O, O, G, G,
    O, O, O, O, O, O, G, G,
    O, O, O, O, O, O, O, O,
    O, O, O, G, O, O, O, O,
    O, O, G, G, G, G, G, O,
    O, O, O, G, O, O, O, O,
    ]
    return logo

def three_arrows():
    G = green
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, G, G, O, O, G, O, O,
    O, G, G, O, O, O, G, G,
    G, O, O, O, O, O, G, G,
    O, O, O, O, O, O, O, O,
    O, O, O, G, O, O, O, O,
    O, O, G, G, G, G, G, O,
    O, O, O, G, O, O, O, O,
    ]
    return logo

while True:
    s.set_pixels(one_arrow())
    time.sleep(1)
    s.set_pixels(two_arrows())
    time.sleep(1)
    s.set_pixels(three_arrows())
    time.sleep(.5)
    s.clear()
    time.sleep(.5)
    s.set_pixels(three_arrows())
    time.sleep(.5)
    s.clear()
    time.sleep(.5)
    s.set_pixels(three_arrows())
    time.sleep(1)
    s.show_message("Reduce, Reuse, Recycle", text_colour=green, scroll_speed=0.05)