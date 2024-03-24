import flet as ft
from flet import *
import subprocess

def main(page:Page)->None:
    def runCommand(e):
        global command,run
        outputFiled.value=""
        x=text.value.split()
        command=subprocess.Popen(x,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        run=True
        for line in command.stdout:
            outputFiled.value+=line.strip()+"\n"
            page.update()
        command.wait()
        run=False
    def stopCommand(e):
        if (run):
            command.terminate()
            command.stdout.close()
            page.update()
    page.vertical_alignment='start'
    page.horizontal_alignment='center'
    page.bgcolor="gray"
    page.padding=20
   # page.window_width=200
    page.scroll='auto'
 #   page.window_center()
    btnRun=ElevatedButton(text="Run",color='white',bgcolor='green',icon="PLAY_CIRCLE_OUTLINE",width=page.window_width,on_click=runCommand)
    btnStop=ElevatedButton(text="Stop",icon="STOP_CIRCLE_OUTLINED",color='white',bgcolor='red',width=page.window_width,on_click=stopCommand)
    h1=Text(value="Command line")
    text=TextField(hint_text="Enter your command ")

    outputFiled=Text(value="",color="white")
                     
    outputFiledContainer=Container(content=outputFiled,
                          width=page.window_width,
                          padding=padding.all(20),
                          bgcolor="black"
                          )
    
    page.add(h1,text,btnRun,btnStop,outputFiledContainer)
    page.update()
ft.app(target=main)
