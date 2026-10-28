# El cuaderno de la abuela Pilar y k vecinos (k = 5): ¿saldrá bien
# la hornada? Lo que cambia de un caso a otro es la RECETA de
# preparación, las constantes de abajo (1 = sí, 0 = no). El modelo y
# el resto del código son siempre los mismos.
from datetime import date

COLUMNAS = [
    "fecha", "pan", "harina_g", "agua_g", "temperatura", "minutos",
    "reposo_min", "horno", "quien", "tirada", "resultado",
]

# El cuaderno, tal como lo pasó Marco al ordenador (un hueco es un
# valor que falta). La última columna es lo que hay que predecir.
CUADERNO = """\
2026-09-07,blanco ,950,480,220,42,50,viejo,Iván,sí,mal
2026-09-07,integral,1050,820,205,45,40,viejo,Iván,no,bien
2026-09-07,blanco,1800,1200,220,34,50,viejo,Pilar,no,bien
2026-09-07,blanco,1100,830,220,36,80,viejo,Pilar,sí,mal
2026-09-07,blanco,1250,930,,35,70,viejo,Pilar,sí,mal
2026-09-07,integral,1750,1360,210,46,110,viejo,Pilar,no,bien
2026-09-07,intgral,650,510,210,44,70,viejo,Iván,no,bien
2026-09-07,blanco,1450,910,220,36,50,viejo,Iván,no,bien
2026-09-07,Centeno,1750,1470,225,51,60,viejo,Iván,no,bien
2026-09-07,blanco,1150,740,215,44,60,viejo,Pilar,sí,mal
2026-09-08,integral,1700,1300,205,52,60,viejo,Iván,sí,mal
2026-09-08,blanco,950,590,215,34,80,viejo,Pilar,no,bien
2026-09-08,INTEGRAL,2000,1290,,46,120,viejo,Iván,sí,mal
2026-09-08,brioch,1450,780,180,29,120,viejo,Iván,no,bien
2026-09-08,blanco,550,300,220,34,70,viejo,Iván,sí,mal
2026-09-08,blanco,1950,1470,215,36,30,viejo,Pilar,sí,mal
2026-09-08,Integral,1400,1090,210,46,80,viejo,Iván,no,bien
2026-09-08,integral ,900,680,205,33,60,viejo,Iván,sí,mal
2026-09-08,integral,1150,900,215,46,80,viejo,Pilar,no,bien
2026-09-08,blanco,1150,720,215,34,60,viejo,Pilar,no,bien
2026-09-09,integral,500,370,210,44,120,viejo,Iván,no,bien
2026-09-09,Integral,1450,920,,46,50,viejo,Iván,sí,mal
2026-09-09,centeno,850,700,235,39,40,viejo,Pilar,sí,mal
2026-09-09,blanco ,1000,610,215,35,30,viejo,Iván,no,bien
2026-09-09,blanco,500,310,215,34,40,viejo,Pilar,no,bien
2026-09-09,INTEGRAL,1150,910,215,44,50,viejo,Iván,no,bien
2026-09-09,integral,1150,850,215,44,110,viejo,Pilar,no,bien
2026-09-09,INTEGRAL,1050,760,210,46,100,viejo,Iván,no,bien
2026-09-09,centeno,1900,1550,230,42,50,viejo,Pilar,sí,mal
2026-09-09,blanco,1250,840,225,35,100,viejo,Pilar,no,bien
2026-09-10,brioch,1650,830,185,31,100,viejo,Iván,no,bien
2026-09-10,brioche,500,240,180,30,110,viejo,Iván,no,bien
2026-09-10,integral,1350,1060,215,46,120,viejo,Pilar,no,bien
2026-09-10,Brioche,1950,1050,175,30,70,viejo,Iván,sí,mal
2026-09-10,brioche,1350,700,180,31,40,viejo,Iván,no,bien
2026-09-10,centeno,1900,1570,,49,40,viejo,Iván,sí,mal
2026-09-10,brioche,1500,750,185,31,120,viejo,Pilar,no,bien
2026-09-10,blanco,1800,1190,220,24,120,viejo,Iván,sí,mal
2026-09-10,integral,800,600,210,59,110,viejo,Pilar,sí,mal
2026-09-10,blanco,1850,1190,220,34,100,viejo,Pilar,no,bien
2026-09-10,brioch,1650,830,185,31,100,viejo,Iván,no,bien
2026-09-10,brioche,500,240,180,30,110,viejo,Iván,no,bien
2026-09-10,integral,1350,1060,215,46,120,viejo,Pilar,no,bien
2026-09-10,Brioche,1950,1050,175,30,70,viejo,Iván,sí,mal
2026-09-10,brioche,1350,700,180,31,40,viejo,Iván,no,bien
2026-09-10,centeno,1900,1570,,49,40,viejo,Iván,sí,mal
2026-09-10,brioche,1500,750,185,31,120,viejo,Pilar,no,bien
2026-09-10,blanco,1800,1190,220,24,120,viejo,Iván,sí,mal
2026-09-10,integral,800,600,210,59,110,viejo,Pilar,sí,mal
2026-09-10,blanco,1850,1190,220,34,100,viejo,Pilar,no,bien
2026-09-11,blanco,1850,1200,220,34,120,viejo,Iván,sí,mal
2026-09-11,integral ,600,440,205,45,50,viejo,Iván,no,bien
2026-09-11,Blanco,1700,1040,220,34,80,viejo,Iván,no,bien
2026-09-11,Blanco,1450,750,220,36,120,viejo,Iván,sí,mal
2026-09-11,Blanco,1350,830,220,35,40,viejo,Iván,sí,mal
2026-09-11,brioche,1850,980,175,31,120,viejo,Iván,no,bien
2026-09-11,blanco,850,440,225,36,70,viejo,Pilar,no,mal
2026-09-11,intgral,1750,1370,215,44,50,viejo,Iván,no,bien
2026-09-11,brioche,1600,610,175,30,80,viejo,Iván,sí,mal
2026-09-11,blanco,1700,1110,220,34,60,viejo,Pilar,no,bien
2026-09-12,blanco,1800,1120,215,35,40,viejo,Iván,no,bien
2026-09-12,blanco,1700,1110,215,35,120,viejo,Pilar,no,bien
2026-09-12,integral,750,580,,37,90,viejo,Iván,sí,mal
2026-09-12,blanco,800,510,225,36,50,viejo,Pilar,no,bien
2026-09-12,brioche,900,450,175,29,90,viejo,Pilar,no,bien
2026-09-12,blanco,600,390,225,36,100,viejo,Iván,no,bien
2026-09-12,blanco,1150,710,220,35,100,viejo,Pilar,no,bien
2026-09-12,blanco ,1350,870,,34,40,viejo,Iván,sí,mal
2026-09-12,centeno,650,630,235,50,80,viejo,Pilar,sí,mal
2026-09-12,blanco,1850,970,,34,40,viejo,Iván,sí,mal
2026-09-14,blanco ,1100,740,220,35,50,viejo,Iván,no,bien
2026-09-14,integral,900,760,210,46,120,viejo,Pilar,sí,mal
2026-09-14,blanco,1800,1340,215,36,40,viejo,Iván,sí,mal
2026-09-14,integral,1550,1130,215,46,100,viejo,Pilar,no,bien
2026-09-14,blanco,600,440,215,35,50,viejo,Iván,sí,mal
2026-09-14,blanco,1300,850,,35,40,viejo,Pilar,sí,mal
2026-09-14,blanco,1400,880,215,36,60,viejo,Pilar,no,bien
2026-09-14,centeno,1300,1080,230,49,70,viejo,Pilar,no,bien
2026-09-14,blanco,2000,1280,225,34,100,viejo,Pilar,no,bien
2026-09-14,brioche,1900,1140,185,30,120,viejo,Iván,sí,mal
2026-09-15,brioche,1850,970,365,30,90,viejo,Iván,no,bien
2026-09-15,blanco,1850,980,437,34,120,viejo,Iván,sí,mal
2026-09-15,brioche,1200,620,347,31,70,viejo,Pilar,no,bien
2026-09-15,integral,1800,1340,419,32,30,viejo,Pilar,sí,mal
2026-09-15,brioche,1850,960,356,31,110,viejo,Pilar,no,bien
2026-09-15,brioche,1000,460,,30,80,viejo,Iván,sí,mal
2026-09-15,centeno,1600,1340,446,49,30,viejo,Pilar,no,bien
2026-09-15,brioche,1250,610,365,45,60,viejo,Iván,sí,mal
2026-09-15,blanco,1100,720,,35,100,viejo,Pilar,sí,mal
2026-09-15,blanco,1550,1010,437,46,70,viejo,Iván,sí,mal
2026-09-16,integral,1950,1400,205,44,110,viejo,Pilar,no,bien
2026-09-16,brioche,950,580,185,30,110,viejo,Pilar,sí,mal
2026-09-16,INTEGRAL,1350,1000,205,46,50,viejo,Iván,no,bien
2026-09-16,blanco,1400,930,225,46,70,viejo,Pilar,no,bien
2026-09-16,centeno,1000,850,235,49,110,viejo,Pilar,no,bien
2026-09-16,blanco,1750,1140,215,36,50,viejo,Pilar,no,bien
2026-09-16,integral,1650,1220,210,45,120,viejo,Pilar,no,bien
2026-09-16,integral,1250,920,,35,100,viejo,Pilar,sí,mal
2026-09-16,blanco,1800,1120,215,48,80,viejo,Pilar,sí,mal
2026-09-16,integral,950,680,,46,80,viejo,Pilar,sí,mal
2026-09-17,centeno,1200,1070,235,49,110,viejo,Pilar,no,bien
2026-09-17,centeno,950,830,225,51,110,viejo,Pilar,no,bien
2026-09-17,blanco,650,420,215,35,80,viejo,Pilar,no,bien
2026-09-17,centeno,950,710,230,50,90,viejo,Pilar,sí,mal
2026-09-17,blanco,650,430,225,35,50,viejo,Pilar,no,bien
2026-09-17,blanco,1550,990,,36,80,viejo,Iván,sí,mal
2026-09-17,integral,1450,1030,215,59,40,viejo,Pilar,sí,mal
2026-09-17,brioche,1950,1040,180,31,100,viejo,Pilar,no,bien
2026-09-17,blanco,1850,1180,215,35,120,viejo,Pilar,no,bien
2026-09-17,centeno,850,710,,51,90,viejo,Pilar,sí,mal
2026-09-18,Blanco,600,430,215,24,120,viejo,Iván,sí,mal
2026-09-18,integral,1850,1410,205,37,30,viejo,Pilar,sí,mal
2026-09-18,blanco,2000,1280,225,45,100,viejo,Pilar,sí,mal
2026-09-18,blanco,1100,730,,35,110,viejo,Pilar,sí,mal
2026-09-18,integral,550,400,210,45,110,viejo,Iván,no,bien
2026-09-18,blanco,1000,670,215,36,120,viejo,Pilar,no,bien
2026-09-18,brioche,750,390,180,29,60,viejo,Pilar,no,bien
2026-09-18,brioch,1600,740,185,30,110,viejo,Iván,no,bien
2026-09-18,brioche,1900,1010,175,17,80,viejo,Pilar,sí,mal
2026-09-18,brioche,1450,720,185,30,80,viejo,Pilar,no,bien
2026-09-19,blanco,1950,1260,220,36,110,viejo,Iván,no,bien
2026-09-19,integral,1150,900,205,45,120,viejo,Pilar,no,bien
2026-09-19,Brioche,600,310,,29,90,viejo,Iván,sí,mal
2026-09-19,integral,1750,1330,,44,70,viejo,Pilar,sí,mal
2026-09-19,integral,1150,900,205,55,60,viejo,Pilar,sí,mal
2026-09-19,blanco,700,440,220,35,70,viejo,Pilar,no,bien
2026-09-19,brioche,800,380,180,31,100,viejo,Pilar,no,bien
2026-09-19,blanco,1050,680,220,36,120,viejo,Pilar,no,bien
2026-09-19,brioche,500,240,180,30,120,viejo,Pilar,no,bien
2026-09-19,blanco,1550,1030,215,35,60,viejo,Pilar,no,bien
2026-09-21,blanco,1500,930,215,34,80,viejo,Pilar,no,bien
2026-09-21,brioche,800,410,145,17,100,nuevo,Pilar,sí,mal
2026-09-21,blanco,800,510,195,36,60,nuevo,Pilar,no,bien
2026-09-21,blanco,900,550,195,35,110,nuevo,Pilar,no,bien
2026-09-21,centeno,1450,1190,195,51,60,nuevo,Pilar,no,bien
2026-09-21,intgral,1450,1040,,46,30,viejo,Iván,sí,mal
2026-09-21,brioche,1650,1050,185,31,120,viejo,Pilar,sí,mal
2026-09-21,blanco,1450,760,215,36,50,nuevo,Iván,sí,mal
2026-09-21,blanco,850,560,,36,80,viejo,Iván,sí,mal
2026-09-21,centeno,750,630,235,51,50,viejo,Pilar,no,bien
2026-09-22,blanco,1450,900,437,24,40,viejo,Pilar,sí,mal
2026-09-22,brioche,1900,930,302,30,30,nuevo,Iván,no,bien
2026-09-22,integral,1450,1040,356,46,40,nuevo,Pilar,no,bien
2026-09-22,brioch,750,400,356,18,70,nuevo,Iván,sí,mal
2026-09-22,integral,650,500,401,45,50,nuevo,Pilar,sí,mal
2026-09-22,integral,800,570,419,44,30,nuevo,Pilar,sí,mal
2026-09-22,centeno,650,530,437,49,70,viejo,Pilar,no,bien
2026-09-22,brioch,900,450,347,29,50,viejo,Iván,no,bien
2026-09-22,brioche,800,320,347,43,40,viejo,Pilar,sí,mal
2026-09-22,blanco ,800,530,428,36,110,nuevo,Iván,sí,mal
2026-09-23,blanco,750,480,215,35,40,viejo,Iván,no,bien
2026-09-23,brioche,1000,360,150,30,80,nuevo,Pilar,sí,mal
2026-09-23,brioche,950,450,175,30,60,nuevo,Pilar,sí,mal
2026-09-23,centeno,900,770,195,50,90,nuevo,Iván,no,bien
2026-09-23,integral,700,540,205,35,50,nuevo,Pilar,sí,mal
2026-09-23,integral,850,660,210,45,120,nuevo,Pilar,sí,mal
2026-09-23,centeno,1200,1060,225,60,40,viejo,Pilar,sí,mal
2026-09-23,brioche,600,320,175,29,50,viejo,Pilar,no,bien
2026-09-23,centeno,700,690,225,51,50,nuevo,Iván,sí,mal
2026-09-23,blanco,1550,1030,,35,110,viejo,Iván,sí,mal
2026-09-24,Integral,1100,810,210,45,50,viejo,Iván,no,bien
2026-09-24,centeno,750,610,200,49,50,nuevo,Pilar,no,bien
2026-09-24,integral,1050,790,205,33,60,viejo,Iván,sí,mal
2026-09-24,Blanco,1200,760,215,46,110,viejo,Iván,no,bien
2026-09-24,integral,1450,1050,215,45,120,viejo,Pilar,no,bien
2026-09-24,brioche,700,440,185,-31,40,nuevo,Pilar,sí,mal
2026-09-24,blanco,900,660,,36,50,viejo,Iván,sí,mal
2026-09-24,INTEGRAL,1250,1110,175,44,50,nuevo,Iván,sí,mal
2026-09-24,blanco,1000,560,215,34,60,viejo,Iván,sí,mal
2026-09-24,brioche,1800,920,,30,30,viejo,Iván,sí,mal
2026-09-25,brioche,550,280,175,30,30,viejo,Pilar,no,bien
2026-09-25,blanco,2000,1260,185,35,90,nuevo,Pilar,no,bien
2026-09-25,brioche,1550,720,150,29,40,nuevo,Pilar,no,bien
2026-09-25,brioche,1100,520,,29,40,viejo,Pilar,sí,mal
2026-09-25,blanco ,1900,1430,225,35,110,viejo,Iván,sí,mal
2026-09-25,blanco,1800,1120,215,28,100,viejo,Pilar,sí,mal
2026-09-25,integral,700,540,215,45,110,viejo,Pilar,no,bien
2026-09-25,blanco,650,400,225,35,30,viejo,Iván,no,bien
2026-09-25,brioche,1800,930,180,30,80,viejo,Pilar,no,bien
2026-09-25,blanco,1950,1200,220,35,30,viejo,Pilar,no,bien
2026-09-26,integral,600,430,175,44,40,nuevo,Pilar,no,bien
2026-09-26,brioch,1350,710,175,38,60,viejo,Iván,sí,mal
2026-09-26,blanco,850,520,220,36,30,nuevo,Pilar,sí,mal
2026-09-26,centeno,850,710,225,50,110,nuevo,Pilar,sí,mal
2026-09-26,brioche,1300,660,180,21,120,nuevo,Pilar,sí,mal
2026-09-26,integral,900,540,205,46,30,viejo,Pilar,sí,mal
2026-09-26,integral,750,670,215,44,120,viejo,Pilar,sí,mal
2026-09-26,blanco,950,530,195,36,40,nuevo,Pilar,sí,mal
2026-09-26,centeno,1200,960,230,51,80,nuevo,Pilar,sí,mal
2026-09-26,blanco,1500,990,225,50,90,viejo,Pilar,sí,mal
2026-09-28,brioche,1200,710,175,31,120,viejo,Pilar,sí,mal
2026-09-28,blanco ,700,440,225,35,110,viejo,Iván,no,bien
2026-09-28,Integral,850,610,175,45,80,nuevo,Iván,no,bien
2026-09-28,centeno,1350,1080,230,49,120,nuevo,Pilar,sí,mal
2026-09-28,Blanco,1650,1220,195,20,90,nuevo,Iván,sí,mal
2026-09-28,brioche,1800,850,145,30,100,nuevo,Pilar,no,bien
2026-09-28,blanco ,1900,1230,215,34,110,nuevo,Iván,sí,mal
2026-09-28,brioche,700,330,145,29,90,nuevo,Iván,no,bien
2026-09-28,integral,1050,800,,46,120,viejo,Pilar,sí,mal
2026-09-28,integral,2000,1520,205,44,100,viejo,Iván,no,bien
2026-09-29,integral,1300,930,180,45,80,nuevo,Pilar,no,bien
2026-09-29,integral,750,640,185,32,60,nuevo,Pilar,sí,mal
2026-09-29,centeno,1800,1520,200,49,60,nuevo,Pilar,no,bien
2026-09-29,brioche,1900,990,155,29,110,nuevo,Pilar,no,bien
2026-09-29,integral,1800,1320,215,45,50,nuevo,Iván,sí,mal
2026-09-29,blanco,1150,640,195,36,120,nuevo,Pilar,sí,mal
2026-09-29,blanco ,950,510,185,45,40,nuevo,Iván,sí,mal
2026-09-29,brioche,1400,670,155,31,80,nuevo,Pilar,no,bien
2026-09-29,integral ,1450,1220,210,45,30,viejo,Iván,sí,mal
2026-09-29,blanco,1050,680,185,34,80,nuevo,Pilar,no,bien
2026-09-30,blanco,600,400,195,35,60,nuevo,Pilar,no,bien
2026-09-30,centeno,1550,1330,230,50,120,viejo,Pilar,no,bien
2026-09-30,centeno,1500,1290,205,50,110,nuevo,Pilar,no,bien
2026-09-30,integral ,950,690,210,46,30,viejo,Iván,no,bien
2026-09-30,blanco,1950,1290,225,36,60,viejo,Pilar,no,bien
2026-09-30,brioche,550,200,155,30,100,nuevo,Iván,sí,mal
2026-09-30,centeno,1450,1170,195,49,40,nuevo,Iván,no,bien
2026-09-30,blanco,1650,1010,,34,50,viejo,Pilar,sí,mal
2026-09-30,brioche,1000,480,175,20,40,viejo,Pilar,no,mal
2026-09-30,brioche,650,330,185,31,50,viejo,Iván,no,bien
2026-09-30,blanco,600,400,195,35,60,nuevo,Pilar,no,bien
2026-09-30,centeno,1550,1330,230,50,120,viejo,Pilar,no,bien
2026-09-30,centeno,1500,1290,205,50,110,nuevo,Pilar,no,bien
2026-09-30,integral ,950,690,210,46,30,viejo,Iván,no,bien
2026-09-30,blanco,1950,1290,225,36,60,viejo,Pilar,no,bien
2026-09-30,brioche,550,200,155,30,100,nuevo,Iván,sí,mal
2026-09-30,centeno,1450,1170,195,49,40,nuevo,Iván,no,bien
2026-09-30,blanco,1650,1010,,34,50,viejo,Pilar,sí,mal
2026-09-30,brioche,1000,480,175,20,40,viejo,Pilar,no,mal
2026-09-30,brioche,650,330,185,31,50,viejo,Iván,no,bien
2026-10-01,blanco,800,500,195,49,80,nuevo,Pilar,sí,mal
2026-10-01,integral,700,540,215,46,60,viejo,Pilar,no,bien
2026-10-01,centeno,2000,1690,235,49,40,viejo,Pilar,no,bien
2026-10-01,centeno,950,670,200,58,120,nuevo,Iván,sí,mal
2026-10-01,centeno,1650,1300,225,50,40,viejo,Iván,no,bien
2026-10-01,integral,850,620,205,0,110,viejo,Pilar,no,bien
2026-10-01,integral,850,670,175,59,80,nuevo,Iván,sí,mal
2026-10-01,integral,800,570,175,46,80,nuevo,Pilar,no,bien
2026-10-01,integral,1350,1010,180,44,120,nuevo,Pilar,no,bien
2026-10-01,blanco,1600,1170,190,34,60,nuevo,Iván,sí,mal
2026-10-02,brioche,1300,640,155,45,30,nuevo,Pilar,sí,mal
2026-10-02,integral,1850,1440,215,45,40,nuevo,Iván,sí,mal
2026-10-02,integral,1950,1390,215,53,80,viejo,Pilar,sí,mal
2026-10-02,integral,1550,1150,210,44,40,nuevo,Pilar,sí,mal
2026-10-02,integral,1800,1280,180,44,90,nuevo,Iván,no,bien
2026-10-02,centeno,750,590,195,50,40,nuevo,Pilar,no,bien
2026-10-02,centeno,900,890,235,50,80,viejo,Pilar,sí,mal
2026-10-02,brioche,1700,870,180,20,90,viejo,Pilar,sí,mal
2026-10-02,brioche,1350,660,145,31,120,nuevo,Pilar,no,bien
2026-10-02,integral ,1350,1130,175,46,80,nuevo,Iván,sí,mal
2026-10-03,Blanco,600,390,215,34,100,viejo,Iván,no,bien
2026-10-03,brioch,1100,580,180,30,90,nuevo,Iván,sí,mal
2026-10-03,brioche,1300,690,150,21,100,nuevo,Pilar,sí,mal
2026-10-03,integral,650,400,215,57,50,viejo,Iván,sí,mal
2026-10-03,blanco ,1650,1090,215,34,100,viejo,Iván,no,bien
2026-10-03,blanco,1750,1070,185,34,50,nuevo,Pilar,no,bien
2026-10-03,brioche,2000,1000,,30,80,viejo,Pilar,sí,mal
2026-10-03,blanco ,1900,1210,215,34,100,nuevo,Iván,sí,mal
2026-10-03,brioche,1100,660,155,30,70,nuevo,Iván,sí,mal
2026-10-03,Centeno,1150,1020,200,50,70,nuevo,Iván,no,bien
2026-10-05,blanco,1500,1000,185,35,40,nuevo,Pilar,no,bien
2026-10-05,blanco ,1350,900,225,49,30,viejo,Iván,sí,mal
2026-10-05,brioche,1350,720,185,17,90,viejo,Pilar,sí,mal
2026-10-05,blanco,950,690,220,35,60,viejo,Pilar,sí,mal
2026-10-05,centeno,1950,1340,235,51,40,viejo,Pilar,sí,mal
2026-10-05,integral,1050,770,175,56,30,nuevo,Pilar,sí,mal
2026-10-05,blanco,1050,680,185,36,100,nuevo,Pilar,sí,mal
2026-10-05,centeno,1000,870,235,61,100,viejo,Iván,sí,mal
2026-10-05,brioche,1550,570,180,30,100,nuevo,Pilar,sí,mal
2026-10-05,blanco,650,420,185,35,110,nuevo,Pilar,no,bien
2026-10-06,centeno,2000,1710,230,51,40,viejo,Iván,no,bien
2026-10-06,brioche,850,520,185,31,80,viejo,Pilar,sí,mal
2026-10-06,integral,1900,1420,175,46,50,nuevo,Pilar,no,bien
2026-10-06,blanco,1450,940,185,22,90,nuevo,Pilar,sí,mal
2026-10-06,integral,750,550,210,44,120,viejo,Pilar,no,bien
2026-10-06,integral,1750,1250,175,46,70,nuevo,Pilar,no,bien
2026-10-06,blanco,1850,1240,,35,80,viejo,Pilar,sí,mal
2026-10-06,blanco,1500,950,195,36,70,nuevo,Pilar,no,bien
2026-10-06,brioche,1000,610,145,31,30,nuevo,Pilar,sí,mal
2026-10-06,integral ,1350,1040,210,46,40,viejo,Iván,no,bien
2026-10-07,integral ,950,720,215,44,110,viejo,Iván,no,bien
2026-10-07,brioche,1200,640,150,39,50,nuevo,Pilar,sí,mal
2026-10-07,blanco ,1950,1300,195,25,80,nuevo,Iván,sí,mal
2026-10-07,integral,800,680,,44,90,viejo,Pilar,sí,mal
2026-10-07,centeno,1800,1590,235,51,120,nuevo,Pilar,sí,mal
2026-10-07,blanco,1500,970,225,34,110,viejo,Pilar,no,bien
2026-10-07,brioche,1650,890,175,31,90,viejo,Pilar,no,bien
2026-10-07,integral,1550,1160,205,46,40,viejo,Pilar,sí,bien
2026-10-07,brioche,1200,590,145,29,60,nuevo,Iván,no,bien
2026-10-07,integral ,1250,970,180,45,80,nuevo,Iván,no,bien
2026-10-07,integral ,950,720,215,44,110,viejo,Iván,no,bien
2026-10-07,brioche,1200,640,150,39,50,nuevo,Pilar,sí,mal
2026-10-07,blanco ,1950,1300,195,25,80,nuevo,Iván,sí,mal
2026-10-07,integral,800,680,,44,90,viejo,Pilar,sí,mal
2026-10-07,centeno,1800,1590,235,51,120,nuevo,Pilar,sí,mal
2026-10-07,blanco,1500,970,225,34,110,viejo,Pilar,no,bien
2026-10-07,brioche,1650,890,175,31,90,viejo,Pilar,no,bien
2026-10-07,integral,1550,1160,205,46,40,viejo,Pilar,sí,bien
2026-10-07,brioche,1200,590,145,29,60,nuevo,Iván,no,bien
2026-10-07,integral ,1250,970,180,45,80,nuevo,Iván,no,bien
2026-10-08,brioche,1050,440,175,31,80,nuevo,Iván,sí,mal
2026-10-08,centeno,1100,920,200,49,100,nuevo,Iván,no,bien
2026-10-08,integral,550,410,175,30,60,nuevo,Iván,sí,mal
2026-10-08,blanco,1150,750,195,36,120,nuevo,Pilar,no,bien
2026-10-08,blanco,1200,780,190,34,70,nuevo,Pilar,no,bien
2026-10-08,blanco ,900,580,999,34,100,viejo,Iván,no,bien
2026-10-08,intgral,1350,1070,175,57,80,nuevo,Iván,sí,mal
2026-10-08,blanco ,1200,730,190,36,90,nuevo,Iván,no,bien
2026-10-08,integral,800,620,210,44,60,viejo,Pilar,no,bien
2026-10-08,blanco,1400,870,225,36,40,nuevo,Pilar,sí,mal
2026-10-09,centeno,850,750,205,50,30,nuevo,Iván,no,bien
2026-10-09,centeno,1100,890,235,63,100,viejo,Pilar,sí,mal
2026-10-09,brioche,1650,840,180,30,60,viejo,Pilar,no,bien
2026-10-09,brioche,1800,840,185,31,120,viejo,Pilar,no,bien
2026-10-09,blanco,1050,700,220,36,40,viejo,Iván,no,bien
2026-10-09,integral,750,550,215,45,100,viejo,Pilar,no,bien
2026-10-09,brioche,1500,720,155,16,40,nuevo,Pilar,sí,mal
2026-10-09,blanco,1900,1190,220,35,40,viejo,Pilar,sí,bien
2026-10-09,brioche,650,340,175,31,90,viejo,Pilar,no,bien
2026-10-09,blanco,950,630,225,50,60,viejo,Pilar,sí,mal
2026-10-10,brioche,1100,530,,30,40,viejo,Pilar,sí,mal
2026-10-10,integral,850,640,205,46,90,viejo,Iván,no,bien
2026-10-10,Centeno,800,710,225,51,80,viejo,Iván,no,bien
2026-10-10,blanco,1250,800,220,35,70,nuevo,Pilar,sí,mal
2026-10-10,blanco,1450,890,225,34,120,viejo,Iván,no,bien
2026-10-10,Integral,1400,1080,215,44,110,viejo,Iván,no,bien
2026-10-10,blanco,1300,960,185,49,40,nuevo,Pilar,sí,mal
2026-10-10,brioche,1700,680,175,31,80,nuevo,Pilar,sí,mal
2026-10-10,integral ,1600,1210,205,45,50,viejo,Iván,no,bien
2026-10-10,integral,500,380,210,44,80,viejo,Pilar,no,bien
"""

# Las hornadas del mes que viene: la tirada aún no se sabe.
MES_QUE_VIENE = """\
2026-10-12,brioche,1850,1190,185,31,110,viejo,Pilar,,mal
2026-10-12,blanco ,1850,1240,215,35,100,viejo,Iván,,bien
2026-10-12,brioche,1650,810,155,29,70,nuevo,Pilar,,bien
2026-10-12,integral,1250,920,215,35,90,viejo,Pilar,,mal
2026-10-12,brioch,1700,800,155,31,100,nuevo,Iván,,bien
2026-10-12,centeno,1200,960,195,49,100,nuevo,Pilar,,bien
2026-10-12,brioche,750,350,145,29,40,nuevo,Pilar,,bien
2026-10-12,blanco,900,550,195,21,80,nuevo,Pilar,,mal
2026-10-12,blanco,900,700,185,34,110,nuevo,Iván,,mal
2026-10-12,blanco,900,600,195,35,40,nuevo,Pilar,,bien
2026-10-13,centeno,1150,990,225,49,50,viejo,Pilar,,bien
2026-10-13,blanco,1300,810,190,35,40,nuevo,Pilar,,bien
2026-10-13,integral,1200,910,205,46,40,nuevo,Pilar,,mal
2026-10-13,Centeno,600,510,230,49,50,viejo,Iván,,bien
2026-10-13,Blanco,1000,620,195,34,40,nuevo,Iván,,bien
2026-10-13,blanco,1950,1290,190,35,50,nuevo,Pilar,,bien
2026-10-13,brioche,1900,950,175,31,50,nuevo,Pilar,,mal
2026-10-13,blanco,600,460,215,36,110,viejo,Pilar,,mal
2026-10-13,brioche,1750,700,185,19,90,nuevo,Iván,,mal
2026-10-13,integral,600,450,215,44,40,nuevo,Pilar,,mal
2026-10-14,integral,500,430,185,45,30,nuevo,Pilar,,mal
2026-10-14,blanco,1450,1090,185,26,70,nuevo,Iván,,mal
2026-10-14,blanco,950,700,225,48,90,viejo,Pilar,,mal
2026-10-14,integral,750,640,180,44,30,nuevo,Pilar,,bien
2026-10-14,blanco,850,550,,35,60,viejo,Pilar,,mal
2026-10-14,blanco,700,450,190,36,100,nuevo,Pilar,,bien
2026-10-14,integral,1900,1630,185,44,60,nuevo,Pilar,,mal
2026-10-14,integral,500,360,185,45,100,nuevo,Pilar,,bien
2026-10-14,brioche,1050,550,180,31,70,nuevo,Pilar,,mal
2026-10-14,brioche,1850,870,155,29,30,nuevo,Iván,,bien
2026-10-15,centeno,1000,840,195,51,50,nuevo,Pilar,,bien
2026-10-15,integral,1550,1160,215,45,90,viejo,Iván,,bien
2026-10-15,Integral,950,620,205,44,70,viejo,Iván,,mal
2026-10-15,Brioche,1950,960,180,30,120,nuevo,Iván,,mal
2026-10-15,brioche,1200,630,175,43,30,viejo,Pilar,,mal
2026-10-15,Blanco,600,330,185,24,50,nuevo,Iván,,mal
2026-10-15,blanco,1950,1280,225,36,30,viejo,Iván,,bien
2026-10-15,blanco,850,570,190,36,110,nuevo,Pilar,,bien
2026-10-15,Centeno,800,660,230,36,50,nuevo,Iván,,mal
2026-10-15,Blanco,1950,1250,190,36,60,nuevo,Iván,,bien
2026-10-16,blanco ,750,480,185,36,30,nuevo,Iván,,bien
2026-10-16,blanco,550,360,220,26,70,viejo,Pilar,,mal
2026-10-16,blanco,550,360,225,34,100,viejo,Iván,,bien
2026-10-16,brioche,1450,680,185,30,30,viejo,Pilar,,bien
2026-10-16,integral,750,560,175,45,80,nuevo,Pilar,,bien
2026-10-16,integral,1550,1160,180,35,100,nuevo,Iván,,mal
2026-10-16,brioche,750,360,150,31,120,nuevo,Pilar,,bien
2026-10-16,blanco,1850,1210,185,20,60,nuevo,Pilar,,mal
2026-10-16,brioche,850,440,180,31,50,nuevo,Pilar,,mal
2026-10-16,brioche,1300,600,150,19,70,nuevo,Iván,,mal
2026-10-17,integral,1600,1190,175,44,110,nuevo,Iván,,bien
2026-10-17,blanco,1150,750,190,35,50,nuevo,Pilar,,bien
2026-10-17,blanco,1600,1050,190,34,70,nuevo,Pilar,,bien
2026-10-17,blanco,600,320,215,34,40,nuevo,Pilar,,mal
2026-10-17,blanco,800,490,190,36,70,nuevo,Iván,,bien
2026-10-17,brioche,1050,540,185,29,90,viejo,Pilar,,bien
2026-10-17,integral,1950,1520,215,46,100,viejo,Iván,,bien
2026-10-17,intgral,600,430,205,46,30,viejo,Iván,,bien
2026-10-17,integral,1500,1090,210,46,70,nuevo,Pilar,,mal
2026-10-17,blanco,1900,1260,190,47,100,nuevo,Pilar,,mal
2026-10-19,brioche,650,300,180,31,70,viejo,Iván,,bien
2026-10-19,Integral,1100,860,175,44,110,nuevo,Iván,,bien
2026-10-19,blanco,1100,670,195,34,70,nuevo,Iván,,bien
2026-10-19,integral,800,610,180,45,90,nuevo,Pilar,,bien
2026-10-19,brioche,1450,760,175,31,40,viejo,Iván,,bien
2026-10-19,brioche,850,440,,30,120,viejo,Iván,,mal
2026-10-19,blanco,1300,670,220,35,90,viejo,Iván,,mal
2026-10-19,Blanco,1250,790,220,34,90,nuevo,Iván,,mal
2026-10-19,blanco,1050,660,220,35,90,viejo,Iván,,bien
2026-10-19,integral ,1650,1380,,46,110,viejo,Iván,,mal
2026-10-20,blanco,1100,720,,36,120,viejo,Pilar,,mal
2026-10-20,blanco,900,580,215,45,50,viejo,Pilar,,mal
2026-10-20,integral,550,360,,36,70,viejo,Pilar,,mal
2026-10-20,centeno,500,410,200,51,80,nuevo,Pilar,,bien
2026-10-20,brioche,1550,830,180,29,30,viejo,Pilar,,bien
2026-10-20,blanco,1150,830,220,34,100,nuevo,Iván,,mal
2026-10-20,centeno,1850,1530,230,49,100,viejo,Pilar,,bien
2026-10-20,blanco,650,430,190,49,100,nuevo,Pilar,,mal
2026-10-20,blanco ,600,370,225,46,70,nuevo,Iván,,mal
2026-10-20,integral,1900,1490,215,45,80,viejo,Pilar,,bien
2026-10-21,blanco,600,390,195,34,90,nuevo,Pilar,,bien
2026-10-21,blanco,900,560,225,34,30,nuevo,Pilar,,mal
2026-10-21,integral,1350,980,180,46,90,nuevo,Pilar,,bien
2026-10-21,centeno,1100,880,205,51,60,nuevo,Iván,,bien
2026-10-21,blanco,1150,730,185,44,70,nuevo,Pilar,,mal
2026-10-21,blanco,550,360,220,35,50,viejo,Pilar,,bien
2026-10-21,blanco,800,520,225,50,110,viejo,Pilar,,mal
2026-10-21,centeno,1500,1260,235,50,30,viejo,Pilar,,bien
2026-10-21,brioche,700,370,180,30,100,viejo,Iván,,bien
2026-10-21,brioche,500,200,175,30,60,viejo,Pilar,,mal
2026-10-22,Integral,1250,990,205,46,80,viejo,Iván,,bien
2026-10-22,Integral,500,390,185,46,70,nuevo,Iván,,bien
2026-10-22,integral,1100,820,210,44,70,viejo,Pilar,,bien
2026-10-22,blanco,1700,1080,215,35,120,viejo,Iván,,bien
2026-10-22,brioche,1650,780,,39,50,viejo,Iván,,mal
2026-10-22,integral,1700,1070,210,44,120,nuevo,Pilar,,mal
2026-10-22,centeno,600,430,225,51,110,nuevo,Pilar,,mal
2026-10-22,Brioche,950,580,175,29,70,viejo,Iván,,mal
2026-10-22,Brioche,600,290,145,18,50,nuevo,Iván,,mal
2026-10-22,blanco,1300,810,215,35,110,viejo,Pilar,,bien
2026-10-23,blanco,1150,710,215,35,70,viejo,Pilar,,mal
2026-10-23,integral,1350,1160,215,44,70,viejo,Pilar,,mal
2026-10-23,blanco,1300,820,195,35,110,nuevo,Iván,,bien
2026-10-23,Blanco,700,440,225,34,80,viejo,Iván,,bien
2026-10-23,blanco,750,470,220,35,50,viejo,Iván,,bien
2026-10-23,blanco,1750,1090,215,35,80,viejo,Pilar,,bien
2026-10-23,blanco,1150,820,195,36,100,nuevo,Pilar,,mal
2026-10-23,integral,900,680,205,44,120,viejo,Iván,,bien
2026-10-23,integral,500,370,175,53,50,nuevo,Pilar,,mal
2026-10-23,blanco,950,600,195,36,120,nuevo,Pilar,,bien
2026-10-24,brioch,1600,750,175,30,60,viejo,Iván,,bien
2026-10-24,centeno,1000,800,205,42,40,nuevo,Iván,,mal
2026-10-24,integral ,1900,1460,185,44,30,nuevo,Iván,,bien
2026-10-24,integral,600,450,215,45,90,viejo,Pilar,,bien
2026-10-24,blanco,650,410,220,43,60,viejo,Iván,,mal
2026-10-24,brioche,1400,720,180,30,110,viejo,Pilar,,bien
2026-10-24,integral,1150,870,185,44,100,nuevo,Iván,,bien
2026-10-24,integral,1050,760,215,33,70,viejo,Pilar,,mal
2026-10-24,brioche,1950,970,145,21,70,nuevo,Iván,,mal
2026-10-24,blanco,1500,1130,195,48,100,nuevo,Pilar,,mal
2026-10-26,brioche,900,480,175,31,80,viejo,Pilar,,bien
2026-10-26,integral,650,480,,44,120,viejo,Pilar,,mal
2026-10-26,blanco,850,530,215,45,120,nuevo,Iván,,mal
2026-10-26,blanco,1650,1010,215,34,60,viejo,Pilar,,bien
2026-10-26,intgral,700,530,180,44,110,nuevo,Iván,,bien
2026-10-26,brioche,1600,840,175,30,60,nuevo,Pilar,,mal
2026-10-26,blanco,2000,1140,225,36,100,viejo,Pilar,,mal
2026-10-26,brioche,2000,960,,18,100,viejo,Iván,,mal
2026-10-26,blanco ,1550,960,195,35,100,nuevo,Iván,,bien
2026-10-26,blanco,1050,680,190,34,110,nuevo,Pilar,,bien
2026-10-27,blanco,1700,1130,195,36,60,nuevo,Pilar,,bien
2026-10-27,blanco,1700,1060,,34,40,viejo,Iván,,mal
2026-10-27,brioche,900,480,185,44,70,viejo,Iván,,mal
2026-10-27,centeno,2000,1890,230,49,70,viejo,Pilar,,mal
2026-10-27,integral,1050,810,215,45,80,viejo,Pilar,,bien
2026-10-27,centeno,1150,840,235,50,110,viejo,Iván,,mal
2026-10-27,centeno,950,940,225,60,100,viejo,Pilar,,mal
2026-10-27,centeno,650,550,235,57,110,nuevo,Iván,,mal
2026-10-27,blanco,1100,700,220,34,60,viejo,Pilar,,bien
2026-10-27,brioche,1500,750,150,22,120,nuevo,Pilar,,bien
2026-10-28,INTEGRAL,1150,860,210,44,70,viejo,Iván,,bien
2026-10-28,brioche,1200,720,155,30,30,nuevo,Iván,,mal
2026-10-28,blanco,650,430,225,20,90,viejo,Pilar,,mal
2026-10-28,blanco,1200,620,220,36,120,viejo,Iván,,mal
2026-10-28,blanco,1700,1090,185,34,40,nuevo,Pilar,,bien
2026-10-28,Blanco,1950,1020,225,36,110,viejo,Iván,,mal
2026-10-28,integral,750,580,180,45,110,nuevo,Pilar,,bien
2026-10-28,integral,1950,1490,175,32,60,nuevo,Pilar,,mal
2026-10-28,blanco,1150,720,190,35,100,nuevo,Pilar,,bien
2026-10-28,centeno,800,570,235,51,70,viejo,Pilar,,mal
2026-10-29,blanco,1650,1040,220,35,60,viejo,Pilar,,bien
2026-10-29,blanco,1800,1200,195,21,80,nuevo,Iván,,mal
2026-10-29,centeno,650,570,230,51,60,nuevo,Pilar,,mal
2026-10-29,blanco,1750,1080,215,36,40,viejo,Pilar,,bien
2026-10-29,brioche,1200,780,,30,70,viejo,Pilar,,mal
2026-10-29,integral,1750,1300,180,44,110,nuevo,Iván,,bien
2026-10-29,blanco,2000,1260,215,35,30,viejo,Iván,,bien
2026-10-29,integral,650,580,205,46,80,viejo,Pilar,,mal
2026-10-29,centeno,950,820,230,35,40,nuevo,Pilar,,mal
2026-10-29,Brioche,1150,550,180,31,50,viejo,Iván,,bien
2026-10-30,blanco,1600,1010,225,36,70,nuevo,Iván,,mal
2026-10-30,Blanco,1850,1160,225,34,80,viejo,Iván,,bien
2026-10-30,Brioche,900,450,145,29,90,nuevo,Iván,,bien
2026-10-30,centeno,1150,920,225,50,70,viejo,Pilar,,bien
2026-10-30,blanco,1900,1190,215,35,40,viejo,Iván,,bien
2026-10-30,integral,500,370,185,54,50,nuevo,Pilar,,mal
2026-10-30,blanco,1900,1240,225,34,40,viejo,Pilar,,bien
2026-10-30,brioche,1500,730,175,31,80,viejo,Pilar,,bien
2026-10-30,centeno,1850,1600,200,49,70,nuevo,Iván,,bien
2026-10-30,blanco,650,420,215,26,120,viejo,Pilar,,mal
2026-10-31,integral,1750,1260,215,46,60,viejo,Iván,,bien
2026-10-31,blanco,1350,830,215,35,90,viejo,Pilar,,bien
2026-10-31,blanco ,600,370,225,34,80,viejo,Iván,,bien
2026-10-31,centeno,750,640,195,50,70,nuevo,Pilar,,bien
2026-10-31,brioch,1750,900,155,29,90,nuevo,Iván,,bien
2026-10-31,blanco,600,390,220,35,120,viejo,Pilar,,bien
2026-10-31,brioche,1850,900,,29,50,viejo,Pilar,,mal
2026-10-31,intgral,1750,1250,205,44,50,viejo,Iván,,bien
2026-10-31,blanco,950,480,215,36,110,nuevo,Pilar,,mal
2026-10-31,brioche,1700,650,175,31,40,viejo,Iván,,mal
2026-11-02,integral ,2000,1460,215,54,80,nuevo,Iván,,mal
2026-11-02,Integral,1300,980,210,46,90,viejo,Iván,,bien
2026-11-02,centeno,1900,1590,225,49,80,viejo,Iván,,bien
2026-11-02,brioche,1650,850,185,31,120,viejo,Iván,,bien
2026-11-02,integral,1900,1350,205,46,40,viejo,Pilar,,bien
2026-11-02,Centeno,1450,1350,225,57,40,viejo,Iván,,mal
2026-11-02,Integral,950,580,185,46,60,nuevo,Iván,,mal
2026-11-02,integral,1550,1200,215,46,90,viejo,Pilar,,bien
2026-11-02,centeno,900,720,205,58,100,nuevo,Pilar,,mal
2026-11-02,blanco,1100,670,220,36,50,viejo,Pilar,,bien
2026-11-03,blanco,550,400,185,34,60,nuevo,Pilar,,mal
2026-11-03,integral,1700,1280,215,44,30,viejo,Pilar,,bien
2026-11-03,blanco,1050,660,185,26,50,nuevo,Iván,,mal
2026-11-03,integral ,1100,820,215,44,50,nuevo,Iván,,mal
2026-11-03,integral ,1500,1110,210,44,110,viejo,Iván,,bien
2026-11-03,Blanco,850,560,225,35,110,viejo,Iván,,bien
2026-11-03,integral,1650,1010,180,44,100,nuevo,Iván,,mal
2026-11-03,centeno,1500,1210,200,39,120,nuevo,Pilar,,mal
2026-11-03,blanco,750,460,215,35,100,viejo,Pilar,,bien
2026-11-03,blanco,1750,1090,190,36,70,nuevo,Pilar,,bien
2026-11-04,blanco,850,560,225,34,70,viejo,Pilar,,bien
2026-11-04,INTEGRAL,1900,1500,215,44,80,viejo,Iván,,bien
2026-11-04,brioche,1850,900,150,29,50,nuevo,Pilar,,bien
2026-11-04,blanco,1800,1180,220,45,100,nuevo,Iván,,mal
2026-11-04,brioch,1500,790,150,22,40,nuevo,Iván,,mal
2026-11-04,blanco,900,580,225,36,40,viejo,Pilar,,bien
2026-11-04,integral,850,640,210,34,80,nuevo,Pilar,,mal
2026-11-04,Integral,1300,990,215,46,40,viejo,Iván,,bien
2026-11-04,integral,2000,1540,180,46,40,nuevo,Pilar,,bien
2026-11-04,blanco,1400,850,215,44,90,viejo,Pilar,,mal
2026-11-05,integral,1700,1280,210,46,50,viejo,Pilar,,bien
2026-11-05,brioche,550,260,155,44,50,nuevo,Pilar,,mal
2026-11-05,blanco,1950,1300,215,34,60,nuevo,Pilar,,mal
2026-11-05,integral,500,390,210,44,40,viejo,Pilar,,bien
2026-11-05,blanco ,1150,890,190,35,120,nuevo,Iván,,mal
2026-11-05,brioche,950,360,175,31,30,viejo,Pilar,,mal
2026-11-05,integral,1550,1190,175,44,80,nuevo,Pilar,,bien
2026-11-05,Brioche,1850,1140,180,30,120,viejo,Iván,,mal
2026-11-05,centeno,1950,1620,225,50,60,viejo,Pilar,,bien
2026-11-05,blanco,800,580,225,23,110,viejo,Pilar,,mal
2026-11-06,blanco,1800,1130,190,35,60,nuevo,Pilar,,bien
2026-11-06,blanco,1100,580,185,24,110,nuevo,Pilar,,bien
2026-11-06,brioch,900,450,180,30,40,nuevo,Iván,,mal
2026-11-06,blanco,1750,1110,225,36,70,viejo,Iván,,bien
2026-11-06,centeno,750,600,205,51,60,nuevo,Pilar,,bien
2026-11-06,blanco,550,340,,36,80,viejo,Pilar,,mal
2026-11-06,blanco,1000,640,185,36,100,nuevo,Pilar,,mal
2026-11-06,blanco,900,600,215,36,80,viejo,Pilar,,bien
2026-11-06,blanco,1150,740,,35,90,viejo,Iván,,mal
2026-11-06,blanco,1050,670,190,36,40,nuevo,Iván,,bien
2026-11-07,integral,1600,1370,180,46,60,nuevo,Pilar,,mal
2026-11-07,brioche,1800,850,185,31,80,nuevo,Iván,,mal
2026-11-07,blanco,1350,850,215,35,40,viejo,Pilar,,bien
2026-11-07,blanco,1900,1220,195,36,70,nuevo,Pilar,,bien
2026-11-07,integral,600,440,210,44,40,viejo,Pilar,,bien
2026-11-07,brioche,700,380,150,30,100,nuevo,Iván,,bien
2026-11-07,brioche,1900,950,175,29,100,nuevo,Pilar,,mal
2026-11-07,centeno,900,740,230,50,100,nuevo,Pilar,,mal
2026-11-07,Brioche,1150,570,145,29,40,nuevo,Iván,,bien
2026-11-07,Blanco,1800,1370,195,34,60,nuevo,Iván,,mal
"""

