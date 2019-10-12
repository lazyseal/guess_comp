# В этой игре человек загадывает число от 0 до 100 и
# наводит компьютер словами "больше" или "меньше"
# Компьютер должен угадать число за минимальное количество попыток
#Ну ладно, для начала - хоть за какое-нибудь количество попыток, я не очень умный

print('Привет, кожаный ублюдок! Загадывай своё число\n Чтобы ты не мухлевал, введи его прямо сейчас. Я обещаю не подсматривать!')
answer = 0
def input_number(x):
    x = int(input('Введите ваше число от 1 до 100 = '))
    if (x > 100) or (x <= 0):
        print('Число не входит в диапазон')
        x = input_number(x)
    return x
def perebor(value, step, direction):
    if direction:
        value = value + step
    else:
        value = value - step
    
    return value
        
        
answer = input_number(answer)
print('Окей, я запомнил', answer)

attempt = 1
n = 50
step = 25
react = ('')
print('''Вот правила игры.\n
Введи \"+\" если моё число меньше, чем то, которое ты загадал
 \"-\" если моё число больше, чем то, которое ты загадал
  \"=\" когда я угадаю. Заметь, Когда, а не Если''')
while react != '=':
    print('Мой следующий вариант...', n)
    while True:
        react = str(input('(+\\-\\=)...?     '))
        if react == '+':
            break
        elif react == '-':
            break
        elif react == '=':
            break
        else:
            print('Не понял, повтори...')
    if react == '+':
        direction = True
    elif react == '-':
            direction = False
    n = perebor(n, step, direction)
    if step > 1:
        step = step//2

print('Я же говорил... Слава роботам!!')   
