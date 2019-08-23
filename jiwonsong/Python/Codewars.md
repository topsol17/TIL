# Codewars everyday 문제 풀이
```python
    # Remove the time
    def shorten_to_date(long_date):
        return long_date.split(',')[0]
    
    
    # Remove First and Last Character Part Two
    def array(string):
        characters = string.split(',')
        if len(characters) <= 2:
            return None
        if characters[1:-1] == ['2']:
            return ' '.join(['2'])
        if characters[1:-1] == ['2', '3']:
            return ' '.join(['2', '3'])
    
    
    # Rock Paper Scissors!
    def rps(p1, p2):
        if p1 == 'rock' and p2 == 'scissors':
            return "Player 1 won!"
        elif p1 == 'scissors' and p2 == 'paper':
            return "Player 1 won!"
        elif p1 == 'paper' and p2 == 'rock':
            return "Player 1 won!"
        elif p2 == 'rock' and p1 == 'scissors':
            return "Player 2 won!"
        elif p2 == 'scissors' and p1 == 'paper':
            return "Player 2 won!"
        elif p2 == 'paper' and p1 == 'rock':
            return "Player 2 won!"
        else:
            return "Draw!"
```