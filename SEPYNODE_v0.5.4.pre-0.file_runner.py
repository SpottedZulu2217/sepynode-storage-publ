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
    functions = []
    SPN_return = None

    #["None", #name\n"println << \"None\" c< 4;", #code, basic #basic, args=["var arg = 1", ]]

    def get_new_inst(self):
        return Basic()

    def run_command(self, txt):
        self.error_a = 0
        self.spaces = 0
        self.helper = ''
        self.chater_2 = str(txt) + " "
        self.list_worlds_2 = txt
        self.i_p = 0
        self.i_k = 0
        self.var_1 = 0
        self.pam_len = 0 # + - len
        self.mad_len = 0 # * / len
        self.and_len = 0 # and len
        self.or_len = 0 # or len
        self.eq_len = 0 # == != > < len
        #for i in range(len(self.chater_2)):
        #    try:
        #        if self.chater_2[i] == '"' and self.i_k == 1 and not self.i_p != 0:
        #            self.list_worlds_2.append([self.chater_2[self.var_1:i], "str"])
        #            self.var_1 = i + 1
        #            self.i_k = 0
        #        elif self.chater_2[i] == '"' and not self.i_p != 0:
        #            self.list_worlds_2.append(self.chater_2[self.var_1:i])
        #            self.var_1 = i + 1
        #            self.i_k = 1
        #        elif self.chater_2[i] == ' ' and not self.i_p != 0:
        #            if not self.i_k:
        #                self.list_worlds_2.append(self.chater_2[self.var_1:i])
        #                self.var_1 = i + 1
        #        elif self.chater_2[i] == "(" and not self.i_k and not self.i_p:
        #            self.list_worlds_2.append(self.chater_2[self.var_1:i])
        #            self.var_1 = i + 1
        #            self.list_worlds_2.append("(")
        #        elif self.chater_2[i] == ")" and not self.i_k and not self.i_p:
        #            self.list_worlds_2.append(self.chater_2[self.var_1:i])
        #            self.var_1 = i + 1
        #            self.list_worlds_2.append(")")
        #        elif self.chater_2[i] == "+":
        #            self.list_worlds_2.append(self.chater_2[self.var_1:i])
        #            self.var_1 = i + 1
        #            self.list_worlds_2.append("+")
        #        elif self.chater_2[i] == "-":
        #            self.list_worlds_2.append(self.chater_2[self.var_1:i])
        #            self.var_1 = i + 1
        #            self.list_worlds_2.append("-")
        #        elif self.chater_2[i] == "/":
        #            self.list_worlds_2.append(self.chater_2[self.var_1:i])
        #            self.var_1 = i + 1
        #            self.list_worlds_2.append("/")
        #        elif self.chater_2[i] == "*":
        #            self.list_worlds_2.append(self.chater_2[self.var_1:i])
        #            self.var_1 = i + 1
        #            self.list_worlds_2.append("*")
        #        elif self.chater_2[i] == "<":
        #            self.list_worlds_2.append(self.chater_2[self.var_1:i])
        #            self.var_1 = i + 1
        #            self.list_worlds_2.append("<")
        #        elif self.chater_2[i] == ">":
        #            self.list_worlds_2.append(self.chater_2[self.var_1:i])
        #            self.var_1 = i + 1
        #            self.list_worlds_2.append(">")
        #    except: pass

        for i in range(len(self.list_worlds_2)):
            if self.list_worlds_2[i] == "":
                self.spaces += 1

        while self.spaces != 0:
            for i in range(len(self.list_worlds_2)):
                try:
                    if self.list_worlds_2[i] == "":
                        del self.list_worlds_2[i]
                        self.spaces -= 1
                except:
                    pass

        for i in range(len(self.list_worlds_2)): # if (main()){};
            for f in range(len(self.functions)):
                if self.exists(self.list_worlds_2, i):
                    if self.functions[f][0] == self.list_worlds_2[i]:
                        if self.exists(self.list_worlds_2, i-1) and self.exists(self.list_worlds_2, i+1):
                            if str(self.list_worlds_2[i - 1]) == ")" and self.list_worlds_2[i + 1] == "(":
                                self.par_len = 0
                                self.par_pos = 0
                                self.par_pos_end = 0
                                self.helper_command = []
                                self.list_worlds_2.append("")
                                for x in range(len(self.list_worlds_2)):
                                    if self.list_worlds_2[x] == "(":
                                        self.par_len += 1
                                        self.par_pos = x

                                    elif self.list_worlds_2[x] == ")" and not self.par_len == 0:
                                        self.par_len -= 1

                                    elif self.list_worlds_2[x-1] == ")" and self.par_len == 0:
                                        self.par_pos_end = x - 1

                                x_ = i + 2
                                x = self.par_pos_end - x_
                                #
                                for y in range(x):
                                    self.helper_command.append(self.list_worlds_2[x_ + y])
                                #
                                self.list_worlds_2[x_] = self.helper_command
                                #
                                for y in range(x - 1):
                                    del self.list_worlds_2[x_ + 1]

                                del self.list_worlds_2[i + 1]
                                if self.list_worlds_2[i-2] == ")":
                                    del self.list_worlds_2[i-2]
                                del self.list_worlds_2[i-1]
                                self.args = []
                                self.l_c = 0#last pos of ,

                                self.list_worlds_2[i+1].append(",")

                                for x in range(len(self.list_worlds_2[i+1])):
                                    if self.list_worlds_2[i+1][x] == ",":
                                        self.args.append(self.list_worlds_2[i+1][self.l_c:x])
                                        self.l_c = x+1

                                self.list_worlds_2[i+1] = self.args.copy()

                                for s in range(len(self.functions[f][3])): #func(var txt = "panos");
                                    run_setup(" ".join(str(item) for item in self.functions[f][3][s]) + ";", basic=self.functions[f][2])

                                for s in range(len(self.list_worlds_2[i+1])): #func(var txt = "panos");
                                    run_setup(" ".join(str(item) for item in self.list_worlds_2[i+1][s]) + ";", basic=self.functions[f][2])

                                self.list_worlds_2[0] = run_setup(self.functions[f][1], basic=self.functions[f][2]).return_

        for i in range(len(self.list_worlds_2)):
            for x in range(len(self.vars_)):
                if self.list_worlds_2[i] == self.vars_[x][0]:
                    self.list_worlds_2[i] = self.vars_[x][1] # str(float())

        for i in range(len(self.list_worlds_2)):
            if self.list_worlds_2[i] in ["true", "false"]:
                self.list_worlds_2[i] = [self.list_worlds_2[i], "bool"]

        for i in range(len(self.list_worlds_2)):
            if self.exists(self.list_worlds_2[i], 0) and self.exists(self.list_worlds_2[i], -1):
                if self.list_worlds_2[i][0] == "\"" and self.list_worlds_2[i][-1] == "\"":
                    self.list_worlds_2[i] = [str(self.list_worlds_2[i][1:-1]), "str"]

        for i in range(len(self.list_worlds_2)):
            if self.is_int(self.list_worlds_2[i]):
                self.list_worlds_2[i] = [str(float(self.list_worlds_2[i])), "int"]

        #for i in range(len(self.list_worlds_2)):
        #    try:
        #        if self.list_worlds_2[i] == "get_input":
        #            if self.list_worlds_2[i+1] == "(":
        #                if self.list_worlds_2[i + 2] == ")":
        #                    #print(self.color_codes[int(self.list_worlds_2[i+2][0][:-2])], "dewvjkf", end="")
        #                    self.list_worlds_2[i] = [input(), "str"] #input(self.color_codes[int(self.list_worlds_2[i+2][0][:-2])]
        #                    del self.list_worlds_2[i+1]
        #                    del self.list_worlds_2[i+1]
        #    except:pass

        #functions (old)


        for i in range(len(self.list_worlds_2)):
            try:
                if self.list_worlds_2[i] == "int":
                    if self.list_worlds_2[i+1] == "<":
                        if self.is_int(self.list_worlds_2[i+2][0]):
                            self.list_worlds_2[i] = [float(self.list_worlds_2[i+2][0]), "int"]
                            del self.list_worlds_2[i+1]
                            del self.list_worlds_2[i+1]
                        else:
                            self.error = f"TypeError at \"{self.list_worlds_2[i + 2][0]}\":int can only be int not str or bool"
                            print(f"\033[91m{self.error}\033[0m")
                            self.mad_len = 0
                elif self.list_worlds_2[i] == "str":
                    if self.list_worlds_2[i+1] == "<":
                        self.list_worlds_2[i] = [str(self.list_worlds_2[i+2][0]), "str"]
                        del self.list_worlds_2[i+1]
                        del self.list_worlds_2[i+1]
                elif self.list_worlds_2[i] == "bool":
                    if self.list_worlds_2[i+1] == "<":
                        if self.list_worlds_2[i+2][0] in ["true", "false"]:
                            if not self.is_int(self.list_worlds_2[i+2][0]):
                                self.list_worlds_2[i] = [self.list_worlds_2[i+2][0], "bool"]
                                del self.list_worlds_2[i+1]
                                del self.list_worlds_2[i+1]
                        else:
                            self.error = f"TypeError at \"{self.list_worlds_2[i + 2][0]}\":int can only be bool"
                            print(f"\033[91m{self.error}\033[0m")
                            self.error_a = 1
                            self.mad_len = 0
            except: pass

        for i in range(len(self.list_worlds_2)):
            if self.list_worlds_2[i] in ["+", "-"]:
                self.pam_len += 1
            elif self.list_worlds_2[i] in ["*", "/"]:
                self.mad_len += 1
            elif self.list_worlds_2[i] == "and":
                self.and_len += 1
            elif self.list_worlds_2[i] == "or":
                self.or_len += 1
            elif self.list_worlds_2[i] in ["==", "!=", ">", "<"]:
                self.eq_len += 1

        self.offset = 0
        while self.offset < self.mad_len:
            for i in range(len(self.list_worlds_2)):
                try:
                    if self.list_worlds_2[i+1] in ["*", "/"]:
                        if self.list_worlds_2[i][1] == "int":
                            if self.list_worlds_2[i+2][1] == "int":
                                self.list_worlds_2[i] = [str(round(float(eval(
                                    str(self.list_worlds_2[i][0]) + self.list_worlds_2[i+1] + str(self.list_worlds_2[i+2][0]))), 16)), "int"]
                                del self.list_worlds_2[i+1]
                                del self.list_worlds_2[i+1]
                                self.offset += 1
                            else:
                                self.error = f"TypeError at \"{self.list_worlds_2[i + 2][0]}\":int can only be moltiplied with int"
                                print(f"\033[91m{self.error}\033[0m")
                                self.error_a = 1
                                self.mad_len = 0
                        else:
                            self.error = f"TypeError at \"{self.list_worlds_2[i + 2][0]}\":only ints can be moltiplied for now!"
                            print(f"\033[91m{self.error}\033[0m")
                            self.error_a = 1
                            self.mad_len = 0
                except:
                    pass

        self.offset = 0
        while self.offset < self.pam_len:
            for i in range(len(self.list_worlds_2)):
                try:
                    if self.list_worlds_2[i+1] in ["+", "-"]:
                        if self.list_worlds_2[i][1] == "int":
                            if self.list_worlds_2[i+2][1] == "int":
                                if self.list_worlds_2[i+1] == "+":
                                    from decimal import Decimal
                                    self.list_worlds_2[i] = [str(Decimal(str(self.list_worlds_2[i][0])) + Decimal(str(self.list_worlds_2[i+2][0]))), "int"]
                                    del self.list_worlds_2[i+1]
                                    del self.list_worlds_2[i+1]
                                    self.offset += 1
                                elif self.list_worlds_2[i+1] == "-":
                                    from decimal import Decimal
                                    self.list_worlds_2[i] = [str(Decimal(str(self.list_worlds_2[i][0])) - Decimal(str(self.list_worlds_2[i+2][0]))), "int"]
                                    del self.list_worlds_2[i+1]
                                    del self.list_worlds_2[i+1]
                                    self.offset += 1
                            else:
                                self.error = f"TypeError at \"{self.list_worlds_2[i + 2][0]}\":int can only be added with int"
                                print(f"\033[91m{self.error}\033[0m")
                                self.error_a = 1
                                self.pam_len = 0
                        elif self.list_worlds_2[i][1] == "str":
                            if self.list_worlds_2[i+2][1] == "str":
                                if self.list_worlds_2[i+1] == "+":#\
                                    self.list_worlds_2[i] = [(str(self.list_worlds_2[i][0]) + str(self.list_worlds_2[i+2][0])), "str"]
                                    del self.list_worlds_2[i+1]
                                    del self.list_worlds_2[i+1]
                                    self.offset += 1
                                elif self.list_worlds_2[i+1] == "-":
                                    self.error = f"TypeError at \"{self.list_worlds_2[i + 2][0]}\":str can't get subtracted with str"
                                    print(f"\033[91m{self.error}\033[0m")
                                    self.error_a = 1
                                    self.pam_len = 0
                            else:
                                self.error = f"TypeError at \"{self.list_worlds_2[i + 2][0]}\":str can't get added with str"
                                print(f"\033[91m{self.error}\033[0m")
                                self.error_a = 1
                                self.pam_len = 0
                except:
                    pass

        if self.error_a:
            exit(-1)

        for i in range(len(self.list_worlds_2)):
            try:
                if self.list_worlds_2[i] == "not":
                    if self.list_worlds_2[i+1] == ["true", "bool"]:
                        self.list_worlds_2[i+1] = ["false", "bool"]
                        del self.list_worlds_2[i]
                    elif self.list_worlds_2[i+1] == ["false", "bool"]:
                        self.list_worlds_2[i+1] = ["true", "bool"]
                        del self.list_worlds_2[i]
                    else:
                        self.error = f"NameError at \"{self.list_worlds_2[i] + ' ' + str(self.list_worlds_2[i + 1])}\"({i}-{i+1}):"
                        print(f"\033[91m{self.error}\033[0m")
                        self.error_a = 1
            except: pass

        if self.error_a:
            exit(-1)

        self.offset = 0
        while self.offset < self.and_len:
            for i in range(len(self.list_worlds_2)):
                try:
                    if self.list_worlds_2[i] == "and":
                        if self.list_worlds_2[i-1] == ["true", "bool"]:
                            if self.list_worlds_2[i+1] == ["true", "bool"]:
                                self.and_len -= 1
                                self.list_worlds_2[i-1] = ["true", "bool"]
                                del self.list_worlds_2[i]
                                del self.list_worlds_2[i]
                            elif self.list_worlds_2[i + 1] == ["false", "bool"]:
                                self.and_len -= 1
                                self.list_worlds_2[i - 1] = ["false", "bool"]
                                del self.list_worlds_2[i]
                                del self.list_worlds_2[i]
                            else:
                                self.error = f"NameError at \"{str(self.list_worlds_2[i - 1]) + ' ' + self.list_worlds_2[i] + ' ' + str(self.list_worlds_2[i + 1])}\":"
                                print(f"\033[91m{self.error}\033[0m")
                                self.error_a = 1
                                self.and_len = 0
                        elif self.list_worlds_2[i-1] == ["false", "bool"]:
                            self.and_len -= 1
                            self.list_worlds_2[i-1] = ["false", "bool"]
                            del self.list_worlds_2[i]
                            del self.list_worlds_2[i]
                        else:
                            self.error = f"NameError at \"{str(self.list_worlds_2[i-1]) + ' ' +self.list_worlds_2[i] + ' '  + str(self.list_worlds_2[i+1])}\":"
                            print(f"\033[91m{self.error}\033[0m")
                            self.error_a = 1
                            self.and_len = 0
                except: pass

        if self.error_a:
            exit(-1)

        self.offset = 0
        while self.offset < self.or_len:
            for i in range(len(self.list_worlds_2)):
                try:
                    if self.list_worlds_2[i] == "or":
                        if self.list_worlds_2[i-1] == ["true", "bool"] or self.list_worlds_2[i+1] == ["true", "bool"]:
                            self.or_len -= 1
                            self.list_worlds_2[i-1] = ["true", "bool"]
                            del self.list_worlds_2[i]
                            del self.list_worlds_2[i]
                        else:
                            self.or_len -= 1
                            self.list_worlds_2[i - 1] = ["false", "bool"]
                            del self.list_worlds_2[i]
                            del self.list_worlds_2[i]
                except: pass

        self.offset = 0
        while self.offset < self.eq_len:
            for i in range(len(self.list_worlds_2)):
                try:
                    if self.list_worlds_2[i] == "==":
                        if self.list_worlds_2[i - 1][1] == "int":
                            if self.list_worlds_2[i + 1][1] == "int":
                                if float(self.list_worlds_2[i - 1][0]) == float(self.list_worlds_2[i + 1][0]):
                                    self.eq_len -= 1
                                    self.list_worlds_2[i - 1] = ["true", "bool"]
                                    del self.list_worlds_2[i]
                                    del self.list_worlds_2[i]
                                else:
                                    self.eq_len -= 1
                                    self.list_worlds_2[i-1] = ["false", "bool"]
                                    del self.list_worlds_2[i]
                                    del self.list_worlds_2[i]
                            else:
                                self.error = f"NameError at \"{self.list_worlds_2[i-1]}{self.list_worlds_2[i]}{self.list_worlds_2[i+1]}\":"
                                print(f"\033[91m{self.error}\033[0m")
                                self.error_a = 1
                                self.eq_len = 0
                        elif self.list_worlds_2[i-1][1] == "bool":
                            if self.list_worlds_2[i + 1][1] == "bool":
                                if self.list_worlds_2[i-1][0] == self.list_worlds_2[i+1][0]:
                                    self.eq_len -= 1
                                    self.list_worlds_2[i-1] = ["true", "bool"]
                                    del self.list_worlds_2[i]
                                    del self.list_worlds_2[i]
                                else:
                                    self.eq_len -= 1
                                    self.list_worlds_2[i - 1] = ["false", "bool"]
                                    del self.list_worlds_2[i]
                                    del self.list_worlds_2[i]
                            else:
                                self.error = f"NameError at \"{self.list_worlds_2[i-1]}{self.list_worlds_2[i]}{self.list_worlds_2[i+1]}\":"
                                print(f"\033[91m{self.error}\033[0m")
                                self.error_a = 1
                                self.eq_len = 0
                        elif self.list_worlds_2[i-1][1] == "str":
                            if self.list_worlds_2[i + 1][1] == "str":
                                if self.list_worlds_2[i-1][0] == self.list_worlds_2[i+1][0]:
                                    self.eq_len -= 1
                                    self.list_worlds_2[i-1] = ["true", "bool"]
                                    del self.list_worlds_2[i]
                                    del self.list_worlds_2[i]
                                else:
                                    self.eq_len -= 1
                                    self.list_worlds_2[i - 1] = ["false", "bool"]
                                    del self.list_worlds_2[i]
                                    del self.list_worlds_2[i]
                            else:
                                self.error = f"NameError at \"{self.list_worlds_2[i-1]}{self.list_worlds_2[i]}{self.list_worlds_2[i+1]}\":"
                                print(f"\033[91m{self.error}\033[0m")
                                self.error_a = 1
                                self.eq_len = 0
                    elif self.list_worlds_2[i] == "!=":
                        if self.list_worlds_2[i-1][1] == "int":
                            if self.list_worlds_2[i + 1][1] == "int":
                                if float(self.list_worlds_2[i-1][0]) != float(self.list_worlds_2[i+1][0]):
                                    self.eq_len -= 1
                                    self.list_worlds_2[i-1] = ["true", "bool"]
                                    del self.list_worlds_2[i]
                                    del self.list_worlds_2[i]
                                else:
                                    self.eq_len -= 1
                                    self.list_worlds_2[i - 1] = ["false", "bool"]
                                    del self.list_worlds_2[i]
                                    del self.list_worlds_2[i]
                            else:
                                self.error = f"NameError at \"{self.list_worlds_2[i-1]}{self.list_worlds_2[i]}{self.list_worlds_2[i+1]}\":"
                                print(f"\033[91m{self.error}\033[0m")
                                self.error_a = 1
                                self.eq_len = 0
                        elif self.list_worlds_2[i-1][1] == "bool":
                            if self.list_worlds_2[i + 1][1] == "bool":
                                if self.list_worlds_2[i-1][0] != self.list_worlds_2[i+1][0]:
                                    self.eq_len -= 1
                                    self.list_worlds_2[i-1] = ["true", "bool"]
                                    del self.list_worlds_2[i]
                                    del self.list_worlds_2[i]
                                else:
                                    self.eq_len -= 1
                                    self.list_worlds_2[i - 1] = ["false", "bool"]
                                    del self.list_worlds_2[i]
                                    del self.list_worlds_2[i]
                            else:
                                self.error = f"NameError at \"{self.list_worlds_2[i-1]}{self.list_worlds_2[i]}{self.list_worlds_2[i+1]}\":"
                                print(f"\033[91m{self.error}\033[0m")
                                self.error_a = 1
                                self.eq_len = 0
                        elif self.list_worlds_2[i - 1][1] == "str":
                            if self.list_worlds_2[i + 1][1] == "str":
                                if self.list_worlds_2[i - 1][0] != self.list_worlds_2[i + 1][0]:
                                    self.eq_len -= 1
                                    self.list_worlds_2[i - 1] = ["true", "bool"]
                                    del self.list_worlds_2[i]
                                    del self.list_worlds_2[i]
                                else:
                                    self.eq_len -= 1
                                    self.list_worlds_2[i - 1] = ["false", "bool"]
                                    del self.list_worlds_2[i]
                                    del self.list_worlds_2[i]
                            else:
                                self.error = f"NameError at \"{self.list_worlds_2[i-1]}{self.list_worlds_2[i]}{self.list_worlds_2[i+1]}\":"
                                print(f"\033[91m{self.error}\033[0m")
                                self.error_a = 1
                                self.eq_len = 0
                    elif self.list_worlds_2[i] == ">":#3 < 4;
                        if self.list_worlds_2[i-1][1] == "int":
                            if self.list_worlds_2[i + 1][1] == "int":
                                if float(self.list_worlds_2[i-1][0]) > float(self.list_worlds_2[i+1][0]):
                                    self.eq_len -= 1
                                    self.list_worlds_2[i-1] = ["true", "bool"]
                                    del self.list_worlds_2[i]
                                    del self.list_worlds_2[i]
                                else:
                                    self.eq_len -= 1
                                    self.list_worlds_2[i - 1] = ["false", "bool"]
                                    del self.list_worlds_2[i]
                                    del self.list_worlds_2[i]
                            else:
                                self.error = f"NameError at \"{self.list_worlds_2[i-1]}{self.list_worlds_2[i]}{self.list_worlds_2[i+1]}\":"
                                print(f"\033[91m{self.error}\033[0m")
                                self.error_a = 1
                                self.eq_len = 0
                    elif self.list_worlds_2[i] == "<":
                        if self.list_worlds_2[i-1][1] == "int":
                            if self.list_worlds_2[i + 1][1] == "int":
                                if float(self.list_worlds_2[i-1][0]) < float(self.list_worlds_2[i+1][0]):
                                    self.eq_len -= 1
                                    self.list_worlds_2[i-1] = ["true", "bool"]
                                    del self.list_worlds_2[i]
                                    del self.list_worlds_2[i]
                                else:
                                    self.eq_len -= 1
                                    self.list_worlds_2[i - 1] = ["false", "bool"]
                                    del self.list_worlds_2[i]
                                    del self.list_worlds_2[i]
                            else:
                                self.error = f"NameError at \"{self.list_worlds_2[i-1]}{self.list_worlds_2[i]}{self.list_worlds_2[i+1]}\":"
                                print(f"\033[91m{self.error}\033[0m")
                                self.error_a = 1
                                self.eq_len = 0
                except: pass

        if self.error_a:
            exit(-1)


        return self.list_worlds_2

    def run(self, txt): #func(var txt = "panos");
        self.return_ = None
        self.spaces = 0
        self.statements_len = 0
        self.tokens_len1 = 0
        self.tokens_len2 = 0
        self.helper_command = []
        self.var_1 = 0
        self.list_worlds = []
        self.chater = str(txt)
        self.i_k = 0 # inside -> ""
        self.i_p = 0 # inside -> ()
        self.i_q = 0 # inside -> []
        self.chater = self.chater + " "
        self.cb_pos = 0
        self.last_stm_pos = 0
        for i in range(len(self.chater)):
            try:#func(var txt = "panos");
                if self.chater[i] == '"' and self.i_k == 1 and not self.i_p != 0:
                    self.list_worlds.append(f"\"{self.chater[self.var_1:i]}\"")
                    self.var_1 = i + 1
                    self.i_k = 0
                elif self.chater[i] == '"' and not self.i_p != 0:
                    self.list_worlds.append(self.chater[self.var_1:i])
                    self.var_1 = i + 1
                    self.i_k = 1
                elif self.chater[i] == ' ' and not self.i_p != 0:
                    if not self.i_k:
                        self.list_worlds.append(self.chater[self.var_1:i])
                        self.var_1 = i + 1

                if self.chater[i] == '}' and not self.i_k:
                    if self.i_p == 1:
                        self.list_worlds.append([self.chater[self.last_stm_pos+1:i], "statement"])
                    self.var_1 = i + 1
                    self.i_p -= 1
                elif self.chater[i] == '{' and not self.i_k:
                    if self.i_p == 0:
                        #self.list_worlds.append(self.chater[self.last_stm_pos:i])
                        self.last_stm_pos = i
                    self.var_1 = i + 1
                    self.i_p += 1

                elif self.chater[i] == "(" and not self.i_k and not self.i_p:
                    self.list_worlds.append(self.chater[self.var_1:i])
                    self.var_1 = i + 1
                    self.list_worlds.append("(")
                elif self.chater[i] == ")" and not self.i_k and not self.i_p:
                    self.list_worlds.append(self.chater[self.var_1:i])
                    self.var_1 = i + 1
                    self.list_worlds.append(")")
                elif self.chater[i] == "+" and not self.i_k and not self.i_p:
                    self.list_worlds.append(self.chater[self.var_1:i])
                    self.var_1 = i + 1
                    self.list_worlds.append("+")
                elif self.chater[i] == "-" and not self.i_k and not self.i_p:
                    self.list_worlds.append(self.chater[self.var_1:i])
                    self.var_1 = i + 1
                    self.list_worlds.append("-")
                elif self.chater[i] == "/" and not self.i_k and not self.i_p:
                    self.list_worlds.append(self.chater[self.var_1:i])
                    self.var_1 = i + 1
                    self.list_worlds.append("/")
                elif self.chater[i] == "*" and not self.i_k and not self.i_p:
                    self.list_worlds.append(self.chater[self.var_1:i])
                    self.var_1 = i + 1
                    self.list_worlds.append("*")
                elif self.chater[i] == "<" and not self.i_k and not self.i_p:
                    self.list_worlds.append(self.chater[self.var_1:i])
                    self.var_1 = i + 1
                    self.list_worlds.append("<")
                elif self.chater[i] == ">" and not self.i_k and not self.i_p:
                    self.list_worlds.append(self.chater[self.var_1:i])
                    self.var_1 = i + 1
                    self.list_worlds.append(">")
                elif self.chater[i] == "," and not self.i_k and not self.i_p:
                    self.list_worlds.append(self.chater[self.var_1:i])
                    self.var_1 = i + 1
                    self.list_worlds.append(",")
            except:
                pass


        for i in range(len(self.list_worlds)):
            if self.list_worlds[i] == "":
                self.spaces += 1

        self.offset = 0
        while self.offset < self.spaces:
            for i in range(len(self.list_worlds)):
                try:
                    if self.list_worlds[i] == "":
                        self.spaces -= 1
                        del self.list_worlds[i]
                except: pass

        #x_ = 1
        #x = len(self.list_worlds) - x_
