import tkinter as tk
import time

def validar_automata(input_string, estados):
    current_state = "q0"
    sequence = [current_state]

    for char in input_string:
        try:
            if estados[current_state][char]:
                current_state = estados[current_state][char]
                sequence.append(current_state)
        except KeyError:
            return {'success': False, 'message': f'Autómata no válido, error en el estado {current_state}', 'sequence': sequence}

    return {'success': True, 'message': 'Autómata válido', 'sequence': sequence}

def validar():
    input_text = entrada.get()
    resultado = validar_automata(input_text, estados)
    resultado_label.config(text=f"Resultado: {resultado['message']}")
    mostrar_secuencia(resultado['sequence'])

def mostrar_secuencia(sequence):
    secuencia_label.config(text="Secuencia de estados:")
    for state in sequence:
        secuencia_label.config(text=secuencia_label.cget("text") + f" -> {state}")
        ventana.update()
        time.sleep(1)

#2-CE-01R       6-DP-99S
#A-B-C-D-E-F-G-H-I-J-K-L-M-N-Ñ-O-P-Q-R-S-T-U-V-W-X-Y-Z  
estados = {
    'q0': {'2':'q1', '3':'q9', '6':'q16', '4':'q9','5':'q9'},
    #'q0': {str(i): 'q9' for i in range(3, 6)},
    
    'q1': {'-': 'q2'},
    'q9': {'-':'q10'}, 
    'q16': {'-': 'q17'},

    'q2': {'C':'q3','D':'q11','E':'q11','F':'q11','G':'q11','H':'q11','I':'q11','J':'q11','K':'q11','L':'q11','M':'q11','N':'q11','Ñ':'q11','O':'q11','P':'q11','Q':'q11','R':'q11','S':'q11','T':'q11','U':'q11','V':'q11','W':'q11','X':'q11','Y':'q11','Z':'q11'}, 
    'q10': {chr(i):'q11' for i in range(65, 91)},
    'q17': {'D': 'q18'},
  
    'q3': {'E':'q4','F':'q12','G':'q12','H':'q12','I':'q12','J':'q12','K':'q12','L':'q12','M':'q12','N':'q12','Ñ':'q12','O':'q12','P':'q12','Q':'q12','R':'q12','S':'q12','T':'q12','U':'q12','V':'q12','W':'q12','X':'q12','Y':'q12','Z':'q12'},
    #'q3': {chr(i):'q12'  for i in range(70, 91)},
    'q11':{chr(i): 'q12' for i in range(65, 91)}, 
    'q18':{'P':'q19', 'A':'q12', 'B':'q12','C':'q12','D':'q12','E':'q12','F':'q12','G':'q12','H':'q12','I':'q12','J':'q12','K':'q12','L':'q12','M':'q12','N':'q12','Ñ':'q12','O':'q12'},
    #'q18':{chr(i):'q12' for i in range(65,79)},

    'q4':{'-':'q5'},
    'q12':{'-':'q13'},
    'q19':{'-':'q20'},

    'q5':{'0':'q6','1':'q14','2':'q14','3':'q14','4':'q14','5':'q14','6':'q14','7':'q14','8':'q14','9':'q14'},
    'q13':{'0':'q6','1':'q14','2':'q14','3':'q14','4':'q14','5':'q14','6':'q14','7':'q14','8':'q14','9':'q14'},
    #'q13':{str(i):'q14' for i in range(1,10)},
    #'q20':{str(i):'q14' for i in range(0,9)},
    'q20':{'9':'q21','0':'q14','1':'q14','2':'q14','3':'q14','4':'q14','5':'q14','6':'q14','7':'q14','8':'q14'},

    'q6':{'1':'q7','2':'q15','3':'q15','4':'q15','5':'q15','6':'q15','7':'q15','8':'q15','9':'q15'},
    #'q6':{str(i):'q15' for i in range(3,10)},
    'q14':{str(i):'q15' for i in range(0,10)},
    #'q21':{str(i):'q15' for i in range(0,9)},
    'q21':{'9':'q22','1':'q15','2':'q15','3':'q15','4':'q15','5':'q15','6':'q15','7':'q15','8':'q15','0':'q15'},

    'q7':{'R':'q8','S':'q8','T':'q8','U':'q8','V':'q8','W':'q8','X':'q8','Y':'q8','Z':'q8'},
    'q15':{chr(i):'q24' for i in range(65,91)},
    'q22':{chr(i):'q23' for i in range(65,84)},

    'q8':{'':''},
    'q24':{'':''},   
    'q23':{'':''},

    #'q25':{},
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
