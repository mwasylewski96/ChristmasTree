import sys
print("Choinka")
print("Jaka ma byc podstawa choinki?:")
podstawa = int(input())
while podstawa % 2 == 0:
    print("Podstawa choinki musi miec liczbe nieparzysta!!!")
    podstawa = int(input())
czubek = 1
pustaprzestrzen = podstawa
while czubek <= podstawa:
    for i in range(int((pustaprzestrzen-1)/2)):
        sys.stdout.write(" ")
    for i in range(czubek):
        sys.stdout.write("*")
    for i in range(int((pustaprzestrzen - 1) / 2)):
        sys.stdout.write(" ")
    print(" ")
    czubek += 2
    pustaprzestrzen -= 2
for i in range(int((podstawa-1)/2)):
    sys.stdout.write(" ")
sys.stdout.write("*")