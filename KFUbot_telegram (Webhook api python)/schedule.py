# -*- coding: utf-8 -*-
times = ['-нет-\n','1️⃣ 8:30-10:00 ','2️⃣ 10:10-11:40 ','3️⃣ 11:50-13:20 ','4️⃣ 13:40-15:10 ','5️⃣ 15:20-16:50 ','6️⃣ 17:00-18:30 ','7. ⏳ 18:40-20:10 ']
monday = ['🎧 Социология \n      👉 ауд. 108 , Шакирова А.Ю.\n','🎧 Культурология \n    	👉 305 ф/к , Панченко О.Л. 	\n',' Электроника\n     👉 007 ф/к , Гумеров  Р.И.\n','Физ-ра \n 	👉 хз , хз\n']
tuesday = ['Основы управленческой деятельности \n 	👉 123 ф/к , Овчинников М.Н.\n','🎧 Технологии и методы программирования \n 	👉 112 физ.к. , Шаймухаметов Р.Р.\n','🎧 Основы управленческой деятельности  \n 	👉 112 физ.к. , Овчинников М.Н. 	\n','Культурология  \n 	👉 410 , Панченко О.Л. 	\n','Социология \n 	👉 410 , Шакирова А.Ю. 	\n','Технологии и методы программирования \n 	👉 1206 , Шаймухаметов Р.Р. 	\n','технологическая практика \n 	👉 1112 , Нигматуллин Р.Р. 	\n']
wednesday = ['Электроника\n 	👉 007 ф/к , Гумеров  Р.И.\n','Англ. яз.  \n 	👉 хз , хз\n',' Операционные системы \n 	👉 910  , Дябилкин Д.А.\n','Дискретная математика \n 	👉 1114  , Замов Н.К. \n']
thursday = ['Документоведение \n 	👉 804 , Рубцова Р.Г.\n','🎧 Документоведение  \n 	👉 1211 , Рубцова Р.Г.\n','Англ. яз.  \n 	👉 хз , хз\n','Физ-ра \n 	👉 хз , хз 	\n']
friday = ['🎧 Электроника\n 	👉 307 ф/к, Ситников С.Ю.\n','🎧 Дискретная математика \n 	👉 216 двойка, Пшеничный П.В. 	\n','Дискретная математика \n 	👉 1114  , Замов Н.К. \n','Операционные системы \n 	👉 910  , Дябилкин Д.А.\n','🎧 Операционные системы\n 	👉 1113  , Дябилкин Д.А.\n']
saturday = ['🎧 Организационное и правовое обеспечение ИБ \n 	👉 112 физ.к., Ситников С.Ю.\n	','Англ. яз.  \n 	👉 хз , хз\n','Организационное и правовое обеспечение ИБ \n 	👉 112 физ.к., Ситников С.Ю.\n	']
mon111=times[1]+monday[0]+times[2]+monday[2]+times[3]+monday[2]+times[4]+monday[3]
mon121=times[1]+monday[0]+times[2]+monday[2]+times[3]+monday[2]+times[4]+monday[3]
mon211=times[1]+monday[1]+times[2]+monday[2]+times[3]+monday[2]+times[4]+monday[3]
mon221=times[1]+monday[1]+times[2]+monday[2]+times[3]+monday[2]+times[4]+monday[3]
mon112=times[1]+monday[0]+times[2]+times[0]+times[3]+times[0]+times[4]+monday[3]
mon122=times[1]+monday[0]+times[2]+times[0]+times[3]+times[0]+times[4]+monday[3]
mon212=times[1]+monday[1]+times[2]+times[0]+times[3]+times[0]+times[4]+monday[3]
mon222=times[1]+monday[1]+times[2]+times[0]+times[3]+times[0]+times[4]+monday[3]
tue11=times[1]+times[0]+times[2]+times[0]+times[3]+times[0]+times[4]+tuesday[2]+times[5]+tuesday[3]+times[6]+tuesday[5]
tue12=times[1]+times[0]+times[2]+times[0]+times[3]+times[0]+times[4]+tuesday[2]+times[5]+tuesday[3]+times[6]+tuesday[6]
tue21=times[1]+times[0]+times[2]+times[0]+times[3]+tuesday[0]+times[4]+tuesday[1]+times[5]+tuesday[4]+times[6]+tuesday[6]
tue22=times[1]+times[0]+times[2]+times[0]+times[3]+tuesday[0]+times[4]+tuesday[1]+times[5]+tuesday[4]+times[6]+tuesday[5]
wed111=times[1] + times[0] + times[2] + times[0] + times[3] + wednesday[1] + times[4] + wednesday[2] + times[5] + times[0] + times[6] + times[0]
wed121=times[1] + times[0] + times[2] + times[0] + times[3] + wednesday[1] + times[4] + wednesday[3] + times[5] + times[0] + times[6] + times[0]
wed112=times[1] + wednesday[0] + times[2] + wednesday[0] + times[3] + wednesday[1] + times[4] + wednesday[2] + times[5] + times[0] + times[6] + times[0]
wed122=times[1] + wednesday[0] + times[2] + wednesday[0] + times[3] + wednesday[1] + times[4] + wednesday[3] + times[5] + times[0] + times[6] + times[0]
wed113=times[1] + times[0] + times[2] + times[0] + times[3] + wednesday[1] + times[4] + wednesday[2] + times[5] + wednesday[0] + times[6] + wednesday[0]
wed123=times[1] + times[0] + times[2] + times[0] + times[3] + wednesday[1] + times[4] + wednesday[3] + times[5] + wednesday[0] + times[6] + wednesday[0]

thu11 = times[1] + thursday[0] + times[2] + thursday[1] + times[3] + thursday[2] + times[4] + thursday[3]
thu12 = times[1] + times[0] + times[2] + thursday[1] + times[3] + thursday[2] + times[4] + thursday[3]
thu21 = times[1] + times[0] + times[2] + times[0] + times[3] + thursday[2] + times[4] + thursday[3]
thu22 = times[1] + times[0] + times[2] + thursday[0] + times[3] + thursday[2] + times[4] + thursday[3]
fri11=times[1] + friday[0] + times[2] + friday[1] + times[3] + friday[2]
fri12=times[1] + friday[0] + times[2] + friday[1] + times[3] + friday[3]
sat2 = times[1] + saturday[2] + times[2] + saturday[0] + times[3] + saturday[1] + times[4] + friday[4]
sat1 = times[1] + times[0] + times[2] + saturday[0] + times[3] + saturday[1] + times[4] + friday[4]
sun = '1. ⏳ 8:30 - 10:00 Спааать 😴 \n 2. ⏳ 10:10 - 11:40 Фильмец, Сериалы 🙃 \n3. ⏳ 11:50 - 13:20 Время поесть 🍿🍫🍭🍨🍧🍦🍰'
