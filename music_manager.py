import pygame

class MusicManager:
    def __init__(self):
        pygame.mixer.init()

    def play_music(self, file_path):
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play(-1)  # Loop infinito
    
    def stop_music(self):
        pygame.mixer.music.stop()
    
    def change_music(self, file_path):
        self.stop_music()
        self.play_music(file_path)
