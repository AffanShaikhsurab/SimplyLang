import string
import unicodedata

TT_INT = "INT"
TT_DOUBLE = "DOUBLE"
TT_ADD = "ADD"
TT_MUL = "MUL"
TT_DIV = "DIV"
TT_BOOL = "BOOL"
TT_MINUS = "MINUS"
TT_LP = "LP"  # Left parentheses
TT_RP = "RP"  # Right parentheses
TT_STOP = "STOP"
TT_EOF = "EOF"
TT_POW = "POW"
TT_MOD = "MOD"
TT_LT = "LT"
TT_GT = "GT"
TT_COLON = "COLON"

TT_STRING = "STRING"
TT_NOT_EQUAL = "NOT_EQUAL"
TT_LBRACKET = "LBRACKET"
TT_RBRACKET = "RBRACKET"
TT_NEWLINE = "NEWLINE"
##Constants
DIGITS = "0123456789"
LETTERS = string.ascii_letters
LETTER_DIGITS = LETTERS + DIGITS
TT_IDENTIFIER = "IDENTIFIER"
TT_EQ = "EQ"
TT_KEYWORD = "KEYWORD"
TT_EQUAL = "EQUAL"
TT_COMMA = "COMMA"


KEYWORDS = {
    "show": TT_KEYWORD,
    "is": TT_KEYWORD,
    "if": TT_KEYWORD,
    "Note": TT_KEYWORD,
    "then": TT_KEYWORD,
    "otherwise": TT_KEYWORD,
    "equals": TT_KEYWORD,
    "till": TT_KEYWORD,
    "do": TT_KEYWORD,
    "check": TT_KEYWORD,
    "tell": TT_KEYWORD,
    "what's": TT_KEYWORD,
    "its": TT_KEYWORD,
    "does": TT_KEYWORD,
    "try": TT_KEYWORD,
    "oops": TT_KEYWORD,
    "get": TT_KEYWORD,
    "you": TT_KEYWORD,
    "see": TT_KEYWORD,
    "in": TT_KEYWORD,
    "Robo": TT_KEYWORD,
    "repeat": TT_KEYWORD,
    "times": TT_KEYWORD,
    "say": TT_KEYWORD,
    "create": TT_KEYWORD,
    "with": TT_KEYWORD,
    "at": TT_KEYWORD,
    "arrange": TT_KEYWORD,
    "ascending": TT_KEYWORD,
    "descending": TT_KEYWORD,
    "length": TT_KEYWORD,
    "of": TT_KEYWORD,
    "stop": TT_KEYWORD,
    "return": TT_KEYWORD,
    "contract": TT_KEYWORD,
    "call": TT_KEYWORD,
}

EMOJI_PATTERN = r"[\U0001F300-\U0001F9FF]|[\u2600-\u26FF\u2700-\u27BF]"


##Position
class Position:
    def __init__(self, index, line, column, filename, text):
        self.index = index
        self.line = line
        self.column = column
        self.filename = filename
        self.text = text

    def advance(self, current_char=None):
        self.index += 1
        self.column += 1

        if current_char == "\n":
            self.line += 1
            self.column = 0

        return self

    def copy(self):
        return Position(self.index, self.line, self.column, self.filename, self.text)


class Error:
    def __init__(self, error_msg, error_type, start, end):
        self.msg = error_msg
        self.type = error_type
        self.start = start
        self.end = end

    def print(self) -> str:
        result = f"{self.type}: {self.msg}\n"
        result += f"File {self.start.filename}, line {self.start.line + 1}, column {self.start.column + 1}\n"
        result += f"{self.start.text.splitlines()[self.start.line]}\n"
        result += " " * self.start.column + "^"
        return result


class IllegalCharError(Error):
    def __init__(self, error_msg, start, end):
        super().__init__(error_msg, "Illegal character", start, end)


class IllegalOperationError(Error):
    def __init__(self, error_msg, start, end, context=None):
        super().__init__(error_msg, "Runtime Error", start, end)
        self.context = context

    def print(self) -> str:
        result = self.generate_traceback()
        result += f"{self.type}: {self.msg}\n"
        result += f"{self.start.text.splitlines()[self.start.line]}\n"
        result += " " * self.start.column + "^"
        return result

    def generate_traceback(self):
        result = ""
        pos = self.start
        context = self.context
        while context:
            result += (
                f"File {pos.filename}, line {pos.line + 1}, in  {context.display_name}\n"
                + result
            )
            pos = context.parent_entry_pos
            context = context.parent
        return "Traceback (most recent call last): \n" + result


class InvalidSyntaxError(Error):
    def __init__(self, error_msg, start, end):
        super().__init__(error_msg, "Illegal syntax", start, end)


class Token:
    def __init__(self, type, value=None, start=None, end=None):
        self.type = type
        self.value = value

        if start:
            self.start = start.copy()
            self.end = start.copy()
            self.end.advance()
        if end:
            self.end = end.copy()

    def matches(self, type, value):
        return self.type == type and self.value == value

    def __repr__(self) -> str:
        return f"{self.value , self.type}"


