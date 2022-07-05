import PySimpleGUI as sg

layout = [[sg.Text("Gardenia App")], [sg.Button("Make me a calendar!")]]

# Create the window
window = sg.Window("Gardenia", layout, margins = (250, 150))

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()