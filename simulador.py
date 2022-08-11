import itertools
import json
import util
import mips

import dearpygui.dearpygui as dpg

open('saida.json', 'w').close()
outfile = open('saida.json', 'a')

# carrega o arquivo json de entrada
def load_arch(filename):
    global json_arq, data
    json_arq = open(filename, 'r').read()
    data = json.loads(json_arq)
    dpg.delete_item('archjson')
    dpg.delete_item('abrirarq')

    execute()


dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()


# interface dearpy
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
                    if mem is not None:
                        dpg.add_text(f"{mem}")


def config_regs():
    regs = data['config']['regs']
    for reg in regs:
        if reg in 'pchilo':
            mips.registradores[reg] = regs[reg]
        else:
            mips.registradores[int(reg[1:])] = regs[reg]


# TODO: logica de configurar memória
def config_mem():
    d = data['config']['mem']
    for dt in d:
        mips.memoria[dt] = d[dt]
    print(mips.memoria)


# TODO: logica de configurar .data
def config_data():
    d = data['data']
    for dt in d:
        mips.memoria[dt] = d[dt]
    print(mips.memoria)


#  logica de executar instruções
def instructions():
    instructions = data['text']
    # for instruction in range(len(instructions)):
    instruction = 0
    while instruction < len(instructions):
        binario = util.hex2bin(instructions[instruction])
        opcode = util.get_instruction(binario)
        indice = instruction
        mips.registradores['pc'] = instruction
        if opcode[0] == 'R':
            desestruturado = util.desestrutura_r(binario)
            indice = mips.functions[opcode[1]](desestruturado['rd'], desestruturado['rs1'], desestruturado['rs2'])
        if opcode[0] == 'J':
            desestruturado = util.desestrutura_j(binario)
            indice = mips.opcode[opcode[1]](desestruturado['jta'])
        if opcode[0] == 'I':
            desestruturado = util.desestrutura_i(binario)
            indice = mips.opcode[opcode[1]](desestruturado['rs'], desestruturado['rt'], desestruturado['imd'])
        json_d = json.dumps(out(instructions[instruction]), indent=4) 
        outfile.write(json_d+',\n')
        instruction += 1
        add_table()
        if indice is not None:
            instruction = indice
    print(mips.registradores)
    print(mips.memoria)





def execute():
    config_regs()
    config_data()
    config_mem()
    print(mips.registradores)
    instructions()


def out(hexa):
    return {
        "hex": hexa,
        "text": util.hex2bin(hexa),
        "regs": {'$'+str(x): v for x, v in mips.registradores.items() if v != 0 and v != "00000000"},
        "mem": {x: v for x, v in mips.memoria.items() if v != 0 and v != "00000000"},
        "stdout": ""

    }


dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
