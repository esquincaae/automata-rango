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

#2-CE-01R     6-DP-99S       4-DG-10R
states = {
    'q0': {str(i): 'q1' for i in range(2, 7)},  # Estado inicial, Espera numeros en el rango (2, 6)
    'q1': {'-': 'q2'},  # Después de recibir un dígito, espera un guión
    'q2': {chr(i): 'q3' for i in range(67, 69)},  # Espera una letra mayúscula en el rango (C, D)
    'q3': {chr(i): 'q4' for i in range(69, 81)},  # Espera otra letra mayúscula en el rango (E, P)
    'q4': {'-': 'q5'},  #Espera un guión
    'q5': {'0':'q6', '1':'q9', '2':'q9', '3':'q9', '4':'q9', '5':'q9', '6':'q9', '7':'q9', '8':'q9', '9':'q9'},# Después del segundo guión, espera un 0 para mandar a q6 ó un numero del (1, 9) para mandar a q9
        'q9':{str(i): 'q7' for i in range(10)}, #Espera numeros en un rango de (0, 9) si y solo si en q5 se recibio un numero en el rango (1, 9)
        'q6': {str(i): 'q7' for i in range(1, 10)},  # Espera digitos del (1, 9) si y solo si en q5 se recibio un 0
    'q7': {chr(i): 'q8' for i in range(82, 84)},  #Espera una letra mayúscula en el rango (R, S)
    'q8': {}  #Estado de aceptación

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
