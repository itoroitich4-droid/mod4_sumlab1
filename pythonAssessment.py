import string

with open("news_article.txt", "r", encoding="utf-8") as file:
    article_text = file.read()

print(article_text[2:9])

def count_specific_word(text, word):
    words = text.split()
    count = 0
    x = 0
    while x < len(words):
        if words[x] == word:
            count += 1
        x += 1
    return count

def identify_most_common_word(text):
    if text == "":
        return None
    words = text.split()
    word_count = {}
    for word in words:
        word = word.strip(".,!?;:\"'()[]")
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    most_common = max(word_count, key=word_count.get)
    return most_common


def count_sentences(text):
    if text == "":
        return 1
    count = 0
    for character in text:
        if character == "." or character == "!" or character == "?":
            count += 1
    return count

def count_paragraphs(text):
    if text == "":
        return 1
    paragraphs = text.strip().split("\n\n")
    return len(paragraphs)


def calculate_average_word_length(text):
    if text == "":
        return 0
    words = text.split()
    total_length = 0
    word_count = 0
    for word in words:
        word = word.strip(string.punctuation)
        if word:
            total_length += len(word)
            word_count += 1
    return total_length / word_count

print("Most common word:", identify_most_common_word(article_text))
print("Average word length:", calculate_average_word_length(article_text))
print("Number of paragraphs:", count_paragraphs(article_text))
print("Number of sentences:", count_sentences(article_text))