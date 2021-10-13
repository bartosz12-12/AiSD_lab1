# Zad1
# def foo(litera, nazwisko):
#     return litera + ". "+ nazwisko
# print(foo("B", "Lipinski"))

# Zad2
# def foo(imie, nazwisko):
#     return imie[0] + ". " + nazwisko
# print(foo("Bartosz", "Lipiński"))

# zad3
# def foo(liczba1, liczba2, wiek):
#     return liczba1*100 + liczba2 - wiek
#
# print(foo(20, 21, 20))

# zad4
# def foo(imie, nazwisko):
#     return imie[0] + ". " + nazwisko
#
# def foo2(imie, nazwisko, func):
#     return  func(imie, nazwisko)
#
# print(foo2("Bartosz", "Lipinski",foo))

#zad5
# def foo(a, b):
#     if a >= 0 and b > 0:
#         return a/b
# print(foo(2, 2))
# print(foo(-1, 1))

# zad6
# suma = 0
# while suma != 100:
#     a = int(input())
#     suma +=a
# print("suma = 100")

# zad7
# lista = [1, 2, 3, 4]
# def foo(lista):
#     return tuple(lista)
#
# print(foo(lista))

#zad8
# lista = []
# a = 0
# while  a != "q":
#     a = input()
#     if a != "q":
#         lista.append(a)
# lista = tuple(lista)
# print(lista)
# zad9
# def foo(a: int):
#     d = {
#         1: "Poniedzialek",
#         2: "Wtorek",
#         3: "Środa",
#         4: "Czwartek",
#         5: "Piątek",
#         6: "Sobota",
#         7: "Niedziela"
#     }
#     return d[a]
# print(foo(6))
# zad10
def foo(napis):
    a = True
    for x in range(len(napis)):
        if napis[x] != napis[-x-1]:
            a = False
    return a

print(foo("kajak"))
