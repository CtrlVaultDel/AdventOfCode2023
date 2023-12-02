// To Test:
// 1. Click in file
// 2. Ctrl + Alt + N
import { getInput, getPerformance, logAnswer } from "../../../templates/ryan-devault/commonHelper.mjs"

async function d2s2(){
    const input = await getInput("./Days/2/ryan-devault/input.txt");
    return input.reduce((acc, game) => {
        const gameData = game.split(": ")
        const rounds = gameData[1].replace("\r", "").split("; ")
        const cubes = {
            red: 0,
            green: 0,
            blue: 0
        }
        rounds.forEach(round => {
            const picks = round.split(", ")
            return picks.forEach(pick => {
                const splitPick = pick.split(" ");
                if(cubes[splitPick[1]] < splitPick[0]){
                    cubes[splitPick[1]] = +splitPick[0]
                }
            }) 
        })
        return acc += (cubes.red * cubes.green * cubes.blue)
    }, 0)
}

logAnswer(d2s2)
getPerformance(d2s2)