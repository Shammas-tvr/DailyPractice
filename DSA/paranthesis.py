def valid_prtheses(para):
    if len(para) <=1:
        return False
    stack=[]
    for n in para:
        if n == "(" :
            stack.append(")")
        elif n == "{":
            stack.append("}")
        elif n == "[":
            stack.append("]")
        else:
            if not stack or n != stack.pop():
                return False
    return len(stack) == 0 


print(valid_prtheses("{}[]()"))