import time
import threading

event = threading.Event()  # по умолчанию там false


def test():
    while True:
        event.wait()  # При раблокировке set больше заблокировать нельзя
        print('test')
        time.sleep(2)


event.clear()  # тут устанавливается значение False
# event.set()  # Устанавливает значение True
threading.Thread(target=test).start()


event = threading.Event()


def image_handler():
    thr_num = threading.current_thread().name
    print(f'Идет подготовка изображения из потока [{thr_num}]')
    event.wait()
    print(f'Изображение отправлено')


time.sleep(10)
event.set()