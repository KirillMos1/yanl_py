import lexer, parser, vm
code = ""

print("Enter code (write ; for stop)")
while ((line := input("> ")) != ";"):
    code += line

lexed = lexer.lex(code)
for token, pos in enumerate(lexed, 1):
    print("-----------------------------\n")
    print(f"Token NO  | {pos}")
    print(f"Type:     | {token.type.__str__()}")
    print(f"Value     | {token.value}")
    print(f"Position: | {token.line}|{token.pos}")
print("-----------------------------\n")