num = int(input("Enter a number: "))

def number_to_words(num):
    # vocabS   
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand", "million", "billion", "trillion"]

    def helper(num):
        if num == 0:
            return "zero"
        elif num < 10:
            return ones[num]
        elif num < 20:
            return teens[num - 10]
        elif num < 100:
            return tens[num // 10] + (" " + ones[num % 10] if num % 10 != 0 else "")
        elif num < 1000:
            return ones[num // 100] + " hundred" + (" " + helper(num % 100) if num % 100 != 0 else "")

    if num == 0:
        return "zero"

    words = ""
    i = 0
    while num > 0:
        if num % 1000 != 0:
            words = helper(num % 1000) + " " + thousands[i] + " " + words
        num //= 1000
        i += 1

    return words.strip()


print(number_to_words(num))