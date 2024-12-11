translations = [
    {
        "translate_words": ["girl", "girls", "woman", "womans", "women", "womens", "hoe", "hoes"],
        "translated": "huzz"
    },
    {
        "translate_words": ["bro", "bros"],
        "translated": "bruzz"
    },
    {
        "translate_words": ["grandma"],
        "translated": "grandmuzz"
    },
    {
        "translate_words": ["grandpa"],
        "translated": "grandpuzz"
    },
    {
        "translate_words": ["mom", "mum", "mommy", "mummy", "mother"],
        "translated": "muzz"
    },
    {
        "translate_words": ["dad", "daddy", "father"],
        "translated": "grandpuzz"
    },

    # HONOURABLE MENTIONS/EXTRAS
    {
        "translate_words": ["ass"],
        "translated": "gyat"
    },
    {
        "translate_words": ["pussy"],
        "translated": "bussy"
    },
    {
        "translate_words": ["this"],
        "translated": "ts"
    }
]

while True:
    input_text = input("") # get input
    if input_text == "": break # no input, return and exit

    text = [] # output as array

    # loop each word in input
    for word in input_text.split(" "):
        # loop through each translation
        found = None
        for translation in translations:
            translate_words = translation["translate_words"]
            translated = translation["translated"]
            # loop through each word in translation_words array
            for translate_word in translate_words:
                if word.lower() == translate_word.lower():
                    found = True
                    break
            # append translated word to output array, or input word if no match
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

    output_text = " ".join(text) # convert output array to string

    print(output_text) # print output