with open("story.txt", "r") as file:
    story = file.read

words = set()

word_start = "<"
word_end = ">"

start_of_word = "a"

for i, char in enumerate(story):
    if char == word_start:
        start_of_word = i
    elif char == word_end and start_of_word != "a":
        word = story[start_of_word: i+1]
        words.add(word)
        start_of_word ="a"

answers = {}

for word in words:
    answer = input("Enter your word for" + word + ": ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(story)