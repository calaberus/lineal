# Datos de ejemplo
productos = [
    {'id': 1, 'nombre': 'iPhone 15', 'marca': 'Apple', 'categoria': 'Smartphone', 'precio': 999.99, 'stock': 10, 'disponible': True},
    {'id': 2, 'nombre': 'Samsung Galaxy S24', 'marca': 'Samsung', 'categoria': 'Smartphone', 'precio': 899.99, 'stock': 8, 'disponible': True},
    {'id': 3, 'nombre': 'MacBook Air M3', 'marca': 'Apple', 'categoria': 'Laptop', 'precio': 1299.99, 'stock': 5, 'disponible': True},
    {'id': 4, 'nombre': 'Dell XPS 13', 'marca': 'Dell', 'categoria': 'Laptop', 'precio': 1199.99, 'stock': 0, 'disponible': False},
    {'id': 5, 'nombre': 'Sony WH-1000XM5', 'marca': 'Sony', 'categoria': 'Audífonos', 'precio': 399.99, 'stock': 15, 'disponible': True}
]

def _norm(valor):
    return valor.strip().lower() if isinstance(valor, str) else valor

def buscar_producto_por_nombre(productos, nombre_buscado):
    """Busca un producto por nombre (búsqueda lineal, case-insensitive)."""
    nombre_norm = _norm(nombre_buscado)
    return next((p for p in productos if _norm(p.get('nombre')) == nombre_norm), None)

def buscar_producto_por_id(productos, id_buscado):
    """Busca un producto por ID (búsqueda lineal)."""
    return next((p for p in productos if p.get('id') == id_buscado), None)

def buscar_productos_por_categoria(productos, categoria_buscada):
    """Devuelve lista de productos que pertenecen a una categoría (case-insensitive)."""
    categoria_norm = _norm(categoria_buscada)
    return [p for p in productos if _norm(p.get('categoria')) == categoria_norm]

def buscar_productos_por_marca(productos, marca_buscada):
    """Devuelve lista de productos de una marca (case-insensitive)."""
    marca_norm = _norm(marca_buscada)
    return [p for p in productos if _norm(p.get('marca')) == marca_norm]

def buscar_productos_disponibles(productos):
    """Devuelve productos con stock > 0 y disponibles."""
    return [p for p in productos if p.get('disponible') and p.get('stock', 0) > 0]

# Pruebas de las funciones
print("=== PRUEBAS DE BÚSQUEDA LINEAL EN PRODUCTOS ===\n")

# Prueba 1: Búsqueda por nombre
print("1. Búsqueda por nombre:")
resultado = buscar_producto_por_nombre(productos, "MacBook Air M3")
print(f"   Buscando 'MacBook Air M3': {resultado}\n")

# Prueba 2: Búsqueda por ID
print("2. Búsqueda por ID:")
resultado = buscar_producto_por_id(productos, 2)
print(f"   Buscando ID 2: {resultado}\n")

# Prueba 3: Búsqueda por categoría
print("3. Búsqueda por categoría:")
resultados = buscar_productos_por_categoria(productos, "Laptop")
print(f"   Productos en categoría 'Laptop':")
for producto in resultados:
    print(f"   - {producto['nombre']} (${producto['precio']})")

# Prueba 4: Búsqueda por marca
print("\n4. Búsqueda por marca:")
resultados = buscar_productos_por_marca(productos, "Apple")
print(f"   Productos de marca 'Apple':")
for producto in resultados:
    print(f"   - {producto['nombre']} (${producto['precio']})")

# Prueba 5: Búsqueda de productos disponibles
print("\n5. Productos disponibles:")
resultados = buscar_productos_disponibles(productos)
print("   Productos con stock disponible:")
for producto in resultados:
    print(f"   - {producto['nombre']} (Stock: {producto['stock']})")

# Prueba 6: Búsqueda que no encuentra resultados
print("\n6. Búsquedas sin resultados:")
resultado = buscar_producto_por_nombre(productos, "Producto Inexistente")
print(f"   Buscando 'Producto Inexistente': {resultado}")

resultado = buscar_producto_por_id(productos, 99)
print(f"   Buscando ID 99: {resultado}")

def buscar_productos_con_filtros(productos, **filtros):
    """
    Busca productos aplicando múltiples filtros.
    Comparación case-insensitive para valores string.
    """
    def cumple(producto):
        for clave, valor in filtros.items():
            if clave not in producto:
                return False
            v_prod = producto[clave]
            if isinstance(valor, str) and isinstance(v_prod, str):
                if _norm(v_prod) != _norm(valor):
                    return False
            else:
                if v_prod != valor:
                    return False
        return True

    return [p for p in productos if cumple(p)]

# Prueba de búsqueda con filtros múltiples
print("\n7. Búsqueda con filtros múltiples:")
resultados = buscar_productos_con_filtros(productos, marca='Apple', categoria='Smartphone')
print("   Productos Apple en categoría Smartphone:")
for producto in resultados:
    print(f"   - {producto['nombre']}")

