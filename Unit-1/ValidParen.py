def isValid(s):
    if s == "":
        return True
    stack = [s[0]]
    for i in range(1,len(s)):
        if s[i] == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
        elif s[i] == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return False
        elif s[i] == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                return False
        else:
            stack.append(s[i])
    return not stack
def main():
    print(isValid( "(){}[]"))
main()