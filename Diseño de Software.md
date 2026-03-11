# Diseño-de-Software

# ACTIVIDAD EJERCICIO BASE (Adaptado a Supermercado)

# Enunciado del Ejercicio:

Se le ha encargado el desarrollo de una aplicación de software para un supermercado que necesita calcular el total de las ventas realizadas por sus productos durante el día. El supermercado paga y registra los productos según su precio unitario y la cantidad vendida.

La aplicación debe registrar el código del producto, el nombre del producto, el precio unitario y la cantidad vendida. Con esta información, el sistema debe calcular el total por producto y el total consolidado de todas las ventas.

## Aclaraciones:

• Tanto el precio del producto como la cantidad vendida pueden variar entre productos.

• El cálculo corresponde únicamente al valor total de venta (sin impuestos ni descuentos).

• La aplicación solo debe calcular el total de ventas de un único día.

• Para simplificar el ejercicio, no se requiere persistencia de los datos (es decir, los datos no necesitan almacenarse de manera permanente).


# Historia de Usuario

**Título:** Cálculo y visualización del total de ventas

**Como:** Administrador del supermercado

**Quiero:** Ingresar los datos de los productos (código, nombre, precio unitario y cantidad vendida)

**Para:** Calcular automáticamente el total de venta por producto y obtener el total consolidado del día.

**Descripción:**

El sistema debe permitir registrar múltiples productos, calcular el total de venta de cada producto y mostrar el total acumulado del día.


# Requisitos:

La herramienta debe permitirme ingresar los siguientes datos de cada producto:

• Código del producto

• Nombre del producto

• Precio unitario

• Cantidad vendida


Calcular el total de venta individual de cada producto mediante la fórmula:

**Total producto = precio unitario × cantidad vendida**


La herramienta debe ser fácil de usar y no requerir conocimientos técnicos avanzados.

# Criterios de Aceptación:

• El sistema permite ingresar uno o más productos.

• Para cada producto válido: Se calcula el total correctamente y se muestra el valor calculado.

• El sistema muestra el total consolidado de todas las ventas.


# Diagrama UML: Caso de Uso

**Actor:** Administrador del Supermercado

**Sistema:** Sistema de Ventas del Supermercado

**Caso de uso principal:**

Calcular Total de Ventas de Productos


Representación textual:

Administrador del Supermercado → (Calcular Total de Ventas de Productos)
<img width="714" height="350" alt="image-Photoroom" src="https://github.com/user-attachments/assets/f9e07aee-ac0f-4e8c-8ebd-85c6f36b1f4f" />

# Caso de Uso Extendido

**Nombre:** Calcular Total de Ventas

**Actores:** Administrador del Supermercado

**Propósito:** Registrar los datos de los productos y calcular el total de las ventas.


### Curso de eventos:

1. El administrador ingresa la cantidad de productos a registrar.

2. Para cada producto:

   • El administrador ingresa el código del producto.

   • El administrador ingresa el nombre del producto.

   • El administrador ingresa el precio unitario.

   • El administrador ingresa la cantidad vendida.

   • La aplicación almacena los datos ingresados.

3. Una vez ingresados todos los productos, el sistema recorre la información almacenada y calcula el total de cada producto mediante la operación:

   **precio unitario × cantidad vendida**

4. El sistema muestra:

   • Total por producto

   • Total general de ventas


# Diagrama de flujo
<img width="683" height="2475" alt="Diagrama de flujo" src="https://github.com/user-attachments/assets/c21b406b-17fe-4d75-a0d6-148a5afebf81" />

"""
