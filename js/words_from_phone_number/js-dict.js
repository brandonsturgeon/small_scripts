const fs = require("fs")

const dictionary = fs.readFileSync("words.txt", "utf8")

const numberMap = {
  1: [],
  2: ["A","B","C"],
  3: ["D", "E", "F"],
  4: ["G", "H", "I"],
  5: ["J", "K", "L"],
  6: ["M", "N", "O"],
  7: ["P", "Q", "R", "S"],
  8: ["T", "U", "V"],
  9: ["W", "X", "Y", "Z"],
  0: []
}

const number = "669"

const generatePatternForDigit = d => `(${numberMap[d].join("|")})`
const generatePatternForDigits = digits => digits.split("").map(d => generatePatternForDigit(d)).join("")
const generatePatternForNumber = number => new RegExp(`^${generatePatternForDigits(number)}$`, "gmi")

console.log(`Phone number: ${number}`)
const pattern = generatePatternForNumber(number)
console.log(pattern)

console.log(dictionary.match(pattern))


/*
 Example Runs:

Phone number: 7378423
/^(P|Q|R|S)(D|E|F)(P|Q|R|S)(T|U|V)(G|H|I)(A|B|C)(D|E|F)$/gim

              |
              v
[ 'restiad', 'Service', 'sestiad' ]

Phone number: 669
/^(M|N|O)(M|N|O)(W|X|Y|Z)$/gim
[ 'MMW', 'MMX', 'moy', 'mow', 'NNW', 'NNX', 'noy', 'now', 'Nox', 'ony' ]
                                                    ^
                                                    |
*/

