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
    return None


def sub(rd, rs1, rs2):
    rd = util.bin2dec(rd)
    rs1 = util.bin2dec(rs1)
    rs2 = util.bin2dec(rs2)
    registradores[rd] = registradores[rs1] - registradores[rs2]
    return None


def jal(jta):
    registradores['ra'] = registradores['pc'] + 1
    return util.address2index(jta)


def sll(rd, rs1, rs2):
    rd = util.bin2dec(rd)
    rs1 = util.bin2dec(rs1)
    rs2 = util.bin2dec(rs2)
    registradores[rd] = registradores[rs1] << registradores[rs2]
    return None


def sllv(rd, rs1, rs2):
    rd = util.bin2dec(rd)
    rs1 = util.bin2dec(rs1)
    rs2 = util.bin2dec(rs2)
    registradores[rd] = registradores[rs1] << registradores[rs2]
    return None


def jr(rd, rs1, rs2):
    rd = util.bin2dec(rd)
    rs1 = util.bin2dec(rs1)
    rs2 = util.bin2dec(rs2)
    return registradores[rs2]


def slt(rd, rs1, rs2):
    rd = util.bin2dec(rd)
    rs1 = util.bin2dec(rs1)
    rs2 = util.bin2dec(rs2)
    if registradores[rs2] < [rs2]:
        registradores[rd] = 1
    return None


def subu(rd, rs1, rs2):
    rd = util.bin2dec(rd)
    rs1 = util.bin2dec(rs1)
    rs2 = util.bin2dec(rs2)
    registradores[rd] = registradores[rs1] - registradores[rs2]
    return None


def mult(rd, rs1, rs2):
    rd = util.bin2dec(rd)
    rs1 = util.bin2dec(rs1)
    rs2 = util.bin2dec(rs2)
    registradores['lo'] = registradores[rd] * registradores[rs1]
    return None


def multu(rd, rs1, rs2):
    rd = util.bin2dec(rd)
    rs1 = util.bin2dec(rs1)
    rs2 = util.bin2dec(rs2)
    registradores['lo'] = registradores[rd] * registradores[rs1]
    return None


def mfhi(rd, rs1, rs2):
    rd = util.bin2dec(rd)
    rs1 = util.bin2dec(rs1)
    rs2 = util.bin2dec(rs2)
    registradores[rd] = registradores['hi']
    return None


def mflo(rd, rs1, rs2):
    rd = util.bin2dec(rd)
    rs1 = util.bin2dec(rs1)
    rs2 = util.bin2dec(rs2)
    registradores[rd] = registradores['lo']
    return None


def m_or(rd, rs1, rs2):
    rd = util.bin2dec(rd)
    rs1 = util.bin2dec(rs1)
    rs2 = util.bin2dec(rs2)
    registradores[rd] = (eval(bin(registradores[rs1]).zfill(32) + "|" + bin(registradores[rs2]).zfill(32)))
    return None


def ori(rs, rt, imd):
    rd = util.bin2dec(rs)
    rs1 = util.bin2dec(rt)
    registradores[rs] = (eval(bin(registradores[rt]).zfill(32) + "|" + imd))
    return None


def nor(rd, rs1, rs2):
    rd = util.bin2dec(rd)
    rs1 = util.bin2dec(rs1)
    rs2 = util.bin2dec(rs2)
    registradores[rd] = (eval("~"+bin(registradores[rs1]).zfill(32) + "& ~" + bin(registradores[rs2]).zfill(32)))
    return None


opcode = {
    '000011': jal,
    '001101': ori,
}

functions = {
    '100000': add,
    '001000': jr,
    '100010': sub,
    '000000': sll,
    '000100': sllv,
    '101010': slt,
    '100011': subu,
    '010000': mfhi,
    '010010': mflo,
    '011000': mult,
    '100111': nor,
    '100101': m_or,
    '011001': multu,

}

