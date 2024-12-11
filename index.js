const readline = require("readline");
const huzz = require("./huzz");

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });

const extras = true;

console.log("===================================");
console.log("=         Huzz Translator         =");
console.log("=                                 =");
console.log("=    Type into terminal to use    =");
console.log("===================================");
console.log("");

(function main() {
    // get input
    rl.question("Translate:  ", inputText => {
        if (!inputText) return rl.close(); // no input, return and exit

        const outputText = huzz.translate(inputText, true);

        console.log(`Translated: ${outputText}`);
        console.log("");

        main();
    });
})();