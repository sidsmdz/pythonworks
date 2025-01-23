def reverse_words(sentence):
    sentence = list(sentence.split())
    left = 0
    right = len(sentence) - 1
    while left < right:
        sentence[left], sentence[right] = sentence[right], sentence[left]
        left += 1
        right -= 1
    # Replace this placeholder return statement with your code
    return ''.join(sentence)
