#!/usr/bin/python3
def multiple_returns(sentence):
    a = len(sentence)
    b = sentence[0]
    if not sentence:
        return (a, None)
    return (a, b)
