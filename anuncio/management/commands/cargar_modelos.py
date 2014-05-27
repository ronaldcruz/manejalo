# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from anuncio.models import Anuncio, Marca, Modelo
from app.models import DataScraping
from demografia.models import Ciudad

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

import datetime
import random
import requests

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        self.stdout.write('Cargando marca y modelos...')

        marcas = [(128, 'Acura'), 
                    (1, 'Aleko'), 
                    (2, 'Alfa Romeo'), 
                    (3, 'Aro'), 
                    (4, 'Asia'), 
                    (130, 'Aston Martin'), 
                    (131, 'Auburn'), 
                    (5, 'Audi'), 
                    (132, 'Austin'), 
                    (133, 'Austin Healey'), 
                    (6, 'Austin Leyland'), 
                    (7, 'Auto Unión'), 
                    (8, 'Autobianchi'), 
                    (235, 'Autorrad'), 
                    (134, 'Avanti'), 
                    (10, 'BMW'), 
                    (294, 'BYD'), 
                    (9, 'Belavtomaz'), 
                    (135, 'Bentley'), 
                    (11, 'Borgward'), 
                    (136, 'Bronto'), 
                    (137, 'Bugatti'), 
                    (12, 'Buggy'), 
                    (13, 'Buick'), 
                    (14, 'Cadillac'), 
                    (379, 'Camara'), 
                    (337, 'Changan'), 
                    (162, 'Chery'), 
                    (15, 'Chevrolet'), 
                    (16, 'Chrysler'), 
                    (17, 'Citroen'), 
                    (172, 'Club Car'), 
                    (138, 'Cord'), 
                    (299, 'DFM'), 
                    (497, 'DFSK'), 
                    (18, 'Dacia'), 
                    (19, 'Daewoo'), 
                    (20, 'Daihatsu'), 
                    (21, 'Datsun'), 
                    (139, 'DeSoto'), 
                    (22, 'Deutz Agrale'), 
                    (23, 'Dodge'), 
                    (336, 'Dongfeng'), 
                    (24, 'Dymex'), 
                    (140, 'Eagle'), 
                    (141, 'Edsel'), 
                    (25, 'Eniak'), 
                    (210, 'FAW'), 
                    (26, 'Ferrari'), 
                    (27, 'Fiat'), 
                    (28, 'Ford'), 
                    (29, 'Ford Importados'), 
                    (305, 'Foton'), 
                    (30, 'G.A.Z.'), 
                    (217, 'GWM'), 
                    (31, 'Galloper'), 
                    (296, 'Geely'), 
                    (32, 'Gmc'), 
                    (189, 'Great Wall'), 
                    (33, 'Grosspal'), 
                    (254, 'Hafei'), 
                    (416, 'Haima'), 
                    (34, 'Henworth'), 
                    (35, 'Hino'), 
                    (36, 'Honda'), 
                    (37, 'Hummer'), 
                    (38, 'Hyundai'), 
                    (39, 'I.E.S.'), 
                    (40, 'Ika'), 
                    (142, 'Infiniti'), 
                    (41, 'Internacional'), 
                    (42, 'Isuzu'), 
                    (43, 'Iveco'), 
                    (304, 'JMC'), 
                    (44, 'Jac'), 
                    (45, 'Jaguar'), 
                    (46, 'Jeep'), 
                    (355, 'Jinbei'), 
                    (47, 'Kamaz'), 
                    (48, 'Kia'), 
                    (49, 'Lada'), 
                    (143, 'Lamborghini'), 
                    (50, 'Lancia'), 
                    (51, 'Land Rover'), 
                    (52, 'Lexus'), 
                    (182, 'Lifan'), 
                    (53, 'Lincoln'), 
                    (144, 'Lotus'), 
                    (58, 'MG'), 
                    (54, 'Mahindra'), 
                    (55, 'Maserati'), 
                    (56, 'Mazda'), 
                    (57, 'Mercedes Benz'), 
                    (169, 'Mercury'), 
                    (59, 'Mini'), 
                    (60, 'Mitsubishi'), 
                    (61, 'Nissan'), 
                    (145, 'Oldsmobile'), 
                    (62, 'Oltcit'), 
                    (63, 'Opel'), 
                    (64, 'Peugeot'), 
                    (65, 'Piaggio'), 
                    (66, 'Plymouth'), 
                    (67, 'Polonez'), 
                    (68, 'Pontiac'), 
                    (69, 'Porsche'), 
                    (70, 'Proton'), 
                    (71, 'Renault'), 
                    (146, 'Rolls-Royce'), 
                    (72, 'Rover'), 
                    (339, 'SMA'), 
                    (73, 'Saab'), 
                    (184, 'Samsung'), 
                    (147, 'Saturn'), 
                    (74, 'Seat'), 
                    (148, 'Shelby'), 
                    (75, 'Siam Di Tella'), 
                    (338, 'Simca'), 
                    (76, 'Skoda'), 
                    (190, 'Smart'), 
                    (77, 'Ssangyong'), 
                    (149, 'Studebaker'), 
                    (78, 'Subaru'), 
                    (79, 'Suzuki'), 
                    (80, 'Tata'), 
                    (81, 'Tavria'), 
                    (82, 'Toyota'), 
                    (83, 'Volkswagen'), 
                    (84, 'Volvo'), 
                    (85, 'Willys'), 
                    (256, 'Xinkai'), 
                    (303, 'ZX Auto'), 
                    (255, 'Zhejiangzoye'), 
                    (492, 'Zna'), 
                    (301, 'Zotye')]


        for code, nombre in marcas:
            try:

                mar = Marca()
                mar.nombre = u'%s' %nombre
                mar.save()

                modelos_json = requests.get('http://www.demotores.cl/frontend/posting/json/modelsByBrandIdTypeEnumCountryId.html?brand=%s&type=CAR&country=29' %code).json()

                for modelo in modelos_json:

                    if modelo['name'] != u'Otro Modelo':
                        mod = Modelo()
                        mod.nombre = u'%s' %modelo['name']
                        mod.marca = mar
                        mod.save()

            except UnicodeDecodeError:
                pass

        self.stdout.write('Carga de marca y modelo finalizada')
