from math import sqrt

def es_primo(numero: int) ->bool:
    if numero <= 1:
        return False
    for divisor in range(2, int(sqrt(numero))+1):
        if numero % divisor == 0:
            return False
    return True

def run():
    for i in range(11):
        primalidad = es_primo(i)
        print('¿Es {} primo?  {}'.format(i, primalidad))

if __name__=='__main__':
    run()

