
def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)

        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: cannot divide by zero."
    
    except ValueError:
        return "Error: please enter numeric values only."
    


