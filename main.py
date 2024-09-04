from pynput import keyboard


# function to listein on strokes
def on_press(key):
    try:
        print('{0} pressed'.format(key.char))
    except AttributeError:
        print('error')



with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

# # register listener
listener = keyboard.Listener(on_press=on_press)
listener.start()

