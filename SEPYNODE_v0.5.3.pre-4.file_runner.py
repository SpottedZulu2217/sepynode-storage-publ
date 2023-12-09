class Basic:
    color_codes = [
        "\033[30m",  # Black 0
        "\033[31m",  # Red 1
        "\033[32m",  # Green 2
        "\033[33m",  # Yellow 3
        "\033[34m",  # Blue 4
        "\033[35m",  # Magenta 5
        "\033[36m",  # Cyan 6
        "\033[0m",  # White 7
        "\033[0m"  # Reset 8
    ]
    vars_ = []

    def run(self, txt):
        self.and_len = 0
        self.or_len = 0
        self.statements_len = 0
        self.tokens_len1 = 0
        self.tokens_len2 = 0
        self.var_1 = 0
        self.list_worlds = []
        self.chater = str(txt)
        self.i_k = 0
        self.i_p = 0
        self.chater = self.chater + " "
        for i in range(len(self.chater)):
            try:
                if self.chater[i] == '"' and self.i_k == 1 and not self.i_p != 0:
                    self.list_worlds.append([self.chater[self.var_1:i], "str"])
                    self.var_1 = i + 1
                    self.i_k = 0
                elif self.chater[i] == '"' and not self.i_p != 0:
                    self.list_worlds.append(self.chater[self.var_1:i])
                    self.var_1 = i + 1
                    self.i_k = 1
                if self.chater[i] == ' ' and not self.i_p != 0:
                    if not self.i_k:
                        self.list_worlds.append(self.chater[self.var_1:i])
                        self.var_1 = i + 1
                if self.chater[i] == '}' and self.i_p > 0 and not self.i_k:
                    if self.i_p > 1:
                        self.list_worlds.append([self.chater[self.var_1:i+self.i_p*2], "statement"])
                        self.var_1 = i + 1
                        self.i_p -= 1
                    else:
                        self.list_worlds.append([self.chater[self.var_1:i], "statement"])
                        self.var_1 = i + 1
                        self.i_p -= 1
                elif self.chater[i] == '{' and not self.i_k:
                    if self.i_p == 0:
                        self.list_worlds.append(self.chater[self.var_1:i])
                        self.var_1 = i + 1
                    self.i_p += 1
            except:
                pass

        for i in range(len(self.list_worlds)):
            try:
                if self.list_worlds[i-1] == "and":
                    self.and_len += 1
            except:
                pass

        for i in range(len(self.list_worlds)):
            try:
                if self.list_worlds[i-1] == "or":
                    self.or_len += 1
            except:
                pass

        for i in range(len(self.list_worlds)):
            if self.is_int(self.list_worlds[i-1]):
                    self.list_worlds[i-1] = [str(self.list_worlds[i-1]), "int"]
            elif self.list_worlds[i-1] in ["true", "false"]:
                self.list_worlds[i-1] = [self.list_worlds[i-1], "bool"]

        for i in range(len(self.list_worlds)):
            if self.list_worlds[i-1] in ["+", "-"]:
                self.tokens_len1 += 1
            elif self.list_worlds[i-1] in ["*", "/"]:
                self.tokens_len2 += 1

        i = 1
        while i < len(self.list_worlds):
            if self.list_worlds[i - 1] == '':
                del self.list_worlds[i - 1]
            else:
                i += 1

        for i in range(len(self.list_worlds)):
            for x in range(len(self.vars_)):
                if self.list_worlds[i-1] == self.vars_[x-1][0]:
                    try:
                        if not self.list_worlds[i] == "=" and not self.list_worlds[i-2] == "del" and not self.list_worlds[i-2] == "res":
                            self.list_worlds[i-1] = self.vars_[x-1][1]
                    except IndexError:
                        self.list_worlds[i-1] = self.vars_[x-1][1]
        for i in range(len(self.list_worlds)):
            try:
                if self.list_worlds[i-1] == "str":
                    if self.list_worlds[i] == "<":
                        self.list_worlds[i-1] = [self.list_worlds[i+1][0], "str"]
                        del self.list_worlds[i]
                        del self.list_worlds[i]
            except:
                pass

        for i in range(len(self.list_worlds)):
            try:
                if self.list_worlds[i-1] == "int":
                    if self.list_worlds[i] == "<":
                        try:
                            self.list_worlds[i-1] = [self.list_worlds[i+1][0], "int"]
                            del self.list_worlds[i]
                            del self.list_worlds[i]
                        except:
                            pass
            except:
                pass

        for i in range(len(self.list_worlds)):
            try:
                if self.list_worlds[i-1] == "bool":
                    if self.list_worlds[i] == "<":
                        if self.list_worlds[i-1] in ["true", "false"]:
                            try:
                                self.list_worlds[i-1] = [self.list_worlds[i+1][0], "bool"]
                                del self.list_worlds[i]
                                del self.list_worlds[i]
                            except:
                                pass
            except:
                pass

        for i in range(len(self.list_worlds)):
            for x in range(self.tokens_len2):
                try:
                    if self.list_worlds[i][1] == "int":  # *
                        if self.list_worlds[i + 1] == "*":
                            if self.list_worlds[i + 2][1] == "int":
                                print("INT:" + str(self.list_worlds[i][0]) + " TOKEN:* " + "INT:" + str(
                                    self.list_worlds[i + 2][0]))
                                print("result:"+str(round(float(self.list_worlds[i][0]) * float(self.list_worlds[i + 2][0]), 16)))
                                self.list_worlds[i] = [str(round(float(self.list_worlds[i][0]) * float(self.list_worlds[i + 2][0]), 16)), "int"]
                                del self.list_worlds[i + 1]
                                del self.list_worlds[i + 1]
                                print(self.list_worlds)
                except:
                    pass
                try:
                    if self.list_worlds[i][1] == "int":  # /
                        if self.list_worlds[i + 1] == "/":
                            if self.list_worlds[i + 2][1] == "int":
                                print("INT:" + str(self.list_worlds[i][0]) + " TOKEN:/ " + "INT:" + str(
                                    self.list_worlds[i + 2][0]))
                                print("result:"+str(round(float(self.list_worlds[i][0]) / float(self.list_worlds[i + 2][0]), 16)))
                                self.list_worlds[i] = [str(round(float(self.list_worlds[i][0]) / float(self.list_worlds[i + 2][0]), 16)), "int"]
                                del self.list_worlds[i + 1]
                                del self.list_worlds[i + 1]
                                print(self.list_worlds)
                except:
                    pass
            try:
                if self.list_worlds[i - 1] == "help":
                    print("Warning:before and after every word or symbol you need to add a space\nVARS: to create a var type \"var \"+the name of the var.\nIf you want to change the value of the var then type the name of the var + \" = \" and there put the new value that you want.\nIf you want to delete a var then type \"del \"+ the name of the var that you want to delete.\nIf you want to reset a var to 0 then type\"res \"+ the name of the var that you want to reset.")
            except:
                pass

        for i in range(len(self.list_worlds)):
            for x in range(self.tokens_len1):
                try:
                    if self.list_worlds[i][1] == "int":  # +
                        if self.list_worlds[i + 1] == "+":
                            if self.list_worlds[i + 2][1] == "int":
                                print("INT:" + str(self.list_worlds[i][0]) + " TOKEN:+ " + "INT:" + str(
                                    self.list_worlds[i + 2][0]))
                                print("result:"+str(round(float(self.list_worlds[i][0]) + float(self.list_worlds[i + 2][0]), 16)))
                                self.list_worlds[i] = [str(round(float(self.list_worlds[i][0]) + float(self.list_worlds[i + 2][0]), 16)), "int"]
                                del self.list_worlds[i + 1]
                                del self.list_worlds[i + 1]
                                print(self.list_worlds)
                            elif self.list_worlds[i + 2][1] == "str":
                                self.error = f"TypeError at \"{self.list_worlds[i+2][0]}\":int can only be added with int"
                                import sys
                                print(f"\033[91m{self.error}\033[0m")
                    elif self.list_worlds[i][1] == "str": #+(str)
                        if self.list_worlds[i + 1] == "+":
                            if self.list_worlds[i + 2][1] == "str":
                                print("STR:" + str(self.list_worlds[i][0]) + " TOKEN:+ " + "STR:" + str(
                                    self.list_worlds[i + 2][0]))
                                print("result:"+str(str(self.list_worlds[i][0]) + str(self.list_worlds[i + 2][0])))
                                self.list_worlds[i] = [str(self.list_worlds[i][0])+str(self.list_worlds[i + 2][0]), "str"]
                                del self.list_worlds[i + 1]
                                del self.list_worlds[i + 1]
                                print(self.list_worlds)
                            else:
                                self.error = f"TypeError at \"{self.list_worlds[i+2][0]}\":str can only be added with str"
                                import sys
                                print(f"\033[91m{self.error}\033[0m")

                except:
                    pass
                try:
                    if self.list_worlds[i][1] == "int":  # -
                        if self.list_worlds[i + 1] == "-":
                            if self.list_worlds[i + 2][1] == "int":
                                print("INT:" + str(self.list_worlds[i][0]) + " TOKEN:- " + "INT:" + str(self.list_worlds[i + 2][0]))
                                print("result:"+str(round(float(self.list_worlds[i][0]) - float(self.list_worlds[i + 2][0]), 16)))
                                self.list_worlds[i] = [str(round(float(self.list_worlds[i][0]) - float(self.list_worlds[i + 2][0]), 16)), "int"]
                                del self.list_worlds[i+1]
                                del self.list_worlds[i+1]
                                print(self.list_worlds)

                except:
                    pass
        for i in range(len(self.list_worlds)):
            try:
                if self.list_worlds[i - 1][1] == "str" and self.list_worlds[i + 1][1] == "str":
                    if self.list_worlds[i] == "==":
                        if str(self.list_worlds[i - 1]) == str(self.list_worlds[i + 1]):
                            self.list_worlds[i - 1] = ["true", "bool"]
                            del self.list_worlds[i]
                            del self.list_worlds[i]
                        else:
                            self.list_worlds[i - 1] = ["false", "bool"]
                            del self.list_worlds[i]
                            del self.list_worlds[i]
                    if self.list_worlds[i] == "!=":
                        if str(self.list_worlds[i - 1]) != str(self.list_worlds[i + 1]):
                            self.list_worlds[i - 1] = ["true", "bool"]
                            del self.list_worlds[i]
                            del self.list_worlds[i]
                        else:
                            self.list_worlds[i - 1] = ["false", "bool"]
                            del self.list_worlds[i]
                            del self.list_worlds[i]
                elif self.list_worlds[i - 1][1] == "int" and self.list_worlds[i + 1][1] == "int":
                    if self.list_worlds[i] == "==":
                        if float(self.list_worlds[i - 1][0]) == float(self.list_worlds[i + 1][0]):
                            self.list_worlds[i - 1] = ["true", "bool"]
                            del self.list_worlds[i]
                            del self.list_worlds[i]
                        else:
                            self.list_worlds[i - 1] = ["false", "bool"]
                            del self.list_worlds[i]
                            del self.list_worlds[i]
                    if self.list_worlds[i] == "<":
                        if float(self.list_worlds[i - 1][0]) < float(self.list_worlds[i + 1][0]):
                            self.list_worlds[i - 1] = ["true", "bool"]
                            del self.list_worlds[i]
                            del self.list_worlds[i]
                        else:
                            self.list_worlds[i - 1] = ["false", "bool"]
                            del self.list_worlds[i]
                            del self.list_worlds[i]
                    if self.list_worlds[i] == ">":
                        if float(self.list_worlds[i - 1][0]) > float(self.list_worlds[i + 1][0]):
                            self.list_worlds[i - 1] = ["true", "bool"]
                            del self.list_worlds[i]
                            del self.list_worlds[i]
                        else:
                            self.list_worlds[i - 1] = ["false", "bool"]
                            del self.list_worlds[i]
                            del self.list_worlds[i]
                    if self.list_worlds[i] == "!=":
                        if float(self.list_worlds[i - 1][0]) != float(self.list_worlds[i + 1][0]):
                            self.list_worlds[i - 1] = ["true", "bool"]
                            del self.list_worlds[i]
                            del self.list_worlds[i]
                        else:
                            self.list_worlds[i - 1] = ["false", "bool"]
                            del self.list_worlds[i]
                            del self.list_worlds[i]
                elif self.list_worlds[i - 1][1] == "bool" and self.list_worlds[i + 1][1] == "bool":
                    if self.list_worlds[i] == "==":
                        if self.list_worlds[i - 1][0] == self.list_worlds[i + 1][0]:
                            self.list_worlds[i - 1] = ["true", "bool"]
                            del self.list_worlds[i]
                            del self.list_worlds[i]
                        else:
                            self.list_worlds[i - 1] = ["false", "bool"]
                            del self.list_worlds[i]
                            del self.list_worlds[i]
            except:
                pass

        for i in range(len(self.list_worlds)):
            try:
                if self.list_worlds[i-1] == "not":
                    if self.list_worlds[i][1] == "bool":
                        if self.list_worlds[i][0] == "true":
                            self.list_worlds[i][0] = "false"
                            del self.list_worlds[i-1]
                        elif self.list_worlds[i][0] == "false":
                            self.list_worlds[i][0] = "true"
                            del self.list_worlds[i-1]
            except:
                pass

        while self.and_len != 0:
            for i in range(len(self.list_worlds)):
                try:
                    if self.list_worlds[i - 1] == "and":
                        self.and_len -= 1
                        if self.list_worlds[i] == ["true", "bool"]:
                            if self.list_worlds[i - 2] == ["true", "bool"]:
                                self.list_worlds[i - 2][0] = "true"
                                del self.list_worlds[i - 1]
                                del self.list_worlds[i - 1]
                            elif self.list_worlds[i - 2] == ["false", "bool"]:
                                self.list_worlds[i - 2][0] = "false"
                                del self.list_worlds[i - 1]
                                del self.list_worlds[i - 1]
                        elif self.list_worlds[i - 2] == ["false", "bool"]:
                            self.list_worlds[i - 2][0] = "false"
                            del self.list_worlds[i - 1]
                            del self.list_worlds[i - 1]
                except:
                    pass

        while self.or_len != 0:
            for i in range(len(self.list_worlds)):
                try:
                    if self.list_worlds[i - 1] == "or":
                        self.or_len -= 1
                        if self.list_worlds[1][1] == "bool":
                            if self.list_worlds[i - 2][1] == "bool":
                                if self.list_worlds[i - 2][0] == "true" or self.list_worlds[i][0] == "true":
                                    self.list_worlds[i - 2][0] = "true"
                                    del self.list_worlds[i - 1]
                                    del self.list_worlds[i - 1]
                                elif self.list_worlds[i - 2][0] == "false" and self.list_worlds[i][0] == "false":
                                    self.list_worlds[i - 2][0] = "false"
                                    del self.list_worlds[i - 1]
                                    del self.list_worlds[i - 1]
                except:
                    pass

        print(f"{self.list_worlds}words!")
        self.list_worlds_for_print = self.list_worlds + ["", ""]  # this is needed because the system checks for a number in the list that doesn't existe
        for i in range(len(self.list_worlds)):
            if self.list_worlds[i-1] == "var": #create vars
                if not self.list_worlds[1] == "var":
                    self.vars_.append([self.list_worlds[i], 0])
                    print("all the vars "+str(self.vars_))

            for x in range(len(self.vars_)): #chance vars
                try:
                    if self.list_worlds[i-1] == self.vars_[x-1][0]:
                        if self.list_worlds[i] == "=":
                            self.vars_[x-1][1] = self.list_worlds[i+1]
                            print("all the vars "+str(self.vars_))
                except:
                    pass

            for x in range(len(self.vars_)): #del vars
                try:
                    if self.list_worlds[i-1] == "del":
                        if self.list_worlds[i] == self.vars_[x-1][0]:
                            del self.vars_[x-1]
                            print("all the vars "+str(self.vars_))
                except:
                    pass

            for x in range(len(self.vars_)): #reset vars
                try:
                    if self.list_worlds[i-1] == "res":
                        if self.list_worlds[i] == self.vars_[x-1][0]:
                            self.vars_[x-1][1] = 0
                            print("all the vars "+str(self.vars_))
                except:
                    pass

            # print
            try:
                if self.list_worlds_for_print[i-1] == "print":#print(self.list_worlds[i+1][0])
                    if self.list_worlds_for_print[i] == "<<":
                        if self.list_worlds_for_print[i+2] == "c<":
                            self.print(self.list_worlds_for_print[i+1][0], int(self.list_worlds_for_print[i+3][0]), "")
                        else:
                            self.print(txt=self.list_worlds_for_print[i+1][0], l="")
            except:
                pass

            # println
            try:
                if self.list_worlds_for_print[i - 1] == "println":  # print(self.list_worlds[i+1][0])
                    if self.list_worlds_for_print[i] == "<<":
                        if self.list_worlds_for_print[i + 2] == "c<":
                            self.print(self.list_worlds_for_print[i + 1][0], int(self.list_worlds_for_print[i + 3][0]))
                        else:
                            self.print(txt=self.list_worlds_for_print[i + 1][0])
            except:
                pass

            try:
                if self.list_worlds[i - 1] == "wait":
                    if self.list_worlds[i] == "<<":
                        if self.list_worlds[i + 1][1] == "int":
                            import time
                            time.sleep(int(self.list_worlds[i + 1][0]))
            except:
                pass

            try:
                if self.list_worlds[i - 1] == 'if':
                    if self.list_worlds[i] == ['true', 'bool']:
                        if self.list_worlds[i+1][1] == "statement":
                            run_setup(self.list_worlds[i+1][0])
            except:
                pass

            try:
                if self.list_worlds[i-1] == "get_input":
                    self.list_worlds[i-1] = [input(), "str"]
            except:
                pass

            try:
                if self.list_worlds[i-1] == "import":
                    if self.list_worlds[i][1] == "str":
                        if self.list_worlds[i][0][-3:] == "spn":
                            with open(self.list_worlds[i][0], "r") as file_for_import:
                                run_setup(file_for_import.read().replace('\n', ''))
                                del self.list_worlds[i-1]
                                del self.list_worlds[i]
            except:
                pass

            if self.list_worlds[i-1] == "exit":
                from sys import exit
                exit()

    def is_int(self, text):
        try:
            float(text)
            return True
        except:
            return False

    def print(self, txt="", color_code=7, l="\n"):
        # Check if the specified color code is within valid range, default to white if not
        self.selected_color = self.color_codes[color_code] if 0 <= color_code <= 7 else self.color_codes[7]  # Default to white

        # Print the colored text with a reset code to ensure subsequent text is not affected
        print(self.selected_color + txt + self.color_codes[8], end=l)

