import FreeSimpleGUI as sg
from zip_extractor import extract_zip

sg.theme('Black')

label1 = sg.Text("Select archive")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key = "archive")

label2 = sg.Text("Select dest dir")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key = "folder")

extract_button = sg.Button("Extract", size=10)
output = sg.Text(key="output", text_color="green")

window = sg.Window("Archive Extractor", 
                     layout=[[label1, input1, choose_button1], 
                            [label2, input2, choose_button2], 
                            [extract_button], 
                            [output]], 
                     font=('Helvetica', 20))
while True:  
    event, values = window.read()
    arvhivepsth = values['archive']
    dest_dir = values['folder']
    extract_zip(arvhivepsth, dest_dir)
    window['output'].update(value="Done!")
    
window.close()