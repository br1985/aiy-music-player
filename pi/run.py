#!/usr/bin/env python

import signal
import subprocess
import sys
import time

import aiy.leds
import aiy.pins
import gpiozero

mplayer = None
state = 'off'

def reset():
    global mplayer

    if mplayer:
        mplayer.terminate()
        mplayer.wait()

    led0.update(aiy.leds.Leds.rgb_off())
    led1.on()
    led2.on()

def push0():
    global state, mplayer

    reset()

    if state != 'radio':
        led0.update(aiy.leds.Leds.rgb_on((0xff, 0x00, 0x00)))
        mplayer = subprocess.Popen(['mplayer', 'http://195.150.20.9/RMFCLASSIC48', '-af', 'volume=-10'])
        state = 'radio'
    else:
        state = 'off'

def push1():
    global state, mplayer

    reset()

    if state != 'insane':
        led1.off()
        mplayer = subprocess.Popen(['mplayer', 'Street Sounds from Sony 1/01 - Insane in the Brain.oga'])
        state = 'insane'
    else:
        state = 'off'

def push2():
    global state, mplayer

    reset()

    if state != 'bowwow':
        led2.off()
        mplayer = subprocess.Popen(['mplayer', 'Street Sounds from Sony 1/03 - Bow Wow Wow.oga'])
        state = 'bowwow'
    else:
        state = 'off'

led0 = aiy.leds.Leds()
led1 = gpiozero.LED(aiy.pins.PIN_A)
led2 = gpiozero.LED(aiy.pins.PIN_C)

button0 = gpiozero.Button(23)
button1 = gpiozero.Button(aiy.pins.PIN_B)
button2 = gpiozero.Button(aiy.pins.PIN_D)

button0.when_pressed = push0
button1.when_released = push1
button2.when_released = push2

reset()

print('ready...')
signal.pause()

