#!/usr/bin/python
#coding: utf-8

#       CopyRight 2013 Allan Psicobyte (psicobyte@gmail.com)
#
#       This program is free software: you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation, either version 3 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program.  If not, see <http://www.gnu.org/licenses/>.


import sys, Image, ImageDraw

Iterations= 5
Gallery= 20

WIDTH= 1200
HEIGHT= 800

LINE= 4


TableauName= "PiMondrian"

if len(sys.argv) > 1:
    argumento = sys.argv[1]
else:
    argumento = ""

Fichero = open("10000pi.txt")
Cadena= Fichero.read()
Fichero.close()

PI = list(Cadena)

ArrayCuadros= []



class SubRectangle:
    """crea un rectángulo con coordenadas y color como subdivisión de un rectágulo padre"""
    def __init__(self, orden, division, color, parent= None):

        self.Parent= parent
        self.Color= color

        if parent is None:
            self.ZeroX= 0
            self.ZeroY= 0
            self.EndX= WIDTH
            self.EndY= HEIGHT
            self.VorH= "V"
            self.Generation= 0

        else:

            self.Generation= parent.Generation + 1
            
            if parent.VorH == "V":
                self.VorH= "H"

                if orden == 1:
                    self.ZeroX= parent.ZeroX
                    self.ZeroY= parent.ZeroY
                    self.EndX= Division(parent.ZeroX, parent.EndX, division)
                    self.EndY= parent.EndY

                elif orden == 2:
                    self.ZeroX= Division(parent.ZeroX, parent.EndX, division)
                    self.ZeroY= parent.ZeroY
                    self.EndX= parent.EndX
                    self.EndY= parent.EndY

            elif parent.VorH == "H":
                self.VorH= "V"

                if orden == 1:
                    self.ZeroX= parent.ZeroX
                    self.ZeroY= parent.ZeroY
                    self.EndX= parent.EndX
                    self.EndY= Division(parent.ZeroY, parent.EndY, division)

                elif orden == 2:
                    self.ZeroX= parent.ZeroX
                    self.ZeroY= Division(parent.ZeroY, parent.EndY, division)
                    self.EndX= parent.EndX
                    self.EndY= parent.EndY



def DivideRectangle(parent):
    """Toma los siguientes tres dígitos de Pi, y divide el cuadro en dos usando como proporción el primero de esos tres dígitos. Los otros dos digitos asignan el color de los cuadros """
    global PI, ArrayCuadros
 
    division= int(PI.pop(0))
    color1= int(PI.pop(0))
    color2= int(PI.pop(0))

    ArrayCuadros.append(SubRectangle(1,division,color1,parent))
    ArrayCuadros.append(SubRectangle(2,division,color2,parent))


def Division(corta,larga,division):
    """Calcula el punto que coresponde a 'división' décimas partes entre 'corta' y 'larga' """

    if division == 0:
        resultado= larga

    else:
        resultado= corta + ((larga - corta) * division / 10)
        resultado= round(resultado,0)

    return resultado


def PintaCuadro(generation,name):

    global WIDTH, HEIGHT, LINE, ArrayCuadros

    img = Image.new("RGB", (WIDTH, HEIGHT), "#000000")

    draw = ImageDraw.Draw(img)

    for elemento in ArrayCuadros:

        if elemento.Color == 0:
            FillColor= "#FFFFFF"
        if elemento.Color == 1:
            FillColor= "#FFFFFF"
        if elemento.Color == 2:
            FillColor= "#FFFFFF"
        if elemento.Color == 3:
            FillColor= "#AA0000"
        if elemento.Color == 4:
            FillColor= "#AA0000"
        if elemento.Color == 5:
            FillColor= "#0000AA"
        if elemento.Color == 6:
            FillColor= "#0000AA"
        if elemento.Color == 7:
            FillColor= "#000000"
        if elemento.Color == 8:
            FillColor= "#000000"
        if elemento.Color == 9:
            FillColor= "#AAAA00"

        linea= round(LINE / 2,0)

        if elemento.Generation == generation:
            draw.rectangle([(elemento.ZeroX + linea, elemento.ZeroY + linea), (elemento.EndX - linea, elemento.EndY - linea)], outline="#000000", fill= FillColor)
    name = name + ".png"
    img.save(name, "PNG")


def Inspiration(Iterations):

    global ArrayCuadros

    ArrayCuadros= []
    # Creamos el rectángulo raiz
    ArrayCuadros.append(SubRectangle(1,0,0))

    # Creamos el resto de rectángulos
    i = 0
    while i < Iterations:
        for elemento in ArrayCuadros:
            if elemento.Generation == i:
                DivideRectangle(elemento)
        i = i + 1


if argumento == "generation":
    Inspiration(Iterations)
    i = 1
    while i <= Iterations:
        nombrecuadro= TableauName + str(i)
        PintaCuadro(i,nombrecuadro)
        i = i + 1


if argumento == "gallery":
    i = 1
    while i <= Gallery:
        Inspiration(Iterations)
        nombrecuadro= TableauName + str(i)
        PintaCuadro(Iterations,nombrecuadro)
        i = i + 1

else:
    Inspiration(Iterations)
    PintaCuadro(Iterations,TableauName)

