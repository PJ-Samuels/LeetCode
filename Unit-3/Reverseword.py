def reverse(str):
    new_str = ""
    temp_str = ""
    arr = []
    for c in str:
        if c != " ":
            temp_str += c
        else:
            arr.append(temp_str)
            temp_str = ""
    if temp_str != "":
        arr.append(temp_str)
    print(arr)
    final_str = ""
    i = len(arr)-1
    while(i >= 0):
        final_str+= arr[i]+" " 
        i-= 1
    
    print(final_str)
    return final_str
def main():
    str = "a good   example"
    val = reverse(str)
    # print("reversed")

main()