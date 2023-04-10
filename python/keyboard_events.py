import keyboard as kb
from pynput import keyboard as kb1
from time import sleep


def pack_keyboard():
    n = 0

    while True:
        print('\033c', end='')
        # Wait for the next event.
        
        event = kb.read_event()
        print(event.name)
        if event.event_type == kb.KEY_DOWN and event.name == 'esc':
            print('ESC was pressed')
            break

        sleep(0.2)
        print(n, end='\r')
        print(' ' * len(str(n)), end='\r')
        n += 1
        

    print('end')

def clear():
    print('\033c', end='')

class Arrow:
    up = u'\u2191'
    down = u'\u2193'
# cursor = u'\u203A' # >
# cursor = u'\u2039' # <
cursor = u'\u25BA' # >

selected = 0
def indexup():
    selected -= 1

def indexdown():
    selected += 1

options = [
    'novo jogo',
    'carregar jogo salvo',
    'configurações',
    'sair',
]

def tela_inicial():
    clear()
    print('Banco Imobiliário', end='\n\n')
    for opt in options:
        print('{} {}'.format(
            cursor if options.index(opt) == selected else ' ',
            opt))
    print(
        '\n\n',
        f'[{Arrow.up}]',
        f'[{Arrow.down}]',
        '[ENTER]',
        sep='   ')
    

def on_press(key):
    pass
    # try:
    #     # print('alphanumeric key {0} pressed'.format(
    #     #     key.char))
    # except AttributeError:
    #     # print('special key {0} pressed'.format(
    #     #     key))

def on_release(key):
    global selected
    print('{0} released'.format(
        key))
    if key == kb1.Key.up:
        selected -= 1
        if selected < 0:
            selected = 0
        print(selected)

    if key == kb1.Key.down:
        selected += 1
        if selected >= len(options):
            selected = len(options) - 1
        print(selected)

    if key == kb1.Key.enter and selected == len(options)-1:
        return False

    if key == kb1.Key.esc:
        # Stop listener
        return False

# Collect events until released
with kb1.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    # print('\033c', end='')
    listener.join()

