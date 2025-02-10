from flask import Flask, request, jsonify, render_tempalte
import subprocess

app = Flask(__name__)

#словарь
data = {
    "открой калькулятор": "gnome-calculator",
    "открой консоль"
}
@app.route('/')
def index():
    return render_tempalte('index.html')
@app.route(rule: '/process', methods=['POST'])
def process():
    user_input = request.json.get('input')
    result = analis(user_input)
    if user_input:
        response = f"вы подошли с запросом: {user_input}"
    else:
        response = "пожалуйста, введите ваш запрос."
    return  jsonify({"response": result})
if __name__ == '__main__':
    app.run(debug=True)