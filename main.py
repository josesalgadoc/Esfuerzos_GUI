from math import sin
from math import radians
from math import log
from math import pi
from math import degrees, atan


import numpy as np

import PySimpleGUI as sg
# from PySimpleGUI.PySimpleGUI import Graph, Text


## Configuracion de sg
sg.theme('NeutralBlue')
sg.set_global_icon('./icon.ico')

menu_def = [
    ['Archivo', ['Salir']]
]

head_principal = [
    [sg.Text(text='Cálculo de Esfuerzos en el Suelo', font=("Helvetica", 11, "bold"), size=(80,1), justification='center'), sg.Image(filename='./images/escudo.png', size=(50,50), key='-IMAGE-')
    ]
]

principal = [
    [sg.Text('Seleccione el método del que quiere realizar los calculos'),
    sg.Combo(['Carga Puntual', 'Franja de Carga Vertical y Linealmente Infinita','Franja de Carga Triangular y Linealmente Infinita','Area Circular Uniformemente Cargada','Area Rectangular Uniformemente Cargada', 'Franja de Carga Trapezoidal'],default_value='Seleccione el método', key='-METODO-')],
    [sg.Button('Calcular')],
]

## Creacion de las ventanas
def make_win_principal():
    layout = [
        [
            [sg.Menu(menu_def, key='-MENU-')], 
            head_principal,
            principal
        ]
    ]
    return sg.Window('Esfuerzos en el Suelo', layout, finalize = True)

### Carga vertical
def verical_point_load():
    layout = [
            [sg.Menu(menu_def, key='-MENU-')], 
            [sg.Text('Carga Puntual', font=("Helvetic", 11, "bold"))],
            [sg.Text('A continuación, suministre los valores requeridos para el calculo en el método Carga Puntual')],
            [
                sg.Column([
                        [sg.Text('Intensidad de la Carga (P)')],
                        [sg.Text('Profundidad (z)')],
                        [sg.Text('Radio del círculo de influencia de la carga al punto (r)')]
                        ]),
                sg.Column([
                        [sg.In('',
                                key='-P_VERTICAL_LOAD-')],
                        [sg.In('', 
                                key='-Z_VERTICAL_LOAD-')],
                        [sg.In('', 
                                key='-R_VERTICAL_LOAD-')]
                        ])
            ],
            [sg.Image(filename='./images/carga_puntual.png', size=(300,300), key='-IMAGE-')],
            [sg.Button('Volver'), sg.Button('Calcular')]
        ]
    return sg.Window('Carga Puntual', layout, finalize = True)

### Carga Infinita vertical
def infinite_vertical_strip_load():
    layout = [
            [sg.Menu(menu_def, key='-MENU-')], 
            [sg.Text('Franja de Carga Vertical y Linealmente Infinita', font=("Helvetic", 11, "bold"))],
            [sg.Text('A continuación, suministre los valores requeridos para el calculo del método')],
            [
                sg.Column([
                        [sg.Text('Intensidad de la Carga (q)')],
                        [sg.Text('Coeficiente de Poisson del material (v)')],
                        [sg.Text('Distancia desde el centro de la carga hasta el punto de interés (r)')],
                        [sg.Text('Ancho de la carga (b)')]
                        ]),
                sg.Column([
                        [sg.In('',
                                key='-q_VERTICAL_STRIP_LOAD-')],
                        [sg.In('', 
                                key='-v_VERTICAL_STRIP_LOAD-')],
                        [sg.In('', 
                                key='-r_VERTICAL_STRIP_LOAD-')],
                        [sg.In('', 
                                key='-b_VERTICAL_STRIP_LOAD-')]
                        ])
            ],
            [sg.Image(filename='./images/vertical_y_linealmente_infinita.png', size=(518,400), key='-IMAGE-')],
            [sg.Button('Volver'), sg.Button('Calcular')]
        ]
    return sg.Window('Franja de Carga Vertical y Linealmente Infinita', layout, finalize = True)

### Carga Triangular
def infinite_triangular_strip_load():
    layout = [
            [sg.Menu(menu_def, key='-MENU-')], 
            [sg.Text('Franja de Carga Triangular y Linealmente Infinita', font=("Helvetic", 11, "bold"))],
            [sg.Text('A continuación, suministre los valores requeridos para el calculo del método')],
            [
                sg.Column([
                        [sg.Text('Intensidad de la Carga (q)')],
                        [sg.Text('Profundidad en metros desde la superficie (h)')],
                        [sg.Text('Ancho de la franja de carga (d)')]
                        ]),
                sg.Column([
                        [sg.In('',
                                key='-q_TRIANGULAR_STRIP_LOAD-')],
                        [sg.In('', 
                                key='-h_TRIANGULAR_STRIP_LOAD-')],
                        [sg.In('', 
                                key='-d_TRIANGULAR_STRIP_LOAD-')]
                        ])
            ],
            [sg.Image(filename='./images/triangular_y_linealmente_infinita.png', size=(512,400), key='-IMAGE-')],
            [sg.Button('Volver'), sg.Button('Calcular')]
        ]
    return sg.Window('Franja de Carga Triangular y Linealmente Infinita', layout, finalize = True)

