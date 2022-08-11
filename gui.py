import json

import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()


def load_arch(filename):
    global json_arq, data
    json_arq = open(filename, 'r').read()
    data = json.loads(json_arq)
    dpg.delete_item('archjson')
    dpg.delete_item('abrirarq')
    return data


with dpg.window(label='MIPS', tag='window'):
    dpg.add_input_text(label='Arquivo json', tag='archjson')
    dpg.add_button(label='Abrir arquivo', callback=lambda: load_arch(dpg.get_value('archjson')), tag='abrirarq')


    def add_table():
        try:
            dpg.delete_item('table')
        except:
            pass
        with dpg.table(label='Registradores', parent='window', tag='table'):
            dpg.add_table_column(label="Registradores")
            dpg.add_table_column(label="Memoria")

            for reg, mem in itertools.zip_longest(mips.registradores.items(), mips.memoria.items()):
                with dpg.table_row():
                    dpg.add_text(f"{reg}")
                    dpg.add_text(f"{mem}")

texto = ''
def mod_txt(txt):
    texto = txt

def inpt():
    dpg.add_input_text(label='Console', parent='window', tag='console')
    dpg.add_button(label='Enviar', parent='window', callback=lambda : mod_txt(dpg.get_value('console')), tag='consolebt')
    dpg.delete_item('console')
    dpg.delete_item('consolebt')
    return texto