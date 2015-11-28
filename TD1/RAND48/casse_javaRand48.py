
def trouve_graine(u,v):

    v1 = u
    v2 = v
    if v1 < 0:
        v1 += 2**32
    if v2 < 0:
        v2 += 2**32

    mult = 25214903917
    incr = 11
    mask = 2**48-1

    i = 0
    res = 0
    graine = v1 * 65536

    while (res!=v2) and (i<65536):
        res = ((graine * mult + incr) & mask) >> 16
        graine += 1
        i += 1

    return graine-1


def LCG48(graine,nb):

    v1 = graine
    mult = 25214903917
    incr = 11
    mask = 2**48-1

    for i in range(nb):
        v1 = ((v1 * mult + incr) & mask)
        v2 = v1 >> 16
        if (v2 & 2**31):
            v2 -= 2**32
        print(v2)

    return None

def LCG48_sans_traitement(graine,nb):

    v1 = graine
    mult = 25214903917
    incr = 11
    mask = 2**48-1

    for i in range(nb):
        v1 = ((v1 * mult + incr) & mask)
        print(v1)

    return None


def trouve_precedent(u,v):

    v1 = u
    v2 = v
    if v1 < 0:
        v1 += 2**32
    if v2 < 0:
        v2 += 2**32

    mult = 25214903917
    incr = 11
    mask = 2**48-1

    i = 0
    res = 0
    while (res!=v2) and (i<65536):
        seed = v1 * 65536 + i
        res = (((seed * mult + incr) & mask) >> 16)
        i += 1

    V1 = seed - incr
    V0 = 0

    for i in range(48):
        mask = 1 << i
        bit = V1 & mask
        V0 = V0 | bit
        if bit == mask:
            V1 -= mult << i

    v0 = V0 >> 16
    if v0 > 2**31:
        v0 -= 2**32

    return v0


def trouve_precedents(u,v,nb):

    l = []
    v1 = u
    v2 = v
    for i in range(nb):
        l.append(trouve_precedent(v1,v2))
        v2 = v1
        v1 = l[-1]

    for i in range(nb):
        print(l[nb-1-i])

    return None
        
