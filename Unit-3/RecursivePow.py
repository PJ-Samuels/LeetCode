def Pow(num, x):
    if x == 0:
        return 1
    if x == 1:
        return num
    else:
        return num*(Pow(num,x-1))
def main():
    val = Pow(2, 10)
    print(val)
main()

