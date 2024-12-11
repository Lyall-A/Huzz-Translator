import json

# vars
extras = True
translations = []
extra_translations = []
allTranslations = []

# load translations
with open("translations.json", "r") as file: translations = json.load(file)
if extras:
    with open("extra_translations.json", "r") as file: extra_translations = json.load(file)

# all translations
allTranslations = translations + extra_translations

print("===================================")
print("=         Huzz Translator         =")
print("=                                 =")
print("=    Type into terminal to use    =")
print("===================================")
print("")

while True:
    # get input
    input_text = input("Translate:  ")
    # no input, return and exit
    if input_text == "": break

    text = [] # output as array

    # loop each word in input
    for word in input_text.split(" "):
        found = None

        # loop through each translation
        for translation in allTranslations:
            translate_words = translation["translate_words"]
            translated = translation["translated"]

            # loop through each word in translation_words array
            for translate_word in translate_words:
                if word.lower() == translate_word.lower():
                    found = True
                    break
            
            # append translated word if found
            if found:
                # match, append translated word in either upper case, lower case or original form depending on the case of the input word
                if word.isupper():
                    text.append(translated.upper()) # convert translated word to upper
                elif word.islower():
                    text.append(translated.lower()) # convert translated word to lower
                else:
                    text.append(translated) # original state
                break
        if not found:
            # no match, append input word
            text.append(word)

    # convert output array to string
    output_text = " ".join(text)

    # print output
    print("Translated: " + output_text)
    print("")