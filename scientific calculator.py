import math

def parse_expression(expression):
    """
    Parse a natural language expression into a mathematical expression.
    This is a simple parser and may not handle all edge cases.
    """
    # Replace common math terms with their equivalents
    expression = expression.lower()
    expression = expression.replace("plus", "+")
    expression = expression.replace("minus", "-")
    expression = expression.replace("times", "*")
    expression = expression.replace("divided by", "/")
    expression = expression.replace("power of", "**")
    expression = expression.replace("sqrt", "math.sqrt")
    expression = expression.replace("log", "math.log")
    expression = expression.replace("sin", "math.sin")
    expression = expression.replace("cos", "math.cos")
    expression = expression.replace("tan", "math.tan")
    
    return expression

def evaluate_expression(expression):
    """
    Evaluate the mathematical expression.
    """
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {str(e)}"

def scientific_calculator():
    """
    Run the scientific calculator.
    """
    print("Welcome to the scientific calculator. Type 'quit' to exit.")
    while True:
        user_input = input("Enter a calculation: ")
        if user_input.lower() == 'quit':
            break
        
        parsed_expression = parse_expression(user_input)
        result = evaluate_expression(parsed_expression)
        print(f"Result: {result}")

if __name__ == "__main__":
    scientific_calculator()
