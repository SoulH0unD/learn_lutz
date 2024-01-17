import sys
from timerdeco2 import timer
force = list if sys.version_info[0] == 3 else (lambda X: X)

@timer(label='[CCC==>]')
def listcomp(N):
    return [x * 2 for x in range(N)]

@timer(label='[MMM==>]')
def mapcall(N):
    return force(map((lambda x: x * 2), range(N)))


for func in (listcomp, mapcall):
    result = func(5)

    func(50000)
    func(500000)
    func(1000000)
    print(result)
    print('allTime = %s\n' % func.alltime)

print('\n**map/comp = %s' % round(mapcall.alltime / listcomp.alltime, 3))