from typing import List, Dict, Any, Optional
from collections import Counter

# Datos de ejemplo (ampliados para mejores pruebas)
productos: List[Dict[str, Any]] = [
    {'id': 1, 'nombre': 'iPhone 15', 'marca': 'Apple', 'categoria': 'Smartphone', 'precio': 999.99, 'stock': 10, 'disponible': True},
    {'id': 2, 'nombre': 'Samsung Galaxy S24', 'marca': 'Samsung', 'categoria': 'Smartphone', 'precio': 899.99, 'stock': 8, 'disponible': True},
    {'id': 3, 'nombre': 'MacBook Air M3', 'marca': 'Apple', 'categoria': 'Laptop', 'precio': 1299.99, 'stock': 5, 'disponible': True},
    {'id': 4, 'nombre': 'Dell XPS 13', 'marca': 'Dell', 'categoria': 'Laptop', 'precio': 1199.99, 'stock': 0, 'disponible': False},
    {'id': 5, 'nombre': 'Sony WH-1000XM5', 'marca': 'Sony', 'categoria': 'Audífonos', 'precio': 399.99, 'stock': 15, 'disponible': True},
    {'id': 6, 'nombre': 'iPad Air', 'marca': 'Apple', 'categoria': 'Tablet', 'precio': 599.99, 'stock': 3, 'disponible': True},
    {'id': 7, 'nombre': 'Samsung Galaxy Tab', 'marca': 'Samsung', 'categoria': 'Tablet', 'precio': 449.99, 'stock': 0, 'disponible': False},
    {'id': 8, 'nombre': 'AirPods Pro', 'marca': 'Apple', 'categoria': 'Audífonos', 'precio': 249.99, 'stock': 20, 'disponible': True},
    {'id': 9, 'nombre': 'Logitech MX Keys', 'marca': 'Logitech', 'categoria': 'Accesorios', 'precio': 99.99, 'stock': 12, 'disponible': True},
    {'id': 10, 'nombre': 'HP Pavilion', 'marca': 'HP', 'categoria': 'Laptop', 'precio': 799.99, 'stock': 2, 'disponible': True}
]

def _norm_str(s: Optional[str]) -> str:
    return s.strip().lower() if isinstance(s, str) else ''

