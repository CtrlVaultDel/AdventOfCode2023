import fs from 'fs/promises';

export async function getInput(filePath) {
    try {
        const data = await fs.readFile(filePath, 'utf8');
        return data.split("\n");
    } catch (err) {
        console.error(err);
        return null;
    }
}

export async function getPerformance(testFunction, numTests = 10){
    const startTime = performance.now();
    for(let i = 0; i < numTests; i++){
        await testFunction()
    }
    const avgPerformance = (performance.now() - startTime)/numTests
    console.log(`${numTests} tests ran. Average performance: ${avgPerformance.toFixed(2)}ms`)
}

export async function logAnswer(func){
    const answer = await func();
    console.log("Answer:", answer);
}