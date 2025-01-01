import sys
print("Masterstream Sigma calculator - italian - powered by Python")
sys.set_int_max_str_digits(2147483647)
cronology = []
while True:
    delcronology = None
    inf = float("inf")
    nan = float("nan")
    pi = 3.14
    e = 2.71
    history = " | ".join(cronology)
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)
    def sin(x, n):
        sin_approx = 0
        for i in range(n):
            coef = (-1) ** i
            num = x ** (2 * i + 1)
            denom = factorial(2 * i + 1)
            sin_approx += (coef * num) / denom
        return sin_approx
    def cos(x, n):
        cos_approx = 0
        for i in range(n):
            coef = (-1) ** i
            num = x ** (2 * i)
            denom = factorial(2 * i)
            cos_approx += (coef * num) / denom
        return cos_approx
    def tan(x, n):
        return sin(x, n) / cos(x, n)
    print("""
    SIGMA EXPRESSIONS: """ + history)
    exp =  input(">>> ")
    try:
        if exp == "delcronology":
            cronology.clear()
        if "0^0" in exp or "0**0" in exp:
            cronology.append(exp+"=indeterminato")
        else:
            cronology.append(exp+"="+str(eval(exp.replace("^","**").replace("x","*").replace(",",".").replace(":","/").replace("[","(").replace("]",")").replace("{","(").replace("}",")"))))
    except ZeroDivisionError:
        if "0/0" in exp or "0:0" in exp:
            cronology.append(exp+"=indeterminato")
        elif "/0" in exp or ":0" in exp:
            cronology.append(exp+"=inf")
        elif "0/" in exp or "0:" in exp:
            cronology.append(exp+"=0")
        else:
            cronology.append(exp+"= Errore: divisione con zero invalida")
    except RecursionError:
        cronology.append(exp+"= Errore: scadenza calcolo")
    except OverflowError:
        cronology.append(exp+"= Errore: scadenza calcolo")
    except TypeError:
        cronology.append(exp+"= Errore: tipi non validi fra loro")
    except ValueError:
        cronology.append(exp+"= Errore: valori non validi")
    except SyntaxError:
        cronology.append(exp + "= Errore: sintassi invalida")
    except NameError:
        cronology.append(exp + "= Errore: nome non definito")
    if cronology[-1] != "delcronology=None":
        print("\n"+cronology[-1])
    else:
        cronology.clear()
