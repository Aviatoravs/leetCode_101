s = list(input("Enter a String of Brackets: "))
if len(s) % 2 != 0 or len(s) == 0:
    print("Invalid String")
else:
    res = list()
    for str in s:
        if str == "(" or str == "{" or str == "[":
            res.append(str)
        else:
            if (res[-1] == "(" and str == ")") or (res[-1] == "{" and str == "}") or (res[-1] == "[" and str == "]"):
                res.pop()
            else:
                print("Invalid paranthesis")
    if len(res) == 0:
        print("valid")
    else:
        ("Invalid Pranthesis")
    print(s)
