# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 01:27:11 2022

@author: emirh
"""

import PyPDF2
import pyttsx3

pdfReader = PyPDF2.PdfFileReader(open('SesliPdf.pdf', 'rb'))
engine = pyttsx3.init()

for page_num in range(pdfReader.numPages):
    text=pdfReader.getPage(page_num).extractText()
    engine.say("Reader start")
    engine.say("Start introduce")
    engine.say("Car")
    engine.say("Color")
    engine.say("Github")
    engine.say("Breakpoint")
    engine.say("Stackoverflow")
    engine.say(text)
    engine.runAndWait()


engine.stop()

