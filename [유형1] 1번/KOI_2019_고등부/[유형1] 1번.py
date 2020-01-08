def gcd(a, b):
    if b > a:   
        (a, b) = (b, a)

    if b is not 0:
        a = gcd(b, a%b)

    return a 


def solution(a, b):
    if 48 % gcd(a, b) is not 0:
        print("정답임")
    else:
        print("오답임") 


solution(14, 21)