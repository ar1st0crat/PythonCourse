import cgi
import html


form = cgi.FieldStorage()
car = html.escape(form.getfirst('car', 'unknown'))
car_no = html.escape(form.getfirst('no', 'unknown'))

print('Content-type: text/html\n')
print('''<!DOCTYPE HTML>
        <html>
        <head>
            <title>Форма добавления автомобиля</title>
        </head>
        <body>''')

print('<h1>Ваши данные приняты!</h1>')
print('<p>Вы указали автомобиль: {}</p>'.format(car))
print('<p>С номером: {}</p>'.format(car_no))

print('''</body></html>''')
