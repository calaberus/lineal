# Datos de ejemplo
productos = [
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

empleados = [
    {'id': 101, 'nombre': 'Ana', 'apellido': 'García', 'departamento': 'Ventas', 'salario': 35000, 'activo': True},
    {'id': 102, 'nombre': 'Carlos', 'apellido': 'López', 'departamento': 'Técnico', 'salario': 42000, 'activo': True},
    {'id': 103, 'nombre': 'María', 'apellido': 'Rodríguez', 'departamento': 'Ventas', 'salario': 38000, 'activo': False},
    {'id': 104, 'nombre': 'José', 'apellido': 'Martínez', 'departamento': 'Inventario', 'salario': 30000, 'activo': True},
    {'id': 105, 'nombre': 'Laura', 'apellido': 'Hernández', 'departamento': 'Técnico', 'salario': 45000, 'activo': True},
    {'id': 106, 'nombre': 'Pedro', 'apellido': 'Gómez', 'departamento': 'Administración', 'salario': 32000, 'activo': False}
]

# Utilidades internas
def _norm(s):
    return s.strip().lower() if isinstance(s, str) else s

# ===============================
# FUNCIONES DE BÚSQUEDA DE PRODUCTOS
# ===============================

def buscar_producto_por_nombre(productos, nombre_buscado):
    """Busca un producto por nombre (case-insensitive)."""
    nombre_norm = _norm(nombre_buscado)
    return next((p for p in productos if _norm(p.get('nombre')) == nombre_norm), None)

def buscar_producto_por_id(productos, id_buscado):
    """Busca un producto por ID."""
    return next((p for p in productos if p.get('id') == id_buscado), None)

def buscar_productos_por_categoria(productos, categoria_buscada):
    """Busca productos por categoría (case-insensitive)."""
    cat_norm = _norm(categoria_buscada)
    return [p for p in productos if _norm(p.get('categoria')) == cat_norm]

def buscar_productos_por_marca(productos, marca_buscada):
    """Busca productos por marca (case-insensitive)."""
    marca_norm = _norm(marca_buscada)
    return [p for p in productos if _norm(p.get('marca')) == marca_norm]

def buscar_productos_disponibles(productos):
    """Busca productos disponibles (disponible=True y stock>0)."""
    return [p for p in productos if p.get('disponible') and p.get('stock', 0) > 0]

def buscar_productos_por_rango_precio(productos, precio_min, precio_max):
    """Busca productos por rango de precio."""
    return [p for p in productos if precio_min <= p.get('precio', 0.0) <= precio_max]

def contar_productos_por_categoria(productos):
    """Cuenta productos por categoría y devuelve diccionario {categoria: contador}."""
    conteo = {}
    for p in productos:
        categoria = p.get('categoria', 'Sin categoría')
        conteo[categoria] = conteo.get(categoria, 0) + 1
    return conteo

# ===============================
# FUNCIONES DE BÚSQUEDA DE EMPLEADOS
# ===============================

def buscar_empleado_por_id(empleados, id_buscado):
    """Busca empleado por ID."""
    return next((e for e in empleados if e.get('id') == id_buscado), None)

def buscar_empleado_por_nombre_completo(empleados, nombre_completo):
    """Busca empleado por nombre completo (soporta coincidencia exacta o por partes)."""
    partes = [p.lower() for p in nombre_completo.strip().split()] if nombre_completo else []
    for e in empleados:
        nombre_emp = f"{e.get('nombre')} {e.get('apellido')}".lower()
        if nombre_completo and nombre_emp == nombre_completo.lower():
            return e
        if len(partes) >= 2 and e.get('nombre').lower() == partes[0] and e.get('apellido').lower() == partes[1]:
            return e
    return None

def buscar_empleados_por_departamento(empleados, departamento_buscado):
    """Busca empleados por departamento (case-insensitive)."""
    depto_norm = _norm(departamento_buscado)
    return [e for e in empleados if _norm(e.get('departamento')) == depto_norm]

def buscar_empleados_activos(empleados):
    """Devuelve lista de empleados activos."""
    return [e for e in empleados if e.get('activo')]

# ===============================
# FUNCIONES DE VALIDACIÓN Y UTILIDAD
# ===============================

def validar_entero(mensaje):
    """Valida que la entrada sea un número entero."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("❌ Error: Por favor ingrese un número entero válido.")

def validar_flotante(mensaje):
    """Valida que la entrada sea un número flotante."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("❌ Error: Por favor ingrese un número válido.")

def validar_opcion(mensaje, opciones_validas):
    """Valida que la opción esté en la lista de opciones válidas."""
    while True:
        try:
            opcion = int(input(mensaje))
            if opcion in opciones_validas:
                return opcion
            print(f"❌ Error: Opción {opcion} no válida. Opciones válidas: {opciones_validas}")
        except ValueError:
            print("❌ Error: Por favor ingrese un número válido.")

def presionar_para_continuar():
    """Espera a que el usuario presione Enter para continuar."""
    input("\n📝 Presione Enter para continuar...")

def mostrar_producto(producto):
    """Muestra la información de un producto formateada."""
    if not producto:
        print("   ❌ Producto no encontrado")
        return
    estado = "✅ Disponible" if producto.get('disponible') and producto.get('stock', 0) > 0 else "❌ No disponible"
    print(f"   📦 ID: {producto['id']}")
    print(f"   🏷️  Nombre: {producto['nombre']}")
    print(f"   🏭 Marca: {producto['marca']}")
    print(f"   📂 Categoría: {producto['categoria']}")
    print(f"   💰 Precio: ${producto['precio']:.2f}")
    print(f"   📊 Stock: {producto['stock']}")
    print(f"   🟢 Estado: {estado}")

def mostrar_empleado(empleado):
    """Muestra la información de un empleado formateada."""
    if not empleado:
        print("   ❌ Empleado no encontrado")
        return
    estado = "✅ Activo" if empleado.get('activo') else "❌ Inactivo"
    print(f"   👤 ID: {empleado['id']}")
    print(f"   📛 Nombre: {empleado['nombre']} {empleado['apellido']}")
    print(f"   🏢 Departamento: {empleado['departamento']}")
    print(f"   💵 Salario: ${empleado['salario']:,}")
    print(f"   🟢 Estado: {estado}")

# ===============================
# MENÚS DEL SISTEMA
# ===============================

def menu_principal():
    """Menú principal del sistema."""
    while True:
        print("\n" + "="*50)
        print("🏢 SISTEMA INTEGRADO DE BÚSQUEDA")
        print("="*50)
        print("1. 🔍 Búsqueda de Productos")
        print("2. 👥 Búsqueda de Empleados")
        print("3. 📊 Estadísticas del Sistema")
        print("4. 🚪 Salir")
        print("="*50)
        opcion = validar_opcion("Seleccione una opción (1-4): ", [1, 2, 3, 4])
        if opcion == 1:
            menu_productos()
        elif opcion == 2:
            menu_empleados()
        elif opcion == 3:
            mostrar_estadisticas()
        else:
            print("\n👋 ¡Gracias por usar el sistema! ¡Hasta pronto!")
            break

def menu_productos():
    """Menú de búsqueda de productos."""
    opciones = {
        1: buscar_producto_id,
        2: buscar_producto_nombre,
        3: buscar_productos_categoria,
        4: buscar_productos_marca,
        5: buscar_productos_disponibles_menu,
        6: buscar_productos_rango_precio,
        7: contar_productos_categoria_menu
    }
    while True:
        print("\n" + "-"*40)
        print("📦 MÓDULO DE BÚSQUEDA DE PRODUCTOS")
        print("-"*40)
        print("1. 🔎 Buscar producto por ID")
        print("2. 🔎 Buscar producto por nombre")
        print("3. 📂 Buscar productos por categoría")
        print("4. 🏭 Buscar productos por marca")
        print("5. ✅ Buscar productos disponibles")
        print("6. 💰 Buscar por rango de precio")
        print("7. 📊 Conteo por categoría")
        print("8. ↩️ Volver al menú principal")
        print("-"*40)
        opcion = validar_opcion("Seleccione una opción (1-8): ", list(range(1,9)))
        if opcion == 8:
            break
        opciones.get(opcion, lambda: None)()

def menu_empleados():
    """Menú de búsqueda de empleados."""
    opciones = {
        1: buscar_empleado_id,
        2: buscar_empleado_nombre,
        3: buscar_empleados_departamento,
        4: buscar_empleados_activos_menu,
        5: listar_todos_empleados
    }
    while True:
        print("\n" + "-"*40)
        print("👥 MÓDULO DE BÚSQUEDA DE EMPLEADOS")
        print("-"*40)
        print("1. 🔎 Buscar empleado por ID")
        print("2. 🔎 Buscar empleado por nombre")
        print("3. 🏢 Buscar empleados por departamento")
        print("4. ✅ Buscar empleados activos")
        print("5. 📊 Listar todos los empleados")
        print("6. ↩️ Volver al menú principal")
        print("-"*40)
        opcion = validar_opcion("Seleccione una opción (1-6): ", list(range(1,7)))
        if opcion == 6:
            break
        opciones.get(opcion, lambda: None)()

# ===============================
# FUNCIONES DE BÚSQUEDA INTERACTIVAS
# ===============================

def buscar_producto_id():
    print("\n🔍 BUSCAR PRODUCTO POR ID")
    print("-" * 30)
    producto = buscar_producto_por_id(productos, validar_entero("Ingrese el ID del producto: "))
    mostrar_producto(producto)
    presionar_para_continuar()

def buscar_producto_nombre():
    print("\n🔍 BUSCAR PRODUCTO POR NOMBRE")
    print("-" * 30)
    nombre = input("Ingrese el nombre del producto: ").strip()
    if nombre:
        mostrar_producto(buscar_producto_por_nombre(productos, nombre))
    else:
        print("❌ Error: Debe ingresar un nombre válido.")
    presionar_para_continuar()

def buscar_productos_categoria():
    print("\n📂 BUSCAR PRODUCTOS POR CATEGORÍA")
    print("-" * 30)
    print("Categorías disponibles: Smartphone, Laptop, Tablet, Audífonos, Accesorios")
    categoria = input("Ingrese la categoría: ").strip()
    if categoria:
        resultados = buscar_productos_por_categoria(productos, categoria)
        if resultados:
            print(f"\n✅ Se encontraron {len(resultados)} productos en la categoría '{categoria}':")
            for producto in resultados:
                print(f"   - {producto['nombre']} (${producto['precio']}, Stock: {producto['stock']})")
        else:
            print(f"❌ No se encontraron productos en la categoría '{categoria}'")
    else:
        print("❌ Error: Debe ingresar una categoría válida.")
    presionar_para_continuar()

def buscar_productos_marca():
    print("\n🏭 BUSCAR PRODUCTOS POR MARCA")
    print("-" * 30)
    print("Marcas disponibles: Apple, Samsung, Dell, Sony, Logitech, HP")
    marca = input("Ingrese la marca: ").strip()
    if marca:
        resultados = buscar_productos_por_marca(productos, marca)
        if resultados:
            print(f"\n✅ Se encontraron {len(resultados)} productos de la marca '{marca}':")
            for producto in resultados:
                print(f"   - {producto['nombre']} (${producto['precio']}, Stock: {producto['stock']})")
        else:
            print(f"❌ No se encontraron productos de la marca '{marca}'")
    else:
        print("❌ Error: Debe ingresar una marca válida.")
    presionar_para_continuar()

def buscar_productos_disponibles_menu():
    print("\n✅ PRODUCTOS DISPONIBLES")
    print("-" * 30)
    resultados = buscar_productos_disponibles(productos)
    if resultados:
        print(f"📊 Total de productos disponibles: {len(resultados)}")
        for producto in resultados:
            print(f"   - {producto['nombre']} (Stock: {producto['stock']}, Precio: ${producto['precio']})")
    else:
        print("❌ No hay productos disponibles en este momento.")
    presionar_para_continuar()

def buscar_productos_rango_precio():
    print("\n💰 BUSCAR PRODUCTOS POR RANGO DE PRECIO")
    print("-" * 30)
    precio_min = validar_flotante("Ingrese el precio mínimo: ")
    precio_max = validar_flotante("Ingrese el precio máximo: ")
    if precio_min <= precio_max:
        resultados = buscar_productos_por_rango_precio(productos, precio_min, precio_max)
        if resultados:
            print(f"\n✅ Se encontraron {len(resultados)} productos entre ${precio_min} y ${precio_max}:")
            for producto in resultados:
                print(f"   - {producto['nombre']}: ${producto['precio']} (Stock: {producto['stock']})")
        else:
            print(f"❌ No se encontraron productos entre ${precio_min} y ${precio_max}")
    else:
        print("❌ Error: El precio mínimo no puede ser mayor al precio máximo.")
    presionar_para_continuar()

def contar_productos_categoria_menu():
    print("\n📊 CONTEO DE PRODUCTOS POR CATEGORÍA")
    print("-" * 30)
    conteo = contar_productos_por_categoria(productos)
    total_productos = len(productos)
    print(f"📈 Distribución de {total_productos} productos:")
    for categoria, cantidad in conteo.items():
        porcentaje = (cantidad / total_productos) * 100 if total_productos else 0
        print(f"   - {categoria}: {cantidad} productos ({porcentaje:.1f}%)")
    presionar_para_continuar()

def buscar_empleado_id():
    print("\n🔍 BUSCAR EMPLEADO POR ID")
    print("-" * 30)
    mostrar_empleado(buscar_empleado_por_id(empleados, validar_entero("Ingrese el ID del empleado: ")))
    presionar_para_continuar()

def buscar_empleado_nombre():
    print("\n🔍 BUSCAR EMPLEADO POR NOMBRE")
    print("-" * 30)
    nombre = input("Ingrese el nombre completo (ej: Ana García): ").strip()
    if nombre:
        mostrar_empleado(buscar_empleado_por_nombre_completo(empleados, nombre))
    else:
        print("❌ Error: Debe ingresar un nombre válido.")
    presionar_para_continuar()

def buscar_empleados_departamento():
    print("\n🏢 BUSCAR EMPLEADOS POR DEPARTAMENTO")
    print("-" * 30)
    print("Departamentos disponibles: Ventas, Técnico, Inventario, Administración")
    departamento = input("Ingrese el departamento: ").strip()
    if departamento:
        resultados = buscar_empleados_por_departamento(empleados, departamento)
        if resultados:
            print(f"\n✅ Se encontraron {len(resultados)} empleados en '{departamento}':")
            for empleado in resultados:
                estado = "Activo" if empleado['activo'] else "Inactivo"
                print(f"   - {empleado['nombre']} {empleado['apellido']} (${empleado['salario']:,}) - {estado}")
        else:
            print(f"❌ No se encontraron empleados en el departamento '{departamento}'")
    else:
        print("❌ Error: Debe ingresar un departamento válido.")
    presionar_para_continuar()

def buscar_empleados_activos_menu():
    print("\n✅ EMPLEADOS ACTIVOS")
    print("-" * 30)
    resultados = buscar_empleados_activos(empleados)
    if resultados:
        print(f"📊 Total de empleados activos: {len(resultados)}")
        for empleado in resultados:
            print(f"   - {empleado['nombre']} {empleado['apellido']} ({empleado['departamento']}) - ${empleado['salario']:,}")
    else:
        print("❌ No hay empleados activos.")
    presionar_para_continuar()

def listar_todos_empleados():
    print("\n📋 LISTA COMPLETA DE EMPLEADOS")
    print("-" * 30)
    if empleados:
        print(f"📊 Total de empleados: {len(empleados)}")
        for empleado in empleados:
            estado = "✅ Activo" if empleado.get('activo') else "❌ Inactivo"
            print(f"   - {empleado['nombre']} {empleado['apellido']} | {empleado['departamento']} | ${empleado['salario']:,} | {estado}")
    else:
        print("❌ No hay empleados registrados.")
    presionar_para_continuar()

def mostrar_estadisticas():
    print("\n📊 ESTADÍSTICAS DEL SISTEMA")
    print("-" * 30)
    productos_disponibles = buscar_productos_disponibles(productos)
    productos_sin_stock = [p for p in productos if p.get('stock', 0) == 0]
    valor_inventario = sum(p.get('precio', 0.0) * p.get('stock', 0) for p in productos)
    print("📦 ESTADÍSTICAS DE PRODUCTOS:")
    print(f"   • Total de productos: {len(productos)}")
    print(f"   • Productos disponibles: {len(productos_disponibles)}")
    print(f"   • Productos sin stock: {len(productos_sin_stock)}")
    print(f"   • Valor total del inventario: ${valor_inventario:,.2f}")
    conteo_categorias = contar_productos_por_categoria(productos)
    print("   • Distribución por categoría:")
    for categoria, cantidad in conteo_categorias.items():
        print(f"     - {categoria}: {cantidad}")
    print("\n👥 ESTADÍSTICAS DE EMPLEADOS:")
    empleados_activos = buscar_empleados_activos(empleados)
    empleados_inactivos = len(empleados) - len(empleados_activos)
    salario_promedio = sum(e.get('salario', 0) for e in empleados) / len(empleados) if empleados else 0
    print(f"   • Total de empleados: {len(empleados)}")
    print(f"   • Empleados activos: {len(empleados_activos)}")
    print(f"   • Empleados inactivos: {empleados_inactivos}")
    print(f"   • Salario promedio: ${salario_promedio:,.2f}")
    departamentos = {}
    for e in empleados:
        d = e.get('departamento', 'Sin departamento')
        departamentos[d] = departamentos.get(d, 0) + 1
    print("   • Distribución por departamento:")
    for departamento, cantidad in departamentos.items():
        print(f"     - {departamento}: {cantidad}")
    presionar_para_continuar()

# ===============================
# INICIO DEL PROGRAMA
# ===============================

if __name__ == "__main__":
    print("🚀 Iniciando Sistema Integrado de Búsqueda...")
    menu_principal()

# Datos de ejemplo
productos = [
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

empleados = [
    {'id': 101, 'nombre': 'Ana', 'apellido': 'García', 'departamento': 'Ventas', 'salario': 35000, 'activo': True},
    {'id': 102, 'nombre': 'Carlos', 'apellido': 'López', 'departamento': 'Técnico', 'salario': 42000, 'activo': True},
    {'id': 103, 'nombre': 'María', 'apellido': 'Rodríguez', 'departamento': 'Ventas', 'salario': 38000, 'activo': False},
    {'id': 104, 'nombre': 'José', 'apellido': 'Martínez', 'departamento': 'Inventario', 'salario': 30000, 'activo': True},
    {'id': 105, 'nombre': 'Laura', 'apellido': 'Hernández', 'departamento': 'Técnico', 'salario': 45000, 'activo': True},
    {'id': 106, 'nombre': 'Pedro', 'apellido': 'Gómez', 'departamento': 'Administración', 'salario': 32000, 'activo': False}
]

# Utilidades internas
def _norm(s):
    return s.strip().lower() if isinstance(s, str) else s

# ===============================
# FUNCIONES DE BÚSQUEDA DE PRODUCTOS
# ===============================

def buscar_producto_por_nombre(productos, nombre_buscado):
    """Busca un producto por nombre (case-insensitive)."""
    nombre_norm = _norm(nombre_buscado)
    return next((p for p in productos if _norm(p.get('nombre')) == nombre_norm), None)

def buscar_producto_por_id(productos, id_buscado):
    """Busca un producto por ID."""
    return next((p for p in productos if p.get('id') == id_buscado), None)

def buscar_productos_por_categoria(productos, categoria_buscada):
    """Busca productos por categoría (case-insensitive)."""
    cat_norm = _norm(categoria_buscada)
    return [p for p in productos if _norm(p.get('categoria')) == cat_norm]

def buscar_productos_por_marca(productos, marca_buscada):
    """Busca productos por marca (case-insensitive)."""
    marca_norm = _norm(marca_buscada)
    return [p for p in productos if _norm(p.get('marca')) == marca_norm]

def buscar_productos_disponibles(productos):
    """Busca productos disponibles (disponible=True y stock>0)."""
    return [p for p in productos if p.get('disponible') and p.get('stock', 0) > 0]

def buscar_productos_por_rango_precio(productos, precio_min, precio_max):
    """Busca productos por rango de precio."""
    return [p for p in productos if precio_min <= p.get('precio', 0.0) <= precio_max]

def contar_productos_por_categoria(productos):
    """Cuenta productos por categoría y devuelve diccionario {categoria: contador}."""
    conteo = {}
    for p in productos:
        categoria = p.get('categoria', 'Sin categoría')
        conteo[categoria] = conteo.get(categoria, 0) + 1
    return conteo

# ===============================
# FUNCIONES DE BÚSQUEDA DE EMPLEADOS
# ===============================

def buscar_empleado_por_id(empleados, id_buscado):
    """Busca empleado por ID."""
    return next((e for e in empleados if e.get('id') == id_buscado), None)

def buscar_empleado_por_nombre_completo(empleados, nombre_completo):
    """Busca empleado por nombre completo (soporta coincidencia exacta o por partes)."""
    partes = [p.lower() for p in nombre_completo.strip().split()] if nombre_completo else []
    for e in empleados:
        nombre_emp = f"{e.get('nombre')} {e.get('apellido')}".lower()
        if nombre_completo and nombre_emp == nombre_completo.lower():
            return e
        if len(partes) >= 2 and e.get('nombre').lower() == partes[0] and e.get('apellido').lower() == partes[1]:
            return e
    return None

def buscar_empleados_por_departamento(empleados, departamento_buscado):
    """Busca empleados por departamento (case-insensitive)."""
    depto_norm = _norm(departamento_buscado)
    return [e for e in empleados if _norm(e.get('departamento')) == depto_norm]

def buscar_empleados_activos(empleados):
    """Devuelve lista de empleados activos."""
    return [e for e in empleados if e.get('activo')]

# ===============================
# FUNCIONES DE VALIDACIÓN Y UTILIDAD
# ===============================

def validar_entero(mensaje):
    """Valida que la entrada sea un número entero."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("❌ Error: Por favor ingrese un número entero válido.")

def validar_flotante(mensaje):
    """Valida que la entrada sea un número flotante."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("❌ Error: Por favor ingrese un número válido.")

def validar_opcion(mensaje, opciones_validas):
    """Valida que la opción esté en la lista de opciones válidas."""
    while True:
        try:
            opcion = int(input(mensaje))
            if opcion in opciones_validas:
                return opcion
            print(f"❌ Error: Opción {opcion} no válida. Opciones válidas: {opciones_validas}")
        except ValueError:
            print("❌ Error: Por favor ingrese un número válido.")

def presionar_para_continuar():
    """Espera a que el usuario presione Enter para continuar."""
    input("\n📝 Presione Enter para continuar...")

def mostrar_producto(producto):
    """Muestra la información de un producto formateada."""
    if not producto:
        print("   ❌ Producto no encontrado")
        return
    estado = "✅ Disponible" if producto.get('disponible') and producto.get('stock', 0) > 0 else "❌ No disponible"
    print(f"   📦 ID: {producto['id']}")
    print(f"   🏷️  Nombre: {producto['nombre']}")
    print(f"   🏭 Marca: {producto['marca']}")
    print(f"   📂 Categoría: {producto['categoria']}")
    print(f"   💰 Precio: ${producto['precio']:.2f}")
    print(f"   📊 Stock: {producto['stock']}")
    print(f"   🟢 Estado: {estado}")

def mostrar_empleado(empleado):
    """Muestra la información de un empleado formateada."""
    if not empleado:
        print("   ❌ Empleado no encontrado")
        return
    estado = "✅ Activo" if empleado.get('activo') else "❌ Inactivo"
    print(f"   👤 ID: {empleado['id']}")
    print(f"   📛 Nombre: {empleado['nombre']} {empleado['apellido']}")
    print(f"   🏢 Departamento: {empleado['departamento']}")
    print(f"   💵 Salario: ${empleado['salario']:,}")
    print(f"   🟢 Estado: {estado}")

# ===============================
# MENÚS DEL SISTEMA
# ===============================

def menu_principal():
    """Menú principal del sistema."""
    while True:
        print("\n" + "="*50)
        print("🏢 SISTEMA INTEGRADO DE BÚSQUEDA")
        print("="*50)
        print("1. 🔍 Búsqueda de Productos")
        print("2. 👥 Búsqueda de Empleados")
        print("3. 📊 Estadísticas del Sistema")
        print("4. 🚪 Salir")
        print("="*50)
        opcion = validar_opcion("Seleccione una opción (1-4): ", [1, 2, 3, 4])
        if opcion == 1:
            menu_productos()
        elif opcion == 2:
            menu_empleados()
        elif opcion == 3:
            mostrar_estadisticas()
        else:
            print("\n👋 ¡Gracias por usar el sistema! ¡Hasta pronto!")
            break

def menu_productos():
    """Menú de búsqueda de productos."""
    opciones = {
        1: buscar_producto_id,
        2: buscar_producto_nombre,
        3: buscar_productos_categoria,
        4: buscar_productos_marca,
        5: buscar_productos_disponibles_menu,
        6: buscar_productos_rango_precio,
        7: contar_productos_categoria_menu
    }
    while True:
        print("\n" + "-"*40)
        print("📦 MÓDULO DE BÚSQUEDA DE PRODUCTOS")
        print("-"*40)
        print("1. 🔎 Buscar producto por ID")
        print("2. 🔎 Buscar producto por nombre")
        print("3. 📂 Buscar productos por categoría")
        print("4. 🏭 Buscar productos por marca")
        print("5. ✅ Buscar productos disponibles")
        print("6. 💰 Buscar por rango de precio")
        print("7. 📊 Conteo por categoría")
        print("8. ↩️ Volver al menú principal")
        print("-"*40)
        opcion = validar_opcion("Seleccione una opción (1-8): ", list(range(1,9)))
        if opcion == 8:
            break
        opciones.get(opcion, lambda: None)()

def menu_empleados():
    """Menú de búsqueda de empleados."""
    opciones = {
        1: buscar_empleado_id,
        2: buscar_empleado_nombre,
        3: buscar_empleados_departamento,
        4: buscar_empleados_activos_menu,
        5: listar_todos_empleados
    }
    while True:
        print("\n" + "-"*40)
        print("👥 MÓDULO DE BÚSQUEDA DE EMPLEADOS")
        print("-"*40)
        print("1. 🔎 Buscar empleado por ID")
        print("2. 🔎 Buscar empleado por nombre")
        print("3. 🏢 Buscar empleados por departamento")
        print("4. ✅ Buscar empleados activos")
        print("5. 📊 Listar todos los empleados")
        print("6. ↩️ Volver al menú principal")
        print("-"*40)
        opcion = validar_opcion("Seleccione una opción (1-6): ", list(range(1,7)))
        if opcion == 6:
            break
        opciones.get(opcion, lambda: None)()

# ===============================
# FUNCIONES DE BÚSQUEDA INTERACTIVAS
# ===============================

def buscar_producto_id():
    print("\n🔍 BUSCAR PRODUCTO POR ID")
    print("-" * 30)
    producto = buscar_producto_por_id(productos, validar_entero("Ingrese el ID del producto: "))
    mostrar_producto(producto)
    presionar_para_continuar()

def buscar_producto_nombre():
    print("\n🔍 BUSCAR PRODUCTO POR NOMBRE")
    print("-" * 30)
    nombre = input("Ingrese el nombre del producto: ").strip()
    if nombre:
        mostrar_producto(buscar_producto_por_nombre(productos, nombre))
    else:
        print("❌ Error: Debe ingresar un nombre válido.")
    presionar_para_continuar()

def buscar_productos_categoria():
    print("\n📂 BUSCAR PRODUCTOS POR CATEGORÍA")
    print("-" * 30)
    print("Categorías disponibles: Smartphone, Laptop, Tablet, Audífonos, Accesorios")
    categoria = input("Ingrese la categoría: ").strip()
    if categoria:
        resultados = buscar_productos_por_categoria(productos, categoria)
        if resultados:
            print(f"\n✅ Se encontraron {len(resultados)} productos en la categoría '{categoria}':")
            for producto in resultados:
                print(f"   - {producto['nombre']} (${producto['precio']}, Stock: {producto['stock']})")
        else:
            print(f"❌ No se encontraron productos en la categoría '{categoria}'")
    else:
        print("❌ Error: Debe ingresar una categoría válida.")
    presionar_para_continuar()

def buscar_productos_marca():
    print("\n🏭 BUSCAR PRODUCTOS POR MARCA")
    print("-" * 30)
    print("Marcas disponibles: Apple, Samsung, Dell, Sony, Logitech, HP")
    marca = input("Ingrese la marca: ").strip()
    if marca:
        resultados = buscar_productos_por_marca(productos, marca)
        if resultados:
            print(f"\n✅ Se encontraron {len(resultados)} productos de la marca '{marca}':")
            for producto in resultados:
                print(f"   - {producto['nombre']} (${producto['precio']}, Stock: {producto['stock']})")
        else:
            print(f"❌ No se encontraron productos de la marca '{marca}'")
    else:
        print("❌ Error: Debe ingresar una marca válida.")
    presionar_para_continuar()

def buscar_productos_disponibles_menu():
    print("\n✅ PRODUCTOS DISPONIBLES")
    print("-" * 30)
    resultados = buscar_productos_disponibles(productos)
    if resultados:
        print(f"📊 Total de productos disponibles: {len(resultados)}")
        for producto in resultados:
            print(f"   - {producto['nombre']} (Stock: {producto['stock']}, Precio: ${producto['precio']})")
    else:
        print("❌ No hay productos disponibles en este momento.")
    presionar_para_continuar()

def buscar_productos_rango_precio():
    print("\n💰 BUSCAR PRODUCTOS POR RANGO DE PRECIO")
    print("-" * 30)
    precio_min = validar_flotante("Ingrese el precio mínimo: ")
    precio_max = validar_flotante("Ingrese el precio máximo: ")
    if precio_min <= precio_max:
        resultados = buscar_productos_por_rango_precio(productos, precio_min, precio_max)
        if resultados:
            print(f"\n✅ Se encontraron {len(resultados)} productos entre ${precio_min} y ${precio_max}:")
            for producto in resultados:
                print(f"   - {producto['nombre']}: ${producto['precio']} (Stock: {producto['stock']})")
        else:
            print(f"❌ No se encontraron productos entre ${precio_min} y ${precio_max}")
    else:
        print("❌ Error: El precio mínimo no puede ser mayor al precio máximo.")
    presionar_para_continuar()

def contar_productos_categoria_menu():
    print("\n📊 CONTEO DE PRODUCTOS POR CATEGORÍA")
    print("-" * 30)
    conteo = contar_productos_por_categoria(productos)
    total_productos = len(productos)
    print(f"📈 Distribución de {total_productos} productos:")
    for categoria, cantidad in conteo.items():
        porcentaje = (cantidad / total_productos) * 100 if total_productos else 0
        print(f"   - {categoria}: {cantidad} productos ({porcentaje:.1f}%)")
    presionar_para_continuar()

def buscar_empleado_id():
    print("\n🔍 BUSCAR EMPLEADO POR ID")
    print("-" * 30)
    mostrar_empleado(buscar_empleado_por_id(empleados, validar_entero("Ingrese el ID del empleado: ")))
    presionar_para_continuar()

def buscar_empleado_nombre():
    print("\n🔍 BUSCAR EMPLEADO POR NOMBRE")
    print("-" * 30)
    nombre = input("Ingrese el nombre completo (ej: Ana García): ").strip()
    if nombre:
        mostrar_empleado(buscar_empleado_por_nombre_completo(empleados, nombre))
    else:
        print("❌ Error: Debe ingresar un nombre válido.")
    presionar_para_continuar()

def buscar_empleados_departamento():
    print("\n🏢 BUSCAR EMPLEADOS POR DEPARTAMENTO")
    print("-" * 30)
    print("Departamentos disponibles: Ventas, Técnico, Inventario, Administración")
    departamento = input("Ingrese el departamento: ").strip()
    if departamento:
        resultados = buscar_empleados_por_departamento(empleados, departamento)
        if resultados:
            print(f"\n✅ Se encontraron {len(resultados)} empleados en '{departamento}':")
            for empleado in resultados:
                estado = "Activo" if empleado['activo'] else "Inactivo"
                print(f"   - {empleado['nombre']} {empleado['apellido']} (${empleado['salario']:,}) - {estado}")
        else:
            print(f"❌ No se encontraron empleados en el departamento '{departamento}'")
    else:
        print("❌ Error: Debe ingresar un departamento válido.")
    presionar_para_continuar()

def buscar_empleados_activos_menu():
    print("\n✅ EMPLEADOS ACTIVOS")
    print("-" * 30)
    resultados = buscar_empleados_activos(empleados)
    if resultados:
        print(f"📊 Total de empleados activos: {len(resultados)}")
        for empleado in resultados:
            print(f"   - {empleado['nombre']} {empleado['apellido']} ({empleado['departamento']}) - ${empleado['salario']:,}")
    else:
        print("❌ No hay empleados activos.")
    presionar_para_continuar()

def listar_todos_empleados():
    print("\n📋 LISTA COMPLETA DE EMPLEADOS")
    print("-" * 30)
    if empleados:
        print(f"📊 Total de empleados: {len(empleados)}")
        for empleado in empleados:
            estado = "✅ Activo" if empleado.get('activo') else "❌ Inactivo"
            print(f"   - {empleado['nombre']} {empleado['apellido']} | {empleado['departamento']} | ${empleado['salario']:,} | {estado}")
    else:
        print("❌ No hay empleados registrados.")
    presionar_para_continuar()

def mostrar_estadisticas():
    print("\n📊 ESTADÍSTICAS DEL SISTEMA")
    print("-" * 30)
    productos_disponibles = buscar_productos_disponibles(productos)
    productos_sin_stock = [p for p in productos if p.get('stock', 0) == 0]
    valor_inventario = sum(p.get('precio', 0.0) * p.get('stock', 0) for p in productos)
    print("📦 ESTADÍSTICAS DE PRODUCTOS:")
    print(f"   • Total de productos: {len(productos)}")
    print(f"   • Productos disponibles: {len(productos_disponibles)}")
    print(f"   • Productos sin stock: {len(productos_sin_stock)}")
    print(f"   • Valor total del inventario: ${valor_inventario:,.2f}")
    conteo_categorias = contar_productos_por_categoria(productos)
    print("   • Distribución por categoría:")
    for categoria, cantidad in conteo_categorias.items():
        print(f"     - {categoria}: {cantidad}")
    print("\n👥 ESTADÍSTICAS DE EMPLEADOS:")
    empleados_activos = buscar_empleados_activos(empleados)
    empleados_inactivos = len(empleados) - len(empleados_activos)
    salario_promedio = sum(e.get('salario', 0) for e in empleados) / len(empleados) if empleados else 0
    print(f"   • Total de empleados: {len(empleados)}")
    print(f"   • Empleados activos: {len(empleados_activos)}")
    print(f"   • Empleados inactivos: {empleados_inactivos}")
    print(f"   • Salario promedio: ${salario_promedio:,.2f}")
    departamentos = {}
    for e in empleados:
        d = e.get('departamento', 'Sin departamento')
        departamentos[d] = departamentos.get(d, 0) + 1
    print("   • Distribución por departamento:")
    for departamento, cantidad in departamentos.items():
        print(f"     - {departamento}: {cantidad}")
    presionar_para_continuar()

# ===============================
# INICIO DEL PROGRAMA
# ===============================

if __name__ == "__main__":
    print("🚀 Iniciando Sistema Integrado de Búsqueda...")
    menu_principal()
    
#¿Cuál es la complejidad temporal ?
# La complejidad temporal de las funciones de búsqueda y filtrado en este código es generalmente O(n), donde n es el número de productos en la lista. Esto se debe a que la mayoría de las funciones recorren la lista completa de productos una vez para aplicar los criterios de búsqueda o filtrado. Algunas funciones que implican ordenamiento, como obtener los productos más caros o más baratos, tienen una complejidad temporal de O(n log n) debido al proceso de ordenamiento.

# ¿En qué casos la búsqueda lineal es eficiente?
# La búsqueda lineal es eficiente cuando se trabaja con listas pequeñas o cuando los datos no están ordenados. También es útil cuando se necesita realizar búsquedas simples y rápidas sin la sobrecarga de estructuras de datos más complejas.

#¿Cuándo sería mejor usar otro algoritmo de búsqueda?
# Sería mejor usar otro algoritmo de búsqueda, como la búsqueda binaria, cuando la lista de productos está ordenada y es grande. La búsqueda binaria tiene una complejidad temporal de O(log n), lo que la hace mucho más eficiente para grandes conjuntos de datos en comparación con la búsqueda lineal. Además, para búsquedas frecuentes, podría ser beneficioso utilizar estructuras de datos como tablas hash o árboles balanceados para mejorar la eficiencia de las búsquedas.
