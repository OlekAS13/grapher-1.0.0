from tkinter import *

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

function = ("y = {} x^2 + {} + {}".format(a, b, c))

print(function)

# a = 0.5
# b = 0
# c = 1

root = Tk()
# root.title("Funkcja kwadratowa")
root.title("Grapher v1.0.0 | " + function)

sx = IntVar(value=20)
sy = IntVar(value=20)

canv = Canvas(root, width=801, height=801, background="white")
canv.pack(side="left")


def drawScales():
    canv.create_line(0, 400, 800, 400, fill="black") # oś X
    canv.create_line(400,0, 400, 800, fill="black") # oś Y

    for i in range(0, 400, sx.get()):
        canv.create_line(400+i, 395, 400+i, 405, fill="black") # rysujemy podziałkę od środka, żeby było symetrycznie wzgl. (0,0)
        canv.create_line(400-i, 395, 400-i, 405, fill="black")

    for i in range(0, 400, sy.get()):
        canv.create_line(395, 400+i, 405, 400+i, fill="black") # tu podobnie, od środka, jak na osi X
        canv.create_line(395, 400-i, 405, 400-i, fill="black")


def drawChart():
    step = 0.1 # ustalamy krok, co ile przesuwać się w obliczeniach kolejnego punktu

    # wyliczamy pierwszy punkt wykresu (najbardziej skrajny na lewo)
    x = -400 / sx.get()
    y = a * pow(x, 2) + b * x + c

    ox = x * sx.get() + 400 # (ox, oy) to punkt, od którego zacząć rysowanie kolejnego odcinka wykresu
    oy = -y * sy.get() + 400

    while x < 401:
        x += step # przesuwamy się o kolejny krok
        y = a * pow(x, 2) + b * x + c
        px = x * sx.get() + 400 # (px, py) to punkt, w którym skończyć rysowanie kolejnego odcinka wykresu
        py = -y * sy.get() + 400

        canv.create_line(ox, oy, px, py, fill="blue") # rysujemy odcinek od (ox, oy) do (px, py)

        ox = px # koniec stanie się nowym początkiem
        oy = py

def redraw(newScale):
    canv.delete("all")
    drawScales()
    drawChart()

scaleX = Scale(root, from_=1, to=100, variable=sx, label="Scale X", orient=HORIZONTAL, command=redraw)
scaleY = Scale(root, from_=1, to=100, variable=sy, label="Scale Y", orient=HORIZONTAL, command=redraw)
scaleY.pack(side="right")
scaleX.pack(side="right")

drawScales()
drawChart()

root.mainloop()