# ── La receta ──────────────────────────────────────────────────────
# 1. Fila a fila, sin aprender nada de los datos.
QUITAR_REPETIDAS = 1
UNIFICAR_NOMBRES = 1
# Imposible: 500 grados o más, o 0 minutos o menos.
IMPOSIBLES_A_HUECO = 1
# Más de 300 grados es °F: se pasa a °C.
GRADOS_A_C = 0
# 2. Partir: 0 al azar (una de cada cinco), 1 por fechas (valida la
# última semana, desde el 2026-10-05).
PARTIR_POR_FECHAS = 1
# 3. Huecos: 0 quitar la fila, 1 rellenar con la mediana, 2 mediana
# y una columna «faltaba» que dice si la temperatura estaba en blanco.
HUECOS = 2
# 4. Columnas del cuaderno que entran en el modelo.
CON_PAN = 1
CON_HARINA_G = 0
CON_AGUA_G = 0
CON_TEMPERATURA = 0
CON_MINUTOS = 0
CON_REPOSO_MIN = 0
CON_HORNO = 1
CON_QUIEN = 0
CON_TIRADA = 0
# Características nuevas: agua / harina, temperatura × minutos y el
# día de la semana (1 lunes … 7 domingo).
HIDRATACION = 1
CALOR = 1
DIA = 0
# Categorías: 0 numerarlas (1, 2, 3…), 1 una columna por categoría.
UNA_COLUMNA_POR_CATEGORIA = 1
# Escala: 1 llevar cada columna de 0 a 1 con el entrenamiento.
NORMALIZAR = 1
K = 5

