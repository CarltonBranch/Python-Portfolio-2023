"""One classic method for composing secret messages is called a square code.
The spaces are removed from the english text and the characters are written
into a square (or rectangle).  For example, the sentence "If man was meant
to stay on the ground god would have given us roots" is 54 characters long,
so it is written into a rectangle with 7 rows and 8 columns.
                ifmanwas
                meanttos        
                tayonthe
                groundgo
                dwouldha
                vegivenu
                sroots
The coded message is obtained by reading down the columns going left to right.
For example, the message above is coded as:

imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn  sseoau

In your program, have the user enter a message in english with no spaces
between the words.
"""
import math


class SquareCode:
    def __init__(self, words):
        self.words = words
        self.raw_words = ""
        self.width = 0
        self.process_words()

    def process_words(self):
        self.raw_words = "".join(self.words.strip().split(" "))
        self.width = math.ceil(math.sqrt(len(self.raw_words)))

    def print_square_string(self):
        print("Printing Square String...")
        char_count = 0
        for char in self.raw_words:
            print(char, end="")
            char_count += 1
            if char_count == self.width:
                print()
                char_count = 0

    def print_square_code(self):
        print("Printing Square Code...")
        result = ""
        for i in range(self.width):
            count = i
            while count < len(self.raw_words):
                result += self.raw_words[count]
                count += self.width
            result += " "
        print(result)


sq = SquareCode(
    "if man was meant to stay on the ground god would have given us \
    roots"
)

sq.print_square_string()
print("\n")
sq.print_square_code()
# should print:  imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau
