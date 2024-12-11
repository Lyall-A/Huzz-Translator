const translations = require("./translations.json");
const extraTranslations = require("./extra_translations.json");

function escapeRegex(string) {
    return string.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")
}

function translate(inputText, extras = true) {
    let outputText = inputText;

    // loop through each translation
    for (const [ translated, translateWords ] of Object.entries({ ...translations, ...(extras ? extraTranslations : { }) })) {
        // loop through each word in translation words
        for (const translateWord of translateWords) {
            // replace words
            outputText = outputText.replace(new RegExp(`\\b${escapeRegex(translateWord)}\\b`, "gi"), match => {
                if (match === match.toUpperCase()) return translated.toUpperCase(); // upper case
                if (match === match.toLowerCase()) return translated.toLowerCase(); // lower case
                if (match.charAt(0) === match.charAt(0).toUpperCase()) return `${translated.charAt(0).toUpperCase()}${translated.substring(1)}`; // capitalize
                return translated; // original
            });
        }
    }

    return outputText;
}

module.exports = {
    translate
}