### Carga Circular
def circular_area_load():
    layout = [
            [sg.Menu(menu_def, key='-MENU-')], 
            [sg.Text('Area Circular Uniformemente Cargada', font=("Helvetic", 11, "bold"))],
            [sg.Text('A continuación, suministre los valores requeridos para el calculo del método')],
            [
                sg.Column([
                        [sg.Text('Intensidad de la Carga (q)')],
                        [sg.Text('Radio de la carga (r)')],
                        [sg.Text('Profundidad (z)')]
                        ]),
                sg.Column([
                        [sg.In('',
                                key='-q_CIRCULAR_LOAD-')],
                        [sg.In('', 
                                key='-r_CIRCULAR_LOAD-')],
                        [sg.In('', 
                                key='-z_CIRCULAR_LOAD-')]
                        ])
            ],
            [sg.Image(filename='./images/circular_uniformemente.png', size=(459,400), key='-IMAGE-')],
            [sg.Button('Volver'), sg.Button('Calcular')]
        ]
    return sg.Window('Area Circular Uniformemente Cargada', layout, finalize = True)

### Carga Rectangular
def rectangular_area_load():
    layout = [
            [sg.Menu(menu_def, key='-MENU-')], 
            [sg.Text('Area Rectangular Uniformemente Cargada', font=("Helvetic", 11, "bold"))],
            [sg.Text('A continuación, suministre los valores requeridos para el calculo del método')],
            [
                sg.Column([
                        [sg.Text('Intensidad de la Carga (q)')],
                        [sg.Text('Ancho de la carga (b)')],
                        [sg.Text('Profundidad de la carga (l)')],
                        [sg.Text('Distancia de la carga al punto de interés (z)')]
                        ]),
                sg.Column([
                        [sg.In('',
                                key='-q_RECTANGULAR_LOAD-')],
                        [sg.In('', 
                                key='-b_RECTANGULAR_LOAD-')],
                        [sg.In('', 
                                key='-l_RECTANGULAR_LOAD-')],
                        [sg.In('', 
                                key='-z_RECTANGULAR_LOAD-')]
                        ])
            ],
            [sg.Image(filename='./images/rectangular_uniforme.png', size=(660,400), key='-IMAGE-')],
            [sg.Button('Volver'), sg.Button('Calcular')]
        ]
    return sg.Window('Area Rectangular Uniformemente Cargada', layout, finalize = True)

### Carga Trapecio
def trapecio_area_load():
    layout = [
            [sg.Menu(menu_def, key='-MENU-')], 
            [sg.Text('Franja de Carga Trapezoidal', font=("Helvetic", 11, "bold"))],
            [sg.Text('A continuación, suministre los valores requeridos para el calculo del método')],
            [
                sg.Column([
                        [sg.Text('Intensidad de la Carga (q)')],
                        [sg.Text('Ancho de carga 1 (b1)')],
                        [sg.Text('Ancho de carga 2 (b2)')],
                        [sg.Text('Angulo 1 (alfa1)')],
                        [sg.Text('Angulo 2 (alfa2)')]

                        ]),
                sg.Column([
                        [sg.In('',
                                key='-q_TRAPECIO_LOAD-')],
                        [sg.In('', 
                                key='-b1_TRAPECIO_LOAD-')],
                        [sg.In('', 
                                key='-b2_TRAPECIO_LOAD-')],
                        [sg.In('', 
                                key='-alfa1_TRAPECIO_LOAD-')],
                        [sg.In('', 
                                key='-alfa2_TRAPECIO_LOAD-')]
                        ])
            ],
            [sg.Image(filename='./images/trapezoidal.png', size=(440,400), key='-IMAGE-')],
            [sg.Button('Volver'), sg.Button('Calcular')]
        ]
    return sg.Window('Franja de Carga Trapezoidal', layout, finalize = True)

