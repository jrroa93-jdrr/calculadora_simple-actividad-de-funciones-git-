# 🧮 Proyecto: Calculadora Simple con Validación (Actividad Git & GitHub)

Este repositorio contiene el desarrollo de la **Actividad Formativa 3.2.2**, enfocada en el uso práctico de Git y GitHub para el control de versiones, trabajo con ramas (*branching*) y la integración de cambios mediante *Pull Requests*.

---

## 🛠️ Características del Proyecto

1. **Lógica Directa:** Operaciones matemáticas estructuradas mediante ciclos (`while`) y condicionales (`if-elif-else`).
2. **Validación de Datos:** Incorporación de un bloque `try-except` para capturar errores de tipo (`ValueError`) si el usuario ingresa caracteres no numéricos, evitando que el programa colapse.
3. **Control de Errores Matemáticos:** Validación integrada para evitar la división por cero de forma segura.

---

## 🌿 Estructura de Ramas del Repositorio

El flujo de trabajo se organizó dividiendo el desarrollo en las siguientes ramas:

* **`main`**: Contiene el código base inicial (la estructura elemental de la calculadora sin validaciones complejas de entrada).
* **`feature-validacion-datos`**: Rama secundaria creada específicamente para desarrollar e implementar la sentencia de validación `try-except`.

---

## 💻 Comandos de Git Utilizados

A continuación, se dejan los comandos secuenciales ejecutados en la terminal para completar la actividad:

```bash
# 1. Inicializar el repositorio y realizar el commit inicial en main
git init
git branch -M main
git add .
git commit -m "Commit inicial: Estructura básica de la calculadora sin funciones"

# 2. Vincular el repositorio local con el servidor de GitHub y subir la base
git remote add origin [https://github.com/jrroa93-jdrr/calculadora_simple-actividad-de-funciones-git-.git](https://github.com/jrroa93-jdrr/calculadora_simple-actividad-de-funciones-git-.git)
git push -u origin main

# 3. Crear y cambiarse a la rama de desarrollo de la nueva característica
git checkout -b feature-validacion-datos

# [Aquí se aplicaron las modificaciones de validación en el archivo main.py]

# 4. Guardar los cambios locales y subirlos a la nueva rama remota
git add .
git commit -m "Actualización: Se añade sentencia try-except para validar la entrada de datos numéricos"
git push -u origin feature-validacion-datos