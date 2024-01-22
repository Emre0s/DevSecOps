from flask import Flask

app = Flask(__name__)

# Örnek bir To-Do List
tasks = []

@app.route('/')
def index():
    return (
        "To-Do List\n\n"
        "1. Görevleri Listele: /list\n"
        "2. Görev Ekle: /add/<task>\n"
        "3. Görev Tamamla: /complete/<index>"
    )

@app.route('/list')
def list_tasks():
    if not tasks:
        return "Görev yok!"
    
    task_list = "\n".join(f"{index + 1}. {task}" for index, task in enumerate(tasks))
    return f"To-Do List\n\n{task_list}"

@app.route('/add/<task>')
def add_task(task):
    tasks.append(task)
    return f"{task} görevi eklendi!"

@app.route('/complete/<int:index>')
def complete_task(index):
    if 1 <= index <= len(tasks):
        completed_task = tasks.pop(index - 1)
        return f"{completed_task} görevi tamamlandı!"
    else:
        return "Geçersiz indeks! Lütfen doğru bir indeks girin."

if __name__ == '__main__':
    app.run(debug=True)
