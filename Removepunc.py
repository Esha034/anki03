str1 = "Hello, welcome to python programming!"

punctuation = [',', ';', '!']  
res = str1.split()
cleaned_res = []

for word in res:
    for char in punctuation:
        word = word.replace(char, '')  
    cleaned_res.append(word)

cleaned_str = ' '.join(cleaned_res)  
print(cleaned_str)
