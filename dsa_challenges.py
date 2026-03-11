
def filter_and_sort_evens(numbers):
    # Keep only even numbers
    evens = [num for num in numbers if num % 2 == 0]
    
    # Sort the list
    evens.sort()
    
    return evens


def count_character_frequency(text):
    freq = {}
    
    # Convert text to lowercase for case-insensitive counting
    text = text.lower()
    
    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
            
    return freq


# Example calls to test the functions

numbers = [5, 2, 9, 8, 1, 4, 6]
print(filter_and_sort_evens(numbers))

text = "Hello World"
print(count_character_frequency(text))