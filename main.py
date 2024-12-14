import json
import re

# vars
extras = True # False to disable the extra non-huzz translations
translations = {}
extra_translations = {}
allTranslations = {}

# load translations
with open("translations.json", "r") as file: translations = json.load(file)
if extras:
    with open("extra_translations.json", "r") as file: extra_translations = json.load(file)

# all translations
allTranslations = {**translations, **extra_translations}

print("===================================")
print("=         Huzz Translator         =")
print("=                                 =")
print("=    Type into terminal to use    =")
print("===================================")
print("");
print("Translations:");
for translated, translateWords in translations.items(): print(f"{", ".join(translateWords)}: {translated}");
if extras:
    print("");
    print("Extra translations:");
    for translated, translateWords in extra_translations.items(): print(f"{", ".join(translateWords)}: {translated}");
print("");

while True:
    input_text = input("Translate:  ") # get input
    if input_text == "": break # no input, return and exit

    output_text = input_text

    # loop through each translation
    for translated, translate_words in allTranslations.items():
        # loop through each word in translation words
        for translate_word in translate_words:
            # replace words
            output_text = re.sub(
                f"\\b{re.escape(translate_word)}\\b",
                lambda match:
                    translated.upper() if match.group(0).isupper() # upper case
                    else translated.lower() if match.group(0).islower() # lower case
                    else translated.capitalize() if match.group(0)[0].isupper() # capitalize
                    else translated, # original
                output_text,
                flags=re.IGNORECASE
            )

    # print output
    print("Translated: " + output_text)
    print("")