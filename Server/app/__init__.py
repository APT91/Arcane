import os, sys, socket, json, hashlib, colorama, PIL
import customtkinter as ctk

ctk.set_appearance_mode('dark')

#This window will show the builder options
class BuilderWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

#This window will be used for settings
class SettingsWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

#This window will be used for showing developer information
class AboutWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

#Main Window
class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title('ArcaneRAT')
        self.geometry('700x500')
        self.resizable(False, False)