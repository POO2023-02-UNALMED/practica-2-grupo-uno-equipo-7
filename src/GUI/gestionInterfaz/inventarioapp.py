import tkinter as tk
from tkinter import messagebox
from tkinter import Frame

class inventarioapp(Frame):
    def __init__(self, padre,  controlador):
        super().__init__(padre)
        self.controlador=controlador
        self.configure(background="red")
        
        
        
        
    
    