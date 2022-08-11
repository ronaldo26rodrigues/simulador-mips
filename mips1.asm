.data
nome: .space 20
sobrenome: .space 20
digite: .asciiz "digite "

.text
jal print

li $v0, 8
la $a0, nome
li $a1, 20
syscall
jal print
li $v0, 8
la $a0, sobrenome
syscall
li $v0, 4
la $a0, nome
syscall
la $a0, sobrenome
syscall

j end

print: 
li $v0, 4
la $a0, digite
syscall
jr $ra

end:
