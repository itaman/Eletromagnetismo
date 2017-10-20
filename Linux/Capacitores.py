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
a=1
while a:
    os.system("clear")
    opc=raw_input('Calcular capacitância do capacitor:\nPlano (P)\nCilíndrico (C)\nEsférico (E)\n \nOu S para sair\nOpção: ')
    while opc not in ['P','p','C','c','E','e','S','s']:
	os.system("clear")
	opc=raw_input('Calcular capacitância do capacitor:\nPlano (P)\nCilíndrico (C)\nEsférico (E)\n \nOu S para sair\nOpção: ')

    if opc in ['P','p']:
	os.system("python CapacitorFlat.py")
    if opc in ['C','c']:
	os.system("python CapacitorCyl.py")
    if opc in ['E','e']:
	os.system("python CapacitorSph.py")
    if opc in ['S','s']:
	a=0
