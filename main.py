def jingle():
    music.play_tone(659, music.beat(BeatFraction.HALF))
    basic.pause(10)
    music.play_tone(659, music.beat(BeatFraction.HALF))
    basic.pause(10)
    music.play_tone(659, music.beat(BeatFraction.WHOLE))
    basic.pause(10)
    music.play_tone(659, music.beat(BeatFraction.HALF))
    basic.pause(10)
    music.play_tone(659, music.beat(BeatFraction.HALF))
    basic.pause(10)
    music.play_tone(659, music.beat(BeatFraction.WHOLE))
    basic.pause(10)
    music.play_tone(659, music.beat(BeatFraction.HALF))
    basic.pause(10)
    music.play_tone(784, music.beat(BeatFraction.HALF))
    basic.pause(10)
    music.play_tone(523, music.beat(BeatFraction.WHOLE))
    basic.pause(10)
    music.play_tone(587, music.beat(BeatFraction.HALF))
    basic.pause(10)
    music.play_tone(659, music.beat(BeatFraction.WHOLE))
    basic.pause(20)
    music.play_tone(698, music.beat(BeatFraction.HALF))
    basic.pause(10)
    music.play_tone(698, music.beat(BeatFraction.HALF))
    basic.pause(10)
    music.play_tone(698, music.beat(BeatFraction.HALF))
    basic.pause(10)
    music.play_tone(698, music.beat(BeatFraction.HALF))
    basic.pause(10)
    music.play_tone(698, music.beat(BeatFraction.HALF))
    basic.pause(10)
    music.play_tone(659, music.beat(BeatFraction.HALF))
    basic.pause(10)
    music.play_tone(659, music.beat(BeatFraction.WHOLE))
    basic.pause(10)
    music.play_tone(659, music.beat(BeatFraction.HALF))
    basic.pause(10)
    music.play_tone(587, music.beat(BeatFraction.HALF))
    basic.pause(10)
    music.play_tone(587, music.beat(BeatFraction.HALF))
    basic.pause(10)
    music.play_tone(659, music.beat(BeatFraction.HALF))
    basic.pause(10)
    music.play_tone(587, music.beat(BeatFraction.WHOLE))
    basic.pause(10)
    music.play_tone(784, music.beat(BeatFraction.WHOLE))

def on_button_pressed_a():
    jingle()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    basic.show_string("Happy Holidays!")
basic.forever(on_forever)
