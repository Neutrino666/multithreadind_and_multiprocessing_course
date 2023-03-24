import time
import threading

data = threading.local() # данные дата доступны только в локальной области видимости


def get():
    print(data.value)


def get_name():
    print(data.name)


def t1():
    data.value = [111]
    # get()
    print('t1:', data.value)


def t2():
    data.name = threading.current_thread().name
    data.value = {2: 1}
    # get()
    print('t2:', data.value)
    get_name() # локальная данные можно получить т.к. не main поток


threading.Thread(target=t1).start()
threading.Thread(target=t2, name='t2').start()

get_name() # Ошибка потому что не нльзя получить локальные данные из main потомка