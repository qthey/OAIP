def main():

    #n = int(input())
    #unique_digits = set()
    #for _ in range(n):
        #number = input()
        #unique_digits.update(set(number))
    #print(len(unique_digits))

    #string1 = input()
    #string2 = input()
    #string3 = input()
    #set1 = set(string1)
    #set2 = set(string2)
    #set3 = set(string3)
    #common_letters = set()
    #for s1, s2 in ((set1, set2), (set1, set3), (set2, set3)):
        #common_letters.update(s1.intersection(s2))
    #result = ''.join(common_letters)
    #print(result)

    #number = input()
    #all_digits = set('0123456789')
    #entered_digits = set(number)
    #missing_digits = all_digits - entered_digits
    #result = ' '.join(missing_digits)
    #print(result)

    #numbers = []
    #while True:
        #num = int(input())
        #if num == 0:
            #break
        #numbers.append(num)
    #count = len(numbers)
    #multiples = [n for n in numbers if n % count == 0]
    #print(multiples)

    #num_colors = int(input())
    #flag_colors = set()
    #for _ in range(num_colors):
        #color = input()
        #flag_colors.add(color)
    #flag_colors = list(flag_colors)
    #num_flags = int(input())
    #garland = [flag_colors[i % len(flag_colors)] for i in range(num_flags)]
    #print(' '.join(garland))

    bird_counts = {}
    while True:
        input_line = input("Введите строку (название птицы: количество) или пустую строку для завершения: ")
        if input_line == "":
            break
        if ": " in input_line:
            bird_name, count_str = input_line.split(": ", 1)
            if count_str.isdigit():
                count = int(count_str)
                if bird_name in bird_counts:
                    bird_counts[bird_name] += count
                else:
                    bird_counts[bird_name] = count
    print(bird_counts)

    input_str = input()
    numbers = map(int, input_str.split())
    stats = []
    for number in numbers:
        binary_representation = bin(number)[2:]
        characteristics = {
            "digits": len(binary_representation),  # Количество разрядов
            "units": binary_representation.count('1'),  # Количество единиц
            "zeros": binary_representation.count('0')  # Количество нулей
        }
        stats.append(characteristics)
    print(stats)

if __name__ == "__main__":
    main()