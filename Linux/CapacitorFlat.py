# -*- coding: UTF-8 -*-
"""
Copyright (c) 2017 Itaman Cavalcanti de Oliveira <itamanman@yahoo.com.br>

Este programa é um software livre; você pode redistribui-lo e/ou 
modifica-lo dentro dos termos da Licença Pública Geral Menor GNU como 
publicada pela Fundação do Software Livre (FSF); na versão 3 da 
Licença, ou (na sua opnião) qualquer versão.

Este programa é distribuido na esperança que possa ser  util, 
mas SEM NENHUMA GARANTIA; sem uma garantia implicita de ADEQUAÇÂO
a qualquer MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a Licença
Pública Geral GNU para maiores detalhes em <www.gnu.org>.

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public License
as published by the Free Software Foundation; either version 3
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details at www.gnu.org
"""
import os
import numpy
def menu():
    os.system("clear")
    optm=raw_input('Sair (0)\nEntrada de Dados (1)\nResultado(2)\nOpção: ')
    while optm not in ['0', '1', '2']:
	os.system("clear")
	optm=raw_input('Sair (0)\nEntrada de Dados (1)\nResultado(2)\nOpção: ')
    return int(optm)
  

def dados ():
    os.system("clear")
    muda=raw_input('Desesja mudar os dados? (S ou N)')
    while muda not in ['S','s','N','n']:
	muda=raw_input('Desesja mudar os dados? (S ou N)')
    if muda in ['S', 's']:
	global l
	l=input('\nEntre com a profundidade do capacitor: ')
	while l<=0:
	    l=input('\nEntre com a profundidade do capacitor: ')
	d=input('\nEm quantas divisões o capacitor é particionado ao longo da largura em materiais diferentes?\n')
	print '\nPara cada divisão, entre com o número de camadas de dielétricos diferentes: \n'
	global camadas
	camadas = [0]*d
	for k in range(d):
	    camadas[k]=input('Divisão %d - Números de camadas: ' %(k+1))
	    
	print 'Para cada divisão, entre com sua largura'
	global div
	div =[0]*d
	for k in range(d):
	    div[k]=input('Divisão %d - Largura: ' %(k+1))
	print 'Para cada divisão do capacitor, entre com a altura e sua respectiva permissividade relativa'
	global alt
	alt=numpy.array([[0]*max(camadas)]*d,float)
	global epsilonRi
	epsilonRi=numpy.array([[0]*max(camadas)]*d,float)
	for k in range(d):
	    for j in range(camadas[k]):
		print '\nDivisão ', k+1, 'Camada ', j+1
		alt[k,j]=input('Altura: ')
		epsilonRi[k,j]=input('Permissividade relativa: ')
	
    data=1
    return data

def calcC():
    C=0
    for k in range (len(camadas)):
	Cs=0
	for j in range(camadas[k]):
	    Cs=Cs+float(alt[k,j])/(float(epsilonRi[k,j])*epsilon0*float(l)*float(div[k]))
	C=C+1/Cs
    return C
  
  
data=0
epsilon0=8.854e-12
opt=menu()
while opt!=0:
    if opt==1:
	data=dados()
	os.system("clear")
    if opt==2:
	if data==0:
	    print "\nAinda não houve entrada de dados"
	    raw_input('\nAperte ENTER para voltar a tela inicial')
	    os.system("clear")
	if data==1:
	    os.system("clear")
	    print "Dados finais"
	    Cap=calcC()
	    print "A capacitância é igual à",Cap, "F."
	    raw_input()
    opt=menu()
 

