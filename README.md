# 📝 Task Manager CLI (Gestor de Tareas)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Estado](https://img.shields.io/badge/Estado-Finalizado-green)
![Data](https://img.shields.io/badge/Persistencia-JSON-orange)

## 📖 Descripción del Proyecto
Este es un **Sistema de Gestión de Tareas (To-Do List)** desarrollado en Python que se ejecuta en la terminal. 

A diferencia de programas simples que pierden la información al cerrarse, este proyecto implementa **persistencia de datos**. Utiliza un archivo `tasks.json` como base de datos local, permitiendo que el usuario cierre el programa y recupere sus tareas intactas al volver a abrirlo.

El objetivo fue crear una herramienta ligera, rápida y útil para la organización personal sin depender de internet.

---

## 💻 Demostración de Funcionalidad
> *Nota: Este proyecto está documentado visualmente aquí en lugar de un video tutorial.*

### 1. Menú Principal Interactivo
El sistema cuenta con un bucle infinito `while True` que mantiene el programa activo hasta que el usuario decide salir, mostrando siempre las opciones disponibles:

```text
--- Gestor de Tareas ---
1. Agregar tarea
2. Ver tareas
3. Marcar tarea como completada
4. Eliminar tarea
5. Salir
Elige una opción: _
