

##-------------------------------------------------------------------------
##-------------------------------------------------------------------------
##                              AUTOR: MATIAS (VIRTUALSODA EN GITHUB)
## 
## MINI SCRIPT QUE PUEDE SER TOMADO COMO UNA IDEA
## PARA UNA MINI LIBRERIA REGEX 
## (O NO , DEPENDE DE LAS NECESIDADES DEL PROGRAMA)
## LA IDEA SURGIO DE QUE NECESITABA UNA FUNCION
## PARA LIMPIAR EL USER INPUT ANTES DE CARGAR LOS DATOS EN UNA BD
##-------------------------------------------------------------------------
##-------------------------------------------------------------------------
## MINI SCRIPT THAT CAN BE USED AS A STARTING POINT TO A REGEX LIB
## I NEEDED A WAY TO CLEAN USER INPUT 
## BEFORE UPLOADING THE DATA TO A DATABASE, SO I MADE THIS
##-------------------------------------------------------------------------
##-------------------------------------------------------------------------





##-------------------------------------
##-------------------------------------
## IMPORT  ## PYTHON IMPORT SECTION
##-------------------------------------
##-------------------------------------
try :

    import re
    import os

except ImportError:

     print(" IMPORT ERROR : [CHECK (CTRL-F) ## PYTHON IMPORT SECTION --> REGEX_MINI_LIB.PY] ")

##-------------------------------------
##-------------------------------------





## LIMPIAR INPUT DE LOS ENTRIES
##------------------------------------------

