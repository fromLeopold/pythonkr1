counter = 0
i = 0
with open('students.txt', 'r', encoding='utf-8') as file:
    for line in file:
        try:
            stude = str(file.readline())
            stude = stude.split()
            i += int(stude[2])
            if int(stude[2]) < 3:
                print(" ".join(stude))
            counter += 1
        except (IndexError):
            break
i = i/counter
print(f'Средний бал по классу: {round(i)}')