class Lex:
    def __init__(self, text, filename):
        self.text = text
        self.pos = Position(-1, 0, -1, filename, text)
        self.current = None
        self.tokens = []
        self.filename = filename
        self.iterate()

    def iterate(self):
        self.pos.advance(self.current)  # Pass current char to track newlines
        self.current = (
            self.text[self.pos.index] if self.pos.index < len(self.text) else None
        )

    def create_token(self):
        while self.current is not None:
            if self.current in " \t":
                self.iterate()

            elif self.current == "\n":
                self.tokens.append(Token(TT_NEWLINE, TT_NEWLINE, start=self.pos))
                self.iterate()

            elif self.current == "+":
                self.tokens.append(Token(TT_ADD, "+", start=self.pos))
                self.iterate()

            elif self.current in LETTERS:
                self.tokens.append(self.make_identifier())

            elif self.current == "-":
                self.tokens.append(Token(TT_MINUS, "-", start=self.pos))
                self.iterate()

            elif self.current == "*":
                self.tokens.append(Token(TT_MUL, "*", start=self.pos))
                self.iterate()

            elif self.current == '"':
                self.tokens.append(Token(TT_STRING, "'", start=self.pos))
                self.iterate()
            elif self.current == ":":
                self.tokens.append(Token(TT_COLON, ":", start=self.pos))
                self.iterate()
            elif self.current == "/":
                self.tokens.append(Token(TT_DIV, "/", start=self.pos))
                self.iterate()

            elif self.current == "^":
                self.tokens.append(Token(TT_POW, "^", start=self.pos))
                self.iterate()

            elif self.current == "%":
                self.tokens.append(Token(TT_MOD, "%", start=self.pos))
                self.iterate()

            elif self.current == "(":
                self.tokens.append(Token(TT_LP, "(", start=self.pos))
                self.iterate()

            elif self.current == ")":
                self.tokens.append(Token(TT_RP, ")", start=self.pos))
                self.iterate()

            elif self.current == "<":
                self.tokens.append(Token(TT_LT, "<", start=self.pos))
                self.iterate()

            elif self.current == ",":
                self.tokens.append(Token(TT_COMMA, ",", start=self.pos))
                self.iterate()
            elif self.current == ">":
                self.tokens.append(Token(TT_GT, ">", start=self.pos))
                self.iterate()
            elif self.current == "[":
                self.tokens.append(Token(TT_LBRACKET, "[", start=self.pos))
                self.iterate()
            elif self.current == "!":
                self.tokens.append(Token(TT_IDENTIFIER, "!", start=self.pos))
                self.iterate()
            elif self.current == "]":
                self.tokens.append(Token(TT_RBRACKET, "]", start=self.pos))
                self.iterate()
            elif self.current == ".":
                self.tokens.append(Token(TT_STOP, ".", start=self.pos))
                self.iterate()
                continue
            elif self.current in DIGITS:
                self.tokens.append(self.create_number())
            elif self.current == "=":
                self.tokens.append(Token(TT_IDENTIFIER, "=", start=self.pos))
                self.iterate()
                continue
            else:
                start = self.pos.copy()
                cur = self.current
                self.iterate()
                return [], IllegalCharError(cur, self.pos, start)
        self.tokens.append(Token(TT_EOF, TT_EOF, start=self.pos))
        return self.tokens, None

    def create_number(self):
        num_str = ""
        dot_count = 0
        pos_start = self.pos.copy()
        while self.current is not None and (
            self.current.isdigit() or self.current == "."
        ):
            if self.current == ".":
                dot_count += 1
                if dot_count > 1:
                    break
            num_str += self.current
            self.iterate()

        if dot_count == 0:
            return Token(TT_INT, int(num_str), pos_start, self.pos)
        else:
            return Token(TT_DOUBLE, float(num_str), pos_start, self.pos)

    def make_identifier(self):
        id_str = ""
        pos_start = self.pos.copy()
        id_str = self.create_identifier()
        if id_str == "equals":
            return Token(TT_EQUAL, TT_EQUAL, pos_start, self.pos)
        elif id_str == "true":
            return Token(TT_BOOL, True, pos_start, self.pos)
        elif id_str == "false":
            return Token(TT_BOOL, False, pos_start, self.pos)

        if all(self.is_emoji(c) for c in id_str):
            return Token("EMOJI", id_str, pos_start, self.pos)
        elif id_str == "not":
            id_str = self.create_identifier()
            if id_str == "equals":
                return Token(TT_NOT_EQUAL, TT_NOT_EQUAL, pos_start, self.pos)
            else:
                self.tokens.append(Token(TT_IDENTIFIER, "not", pos_start, self.pos))
                return Token(TT_IDENTIFIER, id_str, pos_start, self.pos)
        elif id_str in KEYWORDS:
            return Token(TT_KEYWORD, id_str, pos_start, self.pos)
        else:
            return Token(TT_IDENTIFIER, id_str, pos_start, self.pos)

    def create_identifier(self):
        id_str = ""
        while self.current is not None and self.current in " \t":
            self.iterate()
        while self.current is not None and (
            self.current in LETTER_DIGITS + "_" or self.is_emoji(self.current)
        ):
            id_str += self.current
            self.iterate()
        return id_str

    def is_emoji(self, char):
        if char is None:
            return False
        # Two ways to check if character is emoji:
        return unicodedata.category(char).startswith("So") or any(
            0x1F300 <= ord(c) <= 0x1F9FF for c in char
        )


def generate(filename):
    with open(filename) as f:
        text = f.read()
    lexer = Lex(text, filename)
    tokens, error = lexer.create_token()
    # print(tokens)
    return tokens, error
