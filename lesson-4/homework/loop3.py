vowels = "aeiouAEIOU"
txt = input("Enter the text: ")
result = list(txt)
i = 2  

while i < len(result):
    insert_pos = i + 1  

    if result[i] in vowels or (i > 0 and result[i - 1] == '_'):
        insert_pos = i + 2  

    if insert_pos < len(result):
        result.insert(insert_pos, "_")
        i += 1  

    i += 3  

print("".join(result))