def limpiar_input_texto(entry_str, modo_de_limpieza):

    r"""
    ## MODOS DE LIMPIEZA // CLEANING MODES :

    ## NOTA// NOTE : EL FLAG  re.UNICODE
    ## ES PARA QUE \W CAPTURE SIMBOLOS
    ## COMO ß Ð Æ   @ Ł  € Ł Ŋ Ŧ Ħ ← ↓ Ħ Ŋ ← ↓ ← ↓ → Ø @ ¶ € ¶ € ¬ { ¬ ] } 
    ## TENER EN CUENTA QUE CIERTOS CARACTERES
    ## IGUAL SIGUEN PASANDO EL FILTRO
    ##---------------
    ## THE FLAG re.UNICODE IS FOR THE CHARACTERS LISTED ABOVE
    ## SOME OF THEM WILL PASS THE FILTER ANYWAY

     


    ##  "full"
    ##---------------
    ## borra simbolos,numeros,espacios y "_" , solo deja letras
    ## y las concatena con "_" si hay por ejemplo una string
    ## de la forma "deeded edede"; ademas pone todo en lowercase
    ##---------------
    ## erases symbols, numers,spaces and the "_" characters
    ## only leaves letters and .join them with "_" if the 
    ## string has whitespaces , finally, the string
    ## is converted to lowercase



    ## "semifull"
    ##---------------
    ## borra simbolos,numeros,espacios y "_" , solo deja letras.
    ## ademas pone todo en lowercase
    ##---------------
    ## erases symbols, numers,spaces and the "_" characters
    ## only leaves letters, the string is converted to lowercase


    ##  "letras_y_simbolos"
    ##---------------
    ## borra los espacios,letras y simbolos (solo deja numeros)
    ## no concatena con nada
    ##---------------
    ## erases spaces, letters and symbols (only leaves numbers)


    ## "dejar_letras_y_numeros"
    ##---------------
    ## sirve para los inputs del tipo 13a o 3B
    ## no concatena con nada, deja todo en lower case
    ##---------------
    ## all in lowercase , leaves only numbers and letters, like 12v or 4QA


    ## "mail"
    ##---------------
    ## sirve para los inputs del tipo mail o contraseñas
    ## lo unico que evita esto son los simbolos comunes para la inyeccion
    ## ---> ' --> ;
    ##---------------
    ## for mails and passwords, only filters the most common inyection symbols
    ## (listed above)




    """


    if(modo_de_limpieza == "full"):
        
        entry_str = entry_str.split() ## en caso de ser 2 nombres o mas

        temp_str = ""

        #print("despues_split",entry_str);

        if(len(entry_str) >= 1):

            for i in range(0,len(entry_str)):

                entry_str[i].strip() # remover espacios
                entry_str[i] = re.sub(r"[\W+g\d'\_']", '', entry_str[i], re.UNICODE) ## borrar simbolos y numeros
                entry_str[i] = entry_str[i].lower() # poner todo en lowerCase
        else : 

            entry_str[i].strip() # remover espacios
            entry_str[i] = re.sub(r"[\W+g\d'\_']", '', entry_str[i], re.UNICODE) ## borrar simbolos y numeros
            entry_str[i] = entry_str[i].lower() # poner todo en lowerCase




        temp_str = '_'.join(map(str, entry_str)) ## concatenar con "_"




    elif(modo_de_limpieza == "semifull"):

        entry_str = entry_str.split() ## en caso de ser 2 nombres o mas
        temp_str = ""

        #print("despues_split",entry_str);
        if(len(entry_str) >= 1):

            for i in range(0,len(entry_str)):

                entry_str[i].strip() # remover espacios
                entry_str[i] = re.sub(r"[\W+g\d'\_']", '', entry_str[i], re.UNICODE) ## borrar simbolos y numeros
                entry_str[i] = entry_str[i].lower() # poner todo en lowerCase

        else : 

            entry_str[i].strip() # remover espacios
            entry_str[i] = re.sub(r"[\W+g\d'\_']", '', entry_str[i], re.UNICODE) ## borrar simbolos y numeros
            entry_str[i] = entry_str[i].lower() # poner todo en lowerCase




        temp_str = ' '.join(map(str, entry_str)) ## concatenar con " "



    elif(modo_de_limpieza == "letras_y_simbolos"):

        entry_str.strip() # remover espacios
        entry_str = re.sub(r"[\W+g\'_'a-zA-Z]", '',entry_str, re.UNICODE) ## borrar simbolos y letras

        temp_str = entry_str



    elif(modo_de_limpieza == "dejar_letras_y_numeros"):

        entry_str.strip() # remover espacios
        entry_str = re.sub(r"[\W+g'\_']", '', entry_str, re.UNICODE) ## borra simbolos, deja letras y num
        entry_str = entry_str.lower()

        temp_str = entry_str



    elif(modo_de_limpieza == "dejar_letras_y_numeros_2"):

        entry_str.strip() # remover espacios
        entry_str = re.sub(r"[\W+g'\_']", '', entry_str, re.UNICODE) ## borra simbolos, deja letras y num
        entry_str = entry_str.lower()

        temp_str = entry_str

        temp_str = ' '.join(map(str, entry_str)) ## concatenar con " "




    elif(modo_de_limpieza == "mail"):

        entry_str.strip() # remover espacios
        entry_str = re.sub(r"[;']+", '', entry_str, re.UNICODE) ## remueve ; y '

        temp_str = entry_str



    #print(temp_str)


    return temp_str





## ALGUNOS TESTS
##-------------------------------------------------------------------------
##-------------------------------------------------------------------------



test_str1 = "Jose  #$&)/=()?&/)%$/#*]¨_:;:¨;:_  Perez 4_455 53%$$64%$''''34;;;;24&/[]{ "
test_str1 = limpiar_input_texto(test_str1,"full")
print("full --->",test_str1)

test_str2 = "Jose  #$&)/=()?&/)%$/#*]¨_:;:¨;:_  Perez 4_455 53%$$64%$''''34;;;;24&/[]{ " 
print("semifull --->",limpiar_input_texto(test_str2,"semifull"))

test_str3 = "1:_;:_;:_''23°#$#%$#$&BFDFDFHcvdfbg45JHJGFJHJerewefwref6___:[ÑOK/(JHJ%$G$ 7fgbgfhgfh8%$&%&(%$9"
print("letras_y_simbolos --->",limpiar_input_texto(test_str3,"letras_y_simbolos"))

test_str4 = "a#$$b&;:''''::;;:/(IIc)())/(___  d) /(&/(123)&/%&/%&/)"
print("dejar_letras_y_numeros --->",limpiar_input_texto(test_str4,"dejar_letras_y_numeros"))

test_str5 = "ejemplodemail@hotmail.com '');')';;);;)));"
print("mail --->",limpiar_input_texto(test_str5,"mail"))



