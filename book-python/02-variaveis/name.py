LINE = "\n\n#############---LINE---#############\n\n"

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print('This is a string with title'.title())
print("This is a string with upper case".upper())
print("This is a string with lower case".lower())
print(f"Hello, {full_name.title()}!")

# tabulacao em python

print("\tPython")

# tabulacao e qubra de linha

print(LINE)

print("Algumas linguagens de programacao:\n\tJava\n\tCobol\n\tPerl\n\tC++")

print(LINE)

print("remocao de espacos em branco")

print("           remove da esquerda".lstrip())
print("remove da direita            ".rstrip())
print("  remove de ambos os lados   ".strip())

# remocao de prefixo
print(LINE)

print("removendo prefixo [https://]:")

url = "https://labs.nercode.com.br"
print(url.removeprefix("https://"))

url2 = url + "/api/v1"
print(url2.removesuffix("/api/v1"))

