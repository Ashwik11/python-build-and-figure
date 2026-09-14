def analyze_numbers(numbers):
    """Return required statistics without min, max, or sum."""
    if not numbers:
        return {"largest": None, "smallest": None, "total": 0, "average": None, "even": 0, "odd": 0, "positive": 0, "negative": 0}
    largest = smallest = numbers[0]
    total = even = odd = positive = negative = 0
    for number in numbers:
        total += number
        largest = number if number > largest else largest
        smallest = number if number < smallest else smallest
        if number % 2 == 0:
            even += 1
        else:
            odd += 1
        if number > 0:
            positive += 1
        elif number < 0:
            negative += 1
    return {"largest": largest, "smallest": smallest, "total": total, "average": total / len(numbers), "even": even, "odd": odd, "positive": positive, "negative": negative}


print(analyze_numbers([-3, 0, 4, 7, 10]))
