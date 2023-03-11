def collatz(num):
    if num%2==0:
        return num//2
    else:
        return 3*num+1
number: int = int(input("enter the number:"))
end_of_seq = False
func = collatz(number)
while not end_of_seq:
    if func!=1:
        print(func)
        func = collatz(func)
    else:
        print(func)
        end_of_seq = True


