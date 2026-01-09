class TokenType:
    def __init__(self, typeid: int):
        self.typeid = typeid
    def __str__(self):
        match (self.typeid):
            case 00:
                return "NEWLINE (\\n)"
            case 01:
                return "TABULATION (\\t)"
            case 02:
                return "VERTICAL TABULATION (\\v)"
            case 03:
                return "CURSOR RETURN (\\r)"
            case 10:
                return "PRINT"
            case 11:
                return "INPUT"
            case 12:
                return "VAR"
            case 13:
                return "INT"
            case 14:
                return "DOUBLE"
            case 15:
                return "BYTE"
            case 20:
                return "PLUS"
            case 21:
                return "MINUS"
            case 22:
                return "STAR"
            case 23:
                return "EQUAL"
            case 24:
                return "EQUALS"

class Token:
    def __init__(self : Token, type : TokenType, value : str, line : int, pos : int) -> None:
        self.type = type
        self.value = value
        self.line = line
        self.pos = pos