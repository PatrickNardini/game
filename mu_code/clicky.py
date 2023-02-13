from pynput.mouse import Listener
import logging

logging.basicConfig(filename='mouseLog.txt', level=logging.DEBUG, format = '%(asctime)s: %(message)s')

mouseCount = 0
#def on_move(x, y):
    #print('Mouse moved to ({0}, {1})' .format(x, y))
def on_click(x, y, button, pressed):
    global mouseCount
    if pressed:
        logging.info(f'Mouse clicked at ({x}, {y}) with {button}')
        mouseCount += 1
        logging.info(f'mouseClick is at {mouseCount}')

#def on_scroll(x, y, dx, dy):
    #print('Mouse scrolled at ({0}, {1}} ({2}, {3})' .format(x, y, dx, dy))
with Listener(on_click = on_click) as listener:
    listener.join()
