import webbrowser
import os
import sys
import time

def list_to_query(query):
    text_query = ""
    true_text = ""
    for val in query:
        text_query += str(val)+"+"
        true_text += str(val)+" "
    os.system('cls')
    print("Search: '" + true_text[:-1] + "'")
    time.sleep(1)
    return text_query

def main():
    if len(sys.argv) < 2:
        os.system('cls')
        input_query = input("Enter your query: ")
        print("Search: '" + input_query + "'")
        time.sleep(1)
    else:    
        input_query = sys.argv[1:]
        input_query = list_to_query(input_query)[:-1]
    os.system('cls')

    def search(input_query):
        query = "https://www.google.fr/search?q=" + input_query
        webbrowser.open_new(query)

    search(input_query)

main()