import sys
import tkinter as tk
from player import MiyuKikiPlayer

def main():
    print("Iniciando Miyu-kikiPlayer...")
    root = tk.Tk()
    player = MiyuKikiPlayer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
