import googletrans

class Translator():
    def __init__(self, chaine, langue):
        self.chaine=chaine
        self.langue=langue
        self.translator = googletrans.Translator()
    
    def detect_language(self):
        return self.translator.detect(self.chaine).lang
    
    def translate(self):
            detected_lang = self.detect_language()
            print(detected_lang)
            translation = self.translator.translate(self.chaine, dest=self.langue)
            return f"{detected_lang} -> {self.langue}: {translation.text}"
        
""" t=Translator("Bonjour, comment ça va?", "fr")
result = t.translate()
print(result) """