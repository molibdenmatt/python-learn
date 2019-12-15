
numbers = [0, 1]  # zdefiniuj dwa pierwsze wyrazy ciagu F(0) = 0, F(1) = 1

# Wypisz kolejne liczby ciagu Fibonacciego
def fib(ile):
    for i in range(ile-2):  # dla kolejnych 50 liczb z ciagu fibonnaciego
        # new = numbers[-1] + numbers[-2]  # oblicz kolejny wyraz ciagu jako sume dwoch ostatnich
        numbers.append(numbers[-1] + numbers[-2])  # dodaj nowy wyraz ciagu do listy
    return numbers[ile-1]

print(fib(10))

def fib2(ile):
    if ile == 1:
        return 0
    elif ile == 2:
        return 1
    else:
        return fib2(ile-1) + fib2(ile-2)

print(fib2(10))

