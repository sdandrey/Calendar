#Un año es bisiesto si el modulo 400 es 0 o el modulo 4 es 0 y el modulo 100 es 0
def isBisiesto(a):
    if(a % 4 == 0 and a % 100 != 0 or a % 400 == 0):
        return True
    return False
