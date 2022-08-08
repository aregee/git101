number=0
with open('sample_input.txt') as file:
    words = file.read()
    number=number+1
    print(number)
print(len(words.split()))
