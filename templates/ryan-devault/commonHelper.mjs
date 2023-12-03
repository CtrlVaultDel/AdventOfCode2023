import fs from 'fs/promises';
import { artMap } from './artMap.mjs';

export async function getInput(filePath, splitNewLine = true) {
    try {
        const data = await fs.readFile(filePath, 'utf8');
        return splitNewLine ? data.split("\n") : data;
    } catch (err) {
        console.error(err);
        return [];
    }
}

export async function getPerformance(testFunction, numTests = 10){
    const startTime = performance.now();
    for(let i = 0; i < numTests; i++){
        await testFunction()
    }
    const avgTime = (performance.now() - startTime)/numTests
    logAsASCII(`AVG TIME: ${avgTime.toFixed(2)}ms`)
    console.log(`${numTests} tests ran.`)
}

export async function logAnswer(func){
    const answer = await func();
    logAsASCII(`ANSWER: ${answer}`)
}

export function logAsASCII(input) {
    const stringValue = String(input).toUpperCase();
    const charArray = [...stringValue];
  
    // Get the array of ASCII art for each character
    const artArray = charArray.map(char => artMap[char]);
  
    // Log the concatenated lines horizontally
    for (let i = 0; i < artArray[0].split('\n').length; i++) {
        const line = artArray.map(art => art.split('\n')[i]).join(' ');
        console.log(line);
    }
}