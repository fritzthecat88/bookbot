import sys
from stats import main, get_book_text, number_characters, print_report, sort_on

#y = "/Users/aleksanenadovic/workspace/github.com/fritzthecat88/bookbot/books/frankenstein.txt"

if len(sys.argv) > 1:
    y = sys.argv[1]
else:
    print ("how to call --->> Usage: python3 main.py <path_to_book>")
    sys.exit(1) 

num_words = main(y)
print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
print(f"Found {num_words} total words")
print("--------- Character Count -------")

text = get_book_text(y)
dict = number_characters(text)
w = print_report(dict)
w.sort(reverse=True, key=sort_on)

for i in range(0, len(w)):
    if (w[i]['char']).isalpha(): 
        print(f"{w[i]['char']}: {w[i]['num']}")
print("============= END ===============")