import re  # Módulo de expressões regulares para dividir por '-' e '_' (um ou mais)

def to_camel_case(s: str) -> str:
    """
    Converte uma string com palavras separadas por '-' e/ou '_' para camelCase/PascalCase.
    Regra:
      - A primeira palavra só começa com maiúscula se a string original começar com maiúscula (PascalCase).
      - As demais palavras sempre começam com maiúscula.
    Exemplos:
      "the-stealth-warrior"   -> "theStealthWarrior"
      "The_Stealth_Warrior"   -> "TheStealthWarrior"
      "The_Stealth-Warrior"   -> "TheStealthWarrior"
    """
    # Caso base: string vazia retorna vazio
    if not s:
        return ""

    # Descobre se a primeira letra da string original é maiúscula (para decidir camel vs. Pascal)
    keep_pascal = s[0].isupper()

    # Divide a string por um ou mais '-' ou '_' (regex com '+')
    # Ex.: "the__stealth--warrior" -> ["the", "stealth", "warrior"]
    parts = re.split(r'[-_]+', s)

    # Primeira palavra (pode ser vazia em casos extremos, mas normalmente não é)
    first = parts[0]
    if first:
    
        # Se o texto original começa com maiúscula, fazemos PascalCase na primeira palavra
        if keep_pascal:
            first = first[0].upper() + first[1:]
            
        # Caso contrário, camelCase: primeira letra minúscula
        else:
            first = first[0].lower() + first[1:]

    # Demais palavras: inicial sempre maiúscula
    rest = []
    for p in parts[1:]:
        if p:
            rest.append(p[0].upper() + p[1:])
        else:
            # Se houver entrada vazia por separadores repetidos, adiciona vazio (não afeta o join)
            rest.append("")

    # Junta tudo sem separadores
    return "".join([first] + rest)

