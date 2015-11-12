#Rehaan Advani
#Chapter 8 Programming Assignments

def proj8_1():
    try:
        firstTerm, secondTerm = eval(input("Enter the first and second term of a sequence separated by commas: "))
        nthTerm = eval(input("Enter the nth term you want to compute: "))
    except:
        print("\nOops, there is something wrong.")

    seq = sequence(firstTerm, secondTerm, nthTerm)
    print(seq)
    nthTermValue = seq[nthTerm-1]
    print(str(nthTermValue))


def sequence(f, s, n):
    sequenceArray = []
    sequenceArray.append(f)
    sequenceArray.append(s)
    for i in range(n):
        t = s * f
        s = t
        f = s
        sequenceArray.append(t)
    return sequenceArray
proj8_1()

def proj8_3():
    a = eval(input("Enter an integer: "))
    p = eval(input("Enter a prime number: "))
    expr = (a**p)-a

    
proj8_3()
