# Symbolises the beginning of my code
seconds = 0
basic.show_string("BEGIN SHOWER?")
led.stop_animation()

# Code displays an umbrella icon and plays a twinkle sound when the logo is touched
def on_logo_touched():
    basic.show_icon(IconNames.UMBRELLA)
    music.play(music.builtin_playable_sound_effect(soundExpression.twinkle),
        music.PlaybackMode.IN_BACKGROUND)
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

# When Button A is pressed, the countdown of 240 seconds begins
def on_button_pressed_a():
    global seconds
    seconds = 240
    while seconds > 0:
        whaleysans.show_number(seconds)
        basic.pause(1000)
        seconds += 0 - 1
    whaleysans.show_number(0)
    # After the conclusion of the timer, LED lights symbolise a Happy face in combination with a ringtone sound
    basic.show_icon(IconNames.HAPPY)
    music._play_default_background(music.built_in_playable_melody(Melodies.RINGTONE),
        music.PlaybackMode.IN_BACKGROUND)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    pass
input.on_button_pressed(Button.AB, on_button_pressed_ab)

# When Button B is pressed, the animation stops
def on_button_pressed_b():
    basic.clear_screen()
    led.stop_animation()
input.on_button_pressed(Button.B, on_button_pressed_b)
