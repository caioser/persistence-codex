import string as s
import firefox_webdriver as f
import json

class MorseChar:
    def __init__(self, char, dahdit):
        self.char = char
        self.dahdit = dahdit
        self.graphical_representation()
        self.n = ord(char)

    def graphical_representation(self):
        replaces = [["\n", "-", "dah", "dit", "di"],
                    ["", "", "-", ".", "."]]
        self.code = self.dahdit
        for x, y in zip(replaces[0], replaces[1]):
            self.code = self.code.replace(x, y)

    def __repr__(self) -> str:
        return self.__dict__
    
    def __str__(self) -> str:
        return f"< {self.char} > [ {self.code} ]"


class MorseDict:
    d = {}

    def add(self, morseChar):
        self.d[morseChar.char] = morseChar



morse_dict = MorseDict()
morse_dict2 = {}
a = f.driver()
a.get("https://morsecode.world/international/morse.html")
f.WebDriverWait(a, 5).\
    until(f.EC.visibility_of_all_elements_located((f.By.CSS_SELECTOR, "table")))


selected_characters = []
for x in [s.ascii_letters, s.digits, s.punctuation]:
    selected_characters.extend(x)

tables = a.find_elements(f.By.CSS_SELECTOR, "table.dotdash")
starts = ["letter", "digit", "punctuation"]
tables_wanted = []
for table in tables:
    for start in starts:
        if table.text.lower().startswith(start) and "morse" in table.text.lower():
            tables_wanted.append(table)

for t in tables_wanted:
    tr = t.find_elements(f.By.CSS_SELECTOR, "tr")
    for row in tr:
        span_inside = row.find_elements(f.By.CSS_SELECTOR, "span")
        if len(span_inside):
            if span_inside[0].text in selected_characters:
                mc = MorseChar(
                    span_inside[0].text,
                    row.find_elements(f.By.CSS_SELECTOR, "td")[-1].text
                )
                morse_dict2.update({mc.char:mc.code})

                morse_dict.add(mc)