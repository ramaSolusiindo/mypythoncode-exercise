n = int(input("Enter the number: "))
L = [x for x in range(1, n+1)]
for i in range(1, n+1):
    a = list(map(str, L[0:i]))
    s = " ".join(a[1:][::-1] + a)
    print(s.center((4*n)-3, " "))