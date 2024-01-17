"""
Модуль для измерения времени выполнения вызова функции
Определяет суммарное время, лучшее время и лучшее суммарное время
"""

import time, sys
timer = time.clock if sys.platform[:3] == 'win' else time.time


def total(reps, func, *pargs, **kargs):
    """
    Суммарное время выполнения функции func() reps раз.
    Возвращает (суммарное время, последний результат)
    """
    repslist = list(range(reps)) 
    start = timer()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = timer() -  start
    return (elapsed, ret)


def bestof(reps, func, *pargs, **kargs):
    """
    Самая быстра функция fubc() среди resp запусков.
    Возвращает (лучшее времяб последний результат)
    """
    best = 2 ** 32
    for i in range(reps):
        start = timer()
        ret = ret = func(*pargs, **kargs)
        elapsed = timer() -  start
        if elapsed < best: best = elapsed
    return (best, ret)


def bestoftotal(reps1, reps2, func, *pargs, **kargs):
    """
    Лучшее суммарное время:
    (лучшее время из reps1 запусков (суммарное время reps2 запусков func))
    """
    return bestof(reps1, total, reps2, func, *pargs, **kargs)