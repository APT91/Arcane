import os, sys, socket, json, hashlib, colorama, PIL
import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title('ArcaneRAT')
        self.geometry('700x500')
        self.resizable(False, False)