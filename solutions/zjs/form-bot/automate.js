import { chromium } from "playwright";
// import {getInputs, clickButtons, detectField} from "./detector";

function detectField(field) {

    const text = (
        (field.name || "") +
        (field.id || "") +
        (field.placeholder || "")
    ).toLowerCase();

    if (text.includes("job") || text.includes("title")) return "jobTitle";
    if (text.includes("phone") || text.includes("mobile")) return "phone";
    if (text.includes("company")) return "company";
    if (text.includes("location")) return "location";
    if (text.includes("fullname")) return "fullname";
    if (text.includes("firstname")) return "firstname";

    return null;
}

async function clickButtons(page, name) {
    await page.evaluate((name) => {

        const buttons = Array.from(document.querySelectorAll("button"));

        buttons
            .filter(btn => {
                const text = (btn.innerText || "").toLowerCase();
                const id = (btn.id || "").toLowerCase();
                const type = (btn.type || "").toLowerCase();
                const attrName = (btn.name || "").toLowerCase();

                return (
                    text.includes(name.toLowerCase()) ||
                    id.includes(name.toLowerCase()) ||
                    type.includes(name.toLowerCase()) ||
                    attrName.includes(name.toLowerCase())
                );
            })
            .forEach(btn => btn.click());

    }, name);
}

async function getInputs(page) {

    return await page.evaluate(() => {
        const inputs = Array.from(document.querySelectorAll("input, textarea"));

        return inputs.map(input => ({
            name: input.name,
            id: input.id,
            placeholder: input.placeholder,
            type: input.type
        }));
    });
}

async function fillForm(page, data) {

    const inputs = await getInputs(page);

    clickButtons(page, "add");

    for (const field of inputs) {

        const type = detectField(field);

        if (!type) continue;

        const selector =
            field.name
                ? `input[name="${field.name}"]`
                : `#${field.id}`;

        if (!selector) continue;

        if (data[type]) {
            await page.fill(selector, data[type]);
        }
    }
}

async function run() {

    // /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir=/tmp/chrome-debug
    const browser = await chromium.connectOverCDP(
        "http://localhost:9222",
        { timeout: 10000 }
    );

    // const browser = await chromium.launch({
    //     channel: "chrome",
    //     headless: false 
    // });

    const context = browser.contexts()[0];
    const page = context.pages[0];
    await fillForm(page, {
        fullname: "Peidong Xu",
        firstname: "Peidong",
        familyname: "Xu",
        company: "Shopee",
        jobTitle: "backend engineer"
    });

}

run();