ERRATAS = {"intgral": "integral", "brioch": "brioche"}
ENTRADAS = ["pan", "harina_g", "agua_g", "temperatura", "minutos",
            "reposo_min", "horno", "quien", "tirada"]
USAR = {"pan": CON_PAN, "harina_g": CON_HARINA_G, "agua_g": CON_AGUA_G,
        "temperatura": CON_TEMPERATURA, "minutos": CON_MINUTOS,
        "reposo_min": CON_REPOSO_MIN, "horno": CON_HORNO,
        "quien": CON_QUIEN, "tirada": CON_TIRADA}
CATEGORICAS = ["pan", "horno", "quien", "tirada"]
NUMEROS = ["harina_g", "agua_g", "temperatura", "minutos", "reposo_min"]


def leer(texto):
    return [dict(zip(COLUMNAS, linea.split(",")))
            for linea in texto.strip("\n").split("\n")]


def sin_repetidas(filas):
    vistas, quedan = set(), []
    for f in filas:
        clave = tuple(f.values())
        if clave not in vistas:
            vistas.add(clave)
            quedan.append(f)
    return quedan


def limpiar(f):
    h = dict(f)
    for c in NUMEROS:
        h[c] = int(h[c]) if h[c] else None
    h["tirada"] = h["tirada"] or None
    if UNIFICAR_NOMBRES:
        pan = h["pan"].strip().lower()
        h["pan"] = ERRATAS.get(pan, pan)
    t, m = h["temperatura"], h["minutos"]
    if IMPOSIBLES_A_HUECO:
        if t is not None and t >= 500:
            t = None
        if m is not None and m <= 0:
            m = None
    if GRADOS_A_C and t is not None and t > 300:
        t = (t - 32) * 5 / 9
    h["temperatura"], h["minutos"] = t, m
    return h


