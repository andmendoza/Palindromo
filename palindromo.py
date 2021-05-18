def palindromo():
    word = input("Enter your word: ")
    word = word.replace(' ', '')
    word = word.upper()
    word_inverted = word[::-1]
    if word == word_inverted:
        print(word, ", is a palindromo")
    else:
        print(word, ",it's not palindromo")

def main():
    palindromo()



if __name__ == '__main__':
    main()