#
        #for y in range(x):
        #    self.helper_command.append(self.list_worlds[x_ + y])
#
        #self.list_worlds[x_] = self.helper_command
        #for y in range(x-1):
        #    del self.list_worlds[x_ + 1]
#
        #print(self.list_worlds)

        #i = 0
        for i in range(len(self.list_worlds)):
            if self.exists(self.list_worlds, i):
                if self.list_worlds[i] == "var":
                    if self.exists(self.list_worlds, i+1):
                        self.vars_.append([self.list_worlds[i+1], ["None", "bool"]])
                        #print(self.vars_)
                elif self.list_worlds[i] == "=":

                    x_ = i+1
                    x = len(self.list_worlds) - x_

                    for y in range(x):
                        self.helper_command.append(self.list_worlds[x_ + y])

                    self.list_worlds[x_] = self.helper_command
                    for y in range(x - 1):
                        del self.list_worlds[x_ + 1]


                    self.list_worlds[i + 1] = self.run_command(self.list_worlds[i+1])[0]
                    if self.exists(self.list_worlds, i-1) and self.exists(self.list_worlds, i+1):
                        for x in range(len(self.vars_)):
                            if self.vars_[x][0] == self.list_worlds[i-1]:
                                self.vars_[x][1] = self.list_worlds[i+1]
                elif self.list_worlds[i] == "del":
                    if self.exists(self.list_worlds, i+1):
                        for x in range(len(self.vars_)):
                            try:
                                if self.vars_[x][0] == self.list_worlds[i+1]:
                                    del self.vars_[x]
                            except: pass

                elif self.list_worlds[i] == "print":
                    if self.exists(self.list_worlds, i+1) and self.exists(self.list_worlds, i+2) and self.exists(self.list_worlds, i+3) and self.list_worlds[i+1]+self.list_worlds[i+2] == "<<":

                        if str(self.list_worlds[i-3]) + str(self.list_worlds[i-2]) == "c<":
                            for x in range(len(self.list_worlds)):
                                try:
                                    if self.list_worlds[x] + self.list_worlds[x + 1] == "c<":
                                        self.cb_pos = x
                                except:
                                    pass

                            x_ = i + 3
                            x = self.cb_pos - x_

                            for y in range(x):
                                self.helper_command.append(self.list_worlds[x_ + y])

                            self.list_worlds[x_] = self.helper_command

                            for y in range(x - 1):
                                del self.list_worlds[x_ + 1]

                            self.list_worlds[i + 3] = self.run_command(self.list_worlds[i + 3])[0]
                            self.printf(self.list_worlds[i+3][0], int(self.list_worlds[i+6][0]), l="")
                        else:
                            x_ = i + 3
                            x = len(self.list_worlds) - x_

                            for y in range(x):
                                self.helper_command.append(self.list_worlds[x_ + y])

                            self.list_worlds[x_] = self.helper_command
                            for y in range(x - 1):
                                del self.list_worlds[x_ + 1]

                            self.list_worlds[i+3] = self.run_command(self.list_worlds[i+3])
                            self.printf(str(self.list_worlds[i + 3][0][0]), l="")


                elif self.list_worlds[i] == "println":

                    if self.exists(self.list_worlds, i + 1) and self.exists(self.list_worlds, i + 2) and self.exists(
                            self.list_worlds, i + 3) and self.list_worlds[i + 1] + self.list_worlds[i + 2] == "<<":

                        if str(self.list_worlds[i - 3]) + str(self.list_worlds[i - 2]) == "c<":

                            for x in range(len(self.list_worlds)):

                                try:

                                    if self.list_worlds[x] + self.list_worlds[x + 1] == "c<":
                                        self.cb_pos = x

                                except:

                                    pass

                            x_ = i + 3

                            x = self.cb_pos - x_

                            for y in range(x):
                                self.helper_command.append(self.list_worlds[x_ + y])

                            self.list_worlds[x_] = self.helper_command

                            for y in range(x - 1):
                                del self.list_worlds[x_ + 1]

                            #print(self.list_worlds)

                            self.list_worlds[i + 3] = self.run_command(self.list_worlds[i + 3])[0]

                            self.printf(self.list_worlds[i + 3][0], int(self.list_worlds[i + 6][0]))

                        else:

                            x_ = i + 3

                            x = len(self.list_worlds) - x_

                            for y in range(x):
                                self.helper_command.append(self.list_worlds[x_ + y])

                            self.list_worlds[x_] = self.helper_command

                            for y in range(x - 1):
                                del self.list_worlds[x_ + 1]

                            self.list_worlds[i + 3] = self.run_command(self.list_worlds[i + 3])

                            self.printf(str(self.list_worlds[i + 3][0][0]))

                elif self.list_worlds[i] == "wait" and str(self.list_worlds[i+1]) + str(self.list_worlds[i+2]) == "<<":
                    x_ = i + 3

                    x = len(self.list_worlds) - x_

                    for y in range(x):
                        self.helper_command.append(self.list_worlds[x_ + y])

                    self.list_worlds[x_] = self.helper_command

                    for y in range(x - 1):
                        del self.list_worlds[x_ + 1]

                    self.list_worlds[i + 3] = self.run_command(self.list_worlds[i + 3])[0]

                    import time
                    if self.list_worlds[i+3][1] == "int":
                        time.sleep(int(self.list_worlds[i+3][0][:-2]))
                    else:
                        self.error = f"NameError:the wait command takes only int!"
                        print(f"\033[91m{self.error}\033[0m")
                        exit(-1)

                elif self.list_worlds[i] == "if":
                    if str(self.list_worlds[i - 2]) == ")" and self.list_worlds[i+1] == "(":
                        self.par_len = 0
                        self.par_pos = 0
                        self.par_pos_end = 0
                        for x in range(len(self.list_worlds)):
                            if self.list_worlds[x] == "(":
                                self.par_len += 1
                                self.par_pos = x

                            elif self.list_worlds[x] == ")" and not self.par_len == 0:
                                self.par_len -= 1

                            elif self.list_worlds[x-1] == ")" and self.par_len == 0:
                                self.par_pos_end = x-1

                        x_ = i+2
