def main_func(M,N):
    divs=set()
    for x in N:
        for y in range(1,M+1):
            if y%x==0:
                divs.add(y)
    print(divs)
    print("Numbers divisible by N given Prime Numbers: ",len(divs))

M=int(input("Enter the value of M: "))
n_1=input("Enter the Prime elemetnts of N(seperate by ,): ").split(",")
N=[int(x) for x in n_1]
if max(N)>M:
    print("Invalid Values of N given! Please run the code again")
else:
    main_func(M,N)
