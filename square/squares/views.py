from django.shortcuts import render
from django.http import HttpResponse

def table_of_squares(request, num):
    try:
        n = int(num)
    except ValueError:
        return HttpResponse("Invalid number provided.")

    # Create a list of tuples: (number, square)
    squares = [(i, i * i) for i in range(1, n + 1)]
    context = {
        'n': n,
        'squares': squares,
    }
    return render(request, 'squares/table_of_squares.html', context)
