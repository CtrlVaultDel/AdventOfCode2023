// To Test:
// 1. Click in solution1.mjs
// 2. Ctrl + Alt + N
import { getInput } from "../../../templates/ryan-devault/commonHelper.mjs"

const startTime = performance.now();
const numWords = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];

const input = await getInput("./Days/1/ryan-devault/input.txt");
const answer = input.reduce((acc, cur, idx) => {
    let str = cur;
    
    // Convert words to numbers if they exist
    numWords.forEach((word, idx) => {
        while(str.includes(word)){
            str = [
                ...str.slice(0, str.indexOf(word)), 
                `${idx}`, 
                ...str.slice(str.indexOf(word) + word.length)
            ].join("")
        }
    })
    const match = str.match(/[0-9]/g);                                  // 1. Only capture numbers in the string "a,b,c,1,2,3,d,e,f" -> ["1", "2", "3"]
    const num = Number([match[0], match[match.length - 1]].join(""));   // 2. Get the first and last number & join together ["1", "2", "3"] -> 13
    if(idx > 50 && idx < 100){
        console.log("=============")
        console.log("cur", cur)
        console.log("str", str)
        console.log("match", match)
        console.log("num", num)
    }
    return acc += num;                                                  // 3. Update accumulator with resulting value from prior step
}, 0)

console.log(answer);
console.log(performance.now() - startTime);

// 52960 is too low
// 53036 is too low