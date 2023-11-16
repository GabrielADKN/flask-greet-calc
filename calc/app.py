# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_route():
    """Add a and b."""
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    return str(add(a, b))

@app.route('/sub')
def sub_route():
    """Substract b from a."""
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    return str(sub(a, b))

@app.route('/mult')
def mult_route():
    """Multiply a and b."""
    a = int(request.args.get("a", 1))
    b = int(request.args.get("b", 1))
    return str(mult(a, b))

@app.route('/div')
def div_route():
    """Divide a by b."""
    a = int(request.args.get("a", 1))
    b = int(request.args.get("b", 1))
    return str(div(a, b))

@app.route('/math/<operation>')
def math_route(operation):
    """Perform a math operation on a and b."""
    a = int(request.args.get("a", 1))
    b = int(request.args.get("b", 1))
    if operation == "add":
        return str(add(a, b))
    elif operation == "sub":
        return str(sub(a, b))
    elif operation == "mult":
        return str(mult(a, b))
    elif operation == "div":
        return str(div(a, b))
    else:
        return "Invalid operation."

if __name__ == '__main__':
    app.run(debug=True)