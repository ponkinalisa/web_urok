from flask import Flask

app = Flask(__name__)


@app.route('/')
def return_sample_page():
    return ("""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Миссия Колонизация Марса</title>
                  </head>
                  <body>
                    <h1><b>Миссия Колонизация Марса</b></h1>
                  </body>
                </html>""")


@app.route('/index')
def return_sample_page2():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Миссия Колонизация Марса</title>
                  </head>
                  <body>
                    <h1><b>И на Марсе будут яблони цвести!</b></h1>
                  </body>
                </html>"""


@app.route('/promotion')
def prom():
    s = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
         'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return '<br>'.join(s)


@app.route('/image_mars')
def hello_mars():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="/static/img/MARS.png" alt="здесь должна была быть картинка, но не нашлась">
                    <p>Вот она какая, красная планета.</p>
                  </body>
                </html>"""


@app.route('/promotion_image')
def promotion_image():
    s = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
         'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" href="static/css/style.css">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="/static/img/MARS.png" alt="здесь должна была быть картинка, но не нашлась">
                    <div class="p-3 mb-2 bg-success text-white" role="alert">
                      {s[0]}
                    </div>
                    <div class="p-3 mb-2 bg-secondary text-white" role="alert">
                      {s[1]}
                    </div>
                    <div class="p-3 mb-2 bg-info text-white" role="alert">
                      {s[2]}
                    </div>
                    <div class="p-3 mb-2 bg-secondary text-white" role="alert">
                      {s[3]}
                    </div>
                    <div class="p-3 mb-2 bg-warning text-white" role="alert">
                      {s[4]}
                    </div>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')