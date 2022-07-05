import PySimpleGUI as sg
import os.path

input_column = [
    [sg.Text('Basic Plant Information')],
    [sg.Text('Category', size =(15, 1)), sg.InputText()], # make a dropdown?
    [sg.Text('Variety', size =(15, 1)), sg.InputText()],
    [sg.Text('Starter Weeks', size =(15, 1)), sg.InputText()],
    [sg.Text('Frost Overlap Weeks', size =(15, 1)), sg.InputText()],
    [sg.Text('Days to Maturity', size =(15, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]

output_column = [
    [sg.Text('This will house the garden Gantt chart and summary table')],
]

layout = [
    [
        sg.Column(input_column),
        sg.VSeperator(),
        sg.Column(output_column),
    ]
]

# Create the window
window = sg.Window("Gardenia", layout)


# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Cancel" or event == sg.WIN_CLOSED:
        break

window.close()