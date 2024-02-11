import random
import re
import time # Note To Readers: Don't write your interpreters in python... Dont write anything in python that requires doing this.. Don't write this, just don't, use ASM to do shit like this....
i=0
e=0
class gvar:
    definer = r"\((.*?)\)"
    funcName = r"\[(.*?)\]"
    string = r"\"(.*?)\""
    encapsulator = r"\{(.*?)\}"
    line = r"\>(.*?)\<"
    FuncParameters = r"\((.*?)\)"
    varDefiner = r"([^=]+)=(.+)"
    varGreaterThan = r"([^>]+)>(.+)"
    varIsnt = r"([^>]+)!=(.+)"
    varLessThan = r"([^<]+)<(.+)"
    varIs = r"([^=]+)==(.+)"
    commaSeparator = r"([^=]+),(.+)"
    UVars = {}
    UFuncs = {}
    UFuncsParams = {}
    line=1
    class IMPORTS:
        class COLOR:
            RED = "\033[91m"
            GREEN = "\033[92m"
            BLUE = "\033[94m"
            RESET = "\033[0m"
            IS = False
        class THIS:
            SOG = '''-----==============================================================-::::::::::::::::::::::
==================================================================-:::::::::::::::::::::::
--==============================================================-::::::::::::-==++*+=:::::
----=========================================================--:-:-::--==+*####**###+:::::
--------==============================+=+=++*+========+*#####%%%%@@%%%%%##******##+:::::::
+++=======++++***+=-=-=--=----+*=+==+##**##%#++++**+#%%%%%%@@@%%%#######******##=.........
###%%%@@%%%%%%%%%%@###*+####+##++-=+#%#%%##%%%%*%##%%%%@@@@@@%############*##+-...........
#***#######%%%%%%@@%%#%####*--==..-=*%##%#%%%#####%%%%%@@@@@@@%%%##%%#####*=:.::::::::::::
-+****##%%%%%@@%@%%%%%###++-:.....:-+##%%%%%%%##%%%##%%%%%@@@@@%%%#*####*=::::::::::::::::
:::-+*######%%%%%%%%#####*-:::....::=*%%%%%%%%%%%%%%##%%%%@@@@@@@@@%*#+-::::::::::::::::::
::::::=**#%%%%%%%%%#####*+-:::::::.:=*#%%%%%%%%%%@%%%%%%%%%%@@@@@@@%+:::::::::::::::::::::
::::::::%%%%%%%%%%%%%%#%%#+-::::::.:-+*##%%%%%%%@@@@@@@@%%#%%%%@@%%#-:::::::::::::::::::::
..::::::-#%%%%%%%%%@@@@@@%#+---:::..::=*#%#%#%%@@@@@@@@@@%%%%%%%@#=:::::::::::::::::::::::
..:::::::=%@@%%%%@@@@@@@@@%*+=-:::...::+*####%@@@@@#@@@%%%#%%%%%%#=:::::::::::::::::::::::
:::::::::-#@@%%%%%@@@@@%@@@%++--::....::+*###@@@@@@@@@@@#%*%%%%%%%#-::::::::::::::::::::::
:::::::::-*%@%%#%#@@@@@@@@@@+=--::::::::=*##%@%@@@@@@@@@*##%%@@*+=-:::::::::::::::::::::::
::::::::::+%%%%##%%@@@@@@@@@*----:::::::-*##%@%#%@@@@@%###%%%%@#::::::::::::::::::::::::::
::::::::::-+%%%%%##%%@%%%%%@+---:::::::::=*#%%%%#*#%%#%##%%@%@@@*:::::::::::::::::::::::::
:::::::::::=#%%@%%########*#+---::::::::::-*#%#########%@@@@%%%%+:::::::::::::::::::::::::
.:::::::::::=%%%%%%#*+++=------::..:::::::::+**######%%@@@@@@@@#::::::::::::::::::::::::::
.::::::::::-+%%%%%%#*=::::::--::::..:::::::::=+******#%%@@@%%%%#-:::::::::::::::::::::::::
.:::::::::::=*%%###*=::.::::--:::::::::::::::::--:==++*#%%%%%%=--:::::::::::::::::::::::::
.::::::::::::-#%%#*+-::::::---::::::::::::::::......:-=*%@@@%*-:::::::::::::::::::::::::::
::::::::::::--+##**+--::::::----::::::--:::-::......::+#%%%+-------------::::::--------:::
:::::::::::::-=+**+==---::::-=====-----------:.......:=****##=----------------------------
..:::::::::-+*####*+=-:::::::=++++++++===++=::.:::::::-*******----------------------------
::::::::::=*#######*=------:::=*##******#*=::::::::::--+**+==----------:::::::::----------
:::::::::=****#%%%%*=---==-==-=+*#####*#+-:::------======::----:-:::::::::::::::::::::::::
:::::----*####%%#*+++=--=========++*##*+==-------===++++==--::::::::::::::::::::::::::::::
::------+#####**###*+========+++++++*##*++++++++++=++=--=--------------:::::::::::::::::::
::-----=*#######%%#*=====++++++++***#####***+++++++++++=------::------------::--------::::
-------*##%###%%#%#*++==+++=++++++++*####*++***+*++++==+=-:-----------------------------::
------+###%%###%%%##*+=+++++++++++++++++**+******+====-=-:::------------------------------
:----*#%#%%##%%%#%#%*+++++++++**+++**+*+********+==-------:--=----------------------------
---=#%%%%%%%%%#%@%%%+++++++++**+++++++*+******++===-::::---:-==---------------------------
---*%@@@%%%%%#%%%@%**#*++++++*+**+++++*****+*++====+-::---=-::===-------------------------
---%@@@@@@@%%%%#%%@@%#++++++*++**++++*++*++++++=---=+=-=:-==------------------------------
--=#@@@@@@@@%%%%%%%%%#**++++++++++**+*++**+++=++=-:=+--=-:-=-====-------------------------
---+%@@@@@@@@%%%%%%@%%#*++++++++*+**+**++*++===++--++---=-:=====--------------------------
--==#@@@@@@@@@@%%%%%%%#++++++++*++*****+++++=-=++--===---:--===---------------------------
---=#%@@@@@@%%#*#%%@%%%#++++++*++++***+++++++--==:---==----========-----------------------
---=+#%%%##********##%%*++++++++++***+++=++++=---:---====-========-------------==---------
---===+++++++++******#%#++++++*****++*++++=++=--=-==++====-=------------------------------
----======++++++******%%++++++****++++++++++=+=-+++**+==========--------------------------
----=========+++++****#%#++++++++++++++++++++++=+***++===========-----===-----------------
----=========+++++++***#%*+++++++++++++++*****++++*+++=================---------====----==
----==========+++++++***#%#**++++++++++*+++++++++++++++=--==============-----===------====
---============+++++++***%%%%%#*+++++***+++++++++++++===---======----====-----=--------===
--==============++++++***#%%%%%%#*++***++++++++++++++============-----====-------====----=
--================++++++**%@@@%%%#****++++++++++++++++========----===--====---=========--=
----------=========+++++++*#%@@@%%%#*++++++++++++++++++=======---======---========--------
-----------=========++++++++#%%@@%%%#+++++++=======++++++============----========---------
::::::::::---------------====+***#####++++=======================-------------------::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::...
:::::::::::::::::::::::::::::::......................................:....................
::::::::::::::::::::::::::................................................................
:::::::::::::::::::::::::.................................................................
:::::::::::::::::::::::...................................................................
:::::::::::::::::::::::::::...............................................................'''
            IS = False
        class MATH:
            IS = False  
                   
