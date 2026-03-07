import { get } from "axios";
import { load } from "cheerio";
import { URL } from "url";

const visited = new Set();
const queue = [];

async function crawl(startUrl, maxPages = 20) {
    queue.push(startUrl);

    while (queue.length > 0 && visited.size < maxPages) {
        const currentUrl = queue.shift();

        if (visited.has(currentUrl)) continue;

        try {
            console.log("Crawling:", currentUrl);

            const response = await get(currentUrl);
            const html = response.data;

            visited.add(currentUrl);

            const $ = load(html);

            $("a[href]").each((_i, link) => {
                let href = $(link).attr("href");

                try {
                    const absoluteUrl = new URL(href, currentUrl).href;

                    if (!visited.has(absoluteUrl)) {
                        queue.push(absoluteUrl);
                    }
                } catch (err) {
                    // ignore invalid URLs
                }
            });

        } catch (err) {
            console.log("Failed:", currentUrl);
        }
    }

    console.log("Finished. Pages crawled:", visited.size);
}

crawl("https://www.postgresql.org");