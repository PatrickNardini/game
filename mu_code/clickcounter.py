import logging

def on_click(x, y, button, pressed):
    global mouseCount
    if pressed:
        logging.info(f'Mouse clicked at ({x}, {y}) with {button}')
    mouseCount += 1
    logging.info(f'mouseClick is at {mouseCount}')
