strs = input("Enter a list of Strings: ").split(" ")
prefix = strs[0]
for string in strs[1:]:
    while not string.startswith(prefix):
        prefix = prefix[:-1]
        if(prefix == ""):
            prefix = ""
            break
print("No common Prefix found" if(prefix == "") else prefix)