def buscar_productos_disponibles(productos: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Devuelve productos con stock > 0 y disponibles."""
    return [p for p in productos if p.get('stock', 0) > 0 and p.get('disponible')]

def buscar_productos_sin_stock(productos: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Devuelve productos cuyo stock es exactamente 0."""
    return [p for p in productos if p.get('stock', 0) == 0]

def buscar_productos_por_rango_precio(productos: List[Dict[str, Any]], precio_min: float, precio_max: float) -> List[Dict[str, Any]]:
    """Devuelve productos cuyo precio está dentro del rango [precio_min, precio_max]."""
    return [p for p in productos if precio_min <= p.get('precio', 0.0) <= precio_max]

def buscar_productos_por_marca(productos: List[Dict[str, Any]], marca_buscada: str) -> List[Dict[str, Any]]:
    """Devuelve productos que coinciden con la marca (case-insensitive)."""
    marca_norm = _norm_str(marca_buscada)
    return [p for p in productos if _norm_str(p.get('marca')) == marca_norm]

def contar_productos_por_categoria(productos: List[Dict[str, Any]], categoria_buscada: Optional[str] = None):
    """
    Si se pasa categoria_buscada devuelve el conteo (int) de esa categoría,
    si no, devuelve dict con conteos por categoría.
    """
    if categoria_buscada:
        categoria_norm = _norm_str(categoria_buscada)
        return sum(1 for p in productos if _norm_str(p.get('categoria')) == categoria_norm)
    # Conteo general
    categorias = [p.get('categoria', '') for p in productos]
    return dict(Counter(categorias))

def buscar_productos_por_stock_minimo(productos: List[Dict[str, Any]], stock_minimo: int) -> List[Dict[str, Any]]:
    """Devuelve productos con stock >= stock_minimo."""
    return [p for p in productos if p.get('stock', 0) >= stock_minimo]

def buscar_productos_bajo_stock(productos: List[Dict[str, Any]], limite_stock: int = 5) -> List[Dict[str, Any]]:
    """Devuelve productos con 0 < stock <= limite_stock (necesitan reabastecerse)."""
    return [p for p in productos if 0 < p.get('stock', 0) <= limite_stock]

def obtener_productos_mas_caros(productos: List[Dict[str, Any]], cantidad: int = 3) -> List[Dict[str, Any]]:
    """Devuelve los N productos más caros."""
    return sorted(productos, key=lambda x: x.get('precio', 0.0), reverse=True)[:cantidad]

def obtener_productos_mas_baratos(productos: List[Dict[str, Any]], cantidad: int = 3) -> List[Dict[str, Any]]:
    """Devuelve los N productos más baratos."""
    return sorted(productos, key=lambda x: x.get('precio', 0.0))[:cantidad]

def calcular_valor_inventario_total(productos: List[Dict[str, Any]]) -> float:
    """Suma precio * stock para cada producto."""
    return sum(p.get('precio', 0.0) * p.get('stock', 0) for p in productos)

def buscar_productos_con_filtros_multiples(productos: List[Dict[str, Any]], **filtros) -> List[Dict[str, Any]]:
    """
    Aplicación de múltiples filtros:
      - precio_min / precio_max
      - stock_min / stock_max
      - disponible (bool)
      - comparaciones exactas para otras claves (case-insensitive si son str)
    """
    def cumple(p: Dict[str, Any]) -> bool:
        for clave, valor in filtros.items():
            if clave == 'precio_min':
                if p.get('precio', 0.0) < valor: return False
            elif clave == 'precio_max':
                if p.get('precio', 0.0) > valor: return False
            elif clave == 'stock_min':
                if p.get('stock', 0) < valor: return False
            elif clave == 'stock_max':
                if p.get('stock', 0) > valor: return False
            elif clave == 'disponible':
                if p.get('disponible') != valor: return False
            elif clave in p:
                v_prod = p[clave]
                if isinstance(valor, str) and isinstance(v_prod, str):
                    if _norm_str(v_prod) != _norm_str(valor): return False
                else:
                    if v_prod != valor: return False
            else:
                return False
        return True

    return [p for p in productos if cumple(p)]

# Pruebas de las funciones (misma salida que el original)
print("=== BÚSQUEDA POR DISPONIBILIDAD Y CRITERIOS CONDICIONALES ===\n")

# Prueba 1: Productos disponibles
print("1. PRODUCTOS DISPONIBLES:")
disponibles = buscar_productos_disponibles(productos)
print(f"   Total de productos disponibles: {len(disponibles)}")
for producto in disponibles:
    print(f"   - {producto['nombre']} (Stock: {producto['stock']}, Precio: ${producto['precio']})")

# Prueba 2: Productos sin stock
print("\n2. PRODUCTOS SIN STOCK:")
sin_stock = buscar_productos_sin_stock(productos)
print(f"   Total de productos sin stock: {len(sin_stock)}")
for producto in sin_stock:
    print(f"   - {producto['nombre']} ({producto['categoria']})")

# Prueba 3: Búsqueda por rango de precios
print("\n3. PRODUCTOS ENTRE $500 Y $1000:")
en_rango = buscar_productos_por_rango_precio(productos, 500, 1000)
print(f"   Productos encontrados: {len(en_rango)}")
for producto in en_rango:
    print(f"   - {producto['nombre']}: ${producto['precio']}")

# Prueba 4: Búsqueda por marca
print("\n4. PRODUCTOS APPLE:")
productos_apple = buscar_productos_por_marca(productos, "Apple")
print(f"   Total productos Apple: {len(productos_apple)}")
for producto in productos_apple:
    print(f"   - {producto['nombre']} (${producto['precio']}, Stock: {producto['stock']})")

# Prueba 5: Conteo por categoría
print("\n5. CONTEO DE PRODUCTOS POR CATEGORÍA:")
conteo_categorias = contar_productos_por_categoria(productos)
for categoria, cantidad in conteo_categorias.items():
    print(f"   - {categoria}: {cantidad} producto(s)")

# Prueba específica por categoría
print(f"\n   Productos en categoría 'Laptop': {contar_productos_por_categoria(productos, 'Laptop')}")

# Prueba 6: Productos con stock mínimo
print("\n6. PRODUCTOS CON STOCK MÍNIMO DE 10 UNIDADES:")
stock_minimo = buscar_productos_por_stock_minimo(productos, 10)
for producto in stock_minimo:
    print(f"   - {producto['nombre']}: {producto['stock']} unidades")

# Prueba 7: Productos con stock bajo
print("\n7. PRODUCTOS CON STOCK BAJO (≤ 5 unidades):")
bajo_stock = buscar_productos_bajo_stock(productos, 5)
for producto in bajo_stock:
    print(f"   - {producto['nombre']}: {producto['stock']} unidades - ¡Necesita reabastecimiento!")

# Prueba 8: Productos más caros y más baratos
print("\n8. TOP 3 PRODUCTOS MÁS CAROS:")
mas_caros = obtener_productos_mas_caros(productos, 3)
for i, producto in enumerate(mas_caros, 1):
    print(f"   {i}. {producto['nombre']}: ${producto['precio']}")

print("\n   TOP 3 PRODUCTOS MÁS BARATOS:")
mas_baratos = obtener_productos_mas_baratos(productos, 3)
for i, producto in enumerate(mas_baratos, 1):
    print(f"   {i}. {producto['nombre']}: ${producto['precio']}")

# Prueba 9: Valor total del inventario
print(f"\n9. VALOR TOTAL DEL INVENTARIO: ${calcular_valor_inventario_total(productos):,.2f}")

# Prueba 10: Búsqueda con filtros múltiples
print("\n10. BÚSQUEDA AVANZADA:")
print("   a) Productos Apple disponibles entre $200 y $800:")
resultados = buscar_productos_con_filtros_multiples(
    productos, 
    marca='Apple', 
    disponible=True, 
    precio_min=200, 
    precio_max=800
)
for producto in resultados:
    print(f"      - {producto['nombre']}: ${producto['precio']} (Stock: {producto['stock']})")

print("\n   b) Laptops con stock disponible:")
resultados = buscar_productos_con_filtros_multiples(
    productos,
    categoria='Laptop',
    disponible=True,
    stock_min=1
)
for producto in resultados:
    print(f"      - {producto['nombre']}: ${producto['precio']} (Stock: {producto['stock']})")

# Estadísticas adicionales
print("\n=== ESTADÍSTICAS ADICIONALES ===")
total_productos = len(productos)
total_disponibles = len(buscar_productos_disponibles(productos))
porcentaje_disponibles = (total_disponibles / total_productos) * 100 if total_productos else 0.0

print(f"Total de productos en el sistema: {total_productos}")
print(f"Productos disponibles: {total_disponibles} ({porcentaje_disponibles:.1f}%)")
print(f"Productos sin stock: {len(sin_stock)}")
print(f"Valor promedio por producto: ${calcular_valor_inventario_total(productos)/total_productos:.2f}")

from typing import List, Dict, Any, Optional
from collections import Counter

# Datos de ejemplo (ampliados para mejores pruebas)
productos: List[Dict[str, Any]] = [
    {'id': 1, 'nombre': 'iPhone 15', 'marca': 'Apple', 'categoria': 'Smartphone', 'precio': 999.99, 'stock': 10, 'disponible': True},
    {'id': 2, 'nombre': 'Samsung Galaxy S24', 'marca': 'Samsung', 'categoria': 'Smartphone', 'precio': 899.99, 'stock': 8, 'disponible': True},
    {'id': 3, 'nombre': 'MacBook Air M3', 'marca': 'Apple', 'categoria': 'Laptop', 'precio': 1299.99, 'stock': 5, 'disponible': True},
    {'id': 4, 'nombre': 'Dell XPS 13', 'marca': 'Dell', 'categoria': 'Laptop', 'precio': 1199.99, 'stock': 0, 'disponible': False},
    {'id': 5, 'nombre': 'Sony WH-1000XM5', 'marca': 'Sony', 'categoria': 'Audífonos', 'precio': 399.99, 'stock': 15, 'disponible': True},
    {'id': 6, 'nombre': 'iPad Air', 'marca': 'Apple', 'categoria': 'Tablet', 'precio': 599.99, 'stock': 3, 'disponible': True},
    {'id': 7, 'nombre': 'Samsung Galaxy Tab', 'marca': 'Samsung', 'categoria': 'Tablet', 'precio': 449.99, 'stock': 0, 'disponible': False},
    {'id': 8, 'nombre': 'AirPods Pro', 'marca': 'Apple', 'categoria': 'Audífonos', 'precio': 249.99, 'stock': 20, 'disponible': True},
    {'id': 9, 'nombre': 'Logitech MX Keys', 'marca': 'Logitech', 'categoria': 'Accesorios', 'precio': 99.99, 'stock': 12, 'disponible': True},
    {'id': 10, 'nombre': 'HP Pavilion', 'marca': 'HP', 'categoria': 'Laptop', 'precio': 799.99, 'stock': 2, 'disponible': True}
]

def _norm_str(s: Optional[str]) -> str:
    return s.strip().lower() if isinstance(s, str) else ''

def buscar_productos_disponibles(productos: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Devuelve productos con stock > 0 y disponibles."""
    return [p for p in productos if p.get('stock', 0) > 0 and p.get('disponible')]

def buscar_productos_sin_stock(productos: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Devuelve productos cuyo stock es exactamente 0."""
    return [p for p in productos if p.get('stock', 0) == 0]

def buscar_productos_por_rango_precio(productos: List[Dict[str, Any]], precio_min: float, precio_max: float) -> List[Dict[str, Any]]:
    """Devuelve productos cuyo precio está dentro del rango [precio_min, precio_max]."""
    return [p for p in productos if precio_min <= p.get('precio', 0.0) <= precio_max]

def buscar_productos_por_marca(productos: List[Dict[str, Any]], marca_buscada: str) -> List[Dict[str, Any]]:
    """Devuelve productos que coinciden con la marca (case-insensitive)."""
    marca_norm = _norm_str(marca_buscada)
    return [p for p in productos if _norm_str(p.get('marca')) == marca_norm]

def contar_productos_por_categoria(productos: List[Dict[str, Any]], categoria_buscada: Optional[str] = None):
    """
    Si se pasa categoria_buscada devuelve el conteo (int) de esa categoría,
    si no, devuelve dict con conteos por categoría.
    """
    if categoria_buscada:
        categoria_norm = _norm_str(categoria_buscada)
        return sum(1 for p in productos if _norm_str(p.get('categoria')) == categoria_norm)
    # Conteo general
    categorias = [p.get('categoria', '') for p in productos]
    return dict(Counter(categorias))

def buscar_productos_por_stock_minimo(productos: List[Dict[str, Any]], stock_minimo: int) -> List[Dict[str, Any]]:
    """Devuelve productos con stock >= stock_minimo."""
    return [p for p in productos if p.get('stock', 0) >= stock_minimo]

def buscar_productos_bajo_stock(productos: List[Dict[str, Any]], limite_stock: int = 5) -> List[Dict[str, Any]]:
    """Devuelve productos con 0 < stock <= limite_stock (necesitan reabastecerse)."""
    return [p for p in productos if 0 < p.get('stock', 0) <= limite_stock]

def obtener_productos_mas_caros(productos: List[Dict[str, Any]], cantidad: int = 3) -> List[Dict[str, Any]]:
    """Devuelve los N productos más caros."""
    return sorted(productos, key=lambda x: x.get('precio', 0.0), reverse=True)[:cantidad]

def obtener_productos_mas_baratos(productos: List[Dict[str, Any]], cantidad: int = 3) -> List[Dict[str, Any]]:
    """Devuelve los N productos más baratos."""
    return sorted(productos, key=lambda x: x.get('precio', 0.0))[:cantidad]

def calcular_valor_inventario_total(productos: List[Dict[str, Any]]) -> float:
    """Suma precio * stock para cada producto."""
    return sum(p.get('precio', 0.0) * p.get('stock', 0) for p in productos)

def buscar_productos_con_filtros_multiples(productos: List[Dict[str, Any]], **filtros) -> List[Dict[str, Any]]:
    """
    Aplicación de múltiples filtros:
      - precio_min / precio_max
      - stock_min / stock_max
      - disponible (bool)
      - comparaciones exactas para otras claves (case-insensitive si son str)
    """
    def cumple(p: Dict[str, Any]) -> bool:
        for clave, valor in filtros.items():
            if clave == 'precio_min':
                if p.get('precio', 0.0) < valor: return False
            elif clave == 'precio_max':
                if p.get('precio', 0.0) > valor: return False
            elif clave == 'stock_min':
                if p.get('stock', 0) < valor: return False
            elif clave == 'stock_max':
                if p.get('stock', 0) > valor: return False
            elif clave == 'disponible':
                if p.get('disponible') != valor: return False
            elif clave in p:
                v_prod = p[clave]
                if isinstance(valor, str) and isinstance(v_prod, str):
                    if _norm_str(v_prod) != _norm_str(valor): return False
                else:
                    if v_prod != valor: return False
            else:
                return False
        return True

    return [p for p in productos if cumple(p)]

# Pruebas de las funciones (misma salida que el original)
print("=== BÚSQUEDA POR DISPONIBILIDAD Y CRITERIOS CONDICIONALES ===\n")

# Prueba 1: Productos disponibles
print("1. PRODUCTOS DISPONIBLES:")
disponibles = buscar_productos_disponibles(productos)
print(f"   Total de productos disponibles: {len(disponibles)}")
for producto in disponibles:
    print(f"   - {producto['nombre']} (Stock: {producto['stock']}, Precio: ${producto['precio']})")

# Prueba 2: Productos sin stock
print("\n2. PRODUCTOS SIN STOCK:")
sin_stock = buscar_productos_sin_stock(productos)
print(f"   Total de productos sin stock: {len(sin_stock)}")
for producto in sin_stock:
    print(f"   - {producto['nombre']} ({producto['categoria']})")

# Prueba 3: Búsqueda por rango de precios
print("\n3. PRODUCTOS ENTRE $500 Y $1000:")
en_rango = buscar_productos_por_rango_precio(productos, 500, 1000)
print(f"   Productos encontrados: {len(en_rango)}")
for producto in en_rango:
    print(f"   - {producto['nombre']}: ${producto['precio']}")

# Prueba 4: Búsqueda por marca
print("\n4. PRODUCTOS APPLE:")
productos_apple = buscar_productos_por_marca(productos, "Apple")
print(f"   Total productos Apple: {len(productos_apple)}")
for producto in productos_apple:
    print(f"   - {producto['nombre']} (${producto['precio']}, Stock: {producto['stock']})")

# Prueba 5: Conteo por categoría
print("\n5. CONTEO DE PRODUCTOS POR CATEGORÍA:")
conteo_categorias = contar_productos_por_categoria(productos)
for categoria, cantidad in conteo_categorias.items():
    print(f"   - {categoria}: {cantidad} producto(s)")

# Prueba específica por categoría
print(f"\n   Productos en categoría 'Laptop': {contar_productos_por_categoria(productos, 'Laptop')}")

# Prueba 6: Productos con stock mínimo
print("\n6. PRODUCTOS CON STOCK MÍNIMO DE 10 UNIDADES:")
stock_minimo = buscar_productos_por_stock_minimo(productos, 10)
for producto in stock_minimo:
    print(f"   - {producto['nombre']}: {producto['stock']} unidades")

# Prueba 7: Productos con stock bajo
print("\n7. PRODUCTOS CON STOCK BAJO (≤ 5 unidades):")
bajo_stock = buscar_productos_bajo_stock(productos, 5)
for producto in bajo_stock:
    print(f"   - {producto['nombre']}: {producto['stock']} unidades - ¡Necesita reabastecimiento!")

# Prueba 8: Productos más caros y más baratos
print("\n8. TOP 3 PRODUCTOS MÁS CAROS:")
mas_caros = obtener_productos_mas_caros(productos, 3)
for i, producto in enumerate(mas_caros, 1):
    print(f"   {i}. {producto['nombre']}: ${producto['precio']}")

print("\n   TOP 3 PRODUCTOS MÁS BARATOS:")
mas_baratos = obtener_productos_mas_baratos(productos, 3)
for i, producto in enumerate(mas_baratos, 1):
    print(f"   {i}. {producto['nombre']}: ${producto['precio']}")

# Prueba 9: Valor total del inventario
print(f"\n9. VALOR TOTAL DEL INVENTARIO: ${calcular_valor_inventario_total(productos):,.2f}")

# Prueba 10: Búsqueda con filtros múltiples
print("\n10. BÚSQUEDA AVANZADA:")
print("   a) Productos Apple disponibles entre $200 y $800:")
resultados = buscar_productos_con_filtros_multiples(
    productos, 
    marca='Apple', 
    disponible=True, 
    precio_min=200, 
    precio_max=800
)
for producto in resultados:
    print(f"      - {producto['nombre']}: ${producto['precio']} (Stock: {producto['stock']})")

print("\n   b) Laptops con stock disponible:")
resultados = buscar_productos_con_filtros_multiples(
    productos,
    categoria='Laptop',
    disponible=True,
    stock_min=1
)
for producto in resultados:
    print(f"      - {producto['nombre']}: ${producto['precio']} (Stock: {producto['stock']})")

# Estadísticas adicionales
print("\n=== ESTADÍSTICAS ADICIONALES ===")
total_productos = len(productos)
total_disponibles = len(buscar_productos_disponibles(productos))
porcentaje_disponibles = (total_disponibles / total_productos) * 100 if total_productos else 0.0

print(f"Total de productos en el sistema: {total_productos}")
print(f"Productos disponibles: {total_disponibles} ({porcentaje_disponibles:.1f}%)")
print(f"Productos sin stock: {len(sin_stock)}")
print(f"Valor promedio por producto: ${calcular_valor_inventario_total(productos)/total_productos:.2f}")

#¿Cuál es la complejidad temporal ?
# La complejidad temporal de las funciones de búsqueda y filtrado en este código es generalmente O(n), donde n es el número de productos en la lista. Esto se debe a que la mayoría de las funciones recorren la lista completa de productos una vez para aplicar los criterios de búsqueda o filtrado. Algunas funciones que implican ordenamiento, como obtener los productos más caros o más baratos, tienen una complejidad temporal de O(n log n) debido al proceso de ordenamiento.

# ¿En qué casos la búsqueda lineal es eficiente?    
# La búsqueda lineal es eficiente cuando se trabaja con listas pequeñas o cuando los datos no están ordenados. También es útil cuando se necesita realizar búsquedas simples y rápidas sin la sobrecarga de estructuras de datos más complejas.

#¿Cuándo sería mejor usar otro algoritmo de búsqueda?
# Sería mejor usar otro algoritmo de búsqueda, como la búsqueda binaria, cuando la lista de productos está ordenada y es grande. La búsqueda binaria tiene una complejidad temporal de O(log n), lo que la hace mucho más eficiente para grandes conjuntos de datos en comparación con la búsqueda lineal. Además, para búsquedas frecuentes, podría ser beneficioso utilizar estructuras de datos como tablas hash o árboles balanceados para mejorar la eficiencia de las búsquedas.