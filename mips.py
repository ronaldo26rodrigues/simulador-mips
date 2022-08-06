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


def addi(rs, rt, imd):
    rs = util.bin2dec(rs)
    rt = util.bin2dec(rt)
    imd = util.bin2dec(imd)
    registradores[rs] = registradores[rt] + registradores[imd]
    return -1


def addiu(rs, rt, imd):
    rs = util.bin2dec(rs)
    rt = util.bin2dec(rt)
    imd = util.bin2dec(imd)
    registradores[rs] = registradores[rt] + registradores[imd]
    return -1


def addu(rd, rs1, rs2):
    rd = util.bin2dec(rd)
    rs1 = util.bin2dec(rs1)
    rs2 = util.bin2dec(rs2)
    registradores[rd] = registradores[rs1] + registradores[rs2]
    return -1


def andd(rd, rs1, rs2):
    rd = util.bin2dec(rd)
    rs1 = util.bin2dec(rs1)
    rs2 = util.bin2dec(rs2)
    registradores[rd] = registradores[rs1] and registradores[rs2]
    return -1


def andi(rs, rt, imd):
    rs = util.bin2dec(rs)
    rt = util.bin2dec(rt)
    imd = util.bin2dec(imd)
    registradores[rs] = registradores[rt] and registradores[imd]
    return -1


def bgtz(rs, rt, imd):
    rs = util.bin2dec(rs)
    rt = 0
    imd = util.bin2dec(imd)
    if(registradores[rs] > rt): registradores['pc'] + registradores[imd]
    return -1


def beq(rs, rt, imd):
    rs = util.bin2dec(rs)
    rt = 0
    imd = util.bin2dec(imd)
    if(registradores[rs] > rt): registradores['pc'] + registradores[imd]
    return -1


def bltz(rs, rt, imd):
    rs = util.bin2dec(rs)
    rt = 0
    imd = util.bin2dec(imd)
    if(registradores[rs] > rt): registradores['pc'] + registradores[imd]
    return -1


def blez(rs, rt, imd):
    rs = util.bin2dec(rs)
    rt = 0
    imd = util.bin2dec(imd)
    if registradores[rs] > rt: registradores['pc'] + registradores[imd]
    return -1


def bne(rs, rt, imd):
    rs = util.bin2dec(rs)
    rt = 0
    imd = util.bin2dec(imd)
    if registradores[rs] > rt: registradores['pc'] + registradores[imd]
    return -1


def div(rs1, rs2):
    rs1 = util.bin2dec(rs1)
    rs2 = util.bin2dec(rs2)
    registradores['hi'] = registradores[rs1] % registradores[rs2]
    registradores['lo'] = registradores[rs1] // registradores[rs2]
    return -1


def divu(rs1, rs2):
    rs1 = util.bin2dec(rs1)
    rs2 = util.bin2dec(rs2)
    registradores['hi'] = registradores[rs1] % registradores[rs2]
    registradores['lo'] = registradores[rs1] // registradores[rs2]
    return -1

def sub(rd, rs1, rs2):
    rd = util.bin2dec(rd)
    rs1 = util.bin2dec(rs1)
    rs2 = util.bin2dec(rs2)
    registradores[rd] = registradores[rs1] - registradores[rs2]
    return -1


def jal(jta):
    registradores['ra'] = registradores['pc'] + 1
    return util.address2index(jta)

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


def jr(rd, rs1, rs2):
    return registradores[rs2]


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


opcode = {
    '000011': jal,
}

functions = {
    '100000': add,
    '001000': addi,
    '001001': addiu,
    '100001': addu,
    '100100': andd,
    '001100': andi,
    '000111': bgtz,
    '000100': beq,
    '000001': bltz,
    '000110': blez,
    '000101': bne,
    '011010': div,
    '011011': divu,
    '001000': jr,
    '100010': sub,
    '000000': sll,
    '000100': sllv,
    '101010': slt,
    '100011': subu,
}

