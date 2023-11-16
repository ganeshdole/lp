class MacroProcessor:
    def __init__(self):
        self.pntab = {}
        self.paramNo = 1
        self.mdtp = 1
        self.flag = 0
        self.pp = 0
        self.kp = 0
        self.kpdtp = 0

    def process_macro_pass1(self, input_file, intermediate_file, mnt_file, mdt_file, kpdt_file):
        with open(input_file, 'r') as b1, open(intermediate_file, 'w') as f1, \
                open(mnt_file, 'w') as f2, open(mdt_file, 'w') as f3, open(kpdt_file, 'w') as f4:
            for line in b1:
                words = line.split()
                if words[0].upper() == "MACRO":
                    self.flag = 1
                    if len(words) <= 2:
                        f2.write(f"{words[1]}\t{self.pp}\t{self.kp}\t{self.mdtp}\t{self.kpdtp if self.kp == 0 else self.kpdtp + 1}\n")
                        continue
                    params = words[2].split(',')
                    for param in params:
                        if '=' in param:
                            self.kp += 1
                            keyword_param = param.split('=')
                            self.pntab[keyword_param[0][1:]] = self.paramNo
                            f4.write(f"{keyword_param[0][1:]}\t{keyword_param[1].strip() if len(keyword_param) == 2 else '-'}\n")
                        else:
                            self.pntab[param[1:].strip()] = self.paramNo
                            self.pp += 1
                    f2.write(f"{words[1]}\t{self.pp}\t{self.kp}\t{self.mdtp}\t{self.kpdtp if self.kp == 0 else self.kpdtp + 1}\n")
                    self.kpdtp += self.kp
                elif words[0].upper() == "MEND":
                    f3.write(line)
                    self.flag, self.pp, self.kp = 0, 0, 0
                    self.mdtp += 1
                    self.paramNo = 1
                    self.pntab.clear()
                elif self.flag == 1:
                    temp = ""
                    i = 0
                    while i < len(line):
                        if line[i] == '&':
                            i += 1
                            while i < len(line) and line[i] != ' ' and line[i] != ',':
                                temp += line[i]
                                i += 1
                            f3.write(f"#{self.pntab[temp.strip()]}")
                            temp = ""
                        else:
                            f3.write(line[i])
                        i += 1
                    f3.write("\n")
                    self.mdtp += 1
                else:
                    f1.write(line)


if __name__ == "__main__":
    processor = MacroProcessor()
    processor.process_macro_pass1("input.txt", "intermediate.txt", "mnt.txt", "mdt.txt", "kpdt.txt")
