const fs = require("fs")

const regexDictionary = fs.readFileSync("words.txt", "utf8")
const dictionary = {}
regexDictionary.split("\n").map(word => dictionary[word.toUpperCase()] = word)

const numberMap = {
  1: [],
  2: ["A", "B", "C"],
  3: ["D", "E", "F"],
  4: ["G", "H", "I"],
  5: ["J", "K", "L"],
  6: ["M", "N", "O"],
  7: ["P", "Q", "R", "S"],
  8: ["T", "U", "V"],
  9: ["W", "X", "Y", "Z"],
  0: []
}

const funWay = number => {
  const generatePatternForDigit = d => `(${numberMap[d].join("|")})`
  const generatePatternForDigits = digits => digits.split("").map(d => generatePatternForDigit(d)).join("")
  const generatePatternForNumber = number => new RegExp(`^${generatePatternForDigits(number)}$`, "gmi")

  const pattern = generatePatternForNumber(number)

  return regexDictionary.match(pattern)
}

funWay("669")
funWay("7378423")

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

const otherWay = number => {
  let stripped = number.replace("1", "")
  stripped = stripped.replace("0", "")

  let possibleWords = []

  for (let digit of stripped) {
    const possibleLetters = numberMap[digit]

    if ( possibleWords.length === 0 ) {
      possibleWords = possibleLetters
    } else {
      const newWords = []

      for (let possibleWord of possibleWords) {
        for (let possibleLetter of possibleLetters)  {
          newWords.push(possibleWord + possibleLetter)
        }
      }

      possibleWords = newWords
    }
  };

  const dictionaryWords = possibleWords.map(word => dictionary[word])
  const onlyGoodWords = dictionaryWords.filter(w => w)

  return onlyGoodWords
}

/* Benchmarking */
const benchmark = (runs, func, runArg) => {

  const startTime = new Date().getTime()

  for (let run of Array(runs)) {
    func(runArg)
  }

  const endTime = new Date().getTime()
  const runTime = endTime - startTime

  console.log(`[${runArg}] Average: ${runTime/runs}ms`)
}

const largerExampleNumber = "7378423"
const smallerExampleNumber = "669"

console.log("Permutations:")
benchmark(1000, otherWay, largerExampleNumber)
benchmark(1000, otherWay, smallerExampleNumber)

console.log("Regex:")
benchmark(1000, funWay, largerExampleNumber)
benchmark(1000, funWay, smallerExampleNumber)

/*

Permutations:
[7378423] Average: 1.711ms
[669] Average: 0.008ms

Regex:
[7378423] Average: 3.26ms
[669] Average: 5.499ms

*/
