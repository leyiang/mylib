from pynput import keyboard

def is_special_pressed(which, key):
    return key == keyboard.Key[ which ]

special_chars = [
    "enter", "esc", "space", "f1", "cmd",
    "media_next", "up", "down", "left", "right",
]

def is_pressed(which, key):
    if which == " ":
        which = "space"

    if which in special_chars:
        return is_special_pressed( which, key )
    
    try:
        if key.char == which:
            return True
    except AttributeError:
        return False

    return False

def is_some_pressed(which_list, key):
    for which in which_list:
        if is_pressed(which, key):
            return True
    return False
