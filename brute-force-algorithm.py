import string

# Lista de possíveis caracteres para a senha
characters = string.ascii_letters + string.digits + string.punctuation

# Senha que queremos adivinhar
password = "abc123"

# Tentando todas as combinações possíveis
for i in range(1, len(characters) + 1):
    for combination in itertools.product(characters, repeat=i):
        guess = "".join(combination)
        if guess == password:
            print(f"Senha encontrada: {guess}")
            break
    else:
        continue
    break
print("Fim do processo.")