# Datos de ejemplo
productos = [
    {'id': 1, 'nombre': 'iPhone 15', 'marca': 'Apple', 'categoria': 'Smartphone', 'precio': 999.99, 'stock': 10, 'disponible': True},
    {'id': 2, 'nombre': 'Samsung Galaxy S24', 'marca': 'Samsung', 'categoria': 'Smartphone', 'precio': 899.99, 'stock': 8, 'disponible': True},
    {'id': 3, 'nombre': 'MacBook Air M3', 'marca': 'Apple', 'categoria': 'Laptop', 'precio': 1299.99, 'stock': 5, 'disponible': True},
    {'id': 4, 'nombre': 'Dell XPS 13', 'marca': 'Dell', 'categoria': 'Laptop', 'precio': 1199.99, 'stock': 0, 'disponible': False},
    {'id': 5, 'nombre': 'Sony WH-1000XM5', 'marca': 'Sony', 'categoria': 'Audífonos', 'precio': 399.99, 'stock': 15, 'disponible': True}
]

def _norm(valor):
    return valor.strip().lower() if isinstance(valor, str) else valor

def buscar_producto_por_nombre(productos, nombre_buscado):
    """Busca un producto por nombre (búsqueda lineal, case-insensitive)."""
    nombre_norm = _norm(nombre_buscado)
    return next((p for p in productos if _norm(p.get('nombre')) == nombre_norm), None)

def buscar_producto_por_id(productos, id_buscado):
    """Busca un producto por ID (búsqueda lineal)."""
    return next((p for p in productos if p.get('id') == id_buscado), None)

def buscar_productos_por_categoria(productos, categoria_buscada):
    """Devuelve lista de productos que pertenecen a una categoría (case-insensitive)."""
    categoria_norm = _norm(categoria_buscada)
    return [p for p in productos if _norm(p.get('categoria')) == categoria_norm]

def buscar_productos_por_marca(productos, marca_buscada):
    """Devuelve lista de productos de una marca (case-insensitive)."""
    marca_norm = _norm(marca_buscada)
    return [p for p in productos if _norm(p.get('marca')) == marca_norm]

def buscar_productos_disponibles(productos):
    """Devuelve productos con stock > 0 y disponibles."""
    return [p for p in productos if p.get('disponible') and p.get('stock', 0) > 0]

# Pruebas de las funciones
print("=== PRUEBAS DE BÚSQUEDA LINEAL EN PRODUCTOS ===\n")

# Prueba 1: Búsqueda por nombre
print("1. Búsqueda por nombre:")
resultado = buscar_producto_por_nombre(productos, "MacBook Air M3")
print(f"   Buscando 'MacBook Air M3': {resultado}\n")

# Prueba 2: Búsqueda por ID
print("2. Búsqueda por ID:")
resultado = buscar_producto_por_id(productos, 2)
print(f"   Buscando ID 2: {resultado}\n")

# Prueba 3: Búsqueda por categoría
print("3. Búsqueda por categoría:")
resultados = buscar_productos_por_categoria(productos, "Laptop")
print(f"   Productos en categoría 'Laptop':")
for producto in resultados:
    print(f"   - {producto['nombre']} (${producto['precio']})")

# Prueba 4: Búsqueda por marca
print("\n4. Búsqueda por marca:")
resultados = buscar_productos_por_marca(productos, "Apple")
print(f"   Productos de marca 'Apple':")
for producto in resultados:
    print(f"   - {producto['nombre']} (${producto['precio']})")

# Prueba 5: Búsqueda de productos disponibles
print("\n5. Productos disponibles:")
resultados = buscar_productos_disponibles(productos)
print("   Productos con stock disponible:")
for producto in resultados:
    print(f"   - {producto['nombre']} (Stock: {producto['stock']})")

# Prueba 6: Búsqueda que no encuentra resultados
print("\n6. Búsquedas sin resultados:")
resultado = buscar_producto_por_nombre(productos, "Producto Inexistente")
print(f"   Buscando 'Producto Inexistente': {resultado}")

resultado = buscar_producto_por_id(productos, 99)
print(f"   Buscando ID 99: {resultado}")

def buscar_productos_con_filtros(productos, **filtros):
    """
    Busca productos aplicando múltiples filtros.
    Comparación case-insensitive para valores string.
    """
    def cumple(producto):
        for clave, valor in filtros.items():
            if clave not in producto:
                return False
            v_prod = producto[clave]
            if isinstance(valor, str) and isinstance(v_prod, str):
                if _norm(v_prod) != _norm(valor):
                    return False
            else:
                if v_prod != valor:
                    return False
        return True

    return [p for p in productos if cumple(p)]

# Prueba de búsqueda con filtros múltiples
print("\n7. Búsqueda con filtros múltiples:")
resultados = buscar_productos_con_filtros(productos, marca='Apple', categoria='Smartphone')
print("   Productos Apple en categoría Smartphone:")
for producto in resultados:
    print(f"   - {producto['nombre']}") 
    
#¿Cuál es la complejidad temporal ?
# La complejidad temporal de las búsquedas lineales es O(n), donde n es el número de productos en la lista.

# ¿En qué casos la búsqueda lineal es eficiente?        
# La búsqueda lineal es eficiente para listas pequeñas o cuando los elementos están distribuidos de manera uniforme

# ¿Cuándo sería mejor usar otro algoritmo de búsqueda?
# Sería mejor usar otro algoritmo de búsqueda, como la búsqueda binaria, cuando la lista  está ordenada y es grande, ya que la búsqueda binaria tiene una complejidad temporal de O(log n).

