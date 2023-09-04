def main():

    dict = {"I":1, "V": 5, "X": 10, "L": 50, "C":100,"D":500, "M":1000}
    str = "LVIII"
    n = len(str)-1
    count = dict[str[n]]
    while(n > 0):
        if dict[str[n-1]]< dict[str[n]]:
            count += dict[str[n]]-dict[str[n-1]]
        else:
            count += dict[str[n-1]]
        n-=1
    print(count)

main()