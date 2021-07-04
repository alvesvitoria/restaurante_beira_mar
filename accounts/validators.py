def cpf_validator(cpf):
    cpf = cpf.replace('.', '')
    cpf = cpf.replace('-', '')

    if len(cpf) == 11 and cpf.isdigit() and cpf[0] * 11 != cpf:
        cpf_gerado = cpf[:-2]

        soma = 0
        for i, mult in enumerate(range(10, 1, -1)):
            num = int(cpf[i])
            soma += num * mult

        temp = 11 - (soma % 11)
        cpf_gerado += str(temp) if temp <= 9 else '0'

        soma = 0
        for i, mult in enumerate(range(11, 1, -1)):
            num = int(cpf[i])
            soma += num * mult

        temp = 11 - (soma % 11)
        cpf_gerado += str(temp) if temp <= 9 else '0'

        if cpf_gerado == cpf:
            return True
    return False
