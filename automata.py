import tkinter as tk
import time

def validar_automata(input_string, states):
    current_state = "q0"
    sequence = [current_state]

    for char in input_string:
        try:
            if states[current_state][char]:
                current_state = states[current_state][char]
                sequence.append(current_state)
        except KeyError:
            return {'success': False, 'message': f'Autómata no válido, error en el estado {current_state}', 'sequence': sequence}

    if current_state not in ['q8', 'q17']:
        return {'success': False, 'message': f'Autómata no válido, detenido en el estado {current_state}', 'sequence': sequence}

    return {'success': True, 'message': 'Autómata válido', 'sequence': sequence}

def validar():
    input_text = entrada.get()
    resultado = validar_automata(input_text, states)
    resultado_label.config(text=f"Resultado: {resultado['message']}")
    mostrar_secuencia(resultado['sequence'])

def mostrar_secuencia(sequence):
    secuencia_label.config(text="Secuencia de estados:")
    for state in sequence:
        secuencia_label.config(text=secuencia_label.cget("text") + f" -> {state}")
        ventana.update()
        time.sleep(1)
#2-CE-01R    6-DP-99S       4-DG-10R
states = {
    'q0': {'2': 'q1', '3': 'q1', '4': 'q1', '5': 'q1', '6': 'q1'},  # Estado inicial
    'q1': {'-': 'q2'},  # Después de recibir un dígito, espera un guión
    'q2': {chr(i): 'q3' for i in range(67, 69)},  # Después de un guión, espera una letra mayúscula
    'q3': {chr(i): 'q4' for i in range(69, 81)},  # Espera otra letra mayúscula
    'q4': {'-': 'q5'},  # Después de dos letras mayúsculas, espera otro guión
    'q5': {'0':'q6', '1':'q9', '2':'q9', '3':'q9', '4':'q9', '5':'q9', '6':'q9', '7':'q9', '8':'q9', '9':'q9'},#str(i): 'q6' for i in range(10)},  # Después del segundo guión, espera un dígito
        'q9':{str(i): 'q7' for i in range(10)},

    'q6': {str(i): 'q7' for i in range(1, 10)},#'1':'q7', '2':'q7', '3':'q7', '4':'q7', '5':'q7', '6':'q7', '7':'q7', '8':'q7', '9':'q7'},  # Espera otro dígito
    'q7': {chr(i): 'q8' for i in range(82, 84)},  # Finalmente, espera una letra mayúscula
    'q8': {}  # Estado de aceptación, no hay transiciones posibles desde aquí

}

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Validador de Autómata")
ventana.geometry("500x300")

etiqueta = tk.Label(ventana, text="Ingresa la cadena a validar:")
etiqueta.pack()

entrada = tk.Entry(ventana)
entrada.pack()

boton = tk.Button(ventana, text="Validar", command=validar)
boton.pack()

resultado_label = tk.Label(ventana, text="")
resultado_label.pack()

secuencia_label = tk.Label(ventana, text="")
secuencia_label.pack()

ventana.mainloop()
