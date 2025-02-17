from django.shortcuts import render, HttpResponse

def analyze_text(request, text):
    # Convert text to lowercase for uniformity.
    text_lower = text.lower()

    vowels_set = "aeiou"
    vowels_list = []
    consonants_list = []

    # Loop through each character in the text
    for char in text_lower:
        if char.isalpha():  # Only consider alphabetic characters.
            if char in vowels_set:
                vowels_list.append(char)
            else:
                consonants_list.append(char)

    context = {
        'input_text': text,
        'vowel_count': len(vowels_list),
        'consonant_count': len(consonants_list),
        'vowels': vowels_list,
        'consonants': consonants_list,
    }
    return render(request, 'textanalysis/analyze.html', context)
