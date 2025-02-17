from django.shortcuts import render, HttpResponse

def mod_view(request, dividend, divisor):
    try:
        # Compute modulo
        result = dividend % divisor
    except ZeroDivisionError:
        return HttpResponse("Error: Division by zero is not allowed.")
    
    # For simplicity, we can return an HTML response showing the result.
    html = f"""
    <html>
        <head>
            <title>Modulo Result</title>
        </head>
        <body>
            <h1>Modulo Calculation</h1>
            <p>{dividend} % {divisor} = {result}</p>
        </body>
    </html>
    """
    return HttpResponse(html)
