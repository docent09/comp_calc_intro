# Сравнение различных способов вычисления числа ПИ

def leibniz(n):
    """
    Вычисление числа ПИ с помощью ряда Лейбница
    :param n: число слагаемых ряда
    :return: найденное число ПИ
    """
    p = 0 # приближение числа пи
    for i in range(n):
        p += (-1)**i / (2*i + 1)
    return 4*p

def euler(n):
    """
    Вычисление числа ПИ с помощью ряда Эйлера
    :param n: число слагаемых ряда
    :return: найденное число ПИ
    """
    import math
    p = 0 # приближение числа пи
    for i in range(1, n+1):
        p += 1 / i**2
    return math.sqrt(6*p)

def wallis(n):
    """
    Вычисление числа ПИ с помощью произведения Валлиса
    :param n: число слагаемых ряда
    :return: найденное число ПИ
    """
    p = 1 # приближение числа пи
    for i in range(1, n+1):
        p *= (2 * i)**2 / ((2*i-1) * (2*i+1))
    return 2*p

def newton1(k):
    """
    Вычисление числа ПИ с помощью метода Ньютона
    :param k: число слагаемых ряда
    :return: найденное число ПИ
    """
    n = 1/2 
    p = 0 # приближение числа пи
    F = 1 # факториал
    for i in range(k):
        N = 1
        for j in range(i):
            N *= n - j
        p += (-1)**i * N / ((2*i+1) * F)
        F *= i+1
    return 4*p

def newton2(k):
    """
    Вычисление числа ПИ с помощью улучшенного метода Ньютона
    :param k: число слагаемых ряда
    :return: найденное число ПИ
    """
    import math
    n = 1/2
    p = 0 # приближение числа пи
    F = 1
    for i in range(k):
        N = 1
        for j in range(i):
            N *= n - j
        p += (-1)**i * N / ((2*i+1) * F) * 0.5**(2*i+1)
        F *= i+1
    return 12*(p-math.sqrt(3)/8)

if __name__ == "__main__":
    import math
    import time
    tests = [1, 2, 3, 4, 5, 6]
    test = 1

    while test in tests:
        print('Введите номер теста (1, 2, 3, 4, 5, 6):')
        print('Тест #1 - ряд Лейбница')
        print('Тест #2 - ряд Эйлера')
        print('Тест #3 - произведение Валлиса')
        print('Тест #4 - метод Ньютона (биномиальная теорема)')
        print('Тест #5 - улучшенный метод Ньютона (биномиальная теорема)')
        print('Тест #6 - сравнение точности 4 методов при разных n')

        test = int(input())

        if test == 1:
            print('-- Вычисление числа ПИ по формуле ряда Лейбница --')
            print('n', 'Найденное число ПИ', 'Погрешность', sep='\t')
            t1 = time.time()
            for n in range(100, 1001, 100):
                p = leibniz(n)
                e = abs(math.pi - p)
                print(n, p, e, sep='\t')
            print('Время вычисления =', round(time.time()-t1, 5))
            print()

        if test == 2:
            print('-- Вычисление числа ПИ по формуле ряда Эйлера --')
            print('n', 'Найденное число ПИ', 'Погрешность', sep='\t')
            t1 = time.time()
            for n in range(100, 1001, 100):
                p = euler(n)
                e = abs(math.pi - p)
                print(n, p, e, sep='\t')
            print('Время вычисления =', round(time.time()-t1, 5))
            print()

        if test == 3:
            print('-- Вычисление числа ПИ по формуле произведения Валлиса --')
            print('n', 'Найденное число ПИ', 'Погрешность', sep='\t')
            t1 = time.time()
            for n in range(100, 1001, 100):
                p = wallis(n)
                e = abs(math.pi - p)
                print(n, p, e, sep='\t')
            print('Время вычисления =', round(time.time()-t1, 5))
            print()

        if test == 4:
            print('-- Вычисление числа ПИ по методу Ньютона --')
            print('n', 'Найденное число ПИ', 'Погрешность', sep='\t')
            t1 = time.time()
            for n in range(10, 101, 10):
                p = newton1(n)
                e = abs(math.pi - p)
                print(n, p, e, sep='\t')
            print('Время вычисления =', round(time.time()-t1, 5))
            print()

        if test == 5:
            print('-- Вычисление числа ПИ по улучшенному методу Ньютона --')
            print('n', 'Найденное число ПИ', 'Погрешность', sep='\t')
            t1 = time.time()
            for n in range(2, 11, 1):
                p = newton2(n)
                e = abs(math.pi - p)
                print(n, p, e, sep='\t')
            print('Время вычисления =', round(time.time()-t1, 5))
            print()

        if test == 6:
            print('-- Сравнение точности методов расчета ПИ при разных n --')
            print('n' ,'Ряд Лейбница', 'Ряд Эйлера', 'Произв. Валлиса', 'Метод Ньютона', 'Улучшенный метод Ньютона', sep='\t')
            nn = [10, 100]
            for n in nn:
                e1 = round(abs(math.pi - leibniz(n)), 10)
                e2 = round(abs(math.pi - euler(n)), 10)
                e3 = round(abs(math.pi - wallis(n)), 10)
                e4 = round(abs(math.pi - newton1(n)), 10)
                e5 = round(abs(math.pi - newton2(n)), 15)
                
                print (n, e1, e2, e3, e4, e5, sep='\t')
            print()