class run_setup:
    def __init__(self, txt):
        self.var_2 = 0
        self.list_lines = []
        self.chater2 = txt
        self.i_k2 = 0
        self.i_p = 0
        self.p = []
        self.l_l_add = ""
        try:
            for i in range(len(self.chater2)):
                if self.chater2[i] == '"' and self.i_k2 == 1:
                    self.i_k2 = 0
                elif self.chater2[i] == '"':
                    self.i_k2 = 1
                if self.chater2[i] == '{':
                    self.i_p += 1
                elif self.chater2[i] == '}':
                    self.i_p -= 1
                if self.chater2[i] == ';' and self.i_k2 != 1 and self.i_p == 0:
                    self.l_l_add = self.l_l_add + self.chater2[self.var_2:i]
                    basic.run(self.l_l_add)
                    self.l_l_add = ""
                    self.var_2 = i + 1
        except IndexError:
            pass

def replace_letter_outside_quotes_and_braces(input_string, letter_to_replace="\n", replacement_letter=";"):
    result = []
    inside_quotes = False
    inside_braces = 0

    for char in input_string:
        if char == '"':
            inside_quotes = not inside_quotes
        if char == '{':
            inside_braces += 1
        if char == '}':
            inside_braces -= 1

        if not inside_quotes and inside_braces == 0 and char == letter_to_replace:
            result.append(replacement_letter)
        else:
            result.append(char)

    return ''.join(result)

basic = Basic()
print("****************************** SEPYNODEv0.5.3.pre-4.file_runner ******************************")
input_p = input("file: ")
if input_p[-3:] == "spn":
   try:
       with open(input_p, "r") as file:
           input_p = file.read()
           run_setup(input_p.replace("\n", ""))
   except: pass