def partir(hornadas):
    if PARTIR_POR_FECHAS:
        valida = {i for i, h in enumerate(hornadas)
                  if h["fecha"] >= "2026-10-05"}
    else:
        # una de cada cinco, barajadas siempre con la misma semilla
        orden, s = list(range(len(hornadas))), 2026
        for i in range(len(hornadas) - 1, 0, -1):
            s = s * 48271 % 2147483647
            j = s % (i + 1)
            orden[i], orden[j] = orden[j], orden[i]
        valida = set(orden[:len(hornadas) // 5])
    entreno = [h for i, h in enumerate(hornadas) if i not in valida]
    validacion = [h for i, h in enumerate(hornadas) if i in valida]
    return entreno, validacion


def mediana(valores):
    v = sorted(valores)
    if not v:
        return 0
    m = len(v) // 2
    return v[m] if len(v) % 2 else (v[m - 1] + v[m]) / 2


def que_entrena(entreno):
    if HUECOS == 0:
        return [h for h in entreno
                if h["temperatura"] is not None
                and h["minutos"] is not None]
    return entreno


def en_numeros(h, a):
    t, m = h["temperatura"], h["minutos"]
    if t is None:
        t = a["temperatura"]
    if m is None:
        m = a["minutos"]
    x = []
    for c in ENTRADAS:
        if not USAR[c]:
            continue
        if c in CATEGORICAS:
            v = h[c]
            if c == "tirada" and v is None:
                v = a["tirada"]
            cats = a["categorias"][c]
            if UNA_COLUMNA_POR_CATEGORIA:
                x += [1 if v == k else 0 for k in cats]
            else:
                x.append(cats.index(v) + 1 if v in cats else 0)
        elif c == "temperatura":
            x.append(t)
        elif c == "minutos":
            x.append(m)
        else:
            x.append(h[c])
    if HUECOS == 2:
        x.append(1 if h["temperatura"] is None else 0)
    if HIDRATACION:
        x.append(h["agua_g"] / h["harina_g"])
    if CALOR:
        x.append(t * m)
    if DIA:
        x.append(date.fromisoformat(h["fecha"]).isoweekday())
    return x


def aprender(entreno):
    # todo lo que se aprende sale SOLO de las filas que entrenan
    usadas = que_entrena(entreno)
    tiradas = [h["tirada"] for h in usadas if h["tirada"] is not None]
    a = {
        "temperatura": mediana([h["temperatura"] for h in usadas
                                if h["temperatura"] is not None]),
        "minutos": mediana([h["minutos"] for h in usadas
                            if h["minutos"] is not None]),
        "tirada": max(sorted(set(tiradas)), key=tiradas.count,
                      default="no"),
        "categorias": {c: sorted({h[c] for h in usadas
                                  if h[c] is not None})
                       for c in CATEGORICAS},
    }
    filas = [en_numeros(h, a) for h in usadas]
    a["min"] = [min(col) for col in zip(*filas)]
    a["max"] = [max(col) for col in zip(*filas)]
    return a


def vector(h, a):
    x = en_numeros(h, a)
    if not NORMALIZAR:
        return x
    return [(v - lo) / (hi - lo) if hi > lo else 0
            for v, lo, hi in zip(x, a["min"], a["max"])]


def distancia(p, q):
    return sum((u - w) * (u - w) for u, w in zip(p, q))


def predecir(entreno, x):
    # las K hornadas más cercanas; a igual distancia, la que va antes
    cerca = sorted((distancia(e, x), i)
                   for i, (e, _) in enumerate(entreno))[:K]
    bien = sum(1 for _, i in cerca if entreno[i][1] == "bien")
    return "bien" if bien * 2 > len(cerca) else "mal"


def preparar(entreno, prueba):
    a = aprender(entreno)
    con = [(vector(h, a), h["resultado"]) for h in que_entrena(entreno)]
    return con, [(vector(h, a), h["resultado"]) for h in prueba], a


def cifra(bien, total):
    decimas = (2000 * bien + total) // (2 * total)
    return f"{bien} de {total} ({decimas // 10},{decimas % 10} %)"


def medir(entreno, prueba):
    dice = [(predecir(entreno, x), r) for x, r in prueba]
    return sum(1 for d, r in dice if d == r), dice


filas = leer(CUADERNO)
if QUITAR_REPETIDAS:
    filas = sin_repetidas(filas)
hornadas = [limpiar(f) for f in filas]
entreno, validacion = partir(hornadas)
con, val, a = preparar(entreno, validacion)
print(f"filas del cuaderno: {len(hornadas)} "
      f"(entrenan {len(con)}, validan {len(val)})")
print(f"columnas que ve el modelo: {len(a['min'])}")
bien, _ = medir(con, val)
print(f"en tu validación: {cifra(bien, len(val))}")

# El modelo de verdad entrena con TODO el cuaderno preparado.
mes = [limpiar(f) for f in leer(MES_QUE_VIENE)]
con, prueba, _ = preparar(hornadas, mes)
bien, dice = medir(con, prueba)
print(f"el mes que viene: {cifra(bien, len(prueba))}")
print("  salieron mal y dijo «bien»: "
      f"{sum(1 for d, r in dice if r == 'mal' and d == 'bien')}")
print("  salieron bien y dijo «mal»: "
      f"{sum(1 for d, r in dice if r == 'bien' and d == 'mal')}")
