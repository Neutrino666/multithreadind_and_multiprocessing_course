import time
import threading

value = 0
locker = threading.RLock()  # Поток может разблокировать только тот кто поставил блокировку


def inc_value():
    print('Блокируем поток..')
    locker.acquire()
    print('Поток разблок..')


t1 = threading.Thread(target=inc_value)
t2 = threading.Thread(target=inc_value)

t1.start()
t2.start()

locker.release() # Ошибка потому что основной потом пытается разблокировать поток