def interpret(line):
    if r"func[" in line:
        function_name = re.search(gvar.funcName, line) 
        if function_name is not None:
            function_name = re.search(gvar.funcName, line).group(1)
            function_params = re.search(gvar.FuncParameters, line)
            if function_params is not None:
                function_params = re.search(gvar.FuncParameters, line).group(1)
                gvar.UFuncsParams[function_name] = function_params
                function_code = re.search(gvar.encapsulator, line)
                if function_code is not None:
                    function_code = re.search(gvar.encapsulator, line).group(1)
                    gvar.UFuncs[function_name] = function_code
    elif r"if(" in line:
        match = re.search(gvar.definer, line)        
        if match is not None:
            match = re.search(gvar.definer, line).group(1)
            match = re.search(gvar.varIs, match)
            if match is not None: # If it is i == 1, for example.
                arg1 = match.group(1)
                arg2 = match.group(2)
                if arg1 is not int:
                    if gvar.UVars.get(arg1.replace(" ", "")) == arg2.replace(" ", ""):
                        encapsulated = re.search(gvar.encapsulator, line)
                        if encapsulated is not None:
                            interpret(encapsulated.group(1))
                    else:  
                        pass
                else:
                    pass    
            else:
                match = re.search(gvar.varIsnt, match)
                if match is not None:
                    arg1 = match.group(1)
                    arg2 = match.group(2)
                    if arg1 is not int:
                        if gvar.UVars.get(arg1) is not arg2:
                            encapsulated = re.search(gvar.encapsulator, line)
                            if encapsulated is not None:
                                interpret(encapsulated.group(1))
                        else:        
                            pass 
        else:
            print("Line", gvar.line, "> Syntax error!, Missing Closing Bracket! -> ]")               
    elif r"while(" in line:
        match = re.search(gvar.definer, line)    
        if match is not None:
            condition=re.search(gvar.definer, line)
            if "==" in condition.group(1):
                match = re.search(gvar.encapsulator, line).group(1)
                if match is not None:
                    match1 = re.search(gvar.varIs, condition).group(1)
                    print(match1)
                    match2 = re.search(gvar.varIs, condition).group(2)
                    while match1 == match2:
                        interpret(match)                        
    elif r"print(" in line:
        match = re.search(gvar.definer, line)
        if match is not None:
            if re.search(gvar.string, line) == None:
                if gvar.UVars.get(match) == None:
                    print(gvar.UVars.get(match.group(1)))
                else:    
                    print("Line", gvar.line, "> Syntax error!, Nothing provided for function 'print'!")
            else:    
                print(str(re.search(gvar.string, line).group(1)))
        elif match == None: 
            print("Line", gvar.line, "> Syntax error!, Nothing provided for function 'print'!")
        else:
            print("Line", gvar.line, "> Syntax error!, Missing Closing Bracket! -> ]")
    elif r"var(" in line:
        match = re.search(gvar.definer, line)
        if match is not None:
            match_text = match.group(1)
            var_match = re.search(gvar.varDefiner, match_text)
            if var_match is not None:
                gvar.UVars[var_match.group(1)] = var_match.group(2)
            else:
                print("Line", gvar.line, "> Syntax error!, Invalid variable definition!")
        else:
            print("Line", gvar.line, "> Syntax error!, Missing Closing Bracket! -> ]")
    elif r"import(" in line:
        match = re.search(gvar.definer, line)
        if match is not None:
            match = re.search(gvar.definer, line).group(1)
            if match == "COLOR":
                gvar.IMPORTS.COLOR.IS=True
            elif match == "MATH":
                gvar.IMPORTS.MATH.IS=True
                import math    
            elif match == "THIS":
                gvar.IMPORTS.THIS.IS=True
                gvar.UVars["THIS"] = gvar.IMPORTS.THIS.SOG  
                print(gvar.IMPORTS.THIS.SOG)   
        elif match == None:    
            print("Line", gvar.line, "> Syntax error!, Nothing provided for function 'import'!")
        else:
            if ")" in line:
                print("Line", gvar.line, "> Import error!. Import not recognized!")
            else:
                print("Line", gvar.line, "> Syntax error!, Missing Closing Bracket! -> ]")
    elif r"pause(" in line:
        match = re.search(gvar.definer, line)
        if match is not None:
            time.sleep(int(re.search(gvar.definer, line).group(0)))
        elif match is None:
            print("Line", gvar.line, "> Syntax error!, Missing Closing Bracket! -> ]")    
    elif r"sog+(" in line:
        match = re.search(gvar.definer, line)
        if match is not None:
            interpretFile(match.group(1))   
    else:
        if gvar.UFuncs.get(line) is not None:
            interpret(gvar.UFuncs.get(line))
        else:
            if "=" in line:
                    if re.search(gvar.varDefiner, line) is not None:
                        match = re.search(gvar.varDefiner, line)
                        if gvar.UVars.get(match.group(1)) is not None:
                            gvar.UVars.pop(match.group(1), None)
                            gvar.UVars[match.group(1)] = re.search(gvar.varDefiner, line).group(2)
def interpretFile(file):
    file1 = open(file, 'r')
    Lines = file1.readlines()
 
    count = 0
    # Strips the newline character
    for line in Lines:
        count += 1
        interpret(line) 
                                 
while True:
    if i == 0:
        print("Loading resources..")
        while e in range(0, 1000):
            gvar.UVars[e] = e 
            e = e+1
        print("SOG+ Resources loaded, opening terminal..")    
        i=1    
    cmd = input("SOG+ >")
    interpret(cmd)
