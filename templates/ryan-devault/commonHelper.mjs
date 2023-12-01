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