import PySimpleGUI as sg
import pandas as pd

# add colour to window
sg.theme("Black")

EXCEL_FILE = 'DataBase.xlsx'
df = pd.read_excel(EXCEL_FILE)
layout = [
    [sg.Text('To select the bank :')],
    [sg.Text('---------------------------------------------------------------------------------------------------------------')],
    [sg.Text('Month/Year :', size=(15, 1)), sg.InputText(key='Month/Year')],
    [sg.Text('Commercial bank :')],
    [sg.Text('  Resone:'), sg.InputText(key='(COM bank) Resone')],
    [sg.Text('  Amount:'), sg.InputText(key='(COM bank) Amount')],
    [sg.Text('  Total Amount:'), sg.InputText(key='(COM bank) Total Amount')],
    [sg.Text('*******************************************OR******************************************')],
    [sg.Text('Peoples bank :')],
    [sg.Text('  Resone:'), sg.InputText(key='(Peoples bank)Resone')],
    [sg.Text('  Amount:'), sg.InputText(key='(Peoples bank) Amount')],
    [sg.Text('  Total Amount:'), sg.InputText(
        key='(Peoples bank) Total Amount')],



    [sg.Submit(), sg.Exit()]



]

window = sg.Window('My_Balance', layout)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Submit':
        df = df.append(values, ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)
        sg.popup("Data Saved !")
window.close()
