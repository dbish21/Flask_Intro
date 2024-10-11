from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

# Create a dictionary to map operation names to functions
operations = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}

@app.route('/math/<operation>')
def calculate(operation):
    # Get the numbers from the query parameters
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))

    # Check if the operation is valid and get the corresponding function
    operation_func = operations.get(operation)

    if operation_func:
        result = operation_func(a, b)
        return str(result)
    else:
        return "Invalid operation", 400

if __name__ == '__main__':
    app.run(debug=True)
