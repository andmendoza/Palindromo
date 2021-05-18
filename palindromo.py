def palindromo():
    word = input("Enter your word: ")
    if word == word[::-1]:
        print(word, " is a palindromo")
    else:
        print(word, "it's not palindromo")

def main():
    palindromo()



if __name__ == '__main__':
    main()
