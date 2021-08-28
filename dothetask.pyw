import random
import PySimpleGUI as sg

def TextLabel(text): return sg.Text(text+':', justification='l', size=(5,1))
layout = [[TextLabel("Name"), sg.Input(key='-INPUT-0')],
          [TextLabel("Name"), sg.Input(key='-INPUT-1')],
          [TextLabel("To do"), sg.Input(key='-INPUT-2')],
          [TextLabel("Result"), sg.Multiline('Type in your names and i\'ll randomly select who\'s doing the task.', size=(45,9), key='-OUTPUT-0')],
          [sg.Button('Random', key='update', bind_return_key=True), sg.Button('Exit')]]
window = sg.Window(f'Who should do it?', layout, resizable=False, alpha_channel=1, grab_anywhere=False)

    
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        window.close()
    task = values['-INPUT-2']
    name1 = values['-INPUT-0']
    name2 = values['-INPUT-1']
    list = [name1, name2]
    who = random.choice(list)
    result = f'{who} will {task}'
    
    window['-OUTPUT-0'].update(result)
    
window.close()
