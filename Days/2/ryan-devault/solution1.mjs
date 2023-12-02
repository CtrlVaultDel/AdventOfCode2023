// To Test: (Need formulahendry.code-runner extension)
// 1. Click in file
// 2. Ctrl + Alt + N
import { getInput, getPerformance, logAnswer } from "../../../templates/ryan-devault/commonHelper.mjs"

async function d2s1(){
    const input = await getInput("./Days/2/ryan-devault/input.txt");  
    const MAX_VALUES = {
        red: 12,
        green: 13,
        blue: 14
    }
    let answer = 0;
    input.forEach(game => {
        const gameData = game.split(": ")
        const rounds = gameData[1].replace("\r", "").split("; ")
        const isValidGame = rounds.every(round => {
            const picks = round.split(", ")
            return picks.every(pick => {
                const splitPick = pick.split(" ");
                return MAX_VALUES[splitPick[1]] >= splitPick[0]
            }) 
        })
        if(isValidGame){
            // Add the valid game id
            answer += +gameData[0].match(/\d+/g)
        }
    })
    return answer;
}

logAnswer(d2s1);
getPerformance(d2s1)