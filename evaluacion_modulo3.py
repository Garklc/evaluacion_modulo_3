import json

# Archivo donde se guardan las tareas
TASK_FILE = "tasks.json"

def load_tasks():
    """Carga las tareas desde el archivo JSON."""
    try:
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Guarda las tareas en el archivo JSON."""
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    """Agrega una nueva tarea."""
    task_description = input("Ingresa la descripción de la tarea: ")
    tasks.append({"description": task_description, "completed": False})
    print("Tarea agregada exitosamente.")

def list_tasks(tasks):
    """Lista todas las tareas con su estado."""
    if not tasks:
        print("No hay tareas pendientes.")
        return
    print("\n--- Lista de Tareas ---")
    for index, task in enumerate(tasks, start=1):
        status = "Completada" if task["completed"] else "Pendiente"
        print(f"{index}. [{status}] {task['description']}")

def mark_task_completed(tasks):
    """Marca una tarea como completada."""
    list_tasks(tasks)
    try:
        task_index = int(input("Ingresa el número de la tarea que deseas marcar como completada: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]["completed"] = True
            print("Tarea marcada como completada.")
        else:
            print("Número de tarea inválido.")
    except ValueError:
        print("Entrada inválida. Debes ingresar un número.")

def delete_task(tasks):
    """Elimina una tarea."""
    list_tasks(tasks)
    try:
        task_index = int(input("Ingresa el número de la tarea que deseas eliminar: ")) - 1
        if 0 <= task_index < len(tasks):
            deleted_task = tasks.pop(task_index)
            print(f"Tarea eliminada: {deleted_task['description']}")
        else:
            print("Número de tarea inválido.")
    except ValueError:
        print("Entrada inválida. Debes ingresar un número.")

def main_menu():
    """Muestra el menú principal y permite al usuario seleccionar una opción."""
    tasks = load_tasks()

    while True:
        print("\n--- Gestor de Tareas ---")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")

        choice = input("Elige una opción: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingresa un número válido.")

        # Guardar las tareas después de cada operación
        save_tasks(tasks)

if __name__ == "__main__":
    main_menu()