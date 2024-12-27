import re

class DefiParser:
    def __init__(self, defi_path):
        self.rules = {}  # Almacenará reglas de navegación
        self.music = {}  # Almacenará la música por diapositiva
        self.load_defi(defi_path)

    def load_defi(self, defi_path):
        with open(defi_path, "r") as f:
            for line in f:
                # Si es una regla de música
                if line.startswith("MUSIC"):
                    self._parse_music_rule(line)
                # Si es una regla de navegación
                elif line.startswith("RULE"):
                    self._parse_navigation_rule(line)

    def _parse_music_rule(self, line):
        # Ejemplo: MUSIC,1,main.mp3
        parts = line.strip().split(",")
        diapositiva_range = parts[1]
        music_file = parts[2]
        
        # Si hay un rango de diapositivas, lo procesamos
        if "-" in diapositiva_range:
            start, end = map(int, diapositiva_range.split("-"))
            for i in range(start, end + 1):
                self.music[i] = music_file
        else:
            self.music[int(diapositiva_range)] = music_file

    def _parse_navigation_rule(self, line):
        # Ejemplo: RULE,1,HIPERVINCULO_ONLY
        parts = line.strip().split(",")
        diapositiva_range = parts[1]
        rule = parts[2]
        
        # Si hay un rango de diapositivas, lo procesamos
        if "-" in diapositiva_range:
            start, end = map(int, diapositiva_range.split("-"))
            for i in range(start, end + 1):
                self.rules[i] = rule
        else:
            self.rules[int(diapositiva_range)] = rule

    def get_music(self, slide_number):
        # Devuelve el archivo de música correspondiente a la diapositiva
        return self.music.get(slide_number, None)

    def get_rule(self, slide_number):
        # Devuelve la regla de navegación correspondiente a la diapositiva
        return self.rules.get(slide_number, None)

