def is_pangram(sentence):
    alfabeto = set("abcdefghijklmnopqrstuvwxyz")
    sentence = sentence.lower()
    letras = set(c for c in sentence if c.isalpha())
    return alfabeto <= letras