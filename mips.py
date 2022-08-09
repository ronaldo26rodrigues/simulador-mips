import util

registradores = {
    0:  0,
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

memoria = {

}

# fazer as instruções aqui


def add(rd, rs1, rs2):
    rd = util.bin2dec(rd)
    rs1 = util.bin2dec(rs1)
    rs2 = util.bin2dec(rs2)
    registradores[rd] = registradores[rs1] + registradores[rs2]
    return None


def addi(rs, rt, imd):
    rs = util.bin2dec(rs)
    rt = util.bin2dec(rt)
    imd = util.bin2dec(imd)
    print(rs, rt, imd)
    registradores[rt] = registradores[rs] + imd
    return None


def addiu(rs, rt, imd):
    rs = util.bin2dec(rs)
    rt = util.bin2dec(rt)
    imd = util.bin2dec(imd)
    registradores[rt] = int(registradores[rs]) + int(imd)
    return None


def addu(rd, rs1, rs2):
    rd = util.bin2dec(rd)
    rs1 = util.bin2dec(rs1)
    rs2 = util.bin2dec(rs2)
    registradores[rd] = registradores[rs1] + registradores[rs2]
    return None


def andd(rd, rs1, rs2):
    rd = util.bin2dec(rd)
    rs1 = util.bin2dec(rs1)
    rs2 = util.bin2dec(rs2)
    registradores[rd] = (eval(bin(registradores[rs1]).zfill(32) +  '&' +  bin(registradores[rs2]).zfill(32)))
    return None


def andi(rs, rt, imd):
    rs = util.bin2dec(rs)
    rt = util.bin2dec(rt)
    imd = util.bin2dec(imd)
    registradores[rs] = (eval(bin(registradores[rt]).zfill(32) +  '&' +  bin(registradores[imd]).zfill(32)))
    return None


def bgtz(rs, rt, imd):
    rs = util.bin2dec(rs)
    rt = 0
    imd = util.bin2dec(imd)
    if(registradores[rs] > rt) : return registradores['pc'] + registradores[imd]
    return None


def beq(rs, rt, imd):
    rs = util.bin2dec(rs)
    rt = util.bin2dec(rt)
    imd = util.bin2dec(imd)
    print(registradores[rs], registradores[rt], imd, registradores['pc']+imd)
    if registradores[rs] == registradores[rt]:
        return registradores['pc'] + imd + 1
    return None


def bltz(rs, rt, imd):
    rs = util.bin2dec(rs)
    rt = 0
    imd = util.bin2dec(imd)
    if(registradores[rs] < rt): return registradores['pc'] + registradores[imd]
    return None


def blez(rs, rt, imd):
    rs = util.bin2dec(rs)
    rt = 0
    imd = util.bin2dec(imd)
    if registradores[rs] <= rt: return registradores['pc'] + registradores[imd]
    return None


def bne(rs, rt, imd):
    rs = util.bin2dec(rs)
    rt = 0
    imd = util.bin2dec(imd)
    if registradores[rs] != rt: return registradores['pc'] + registradores[imd]
    return None


def div(rs1, rs2):
    rs1 = util.bin2dec(rs1)
    rs2 = util.bin2dec(rs2)
    registradores['hi'] = registradores[rs1] % registradores[rs2]
    registradores['lo'] = registradores[rs1] // registradores[rs2]
    return None


def divu(rs1, rs2):
    rs1 = util.bin2dec(rs1)
    rs2 = util.bin2dec(rs2)
    registradores['hi'] = registradores[rs1] % registradores[rs2]
    registradores['lo'] = registradores[rs1] // registradores[rs2]
    return None


def j(jta):
    return util.address2index(jta)


def jal(jta):
    registradores[31] = registradores['pc'] + 1
    return util.address2index(jta)+1


def sll(rd, rs1, rs2):
    rd = util.bin2dec(rd)
    rs1 = util.bin2dec(rs1)
    rs2 = util.bin2dec(rs2)
    registradores[rd] = registradores[rs1] >> registradores[rs2]
    return None


def sllv(rd, rs1, rs2):
    rd = util.bin2dec(rd)
    rs1 = util.bin2dec(rs1)
    rs2 = util.bin2dec(rs2)
    registradores[rd] = registradores[rs1] >> registradores[rs2]
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


def slti(rs, rt, imd):
    rs = util.bin2dec(rs)
    rt = 0
    imd = util.bin2dec(imd)
    if registradores[rt] < [imd]:
        registradores[rs] = 1
    else:
        registradores[rs] = 0
    return None


def sra(rd, rs1, rs2):
    rd = util.bin2dec(rd)
    rs1 = util.bin2dec(rs1)
    rs2 = util.bin2dec(rs2)
    if registradores[rs2] > registradores[rs1]:
        registradores[rd] = 1
    return None

def srav(rd, rs1, rs2):
    rd = util.bin2dec(rd)
    rs1 = util.bin2dec(rs1)
    rs2 = util.bin2dec(rs2)
    if registradores[rs2] >> [rs2]:
        registradores[rd] = 1
    return None


def srl(rd, rs1, rs2):
    rd = util.bin2dec(rd)
    rs1 = util.bin2dec(rs1)
    rs2 = util.bin2dec(rs2)
    registradores[rd] = registradores[rs1] << registradores[rs2]
    return None


def srlv(rd, rs1, rs2):
    rd = util.bin2dec(rd)
    rs1 = util.bin2dec(rs1)
    rs2 = util.bin2dec(rs2)
    registradores[rd] = registradores[rs1] >> registradores[rs2]
    return None


def sub(rd, rs1, rs2):
    rd = util.bin2dec(rd)
    rs1 = util.bin2dec(rs1)
    rs2 = util.bin2dec(rs2)
    registradores[rd] = registradores[rs1] - registradores[rs2]
    return None


def subu(rd, rs1, rs2):
    rd = util.bin2dec(rd)
    rs1 = util.bin2dec(rs1)
    rs2 = util.bin2dec(rs2)
    registradores[rd] = registradores[rs1] - registradores[rs2]
    return None

def sw(rs, rt, imd):
    rs = util.bin2dec(rs)
    rt = 0
    imd = util.bin2dec(imd)
    registradores[rs] = registradores[rt] + 10
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
    rs = util.bin2dec(rs)
    rt = util.bin2dec(rt)
    registradores[rt] = (eval(bin(registradores[rs]) + " | " + imd))
    return None


def nor(rd, rs1, rs2):
    rd = util.bin2dec(rd)
    rs1 = util.bin2dec(rs1)
    rs2 = util.bin2dec(rs2)
    registradores[rd] = (eval("~"+bin(registradores[rs1]) + " & ~" + bin(registradores[rs2])))


def xor(rd, rs1, rs2):
    rd = util.bin2dec(rd)
    rs1 = util.bin2dec(rs1)
    rs2 = util.bin2dec(rs2)
    registradores[rd] = (eval(bin(registradores[rs1]) + '^' + bin(registradores[rs2])))
    return None


def xori(rs, rt, imd):
    rs = util.bin2dec(rs)
    rt = util.bin2dec(rt)
    imd = util.bin2dec(imd)
    registradores[rs] = (eval(bin(registradores[rt]).zfill(32) +  '^' +  bin(registradores[imd]).zfill(32)))
    return None


def lui(rs, rt, imd):
    rs = util.bin2dec(rs)
    rt = util.bin2dec(rt)
    imd = util.bin2dec(imd + '0'*(32-len(imd)))
    registradores[1] = imd
    return None


def lw(rs, rt, imd):
    rs = util.bin2dec(rs)
    rt = util.bin2dec(rt)
    imd = util.bin2dec(imd)
    registradores[rt] = memoria[str(registradores[rs]+imd)]
    return None


def lb(rs, rt, imd):
    rs = util.bin2dec(rs)
    rt = util.bin2dec(rt)
    imd = util.bin2dec(imd)
    b = memoria[str(registradores[rs]+imd)]
    registradores[rt] = b[0]*(32-len(b)) + b
    return None


def lbu(rs, rt, imd):
    rs = util.bin2dec(rs)
    rt = util.bin2dec(rt)
    imd = util.bin2dec(imd)
    b = memoria[str(registradores[rs]+imd)]
    registradores[rt] = '0'*(32-len(b)) + b
    return None


def sb(rs, rt, imd):
    rs = util.bin2dec(rs)
    rt = util.bin2dec(rt)
    imd = util.bin2dec(imd)
    memoria[str(registradores[rs]+imd)] = registradores[rt]
    return None


def syscall(a, b, c):
    syscalls[registradores[2]]()
    return None

def print_integer():
    print(int(registradores[4]))
    return None

def read_integer():
    registradores[2] = int(input())
    return None

def read_memory():
    txt = ''
    r = registradores[4]
    offset = 0
    atual = ''
    while '00' not in atual:
        atual = util.dec2hex(memoria[str(int(r + offset))])
        txt += util.hex2ascii(atual)
        offset += 4
        atual = util.dec2hex(memoria[str(int(r + offset))])
    txt += util.hex2ascii(atual[(str(atual).rfind('0') + 1):])
    return txt


def print_string():
    print(read_memory())
    return None

syscalls = {
    1: print_integer,
    4: print_string
}


opcode = {
    '001000': addi,
    '001001': addiu,
    '001100': andi,
    '000111': bgtz,
    '000100': beq,
    '000001': bltz,
    '000110': blez,
    '000101': bne,
    '000010': j,
    '000011': jal,
    '001101': ori,
    '001110': xori,
    '001111': lui,
    '100011': lw,
    '100000': lb,
    '100100': lbu,
    '101011': sw,
    '001010': slti
}

functions = {
    '100000': add,
    '100001': addu,
    '100100': andd,
    '011010': div,
    '011011': divu,
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
    '100110': xor,
    '000011': sra,
    '000111': srav,
    '000010': srl,
    '000110': srlv,
    '001100': syscall
    
}

