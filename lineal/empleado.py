# Datos de ejemplo
empleados = [
    {'id': 101, 'nombre': 'Ana', 'apellido': 'García', 'departamento': 'Ventas', 'salario': 35000, 'activo': True},
    {'id': 102, 'nombre': 'Carlos', 'apellido': 'López', 'departamento': 'Técnico', 'salario': 42000, 'activo': True},
    {'id': 103, 'nombre': 'María', 'apellido': 'Rodríguez', 'departamento': 'Ventas', 'salario': 38000, 'activo': False},
    {'id': 104, 'nombre': 'José', 'apellido': 'Martínez', 'departamento': 'Inventario', 'salario': 30000, 'activo': True},
    {'id': 105, 'nombre': 'Laura', 'apellido': 'Hernández', 'departamento': 'Técnico', 'salario': 45000, 'activo': True},
    {'id': 106, 'nombre': 'Pedro', 'apellido': 'Gómez', 'departamento': 'Administración', 'salario': 32000, 'activo': False}
]

def buscar_empleado_por_id(empleados, id_buscado):
    """Busca un empleado por su ID"""
    return next((e for e in empleados if e['id'] == id_buscado), None)

def buscar_empleado_por_nombre_completo(empleados, nombre_completo):
    """Busca un empleado por nombre completo (nombre + apellido)"""
    nombre_completo = nombre_completo.strip()
    partes = nombre_completo.split()
    nombre_cmp = nombre_completo.lower()

    for e in empleados:
        nombre_empleado = f"{e['nombre']} {e['apellido']}"
        if nombre_cmp == nombre_empleado.lower():
            return e
        if len(partes) >= 2:
            if e['nombre'].lower() == partes[0].lower() and e['apellido'].lower() == partes[1].lower():
                return e
    return None

def buscar_empleados_por_departamento(empleados, departamento_buscado):
    """Busca todos los empleados de un departamento específico"""
    dept = departamento_buscado.lower()
    return [e for e in empleados if e['departamento'].lower() == dept]

def buscar_empleados_activos(empleados):
    """Busca todos los empleados activos"""
    return [e for e in empleados if e.get('activo')]

def buscar_empleados_por_rango_salario(empleados, salario_min, salario_max):
    """Busca empleados dentro de un rango salarial"""
    return [e for e in empleados if salario_min <= e.get('salario', 0) <= salario_max]

def buscar_empleados_por_nombre_o_apellido(empleados, texto_buscado):
    """Busca empleados por nombre o apellido (búsqueda parcial)"""
    t = texto_buscado.lower()
    return [e for e in empleados if t in e['nombre'].lower() or t in e['apellido'].lower()]

def obtener_resumen_departamentos(empleados):
    """Genera un resumen de empleados por departamento"""
    resumen = {}
    for e in empleados:
        depto = e['departamento']
        resumen[depto] = resumen.get(depto, 0) + 1
    return resumen

# Pruebas de las funciones
print("=== PRUEBAS DE BÚSQUEDA EN EMPLEADOS ===\n")

# Prueba 1: Búsqueda por ID
print("1. Búsqueda por ID:")
resultado = buscar_empleado_por_id(empleados, 102)
print(f"   Buscando ID 102: {resultado}\n")

# Prueba 2: Búsqueda por nombre completo
print("2. Búsqueda por nombre completo:")
resultado = buscar_empleado_por_nombre_completo(empleados, "Ana García")
print(f"   Buscando 'Ana García': {resultado['nombre']} {resultado['apellido']} - {resultado['departamento']}")

resultado = buscar_empleado_por_nombre_completo(empleados, "Carlos López")
print(f"   Buscando 'Carlos López': {resultado['nombre']} {resultado['apellido']} - {resultado['departamento']}\n")

# Prueba 3: Búsqueda por departamento
print("3. Búsqueda por departamento:")
resultados = buscar_empleados_por_departamento(empleados, "Ventas")
print("   Empleados en departamento 'Ventas':")
for empleado in resultados:
    estado = "Activo" if empleado['activo'] else "Inactivo"
    print(f"   - {empleado['nombre']} {empleado['apellido']} (${empleado['salario']}) - {estado}")

# Prueba 4: Búsqueda de empleados activos
print("\n4. Empleados activos:")
resultados = buscar_empleados_activos(empleados)
print("   Lista de empleados activos:")
for empleado in resultados:
    print(f"   - {empleado['nombre']} {empleado['apellido']} ({empleado['departamento']})")

