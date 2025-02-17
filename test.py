import nltk
nltk.download('punkt_tab')

tokenizer = nltk.tokenize.punkt.PunktLanguageVars()
words = "I can't believe it's 2025!"

print(tokenizer.word_tokenize(words))
print(nltk.word_tokenize(words))