def run():

    # carga_puntual, franja_vertical_infinita = 0, 0

    principal_window = make_win_principal()
    vertical_load_window, vertical_strip_load, triangular_strip_load, circular_area, rectangular_area, trapecio_load = None, None, None, None, None, None

    while True:
        window, event, values = sg.read_all_windows()

        if event in (sg.WIN_CLOSED, 'Salir'):
            break

        if window == principal_window:
            if event == 'Calcular':
                principal_window.hide()
                if values['-METODO-'] == 'Carga Puntual' and not vertical_load_window:
                    vertical_load_window = verical_point_load()
                if values['-METODO-'] == 'Franja de Carga Vertical y Linealmente Infinita':
                    vertical_strip_load = infinite_vertical_strip_load()
                if values['-METODO-'] == 'Franja de Carga Triangular y Linealmente Infinita':
                    triangular_strip_load = infinite_triangular_strip_load()
                if values['-METODO-'] == 'Area Circular Uniformemente Cargada':
                    circular_area = circular_area_load()
                if values['-METODO-'] == 'Area Rectangular Uniformemente Cargada':
                    rectangular_area = rectangular_area_load()
                if values['-METODO-'] == 'Franja de Carga Trapezoidal':
                    trapecio_load = trapecio_area_load()

        if window == vertical_load_window:
            if event == 'Volver':
                window.close()
                vertical_load_window = None
                principal_window.un_hide()

            if event == 'Calcular':              

                carga_puntual = (float(values['-P_VERTICAL_LOAD-']) / (float(values['-Z_VERTICAL_LOAD-'])**2)) * ((3 / (2*pi)) * (1 / (((float(values['-R_VERTICAL_LOAD-']) / float(values['-Z_VERTICAL_LOAD-']))**2) + 1) ** (5/2)))

                sg.Popup('El incremento de carga es ' + str(carga_puntual))

        if window == vertical_strip_load:
            if event == 'Volver':
                window.close()
                vertical_strip_load = None
                principal_window.un_hide()

            if event == 'Calcular':              

                # franja_vertical_infinita = (q / pi) * ((((1-ν) * np.log(r/(2*b))) + ν) / ((1+ν) * (((2*b)**2) / ((r**2) - 1))))

                franja_vertical_infinita = (float(values['-q_VERTICAL_STRIP_LOAD-']) / pi) * ((((1-float(values['-v_VERTICAL_STRIP_LOAD-'])) * np.log(float(values['-r_VERTICAL_STRIP_LOAD-']) / (2*float(values['-b_VERTICAL_STRIP_LOAD-'])))) + float(values['-v_VERTICAL_STRIP_LOAD-'])) / ((1+float(values['-v_VERTICAL_STRIP_LOAD-'])) * (((2*float(values['-b_VERTICAL_STRIP_LOAD-']))**2) / ((float(values['-r_VERTICAL_STRIP_LOAD-'])**2) - 1))))

                sg.Popup('El incremento de carga es ' + str(franja_vertical_infinita))

        if window == triangular_strip_load:
            if event == 'Volver':
                window.close()
                triangular_strip_load = None
                principal_window.un_hide()

            if event == 'Calcular':              

                # franja_triangular_infinita = (q/(2*pi)) * (1- ((2*h) /(((h**2) + (d**2) ** (1/2)))))

                franja_triangular_infinita = (float(values['-q_TRIANGULAR_STRIP_LOAD-']) / (2*pi)) * (1 - ((2*float(values['-h_TRIANGULAR_STRIP_LOAD-'])) / (((float(values['-h_TRIANGULAR_STRIP_LOAD-'])**2) + (float(values['-d_TRIANGULAR_STRIP_LOAD-'])**2) ** (1/2)))))

                sg.Popup('El incremento de carga es ' + str(franja_triangular_infinita))

        if window == rectangular_area:
            if event == 'Volver':
                window.close()
                rectangular_area = None
                principal_window.un_hide()

            if event == 'Calcular':              

                b = float(values['-b_RECTANGULAR_LOAD-'])
                l = float(values['-z_RECTANGULAR_LOAD-'])
                q = float(values['-q_RECTANGULAR_LOAD-'])
                m = b/z
                n = l/z

                rectangular_uniforme_area = ((q / (4*pi)) * (((2*m*n) * ((m**2)+(n**2)+2) * (((m**2)+(n**2)+1)**(1/2))) / (((m**2)+(n**2)+((m**2)*(n**2))+1) * ((m**2)+(n**2)+1)))) + (degrees(atan((((2*m*n) * (((m**2)+(n**2)+1)*(1/2))) / ((m**2)+(n**2)+((m**2)*(n**2))-1)))))

                sg.Popup('El incremento de carga es ' + str(rectangular_uniforme_area))

        if window == circular_area:
            if event == 'Volver':
                window.close()
                circular_area = None
                principal_window.un_hide()

            if event == 'Calcular':              

                q = float(values['-q_CIRCULAR_LOAD-'])
                r = float(values['-r_CIRCULAR_LOAD-'])
                z = float(values['-z_CIRCULAR_LOAD-'])
                
                circular_uniforme_area = (q) * (1 - (1 / ((1+((r/z)**2))**(3/2))))

                sg.Popup('El incremento de carga es ' + str(circular_uniforme_area))

        if window == trapecio_load:
            if event == 'Volver':
                window.close()
                trapecio_load = None
                principal_window.un_hide()

            if event == 'Calcular':              

                b1 = float(values['-b1_TRAPECIO_LOAD-'])
                b2 = float(values['-b2_TRAPECIO_LOAD-'])
                q = float(values['-q_TRAPECIO_LOAD-'])
                alfa1 = float(values['-alfa1_TRAPECIO_LOAD-'])
                alfa2 = float(values['-alfa2_TRAPECIO_LOAD-'])
                
                trapezoide_load = (q/pi) * ((((b1+b2) / b2) * (alfa1+alfa2)) - (((b1/b2)*(alfa2))))

                sg.Popup('El incremento de carga es ' + str(trapezoide_load))

    window.close()

if __name__ == '__main__':
    run()