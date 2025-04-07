def point_addition(P, Q):
    a = 2
    b = 12
    p = 17
    x1, y1 = P
    x2, y2 = Q
   
    if P == (None, None):
        return Q
    if Q == (None, None):
        return P
    if P == Q:
        return point_doubling(P)
    if x1 == x2:
        return (None, None)
    m = (y2 - y1)/(x2 - x1)
    x3 = (m**2 - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p
    return (x3, y3)
 
def point_doubling(P):
    a = 2
    p = 17
    x1, y1 = P
   
    m = (3 * x1**2 + a) * pow(2 * y1, p-2, p) % p
    x3 = (m**2 - 2 * x1) % p
    y3 = (m * (x1 - x3) - y1) % p
    return (x3, y3)
 
def gen_key_from_ecc():
    P = (5, 1)
    Q = (6, 3)
    result_point = point_addition(P, Q)
    if result_point == (None, None):
        result_point = point_doubling(P)
   
    x, y = result_point
    key_str = (str(x) + str(y)).encode()
    key = (key_str * 16)[:16]
    return key