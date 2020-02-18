## Animated signs

--- task ---

1\. To program our Raspberry Pi Sense HAT, we first need to `import` some code to use it's functions. We also can define some colours using RGB (red, green and blue) colour codes. I'm just going to use a code for green and one for nothing(when I want the LED to turn off). To find more colour codes, check out [this website](https://flaviocopes.com/rgb-color-codes/)

+ Add the following lines of code to the top of your program.

```python
from sense_hat import SenseHat
import time

s = SenseHat()
green = (0, 255, 0)
nothing = (0, 0, 0)
```

--- /task ---

--- task ---

2\. The `show_message()` function is used to write a message on the LED matrix. You can change the colour to one of the colours you defined earlier and change the speed that the text scrolls across the screen. The lower the number the faster the text will scroll.

+ Use the `show_message()` function now

```python
from sense_hat import SenseHat
import time

s = SenseHat()
green = (0, 255, 0)
nothing = (0, 0, 0)

s.show_message("Reduce, Reuse, Recycle", text_colour=green, scroll_speed=0.05)
```

--- /task ---

--- task ---

3\. To design your images, create a function for each one. This will allow you to reuse your image as many times as you like. I've created 3 images for one arrow, two arrows and three arrows. These will create the "Reduce, Reuse, Recycle" logo. Each letter in the `logo` grid is one LED in the LED matrix. If you want it green, use `G`. If you want it blank, use `O`.

+ Add some images using the code below to help. Use the `set_pixels()` function to preview your images. You can use `#` to stop the message (just for now).

```python
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

s.set_pixels(three_arrows())
#s.show_message("Reduce, Reuse, Recycle", text_colour=green, scroll_speed=0.05)
```

--- /task ---

--- task ---

4\. Now let's put it all together. We will use a `while` loop to repeat some instructions. You can use `time.sleep(1)` to pause for one second between instructions. My sign will slowly build the three arrows logo, then flash the logo twice before showing my message.

+ Edit your code so that it shows your message and your images repeatedly. 

```python
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
```

--- /task ---