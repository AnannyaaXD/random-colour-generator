# -*- coding: utf-8 -*-
"""
Created on Sun May 28 15:26:27 2023

@author: Chiyo
"""

from tkinter import *
import random

root = Tk()
root.title("Colours")
root.geometry("500x500")

Colours = ["AntiqueWhite1" , "AntiqueWhite2" , "AntiqueWhite3" , "AntiqueWhite4" ,
           "CadetBlue1" , "CadetBlue2" , "CadetBlue3" , "CadetBlue4" , 
           "DarkGoldenrod1" , "DarkGoldenrod2" , "DarkGoldenrod3" , "DarkGoldenrod4" , 
           "DarkOliveGreen1" , "DarkOliveGreen2" ,"DarkOliveGreen3" , "DarkOliveGreen4" , 
           "DarkOrange1" , "DarkOrange2" , "DarkOrange3" , "DarkOrange4" , 
           "DarkOrchid1" , "DarkOrchid2" , "DarkOrchid3" , "DarkOrchid4" , 
           "DarkSeaGreen1" , "DarkSeaGreen2" , "DarkSeaGreen3" , "DarkSeaGreen4" , 
           "DarkSlateGray1" , "DarkSlateGray2" , "DarkSlateGray3" , "DarSlateGray4" , 
           "DeepPink2" , "DeepPink3" , "DeepPink4" , 
           "DeepSkyBlue2" , "DeepSkyBlue3" , "DeepSkyBlue4" , 
           "DodgerBlue2" , "DodgerBlue3" , "DodgerBlue4" , 
           "HotPink1" , "HotPink2" , "HotPink3" , "HotPink4" , 
           "IndianRed1" , "IndianRed2" , "IndianRed3" , "IndianRed4" , 
           "LavenderBlush2" , "LavenderBlush3" , "LavenderBlush4" , 
           "LemonChiffon2" , "LemonChiffon3" , "LemonChiffon4" , 
           "LightBlue1" , "LightBlue2" , "LightBlue3" , "LightBlue4" , 
           "LightCyan2" , "LightCyan3" , "LightCyan4" , 
           "LightGoldenrod1" , "LightGoldenrod2" , "LightGoldenrod3" , "LightGoldenrod4" , 
           "LightPink1" , "LightPink2" , "LightPink3" , "LightPink4" , 
           "LightSalmon2" , "LightSalmon3" ,  "LightSalmon4" , 
           "LightSkyBlue1" , "LightSkyBlue2" , "LightSkyBlue3" , "LightSkyBlue4" , 
           "LightSteelBlue1" , "LightSteelBlue2" , "LightSteelBlue3" , "LightSteelBlue4" , 
           "LightYellow2" , "LightYellow3" , "LightYellow4" , 
           "MediumOrchid1" , "MediumOrchid2" , "MediumOrchid3" , "MediumOrchid4"
           "MediumPurple1" , "MediumPurple2" , "MediumPurple3" , "MediumPurple4" , 
           "MistyRose2" , "MistyRose3" , "MistyRose4" , 
           "NavajoWhite2" , "NavajoWhite3" , "NavajoWhite4" , 
           "OliveDrab1" , "OliveDrab2" , "OliveDrab4" , 
           "OrangeRed2" , "OrangeRed3" , "OrangeRed4" , 
           "PaleGreen1" , "PaleGreen2" , "PaleGreen3" , "PaleGreen4" , 
           "PaleTurquoise1" , "PaleTurquoise2" , "PaleTurquoise3" , "PaleTurquoise4" , 
           "PaleVioletRed1" , "PaleVioletRed2" , "PaleVioletRed3" , "PaleVioletRed4" , 
           "PeachPuff2" , "PeachPuff3" , "PeachPuff4" , 
           "RosyBrown1" , "RosyBrown2" , "RosyBrown3" , "RosyBrown4" , 
           "RoyalBlue1" , "RoyaBlue2" , "RoyalBlue3" , "RoyalBlue4" , 
           "SeaGreen1" , "SeaGreen2" , "SeaGreen3" , 
           "SkyBlue1" , "SkyBlue2" , "SkyBlue3" , "SkyBlue4" , 
           "SlateBlue1" , "SlateBlue2" , "SlateBlue3" , "SlateBlue4" , 
           "SlateGray1" , "SlateGray2" , "SlateGray3" , "SlateGray4" , 
           "SpringGreen2" , "SpringGreen3" , "SpringGreen4" , 
           "SteelBlue1" , "SteelBlue2" , "SteelBlue3" , "SteelBlue4" , 
           "VioletRed1" , "VioletRed2" , "VioletRed3" , "VioletRed4" , 
           "alice blue" , 
           "antique white" , 
           "aquamarine" , "aquamarine2" , "aquamarine4" , 
           "azure" , "azure2" , "azure3" , "azure4" , 
           "bisque" , "bisque2" , "bisque3" , "bisque4" , 
           "blanched almond" , 
           "blue" , "blue violet" , "blue2" , "blue4" , 
           "brown1" , "brown2" , "brown3" , "brown4" , 
           "burlywood1" , "burlywood2" , "burlywood3" , "burlywood4" , 
           "cadet blue" , 
           "chartreuse2" , "chartreuse3" , "chartreuse4" , 
           "chocolate1" , "chocolate2" , "chocolate3" , 
           "coral" , "coral1" , "coral2" , "coral3" , "coral4" , 
           "cornflower" , 
           "cornsilk2" , "cornsilk3" , "cornsilk4" , 
           "cyan" , "cyan2" , "cyan3" , "cyan4" , 
           "dark goldenrod" , "dark green" , "dark turquoise" , "dark violet" , "dark khaki" , "dark olive green" , "dark orange" , "dark orchid" , "dark salmon" , "dark sea green" , 
           "dark slate blue" , "dark slate gray" , 
           "deep pink" , "deep sky blue" , 
           "dim gray" , 
           "dodger blue" , 
           "firebrick1" , "firebrick2" , "firebrick3" , "firebrick4"]

def random_colour_generator():
    random_colours = random.randint(0 , 100)
    print([Colours][random_colours])
    root.configure(background = [Colours][random_colours])

btn = Button(root , text="Click To Change Background Colour" , command=random_colour_generator)
btn.place(relx=0.5 , rely=0.5 , anchor=CENTER)

root.mainloop()