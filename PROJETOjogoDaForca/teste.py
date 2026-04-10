array = [{"nome": "bruno", "idade": 20}, {"nome": "luis", "idade": 53}, {"nome": "moises", "idade": 34}]

nome = "bruno"

for i in range(len(array)):
    if nome in array[i]:
        print(array["nome"])
        array["nome"] += 20 
        print(array["idade"])
