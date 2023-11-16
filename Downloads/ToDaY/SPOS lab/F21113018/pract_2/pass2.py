aptab = {}
aptab_inverse = {}
mdtp_hash = {}
kpdtp_hash = {}
kp_hash = {}
macro_name_hash = {}
mdt = []
kpdt = []

with open("mdt.txt", "r") as file:
    mdt = file.readlines()

with open("kpdt.txt", "r") as file:
    kpdt = file.readlines()

with open("mnt.txt", "r") as file:
    for line in file:
        word = line.strip().split("\t")
        s1 = word[0] + word[1]
        macro_name_hash[word[0]] = 1
        kp_hash[s1] = int(word[2])
        mdtp_hash[s1] = int(word[3])
        kpdtp_hash[s1] = int(word[4])

with open("intermediate.txt", "r") as b1, open("Pass2.txt", "w") as f1:
    for line in b1:
        b1_split = line.strip().split()
        if b1_split[0] in macro_name_hash:
            pp = len(b1_split[1].split(",")) - len(b1_split[1].split("=")) + 1
            kp = kp_hash[b1_split[0] + str(pp)]
            mdtp = mdtp_hash[b1_split[0] + str(pp)]
            kpdtp = kpdtp_hash[b1_split[0] + str(pp)]
            actual_params = b1_split[1].split(",")
            param_no = 1
            for j in range(pp):
                aptab[param_no] = actual_params[param_no - 1]
                aptab_inverse[actual_params[param_no - 1]] = param_no
                param_no += 1

            i = kpdtp - 1
            for j in range(kp):
                temp = kpdt[i].strip().split("\t")
                aptab[param_no] = temp[1]
                aptab_inverse[temp[0]] = param_no
                i += 1
                param_no += 1

            i = pp + 1
            while i <= len(actual_params):
                initialized_params = actual_params[i - 1].split("=")
                aptab[aptab_inverse[initialized_params[0][1:]]] = initialized_params[1]
                i += 1

            i = mdtp - 1
            while mdt[i].strip().upper() != "MEND":
                f1.write("+ ")
                j = 0
                while j < len(mdt[i]):
                    if mdt[i][j] == '#':
                        j += 1
                        f1.write(aptab[int(mdt[i][j])])
                    else:
                        f1.write(mdt[i][j])
                    j += 1
                f1.write("\n")
                i += 1

            aptab.clear()
            aptab_inverse.clear()
        else:
            f1.write("+ " + line)

print("Pass2.txt file has been generated successfully.")
