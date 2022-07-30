import json
import util
import mips

json_arq = open('teste_mips.json', 'r').read()

data = json.loads(json_arq)

print(data)


def config_regs():
    regs = data['config']['regs']
    for reg in regs:
        if reg in 'pchilo':
            mips.registradores[reg] = regs[reg]
        else:
            mips.registradores[int(reg[1:])] = regs[reg]


# TODO: logica de configurar memória
def config_mem():
    pass


# TODO: logica de configurar .data
def config_data():
    pass


# TODO: logica de executar instruções
def instructions():
    instructions = data['text']
    for instruction in instructions:
        print(util.hex2bin(instruction))


def execute():
    config_regs()
    config_data()
    config_mem()
    instructions()


execute()
print(mips.registradores)
