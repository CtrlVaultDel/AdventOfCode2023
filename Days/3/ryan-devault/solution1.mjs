// To Test: (Need formulahendry.code-runner extension)
// 1. Click in file
// 2. Ctrl + Alt + N
import { getInput, getPerformance, logAnswer } from "../../../templates/ryan-devault/commonHelper.mjs"

async function d3s1(){
    const input = await getInput("./Days/3/sample.txt");
    let matrix = input.map(line => line.replace("\r", ""))
    // const input = await getInput("./Days/3/ryan-devault/input.txt");
    console.log(matrix)
}
d3s1()
// logAnswer(d3s1);
// getPerformance(d3s1);