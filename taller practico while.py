# Código mostrado al usuario (función real que pueden ejecutar)
code_str = '''def solicitar_contrasena():
    """
    Solicita al usuario una contraseña y repite la solicitud hasta que
    la contraseña tenga al menos 8 caracteres.
    """
    while True:
        pwd = input("Introduce una contraseña (mínimo 8 caracteres): ")
        if len(pwd) >= 8:
            print("Contraseña aceptada.")
            return pwd
        else:
            print(f"Contraseña demasiado corta ({len(pwd)} caracteres). Intenta de nuevo.")'''

print("=== Código (cópialo y ejecútalo en tu entorno si quieres interacción real) ===\n")
print(code_str)
print("\n=== Ejecución de ejemplo (simulada) ===\n")

# Simulación de ejecución con entradas de ejemplo
simulated_inputs = ["abc", "1234567", "miContra1", "contraseñaSegura123"]
prompt = "Introduce una contraseña (mínimo 8 caracteres): "

# Simulated interaction printing
for i, entry in enumerate(simulated_inputs):
    print(prompt + entry)
    if len(entry) >= 8:
        print("Contraseña aceptada.")
        break
    else:
        print(f"Contraseña demasiado corta ({len(entry)} caracteres). Intenta de nuevo.")

