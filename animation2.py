print("animation2")
import init
import functions
import config
import time
import statemachine
import math
import init
import button

##
##  Copyright 2013 Paradise Arcade Shop, ParadiseArcadeShop.com
##  All rights reserved.  Use is subject to license terms.
##
##  Code is provided for entertainment purposes and use with the Kaimana controller.
##  Code may be copied, modified, resused with this Copyright notice.
##  No commercial use without written permission from Paradise Arcade Shop.
##
##  Paradise Arcade Shop Kaimana LED Driver Board
##  Initial Release October 15, 2013
##
##  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
##  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
##  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
##  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
##  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
##  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
##  THE SOFTWARE.
##
##  Kaimana animations based on original source released by ParadiseArcadeShop.com October 15, 2013
##

## initialize idle_mode3()
color_cycle_data = [
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,

    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,

    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,

    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,

    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,

    0,   2,   4,   6,   8,  10,  12,  14,  16,  18,  20,  22,  24,  26,  28,  30,
   32,  35,  38,  41,  44,  47,  50,  53,  56,  59,  62,  65,  68,  71,  74,  77,
   81,  85,  89,  93,  97, 101, 105, 109, 113, 117, 121, 125, 129, 133, 137, 141,
  148, 155, 162, 169, 176, 183, 190, 197, 204, 211, 218, 225, 232, 239, 246, 253,

  255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
  255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
  255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
  255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,

  255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
  255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
  255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
  255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,

  255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
  255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
  255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
  255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,

  255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
  255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
  255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
  255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,

  255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
  255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
  255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
  255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,

  253, 246, 239, 232, 225, 218, 211, 204, 197, 190, 183, 176, 169, 162, 155, 148,
  141, 137, 133, 129, 125, 121, 117, 113, 109, 105, 101,  97,  93,  89,  85,  81,
   77,  74,  71,  68,  65,  62,  59,  56,  53,  50,  47,  44,  41,  38,  35,  32,
   30,  28,  26,  24,  22,  20,  18,  16,  14,  12,  10,   8,   6,   4,   2,   0
]

idle_size = 768         # size of animation array
idle_offset_2 = 512     # used to create animation -- see code
idle_offset_1 = 256     # used to create animation -- see code
idle_offset_0 = 0       # used to create animation -- see code
idle_offset = 12        # used to create animation -- see code


# Turns all LEDs red, then green, then blue, then off
def idol_startup():
    functions.pixels_fill((0,0,0))
    functions.pixels_show(config.brightness_mod)
    time.sleep(0.1) 

    for bright in range(10,0,-1):
        functions.pixels_fill((255,0,0))
        functions.pixels_show(bright/10)
        time.sleep(0.1)

    functions.pixels_fill((0,0,0))
    functions.pixels_show(config.brightness_mod)
    time.sleep(0.1) 

    for bright in range(10,0,-1):
        functions.pixels_fill((0,255,0))
        functions.pixels_show(bright/10)
        time.sleep(0.1)

    functions.pixels_fill((0,0,0))
    functions.pixels_show(config.brightness_mod)
    time.sleep(0.1) 

    for bright in range(10,0,-1):
        functions.pixels_fill((0,0,255))
        functions.pixels_show(bright/10)
        time.sleep(0.1)

    functions.pixels_fill((0,0,0))
    functions.pixels_show(config.brightness_mod)
    time.sleep(1) 



# Kaimana Color Fade Animation
def idle_mode4():

    if config.idle_after == 0:
        functions.pixels_fill((0,0,0))
        functions.pixels_show(config.brightness_mod)
        return

    # set initial color to BLACK
    functions.pixels_fill((0,0,0))
    functions.pixels_show(config.brightness_mod)

    while True:
        for index in range(idle_size):
            if init.idle_counter < functions.idle_after():
                return
            for i in range(config.led_count):
                if init.idle_counter < functions.idle_after():
                    return
                color_r = color_cycle_data[((index+idle_offset_2+((config.led_count-i)*idle_offset))%idle_size)]
                color_g = color_cycle_data[((index+idle_offset_1+((config.led_count-i)*idle_offset))%idle_size)]
                color_b = color_cycle_data[((index+idle_offset_0+((config.led_count-i)*idle_offset))%idle_size)]
                #print(color_r,color_g,color_b)
                functions.pixels_set(i, (color_r, color_g, color_b))
            functions.pixels_show(config.brightness_mod)
            time.sleep(0.01)
