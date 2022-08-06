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
    # for instruction in range(len(instructions)):
    instruction = 0
    while instruction < len(instructions):
        binario = util.hex2bin(instructions[instruction])
        opcode = util.get_instruction(binario)
        indice = instruction
        if opcode[0] == 'R':
            desestruturado = util.desestrutura_r(binario)
            print(desestruturado)
            indice = mips.instrucoes[opcode[1]](desestruturado['rd'], desestruturado['rs1'], desestruturado['rs2'])
        if opcode[0] == 'J':
            desestruturado = util.desestrutura_j(binario)
            indice = mips.instrucoes[opcode[1]](desestruturado['jta'])
        if opcode[0] == 'I':
            desestruturado = util.desestrutura_i(binario)
            indice = mips.instrucoes[opcode[1]](desestruturado['rs'], desestruturado['rt'], desestruturado['imd'])
        instruction += 1
        if indice >= 0:
            instruction = indice
        # print(util.hex2bin(instruction))


def execute():
    config_regs()
    config_data()
    config_mem()
    print(mips.registradores)
    instructions()


execute()
print(mips.registradores)
