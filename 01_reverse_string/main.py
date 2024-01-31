def reverse(text: str):
# --- Directions
# Given a string, return a new string with the reversed
# order of characters
# --- Examples
#   reverse('apple') === 'elppa'
#   reverse('hello') === 'olleh'
#   reverse('Greetings!') === '!sgniteerG'
    return ''.join(list(text)[::-1])

if __name__ == "__main__":
    print(f"Reverse is: {reverse(input('Given a string: '))}")