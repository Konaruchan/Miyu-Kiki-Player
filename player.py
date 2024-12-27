import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import webbrowser
import requests
import shutil
import win32com.client
from music_manager import MusicManager
from defi_parser import DefiParser

class MiyuKikiPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Miyu-kiki Chaos Club")
        self.root.geometry("400x300")

        # Icono personalizado
        self.root.iconbitmap('icon.ico')

        # Botones iniciales usando un estilo más bonito
        self.button_frame = ttk.Frame(self.root)
        self.button_frame.pack(fill=tk.BOTH, expand=True)

        self.play_button = tk.Button(self.button_frame, text="Play", command=self.start_game)
        self.play_button.grid(row=0, column=0, sticky="nsew")

        self.update_button = tk.Button(self.button_frame, text="Check for Updates", command=self.check_for_updates)
        self.update_button.grid(row=0, column=1, sticky="nsew")

        self.changelog_button = tk.Button(self.button_frame, text="Changelog", command=self.show_changelog)
        self.changelog_button.grid(row=1, column=0, sticky="nsew")

        self.manga_button = tk.Button(self.button_frame, text="Original Manga", command=self.open_manga_link)
        self.manga_button.grid(row=1, column=1, sticky="nsew")

        for i in range(2):
            self.button_frame.columnconfigure(i, weight=1)
            self.button_frame.rowconfigure(i, weight=1)

        # Instancias y configuración inicial
        self.ppt_app = win32com.client.Dispatch("PowerPoint.Application")
        self.ppt_app.WindowState = 2  # Maximizar la ventana de PowerPoint
        self.music_manager = MusicManager()
        self.defi_parser = DefiParser("./GameFiles/Definitions/miyu_kiki.defi")
        self.presentation = None
        self.current_slide = None
        self.current_music = None

    def start_game(self):
        # Inicia el juego y oculta los botones iniciales
        self.button_frame.pack_forget()

        self.quick_save_button = tk.Button(self.root, text="Quick Save", command=self.quick_save)
        self.quick_save_button.pack(pady=10)

        self.quick_load_button = tk.Button(self.root, text="Quick Load", command=self.quick_load)
        self.quick_load_button.pack(pady=10)

        self.load_shika("./GameFiles/Shika/miyu_kiki.shika")

        if self.presentation:
            self.current_slide = 1
            self.play_slide(self.current_slide)

        self.root.after(100, self.check_slide_changes)

    def convert_to_pptx(self, file_path):
        if file_path.endswith(".shika"):
            pptx_path = file_path.replace(".shika", "_copy.pptx")
            if not os.path.exists(pptx_path):
                shutil.copy(file_path, pptx_path)  # Crea una copia con la extensión correcta
            return pptx_path
        return file_path

    def load_shika(self, file_path):
        file_path = self.convert_to_pptx(file_path)
        absolute_path = os.path.abspath(file_path)
        print(f"Ruta absoluta del archivo: {absolute_path}")

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Archivo {file_path} no encontrado.")

        print(f"Cargando presentación: {file_path}")
        try:
            self.presentation = self.ppt_app.Presentations.Open(absolute_path, ReadOnly=False, WithWindow=True)
            print(f"Presentación {absolute_path} cargada exitosamente.")
            self.presentation.SlideShowSettings.Run()
        except Exception as e:
            print(f"Error al cargar la presentación: {e}")
            self.presentation = None

    def play_slide(self, slide_number):
        music_file = self.defi_parser.get_music(slide_number)

        if music_file and music_file != self.current_music:
            music_path = f"./GameFiles/BGM/{music_file}"
            if not os.path.exists(music_path):
                raise FileNotFoundError(f"Archivo de música {music_path} no encontrado.")
            self.music_manager.play_music(music_path)
            self.current_music = music_file

        if self.presentation:
            try:
                current_index = self.presentation.SlideShowWindow.View.Slide.SlideIndex
                if current_index != slide_number:
                    self.presentation.SlideShowWindow.View.GotoSlide(slide_number)
            except Exception as e:
                print(f"Error al cambiar de diapositiva: {e}")

    def check_slide_changes(self):
        try:
            if self.presentation and self.presentation.SlideShowWindow:
                current_slide_index = self.presentation.SlideShowWindow.View.Slide.SlideIndex
                if current_slide_index != self.current_slide:
                    self.current_slide = current_slide_index
                    self.play_slide(self.current_slide)
        except Exception as e:
            print(f"Error al verificar cambios de diapositiva: {e}")

        self.root.after(100, self.check_slide_changes)

    def quick_save(self):
        try:
            with open("save_state.txt", "w") as save_file:
                save_file.write(str(self.current_slide))
            messagebox.showinfo("Quick Save", "Game saved successfully!")
        except Exception as e:
            messagebox.showerror("Quick Save", f"Error saving game: {e}")

    def quick_load(self):
        try:
            with open("save_state.txt", "r") as save_file:
                saved_slide = int(save_file.read().strip())
                self.current_slide = saved_slide
                self.play_slide(self.current_slide)
            messagebox.showinfo("Quick Load", "Game loaded successfully!")
        except Exception as e:
            messagebox.showerror("Quick Load", f"Error loading game: {e}")

    def check_for_updates(self):
        self.show_loading_bar("Checking for updates...")
        repo_url = "https://github.com/KonaruChan/Miyu-Kiki-Player/raw/main/Last%20Shika/"
        try:
            response = requests.get(repo_url + "ActualVersion.txt")
            response.raise_for_status()
            actual_version = response.text.strip().splitlines()

            game_version_remote = actual_version[0].split(": ")[1]
            client_version_remote = actual_version[1].split(": ")[1]

            with open("Game_version.txt", "r") as f:
                game_version_local = f.read().strip()

            with open("Client_Version.txt", "r") as f:
                client_version_local = f.read().strip()

            if game_version_local < game_version_remote:
                self.update_shika(repo_url)

            if client_version_local < client_version_remote:
                messagebox.showinfo("Update Available", "New client version available. Please update manually.")
            else:
                messagebox.showinfo("No Updates", "Your game is up to date.")
        except Exception as e:
            messagebox.showerror("Update Error", f"Error checking for updates: {e}")
        finally:
            self.hide_loading_bar()

    def update_shika(self, repo_url):
        self.show_loading_bar("Updating Shika...")
        try:
            response = requests.get(repo_url + "miyu_kiki.shika", stream=True)
            response.raise_for_status()

            local_shika_path = "./GameFiles/Shika/miyu_kiki.shika"
            with open(local_shika_path, "wb") as f:
                shutil.copyfileobj(response.raw, f)

            # Download changelog
            response = requests.get(repo_url + "Changelogs.pdf", stream=True)
            response.raise_for_status()
            with open("Changelogs.pdf", "wb") as f:
                shutil.copyfileobj(response.raw, f)

            messagebox.showinfo("Update Complete", "Shika updated successfully!")
        except Exception as e:
            messagebox.showerror("Update Error", f"Error updating Shika: {e}")
        finally:
            self.hide_loading_bar()

    def show_loading_bar(self, text):
        self.loading_window = tk.Toplevel(self.root)
        self.loading_window.title("Loading")
        self.loading_window.geometry("300x100")

        tk.Label(self.loading_window, text=text).pack(pady=10)
        self.progress_bar = ttk.Progressbar(self.loading_window, mode='indeterminate')
        self.progress_bar.pack(pady=10)
        self.progress_bar.start()

    def hide_loading_bar(self):
        self.progress_bar.stop()
        self.loading_window.destroy()

    def show_changelog(self):
        try:
            os.startfile("Changelogs.pdf")
        except Exception as e:
            messagebox.showerror("Changelog Error", f"Error opening changelog: {e}")

    def open_manga_link(self):
        webbrowser.open("https://shikashimonthlyfriday.com/es/")

if __name__ == "__main__":
    root = tk.Tk()
    app = MiyuKikiPlayer(root)
    root.mainloop()
