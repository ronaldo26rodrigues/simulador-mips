import json
import util
import mips

json_arq = open('teste_mips.json', 'r').read()

data = json.loads(json_arq)

print(data)

outfile = open('saida.json', 'a')


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
    d = data['data']
    for dt in d:
        mips.memoria[dt] = d[dt]
    print(mips.memoria)


# TODO: logica de executar instruções
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
        outfile.write(',\n'+json_d)
        instruction += 1

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
        "text": "",
        "regs": {'$'+str(x): v for x, v in mips.registradores.items() if v != 0 and v != "00000000"},
        "mem": {x: v for x, v in mips.memoria.items() if v != 0 and v != "00000000"},
        "stdout": ""

    }


execute()
