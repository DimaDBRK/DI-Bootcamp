#Week3 Day3
#Dmitry Dubrov
# Daily Challenge: Translator
# You have to recreate the result using a translator module.

french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 

# Look at this result :
# {"Bonjour": "Hello", "Au revoir": "Goodbye", "Bienvenue": "Welcome", 
# "A bientôt": "See you soon"}
def transl_list(list_in):
    from googletrans import Translator #pay attantion: this version should be 
    #installed before, v3 which install auto doesn't work: 
    # pip install googletrans==4.0.0-rc1
    translator = Translator()
    res = {}
    for items in french_words:
        transl_res = str(translator.translate(items,src='fr', dest='en').text)
        res[items] = transl_res
    return res

print(transl_list(french_words))