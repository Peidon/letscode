import axios from "axios";
import { load } from "cheerio";
import { URL } from "url";

import { pushUrl, popUrl, markVisited, isVisited } from "./queue";

async function crawl() {
    while (true) {

        const url = await popUrl();

        if (!url) {
            await new Promise(r => setTimeout(r, 1000));
            continue;
        }

        if (await isVisited(url)) continue;

        try {
            console.log("Crawling:", url);

            const resp = await axios.get(url, { timeout: 5000 });

            await markVisited(url);

            const $ = load(resp.data);

            $("a[href]").each(async (_i, el) => {

                const link = $(el).attr("href");

                try {
                    const absolute = new URL(link, url).href;

                    if (!(await isVisited(absolute))) {
                        await pushUrl(absolute);
                    }

                } catch (err) {}

            });

        } catch (err) {
            console.log("Failed:", url);
        }
    }
}

crawl();