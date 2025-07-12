from fastapi import FastAPI
from models import Todo

app = FastAPI()

@app.get('/')
async def root() -> dict[str, str]:
    return {'message': "buenas mundo"}

todos = []

# Obtener todos los todos
@app.get('/todos')
async def get_all_todos() -> dict[str, list]:
    return {"todos": todos}

# Obtener solo un todo

@app.get('/todos/{todo_id}')
async def get_one_todo(todo_id : int):
    for todo in todos:
        if todo_id == todo.id:
            return {"todo": todo}
    return {"Mensaje": "No se encontró el to-do"}

# Crear un todo

@app.post('/todos')
async def create_one_todo(todo: Todo):
    todos.append(todo)
    return {"message": "Se agregó un to-do"}

# Modificar un to-do

@app.put('/todos/{todo_id}')
async def update_one_todo(todo_id : int, todo_object : Todo):
    for todo in todos:
        if todo_id == todo.id:
            todo.id = todo_id
            todo.description = todo_object.description
            return {"todo": todo}
    return {"Mensaje": "No se encontró el to-do para actualizar"}



# Eliminar un todo

@app.delete('/todos/{todo_id}')
async def delete_one_todo(todo_id : int):
    for todo in todos:
        if todo_id == todo.id:
            todos.remove(todo)
            return {"Mensaje": "To-do eliminado"}
    return {"Mensaje": "No se encontró el to-do"}