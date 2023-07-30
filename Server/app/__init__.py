import json
import customtkinter as ctk
import tkinter as tk

ctk.set_appearance_mode('dark')

#This window will show the builder options
class BuilderWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title('Arcane | Builder')
        self.geometry('300x300')
        self.resizable(False, False)

#This window will be used for settings
class SettingsWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title('Arcane | Settings')
        self.geometry('300x300')
        self.resizable(False, False)

#This window will be used for showing developer information
class AboutWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title('Arcane | About')
        self.geometry('300x300')
        self.resizable(False, False)


#Main Window
class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title('Arcane')
        self.geometry('900x500')
        self.resizable(False, False)

        #Build Side Nav
        self.side_nav = ctk.CTkFrame(master=self, width=200, height=490, fg_color='#121313').grid(padx=5, pady=5, row=0, column=0)
        self.side_label = ctk.CTkLabel(master=self.side_nav, width=100, height=50, fg_color='#121313', bg_color='#121313', text_color='#b8086b', text='Arcane', font=ctk.CTkFont(size=20)).grid(padx=5, pady=(5, 440), row=0, column=0)
        self.builder_window = ctk.CTkButton(master=self.side_nav, height=50, width=150, fg_color='#3d3a3c', bg_color='#3d3a3c', text_color='#b8086b', text='Builder', hover_color='#3d3a3c', font=ctk.CTkFont(size=15), command=lambda: BuilderWindow()).grid(padx=5, pady=(5, 320), row=0, column=0)
        self.settings_window = ctk.CTkButton(master=self.side_nav, height=50, width=150, fg_color='#3d3a3c', bg_color='#3d3a3c', text_color='#b8086b', text='Settings', hover_color='#3d3a3c', font=ctk.CTkFont(size=15), command=lambda: SettingsWindow()).grid(padx=5, pady=(5, 200), row=0, column=0)
        self.about_window = ctk.CTkButton(master=self.side_nav, height=50, width=150, fg_color='#3d3a3c', bg_color='#3d3a3c', text_color='#b8086b', text='About', hover_color='#3d3a3c', font=ctk.CTkFont(size=15), command=lambda: AboutWindow()).grid(padx=5, pady=(5, 80), row=0, column=0)


        #Build Command Display
        self.main_frame = ctk.CTkFrame(master=self, height=490, width=680, fg_color='#121313').grid(padx=5, pady=5, row=0, column=1)