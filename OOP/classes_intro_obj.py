from classes_intro_blueprints import Pessoa
from classes_intro_blueprints import escola
from classes_intro_blueprints import medida
from classes_intro_blueprints import medida_peso
from classes_intro_blueprints import morada
from classes_intro_blueprints import minha_escola
from classes_intro_blueprints import musica_favorita

pessoa = Pessoa("Gonçalo", 17)
ba = escola (2549)
altura = medida (1.78)
peso = medida_peso (64)
casa = morada ("vila chã")
epbjc = minha_escola ("EPBJC")
musica = musica_favorita ("travis scott")

 
print(pessoa.saudacao())
print(ba.saudacao())
print(altura.alturas())
print(peso.peso_eu())
print(casa.minha_morada())
print(epbjc.a_minha_escola())
print(musica.musica_favorita())