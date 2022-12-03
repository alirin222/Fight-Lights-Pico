print("config")
#Fight Lights Pico

from machine import Pin
from init import random, rainbow
import button
import functions
import init

blank = (0,0,0)
red = (255,0,0)
orange = (255,127,0)
light_orange = (255,200,0)
yellow = (255,255,0)
lime = (160,255,0)
green = (0,255,0)
turqoise = (64,224,208)
blue = (0,0,255)
light_blue = (0,193,255)
violet = (170,0,255)
pink = (255,0,170)
cyan = (0,255,255)
white = (255,255,255)

colors = [red,orange,light_orange,yellow,lime,green,turqoise,blue,light_blue,violet,pink,cyan,white]

idle_mode1_colors = colors
idle_mode1_speed = 5
profile_name = "Hitbox"
led_count = 24
PIN_NUM = 0
leniency = 1
brightness_mod = 1
brightness_steps = 0.1
startup_animation = True
idle_mode = 4
idle_after = 20
save_stats = False
input_reset_time = 50
profile_color = (255,0,0)
clear_background_on_press = False
background = ((0.5,red,1),(0.5,red,2),(0.5,white,3),(0.5,white,4),(0.5,white,5),(0.5,white,6),(0.5,white,7),(0.5,white,8),(0.5,white,9),(0.5,white,10),(0.5,white,11),(0.5,white,12),(0.5,white,13),(0.5,white,14),(0.5,white,15),(0.5,white,16),(0.5,white,17),(0.5,white,18),(0.5,red,19),(0.5,red,20),(0.5,red,21),(0.5,red,22),(0.5,red,23),(0.5,red,24))
fadeout_speed = 6
fadein_speed = 20
up_MyButton = button.MyButton(1, 'up', functions.clear_led)
down_MyButton = button.MyButton(2, 'down', functions.clear_led)
right_MyButton = button.MyButton(3, 'right', functions.clear_led)
left_MyButton = button.MyButton(4, 'left', functions.clear_led)
select_MyButton = button.MyButton(5, 'select', functions.clear_led)
ps_MyButton = button.MyButton(6, 'ps', functions.clear_led)
start_MyButton = button.MyButton(7, 'start', functions.clear_led)
p1_MyButton = button.MyButton(8, 'p1', functions.clear_led)
p2_MyButton = button.MyButton(9, 'p2', functions.clear_led)
p3_MyButton = button.MyButton(10, 'p3', functions.clear_led)
p4_MyButton = button.MyButton(11, 'p4', functions.clear_led)
k1_MyButton = button.MyButton(12, 'k1', functions.clear_led)
k2_MyButton = button.MyButton(13, 'k2', functions.clear_led)
k3_MyButton = button.MyButton(14, 'k3', functions.clear_led)
k4_MyButton = button.MyButton(15, 'k4', functions.clear_led)

button_list = [up_MyButton,down_MyButton,right_MyButton,left_MyButton,select_MyButton,ps_MyButton,start_MyButton,p1_MyButton,p2_MyButton,p3_MyButton,p4_MyButton,k1_MyButton,k2_MyButton,k3_MyButton,k4_MyButton]
init.button_list_length = len(button_list)


up_MyButton.set_config((1,2,), random, True)
down_MyButton.set_config((21,22,), random, True)
right_MyButton.set_config((19,20,), random, True)
left_MyButton.set_config((23,24,), random, True)
select_MyButton.set_config((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,), violet, False)
ps_MyButton.set_config((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,), light_blue, False)
start_MyButton.set_config((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,), red, False)
p1_MyButton.set_config((17,18,), random, True)
p2_MyButton.set_config((15,16,), random, True)
p3_MyButton.set_config((13,14,), random, True)
p4_MyButton.set_config((11,12,), random, True)
k1_MyButton.set_config((3,4,), random, True)
k2_MyButton.set_config((5,6,), random, True)
k3_MyButton.set_config((7,8,), random, True)
k4_MyButton.set_config((9,10,), random, True)

ledOptions_led_buttons = [start_MyButton,select_MyButton]
ledOptions_start_time = 3
ledOptions_increase_brightness = [up_MyButton]
ledOptions_decrease_brightness = [down_MyButton]
ledOptions_left_button = [left_MyButton]
ledOptions_right_button = [right_MyButton]
ledOptions_confirm = [k1_MyButton]
