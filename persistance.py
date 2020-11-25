my_list=("999")
x=(my_list.split(' '))
print(x)
b=(",".join(my_list))
print(b)
def jumlah(number):
    hasil= 1
    for i in (number):
        hasil *= i
    return hasil
number=(9,9,9)
b=jumlah(number)
print(b)
def jumlah(b):
    string = str(b) 
    hasil= 0
    for i in (number):
        hasil += i
    return hasil
print(jumlah(b))