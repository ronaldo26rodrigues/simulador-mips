import util

registradores = {
    0:  '00000000',
    1:  '00000000',
    2:  '00000000',
    3:  '00000000',
    4:  '00000000',
    5:  '00000000',
    6:  '00000000',
    7:  '00000000',
    8:  '00000000',
    9:  '00000000',
    10: '00000000',
    11: '00000000',
    12: '00000000',
    13: '00000000',
    14: '00000000',
    15: '00000000',
    16: '00000000',
    17: '00000000',
    18: '00000000',
    19: '00000000',
    20: '00000000',
    21: '00000000',
    22: '00000000',
    23: '00000000',
    24: '00000000',
    25: '00000000',
    26: '00000000',
    27: '00000000',
    28: '00000000',
    29: '00000000',
    30: '00000000',
    31: '00000000',
    'pc': '00000000',
    'hi': '00000000',
    'lo': '00000000',
}

# fazer as instruções aqui


def add(rd, rs1, rs2):
    rd = util.bin2dec(rd)
    rs1 = util.bin2dec(rs1)
    rs2 = util.bin2dec(rs2)
    registradores[rd] = registradores[rs1] + registradores[rs2]
    return -1

def sub(rd, rs1, rs2):
    rd = util.bin2dec(rd)
    rs1 = util.bin2dec(rs1)
    rs2 = util.bin2dec(rs2)
    registradores[rd] = registradores[rs1] - registradores[rs2]
    return -1

def sll(rd, rs1, rs2):
    rd = util.bin2dec(rd)
    rs1 = util.bin2dec(rs1)
    rs2 = util.bin2dec(rs2)
    registradores[rd] = registradores[rs1] << registradores[rs2]
    return -1

def sllv(rd, rs1, rs2):
    rd = util.bin2dec(rd)
    rs1 = util.bin2dec(rs1)
    rs2 = util.bin2dec(rs2)
    registradores[rd] = registradores[rs1] << registradores[rs2]
    return -1

def slt(rd, rs1, rs2):
    rd = util.bin2dec(rd)
    rs1 = util.bin2dec(rs1)
    rs2 = util.bin2dec(rs2)
    if registradores[rs2] < [rs2]:
     registradores[rd] = 1
    return -1

def subu(rd, rs1, rs2):
    rd = util.bin2dec(rd)
    rs1 = util.bin2dec(rs1)
    rs2 = util.bin2dec(rs2)
    registradores[rd] = registradores[rs1] - registradores[rs2]
    return -1

instrucoes = {
    '100000': add
     
}

instrucoes = {
    '100010': sub
     
}

instrucoes = {
    '000000': sll
     
}

instrucoes = {
    '000100': sllv
     
}

instrucoes = {
    '101010': slt
     
}

instrucoes = {
    '100011': subu
     
}