TOKEN = '5501426845:AAF1fsgyRtKsoV0RyQvgjVsYiNddlBs4Bf8'
URL = 'https://api.telegram.org/bot{TOKEN}/{method}'


links = 'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric'
TOKEN_WEATHER = 'c911289b798a07d2686f51df9dd84fc4'


MESSAGE = {
            'start': 'Вітаю, {}!',
            'start_menu': 'Цього бота створено в навчальних цілях.\nВін '
                          'здатен показувати погоду в різних куточках світу, '
                          'та розважити Вас картинками з котами.\nВведіть '
                          'назву міста, або скористайтесь кнопками '
                          'швидкого доступу. Усі данні взяті з сайту https://openweathermap.org',
            'weather': 'Температура повітря: {} по Цельсію\nХмарність: {}%\nШвидкість вітру: {}м/с\n'
                       'Вологість повітря: {}%',
            'error': 'Виникла помилка, можливо було введено некоректну назу міста.'
                     ' Перевірте правильність та повторіть запит.',
            'date_time': 'Дата: {}\nЧас: {}'
           }