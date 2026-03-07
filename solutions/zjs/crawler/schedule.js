import { pushUrl } from "./queue";

const seeds = [
    "https://example.com"
];

async function start() {

    for (const url of seeds) {
        await pushUrl(url);
    }

    console.log("Seed URLs added");
}

start();