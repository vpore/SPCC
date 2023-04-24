digits = "1234567890"
chars = "abcdefghijklmnopqrstuvwxyz"
operators = "+*/-="
separators = ',;'
keywords = ['int','float','bool','string','char','new','if','public']

TK_KEYWORD = 'KEYWORD'
TK_OPERATOR = 'OPERATOR'
TK_IDENTIFIER = 'IDENTIFIER'
TK_SEP = 'SEPARATOR'
TK_CONST  = 'CONSTANT'

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f'{self.type}:{self.value}'

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pointer = 0
        self.length = len(text)
        self.tokens = []
        self.current_char = self.text[self.pointer]
        # self.is_identifier = False
    
    def forward(self):
        self.pointer+=1
        if(self.pointer<len(self.text)):
            self.current_char = self.text[self.pointer]

    def get_tokens(self):
        while(self.pointer!=self.length):
            if(self.current_char=='\n'):
                break
            elif(self.current_char in digits):
                self.tokens.append(self.get_number())
            elif(self.current_char in operators):
                self.tokens.append(Token(type=TK_OPERATOR,value=self.current_char))
                # if(self.is_identifier==True):
                #     self.is_identifier=False
                self.forward()
            elif(self.current_char in chars):
                # if(self.is_identifier==True):
                #     self.is_identifier = False
                #     self.tokens.append(self.get_identifier())
                # else:
                self.tokens.append(self.get_word())
            elif(self.current_char in separators):
                self.tokens.append(Token(type=TK_SEP,value=self.current_char))
                self.forward()
            else:
                self.forward()
        return self.tokens

    def get_number(self):
        num_value = ""
        dot_count = 0
        try:
            while(self.current_char in digits):
                num_value+=self.current_char
                self.forward()
                if(self.current_char=='.' and dot_count<1):
                    dot_count+=1
                    num_value+=self.current_char
                    self.forward()
        except:
            pass
        return Token(type=TK_CONST, value=num_value)
    
    # def get_identifier(self):
    #     value = ""
    #     while(self.current_char in chars + digits + '_'):
    #         value+=self.current_char
    #         self.forward()
    #     return Token(type=TK_IDENTIFIER, value=value)
    
    def get_word(self):
        word_value = ""
        try:
            while(self.current_char in chars):
                word_value+=self.current_char
                self.forward()
        except:
            pass
        if(word_value in keywords):
            # self.is_identifier = True
            return Token(type=TK_KEYWORD, value=word_value)
        else:
            return Token(type=TK_IDENTIFIER, value=word_value)