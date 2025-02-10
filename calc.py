from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        operation = request.form['operation']
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                return "Ошибка! Деление на ноль."
        else:
            result = "Неизвестная операция"

        return f"Результат: {result}"
    except Exception as e:
        return f"Ошибка: {e}"


if __name__ == '__main__':
    app.run(debug=True)