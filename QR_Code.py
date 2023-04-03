import qrcode as qr
import PySimpleGUI as sg 

sg.theme('GrayGrayGray')
font =('Verdana', 12)

qr_image = [sg.Image('', key = 'QRCODE')]

# the layout
index = 0
color = {0: ("gray", "blue"), 1: ("gray", "blue")}
layout = [
    [sg.Text('Enter Url:'), sg.Input(text_color= 'black', key= 'Url' )],
    [sg.Button('Create', key='Submit',  mouseover_colors= color[index], use_ttk_buttons=True, size= (7,1)),  sg.Button('Close', key='CLOSE', mouseover_colors= color[index], use_ttk_buttons=True, size= (7,1))],
    [sg.Column([qr_image], justification= 'center')],
]

 # Create the Window
window = sg.Window('QR coode Generator', layout, font= font)

# Event loop  
while True:
    event , values = window.read()
    if event == sg.WIN_CLOSED or event == 'CLOSE':
        break
    elif event == 'Submit':
        url = values['Url']
        if url:
            qr_code = qr.QRCode(
                version=1,
                error_correction=qr.constants.ERROR_CORRECT_L,
                box_size=20,
                border=4,
                )
            qr_code.add_data('Data')
            qr_code.make(fit=True)
            img = qr_code.make_image(fback_color=(0, 0, 0), fill_color=(128, 128, 128))
            img.save('qrCode.png')
            window['QRCODE'].update('qrCode.png')
window.close()