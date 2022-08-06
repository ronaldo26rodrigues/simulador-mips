def desestrutura_r(binario):
    """6 bits - opcode | 5 bits registrador | 5 bits registrador | 5 bits registrador | 5 bits shitf amount | 6 bits
    function """
    instrucao = {
        'opcode': binario[0:6],
        'rd': binario[6:11],
        'rs1': binario[11:16],
        'rs2': binario[16:21],
        'sa': binario[21:26],
        'fn': binario[26:32]
    }
    return instrucao

def desestrutura_i(binario):
    """6 bits - opcode | 5 bits registrador | 5 bits registrador | 16 bits immediate """
    instrucao = {
        'opcode': binario[0:6],
        'rs': binario[6:11],
        'rt': binario[11:16],
        'imd': binario[16:32]
    }
    return instrucao

def desestrutura_j(binario):
    """6 bits - opcode | 26 bits Jump """
    instrucao = {
        'opcode': binario[0:6],
        'jta': binario[6:32]
    }
    return instrucao

def hex2bin(hexa):
    return bin(int(hexa, 16))[2:].zfill(32)

def get_instruction(bin):
    if bin[0:6] == '000000':
        return 'R', bin[26:32]
    elif bin[0:6] == '000010' or bin[0:6] == '000011':
        return 'J', bin[0:6]
    else:
        return 'I', bin[0:6]
