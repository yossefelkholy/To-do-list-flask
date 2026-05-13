from flask import Flask, render_template, request, redirect

app = Flask(__name__)
FILE_NAME = "data.txt"

def load_tasks():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return file.read().splitlines()
    except:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")

@app.route('/', methods=['GET', 'POST'])
def home():
    tasks = load_tasks()
    if request.method == 'POST':
        task = request.form.get('task')
        if task:
            tasks.append(task)
            save_tasks(tasks)
            return redirect('/')
    return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:index>')
def delete(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)