# [코딩일지] 파이썬 예제뽀개기

* [유튜브 링크](https://www.youtube.com/playlist?list=PLGPF8gvWLYyomy0D1-uoQHTWPvjXTjr_a)
* [Checkio 사이트](https://py.checkio.org/)

## 문제풀이
```python
# 1. Say Hi
def say_hi(name: str, age: int) -> str:
    return "Hi. My name is {} and I'm {} years old".format(name, age)

if __name__  == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", "First"
    assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", "Second"
    print('Done. Time to check.')


# 2. Correct Sentence
def correct_sentence(text: str) -> str:
    text - text[0].upper() + text[1:]

    if not text.endswith('.'):
        text += '.'
    return text

if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert correct_sentence("greetings, friends.") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    assert correct_sentence("welcome to New York") == "Welcome to New York."
    
    print("Coding complete? Click 'Check' to earn cool rewards!")
```
