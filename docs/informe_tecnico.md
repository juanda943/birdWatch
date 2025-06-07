# Informe Técnico: Sistema de Registro de Avistamiento de Aves

## 1. Introducción
El presente documento describe el desarrollo de un sistema web para el registro de avistamientos de aves, diseñado como proyecto final de la asignatura de Estructuras de Datos. El sistema permite ingresar, visualizar y ordenar registros usando estructuras como listas, colas y árboles binarios.

## 2. Objetivos
- Aplicar estructuras de datos para resolver un problema real.
- Implementar una aplicación web funcional con Flask.
- Facilitar el análisis y visualización de datos de avistamiento.

## 3. Justificación del Problema
La observación de aves es una actividad científica y recreativa que genera datos valiosos para estudios ecológicos. Este sistema busca facilitar el registro y consulta de dichos datos.

## 4. Estructuras de Datos Usadas
- **Listas dinámicas:** almacenan todos los registros.
- **Colas (deque):** mantienen los últimos 10 registros.
- **Árbol Binario de Búsqueda (BST):** clasifica avistamientos por especie.

## 5. Algoritmos Implementados
- **Ordenamiento por Fecha y Lugar:** usando `sorted` y claves personalizadas.
- **Recorridos en Orden del BST:** para listar especies en orden alfabético.
- **Búsqueda lineal en listas.**

## 6. Análisis de Complejidad (Resumen)
- Lista: inserción O(1), búsqueda O(n).
- Cola: inserción/borrado en extremos O(1).
- Árbol BST: inserción y búsqueda promedio O(log n), peor caso O(n).

## 7. Arquitectura del Sistema
- Flask como backend web.
- HTML con Jinja2 para frontend.
- Rutas para registrar, listar y ordenar avistamientos.
- Controladores Python para la lógica de estructuras.

## 8. Conclusiones
El sistema permite demostrar de manera práctica el uso de estructuras de datos fundamentales en un entorno realista y educativo. La arquitectura modular facilita su mantenimiento y futuras extensiones.

