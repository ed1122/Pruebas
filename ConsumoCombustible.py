def l100kmtompg(liters):
    #
    gal=liters/3.785411784
    mill=100/1.609344
    G = mill/gal
    return G

#

def mpgtol100km(miles):
#
    lit=3.785411784
    km=miles*1.609344
    G = 100*(lit/km)
    return G
    return M
#

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))
