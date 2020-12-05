semana = input("Que semana toca? Escribe el numero: ")

nrsp1 = 1
nrsp = 1


##READ FILE AND MODIFY LINES
a_file = open("G:/My Drive/IQVIA/IQVIAtest2.Rmd", "r")
list_of_lines = a_file.readlines()

#INCREMENT 1 THE PERIODS
periodonrsp1 = list_of_lines[421]
periodonrsp2 = list_of_lines[422]
lista1 = [n for n in periodonrsp1]
lista2 = [n for n in periodonrsp2]

nrsp1 = ''.join(lista1[15]+lista1[16]+lista1[17]+lista1[18])
nrsp1 = int(nrsp1)+1

nrsp2 = ''.join(lista2[15]+lista2[16]+lista2[17]+lista2[18])
nrsp2 = int(nrsp2)+1

#UPDATE LINES
list_of_lines[19] = f"TotIMS0619 <- read_excel(\"G:/My Drive/IQVIA/LAST_WEEK/TOTIMS{semana}20.xlsx\")\n"
list_of_lines[79] = f"write_xlsx(padresHijos, \"G:/My Drive/IQVIA/LAST_WEEK/PadresHijosIQVIA{semana}20.xlsx\")\n"
list_of_lines[421] = f"perini_sirval<-{nrsp1}\n"
list_of_lines[422] = f"perfin_sirval<-{nrsp2}\n"
list_of_lines[542] = f"TotIMS0619 <- read_excel(\"G:/My Drive/IQVIA/LAST_WEEK/input{semana}.xlsx\")\n"
list_of_lines[546] = f"input=\"G:/My Drive/IQVIA/LAST_WEEK/input{semana}.xlsx\"\n"
list_of_lines[578] = f"write_xlsx(list(DATOSTOTALES=castle), \"G:/My Drive/IQVIA/LAST_WEEK/IQVIAP2{semana}20.xlsx\")\n"
list_of_lines[609] = f"write_xlsx(hijos,\"G:/My Drive/IQVIA/LAST_WEEK/Padres{semana}20.xlsx\")\n"
list_of_lines[619] = f"  prueb1 <- read_excel(\"G:/My Drive/IQVIA/LAST_WEEK/lote{semana}20.xlsx\" ,sheet=sheets2[i])\n"
list_of_lines[645] = f"outf=\"G:/My Drive/IQVIA/LAST_WEEK/PADRE{semana}20.xlsx\"\n"
list_of_lines[662] = f"outfi=\"G:/My Drive/IQVIA/LAST_WEEK/IQVIA{semana}20.xlsx\"\n"


   
##NOW WRITE THE LINES 

a_file = open("G:/My Drive/IQVIA/IQVIAtest2.Rmd", "w")
a_file.writelines(list_of_lines)
a_file.close()




