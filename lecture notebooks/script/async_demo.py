import asyncio
import datetime


# Демонстрация event_loop
# call_soon, call_later

def display_date(end_time, loop):
    ''' показ времени каждую секунду '''
    print(datetime.datetime.now())
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, display_date, end_time, loop)
    else:
        loop.stop()

# Получаем себе цикл обработки сообщений (из текущего потока)
loop = asyncio.get_event_loop()

# вызываем функцию display_date()
end_time = loop.time() + 5.0
loop.call_soon(display_date, end_time, loop)

# говорим циклу выполняться вечно (но он прервется вызовом loop.stop() из функции)
loop.run_forever()
# Закрываем цикл обработки сообщений (в jupyter'е я это делать, конечно, не буду)
loop.close()