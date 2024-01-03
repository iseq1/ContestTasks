def main():
    n = int(input())
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    answer = ''
    for i in range(n):
        person = input().split(',')
        name = set()
        name.update(person[0]), name.update(person[1]), name.update(person[2])
        characterAmount = len(name)
        sum_of_digits = sum(int(digit) for digit in str(person[3]) + str(person[4])) * 64
        firstSurnameCharacter = [i+1 for i in range(len(alphabet)) if person[0][0].lower() == alphabet[i]][0] * 256
        itog = format(characterAmount + sum_of_digits + firstSurnameCharacter, 'X')[-3:]
        if i != n-1:
            answer += itog+' '
        else:
            answer += itog
    print(answer)



if __name__ == "__main__":
    main()