# Prueba 5: Búsqueda por rango salarial
print("\n5. Búsqueda por rango salarial:")
resultados = buscar_empleados_por_rango_salario(empleados, 35000, 40000)
print("   Empleados con salario entre $35,000 y $40,000:")
for empleado in resultados:
    print(f"   - {empleado['nombre']} {empleado['apellido']}: ${empleado['salario']:,}")

# Prueba 6: Búsqueda por nombre o apellido (parcial)
print("\n6. Búsqueda parcial por nombre/apellido:")
resultados = buscar_empleados_por_nombre_o_apellido(empleados, "Garc")
print("   Empleados que contienen 'Garc' en nombre o apellido:")
for empleado in resultados:
    print(f"   - {empleado['nombre']} {empleado['apellido']}")

resultados = buscar_empleados_por_nombre_o_apellido(empleados, "Mar")
print("   Empleados que contienen 'Mar' en nombre o apellido:")
for empleado in resultados:
    print(f"   - {empleado['nombre']} {empleado['apellido']}")

# Prueba 7: Resumen de departamentos
print("\n7. Resumen por departamento:")
resumen = obtener_resumen_departamentos(empleados)
for departamento, cantidad in resumen.items():
    print(f"   - {departamento}: {cantidad} empleado(s)")

# Prueba 8: Búsquedas sin resultados
print("\n8. Búsquedas sin resultados:")
resultado = buscar_empleado_por_id(empleados, 999)
print(f"   Buscando ID 999: {resultado}")

resultado = buscar_empleado_por_nombre_completo(empleados, "Juan Pérez")
print(f"   Buscando 'Juan Pérez': {resultado}")

# Función adicional: Búsqueda avanzada con múltiples criterios
def buscar_empleados_avanzado(empleados, **criterios):
    """Búsqueda avanzada de empleados con múltiples criterios"""
    resultados = []
    for e in empleados:
        cumple = True
        for criterio, valor in criterios.items():
            if criterio == 'salario_min':
                if e.get('salario', 0) < valor:
                    cumple = False; break
            elif criterio == 'salario_max':
                if e.get('salario', 0) > valor:
                    cumple = False; break
            elif criterio == 'nombre_contiene':
                if valor.lower() not in e['nombre'].lower():
                    cumple = False; break
            elif criterio == 'apellido_contiene':
                if valor.lower() not in e['apellido'].lower():
                    cumple = False; break
            elif criterio in e:
                if isinstance(valor, str):
                    if str(e[criterio]).lower() != valor.lower():
                        cumple = False; break
                else:
                    if e[criterio] != valor:
                        cumple = False; break
            else:
                cumple = False; break
        if cumple:
            resultados.append(e)
    return resultados

# Prueba de búsqueda avanzada
print("\n9. Búsqueda avanzada:")
resultados = buscar_empleados_avanzado(empleados, departamento='Técnico', activo=True)
print("   Empleados técnicos activos:")
for empleado in resultados:
    print(f"   - {empleado['nombre']} {empleado['apellido']} (${empleado['salario']:,})")

resultados = buscar_empleados_avanzado(empleados, salario_min=40000, activo=True)
print("\n   Empleados activos con salario >= $40,000:")
for empleado in resultados:
    print(f"   - {empleado['nombre']} {empleado['apellido']} (${empleado['salario']:,})")
  
#¿Cuál es la complejidad temporal ?
# La complejidad temporal de las funciones de búsqueda en este código es O(n) en el peor de los casos, donde n es el número de empleados en la lista. Esto se debe a que la mayoría de las funciones recorren la lista completa de empleados una vez para aplicar los criterios de búsqueda.

# ¿En qué casos la búsqueda lineal es eficiente?
# La búsqueda lineal es eficiente cuando se trabaja con listas pequeñas o cuando los datos no están ordenados. También es útil cuando se necesita realizar búsquedas simples y rápidas sin la sobrecarga de estructuras de datos más complejas.

#¿Cuándo sería mejor usar otro algoritmo de búsqueda?
# Sería mejor usar otro algoritmo de búsqueda, como la búsqueda binaria, cuando la lista está ordenada y es grande. La búsqueda binaria tiene una complejidad temporal de O(log n), lo que la hace mucho más eficiente para grandes conjuntos de datos en comparación con la búsqueda lineal. Además, para búsquedas frecuentes, podría ser beneficioso utilizar estructuras de datos como tablas hash o árboles balanceados para mejorar la eficiencia de las búsquedas.

