import string as s
import pyperclip as clip
import json
import qrcode
import cv2
from random import choice



def four_diff_chars():
    char_type = [
        s.ascii_uppercase,
        s.ascii_lowercase,
        s.digits,
        s.punctuation
    ]
    which = list(range(len(char_type)))
    gen = []
    while len(which):
        temp = choice(which)
        gen.append(choice(char_type[temp]))
        # print(gen, temp, which, sep=" from: ", end=" --> ")
        which.remove(temp)
        # print(which)
    return "".join(gen)

def joining_gens(n=4):
    new_pass = []
    for x in range(n):
        new_pass.append(four_diff_chars())
    return "".join(new_pass)

def pass_options(n=16):
    opts = []
    for x in range(n):
        opts.append(joining_gens())
        print(opts[x])
    return opts

def password_gen():
    whatever = pass_options()
    only_one = choice(whatever)
    img = qrcode.make(only_one)
    img.save("data/whatever.png")
    clip.copy(only_one)


class Chave:
    def __init__(self) -> None:
        try:
            self.main_key_read()
        except:
            print("txt not found")

    def main_key_gen():
        with open("data/chave.txt", "r") as txt:
            key = txt.read()

        img = qrcode.make(key)
        img.save("data/chave.png")

    def main_key_read(self):
        img = cv2.imread("data/chave.png")
        det = cv2.QRCodeDetector()
        # val, pts, st_code 
        self.a, self.b, self.c = det.detectAndDecode(img)
        # print(self.a)

    @property
    def bin(self):
        return [["1" if x > 0 else "0" for x in arr] for arr in self.c]
    
    def visual(self, on="-", off="."):
        """https://morsecode.world/american/morse.html"""
        return ["".join([on if int(x) > 0 else off for x in arr]) for arr in self.c]
    
    def see(self, on, off):
        """https://python-tcod.readthedocs.io/en/latest/tcod/charmap-reference.html"""
        for a in range(4):
            print(on*(len(self.c[0])+8))
        for x in self.visual(on, off):
            print(on*4, x, on*4, sep="")
        for b in range(4):
            print(on*(len(self.c[0])+8))#u"\u2588"



chave = Chave()
in_morse = chave.visual()

with open("data/morse_dict.json", "r") as j:
    morse_dict = json.loads(j.read())

# unique_lengths. ex:[15, 6, 5, 4, 3, 2, 1]
u = list(set(map(len, list(morse_dict.values()))))[::-1]
# k = [(k,v) for k, v in morse_dict.items() if len(v) == 5]


# t = in_morse[0]
# _sep = "       "
temp_tries = u
my_cryp = []
for t in in_morse:
    # print("iniciando =====================", t, temp_tries, sep="\n")
    for length in temp_tries:
        k = [(k,v) for k, v in morse_dict.items() if len(v) == length]
        # print("for length = ", length, " will be used:")
        # print(k)
        
        while len(k):
            # print("while length of k is not 0 ===================", k, sep="\n")
            replaces = []
            efficiency = 0
            # print(f"replaces = {replaces}", f"efficiency {efficiency}", f"len(k) = {len(k)}", sep="\n")
            # print(" "*length, " ", f'.{t.count(".")} -{t.count("-")}', t, sep=_sep)
            for code in k:
                is_eff = ""
                replaces.append(t.replace(code[1], code[0]))
                if len(replaces[-1]) < len(replaces[efficiency]):
                    efficiency = k.index(code)
                    is_eff = "[EFFICIENCY]"
                # t = t.replace(code[1], code[0])
                # print(code[1], code[0], f'.{replaces[-1].count(".")} -{replaces[-1].count("-")}', replaces[-1], is_eff, sep=_sep)

            # print("most efficienty is ", efficiency ,k[efficiency], " and popped from 'k'; 't' replaced:")
            t = t.replace(k[efficiency][1], k[efficiency][0])
            # print(t)
            k.pop(efficiency)
        
        print("final result: ", t, sep="\n")
    my_cryp.append(t)


def to_morse(s):
    return " ".join([morse_dict.get(x.upper()) if x.upper() in list(morse_dict.keys()) else "/" for x in s])

def see(l_with_crypt, on=u"\u2588", off=" "):
    """https://python-tcod.readthedocs.io/en/latest/tcod/charmap-reference.html"""
    dah_di = []
    for x in l_with_crypt:
        dah_di.append(to_morse(x)\
                        .replace(" ", "")\
                        .replace("-", on+on)\
                        .replace(".", off+off))
        
    to_txt = []
    for a in range(4):
        to_txt.append(on*(len(dah_di[0])+8))
        print(on*(len(dah_di[0])+8))
    for x in dah_di:
        to_txt.append("".join([on*4, x, on*4]))
        print(on*4, x, on*4, sep="")
    for b in range(4):
        to_txt.append(on*(len(dah_di[0])+8))
        print(on*(len(dah_di[0])+8))#u"\u2588"

    # UnicodeEncodeError: 'charmap' codec can't encode characters in position 0-145: character maps to <undefined>
    # with open("data/see_mycryp.txt", "w") as txt:
    #     txt.write("\n".join(to_txt))

see(my_cryp)