def mystery(a,b):
    if b == 0:
        return 0
    elif b % 2 == 0:
        return mystery (a + a,b / 2)
    else:
        return mystery(a + a,b // 2) + a



#a optellen met zichzelf tot b 0 is, indien er een
#oneven getal word ingevoerd, zal het uiteindelijk resultaat nog eens
#plus a worden gedaan