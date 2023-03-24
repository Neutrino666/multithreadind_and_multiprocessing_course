import time
import threading


def image_handler():
    thr_num = threading.current_thread().name
    print(f'Идет подготовка изображения из потока [{thr_num}]')
    event.wait()
    print(f'Изображение отправлено')


event = threading.Event()

for i in range(10):   # Создается 10 потоков
    threading.Thread(target=image_handler, name=str(i)).start()
    print(f'Поток [{i}] запущен')
    time.sleep(1)


if threading.active_count() >= 10: # при 10 потоках и выходе из цикла выше
    event.set()  # event устанавливает True
