from flask import Flask, render_template, request, redirect

app = Flask(__name__)

users = {
    'supply': {'username': 'cherry', 'password': '6354', 'url': 'https://chatchanokt24.github.io/supplyV3/', 'thai_name': 'เจ้าหน้าที่จัดซื้อจัดจ้าง'},
    'warehouse': {'username': 'banana', 'password': '1539', 'url': 'https://chatchanokt24.github.io/supplyV3/', 'thai_name': 'เจ้าหน้าที่คลัง'},
    'logistic': {'username': 'lychee', 'password': '2451', 'url': 'https://chatchanokt24.github.io/supplyV3/', 'thai_name': 'เจ้าหน้าที่ขนส่ง'},
    'budgeting': {'username': 'mango', 'password': '3951', 'url': 'https://chatchanokt24.github.io/supplyV3/', 'thai_name': 'เจ้าหน้าที่งบประมาณ'}
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login/<dept>', methods=['GET', 'POST'])
def login(dept):
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == users[dept]['username'] and password == users[dept]['password']:
            return redirect(users[dept]['url'])
        else:
            return "Invalid username or password"
    thai_name = users[dept]['thai_name']
    return render_template('login.html', dept=dept, thai_name=thai_name)

if __name__ == '__main__':
    app.run(debug=True)
