def gen_acro(phrase):

    list_words = phrase.split(" ")
    final_acro = ""

    for i in list_words:
        final_acro+=i[0].upper()
 
    return final_acro
