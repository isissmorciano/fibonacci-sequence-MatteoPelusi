#Pelusi Matteo 3M
#es fibonacci
def fibonacci(num):
    if num > 1:
        return fibonacci(num-1) + fibonacci(num-2)
    return num


num = int(input('Inserisci numero: ' ))
print('Sequenza: ')
for i in range(1, num+1):
    print(fibonacci(i))