#
                        x = self.par_pos_end - x_
#
                        for y in range(x):
                            self.helper_command.append(self.list_worlds[x_ + y])
#
                        self.list_worlds[x_] = self.helper_command
#
                        for y in range(x - 1):
                            del self.list_worlds[x_ + 1]

                        del self.list_worlds[i+1]
                        del self.list_worlds[i+2]

                        self.list_worlds[i+1] = self.run_command(self.list_worlds[i+1])[0]
                        if self.exists(self.list_worlds, i+2):
                            if self.list_worlds[i+2][1] == "statement":
                                if self.list_worlds[i+1] == ["true", "bool"]:
                                    run_setup(self.list_worlds[i+2][0], basic)

                elif self.list_worlds[i] == "import":
                    if self.exists(self.list_worlds, i+1):
                        x_ = i + 1

                        x = len(self.list_worlds) - x_

                        for y in range(x):
                            self.helper_command.append(self.list_worlds[x_ + y])

                        self.list_worlds[x_] = self.helper_command

                        for y in range(x - 1):
                            del self.list_worlds[x_ + 1]

                        self.list_worlds[i + 1] = self.run_command(self.list_worlds[i + 1])[0]

                        try:
                            with open(self.list_worlds[i + 1][0], "r") as file:
                                run_setup(file.read().replace("\n", ""), basic)
                        except:
                            self.error = f"FileNotFoundError:the file\"{self.list_worlds[i+1][0]}\" was not found"
                            print(f"\033[91m{self.error}\033[0m")
                            exit(-1)

                #elif self.list_worlds[i] == "exit":
                #    if self.exists(self.list_worlds, i+1) and self.exists(self.list_worlds, i+2):
                #        if self.list_worlds[i+1] == "(" and self.list_worlds[i+2] == ")":
                #            exit()

                elif self.list_worlds[i] == "PYSPN":
                    if self.exists(self.list_worlds, i+1):
                        x_ = i + 1

                        x = len(self.list_worlds) - x_

                        for y in range(x):
                            self.helper_command.append(self.list_worlds[x_ + y])

                        self.list_worlds[x_] = self.helper_command

                        for y in range(x - 1):
                            del self.list_worlds[x_ + 1]

                        self.list_worlds[i + 1] = self.run_command(self.list_worlds[i + 1])[0]

                        self.list_worlds[i] = self.__exec__(self.list_worlds[i+1][0])

                        self.vars_.append(["SPN_return", [str(self.list_worlds[i]), "str"]])

                        del self.list_worlds[i+1]

                        #var command = txt + ")";
                        #PYSPN "tkinter.Label(win, text=' + command + ';


                elif self.list_worlds[i] == "void":#void main(python, main){};
                    #for y in range(len(self.list_worlds)):
                    #    if self.exists(self.list_worlds, y):
                    #        if self.exists(self.list_worlds[y], 1):
                    #            if self.list_worlds[y][1] == "str":
                    #                self.list_worlds[y] = "\"" + self.list_worlds[y][0] + "\""
                    if self.exists(self.list_worlds, i-2) and self.exists(self.list_worlds, i+2):
                        if str(self.list_worlds[i - 2]) == ")" and self.list_worlds[i + 2] == "(":
                            self.par_len = 0
                            self.par_pos = 0
                            self.par_pos_end = 0
                            for x in range(len(self.list_worlds)):
                                if self.list_worlds[x] == "(":
                                    self.par_len += 1
                                    self.par_pos = x

                                elif self.list_worlds[x] == ")" and not self.par_len == 0:
                                    self.par_len -= 1

                                elif self.list_worlds[x - 1] == ")" and self.par_len == 0:
                                    self.par_pos_end = x - 1

                            x_ = i + 2
                            #
                            x = self.par_pos_end - x_
                            #
                            for y in range(x):
                                self.helper_command.append(self.list_worlds[x_ + y])
                            #
                            self.list_worlds[x_] = self.helper_command
                            #
                            for y in range(x - 1):
                                del self.list_worlds[x_ + 1]
                            del self.list_worlds[i + 3]

                            del self.list_worlds[i+2][0]
                            self.args = []
                            self.l_c = 0#last pos of ,

                            self.list_worlds[i+2].append(",")

                            for x in range(len(self.list_worlds[i+2])):
                                if self.list_worlds[i+2][x] == ",":
                                    self.args.append(self.list_worlds[i+2][self.l_c:x])
                                    self.l_c = x+1

                            self.list_worlds[i+2] = self.args.copy()

                            self.functions.append([
                                self.list_worlds[i+1],  # name
                                self.list_worlds[i+3][0],  # code
                                self.get_new_inst(), # basic
                                self.list_worlds[i+2] # args
                            ])

                elif i == 0:
                    for x in range(len(self.functions)):
                        if self.functions[x][0] == self.list_worlds[0]:
                            #for y in range(len(self.list_worlds)):
                            #    if self.exists(self.list_worlds, y):
                            #        if self.exists(self.list_worlds[y], 1):
                            #            if self.list_worlds[y][1] == "str":
                            #                self.list_worlds[y] = "\"" + self.list_worlds[y][0] + "\""
                            self.list_worlds = self.run_command(self.list_worlds)
                            if self.exists(self.list_worlds, 1):
                                del self.list_worlds[1]


                if self.list_worlds[i] == "return":
                    if self.exists(self.list_worlds, i+1):
                        x_ = i + 1

                        x = len(self.list_worlds) - x_

                        for y in range(x):
                            self.helper_command.append(self.list_worlds[x_ + y])

                        self.list_worlds[x_] = self.helper_command

                        for y in range(x - 1):
                            del self.list_worlds[x_ + 1]

                        self.list_worlds[i + 1] = self.run_command(self.list_worlds[i + 1])[0]

                        self.return_ = self.list_worlds[i+1]

                elif self.list_worlds[i] == "while":
                    if str(self.list_worlds[i - 2]) == ")" and self.list_worlds[i + 1] == "(":
                        self.while_ = self.list_worlds.copy()
                        self.par_len = 0
                        self.par_pos = 0
                        self.par_pos_end = 0
                        for x in range(len(self.list_worlds)):
                            if self.list_worlds[x] == "(":
                                self.par_len += 1
                                self.par_pos = x

                            elif self.list_worlds[x] == ")" and not self.par_len == 0:
                                self.par_len -= 1

                            elif self.list_worlds[x - 1] == ")" and self.par_len == 0:
                                self.par_pos_end = x - 1

                        x_ = i + 2
                        #
                        x = self.par_pos_end - x_
                        #
                        for y in range(x):
                            self.helper_command.append(self.list_worlds[x_ + y])
                        #
                        self.list_worlds[x_] = self.helper_command
                        #
                        for y in range(x - 1):
                            del self.list_worlds[x_ + 1]

                        del self.list_worlds[i + 1]
                        del self.list_worlds[i + 2]

                        self.list_worlds[i + 1] = self.run_command(self.list_worlds[i + 1])[0]
                        self.list_worlds_copy = self.list_worlds.copy()
                        if self.exists(self.list_worlds, i + 2):
                            if self.list_worlds[i + 2][1] == "statement":
                                while self.list_worlds[i+1] == ["true", "bool"]:
                                    run_setup(self.list_worlds_copy[i+2][0], basic)  #list_worlds_copy[i+2][0]

                                    self.list_worlds = self.while_.copy()
                                    self.par_len = 0
                                    self.par_pos = 0
                                    self.par_pos_end = 0
                                    self.helper_command = []
                                    for x in range(len(self.list_worlds)):
                                        if self.list_worlds[x] == "(":
                                            self.par_len += 1
                                            self.par_pos = x

                                        elif self.list_worlds[x] == ")" and not self.par_len == 0:
                                            self.par_len -= 1

                                        elif self.list_worlds[x - 1] == ")" and self.par_len == 0:
                                            self.par_pos_end = x - 1

                                    x_ = i + 2
                                    #
                                    x = self.par_pos_end - x_
                                    #
                                    for y in range(x):
                                        #print(self.list_worlds[x_ + y])
                                        self.helper_command.append(self.list_worlds[x_ + y])
                                    #
                                    self.list_worlds[x_] = self.helper_command
                                    #
                                    for y in range(x - 1):
                                        del self.list_worlds[x_ + 1]

                                    del self.list_worlds[i + 3]
                                    del self.list_worlds[i + 1]

                                    self.list_worlds[i + 1] = self.run_command(self.list_worlds[i + 1])[0]

        return self.return_


    def is_int(self, text):
        try:
            float(text)
            return 1
        except:
            return 0

    def exists(self, list, index):
        try:
            if list[index]:
                return 1
        except:
            return 0

    def __exec__(self, code): #PYSPN "import tkinter; win = tkinter.Tk(); label = tkinter.Label(win, text='sepynode window!!!'); label.pack(); win.mainloop()";
        exec(code, globals())
        return basic.SPN_return

    def printf(self, txt="", color_code=7, l="\n"):
        # Check if the specified color code is within valid range, default to white if not
        self.selected_color = self.color_codes[color_code] if 0 <= color_code <= 7 else self.color_codes[7]  # Default to white

        # Print the colored text with a reset code to ensure subsequent text is not affected
        print(self.selected_color + txt + self.color_codes[8], end=l)


class run_setup:
    def __init__(self, txt, basic=None):
        self.return_ = [None]
        self.var_2 = 0
        self.list_lines = []
        self.chater2 = txt
        self.i_k2 = 0
        self.i_p = 0
        self.p = []
        self.l_l_add = ""
        # try:
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
                self.return_ = basic.run(self.l_l_add)
                self.l_l_add = ""
                self.var_2 = i + 1
        # except IndexError:
        #    pass


basic = Basic()
exec("""def SPN_return(txt):
    basic.SPN_return = txt""", globals()) #PYSPN "SPN_return('panos' + ' is my name!!!')";
print("****************************** SEPYNODEv0.5.4.pre-0.file_runner ******************************")

run_setup("import \"SEPYNODE.spn\";", basic)
input_p = "tests.spn"#input("file: ")
with open(input_p, "r") as file:
    input_p = file.read()
    import time
    st = time.time()
    run_setup(input_p.replace('\n', '').replace("\\n", "\n"), basic)
    print(f"time: {time.time() - st}s")