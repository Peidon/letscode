import Redis from "ioredis";

const redis = new Redis();

async function pushUrl(url) {
    await redis.lpush("crawl:queue", url);
}

async function popUrl() {
    return await redis.rpop("crawl:queue");
}

async function markVisited(url) {
    await redis.sadd("crawl:visited", url);
}

async function isVisited(url) {
    return await redis.sismember("crawl:visited", url);
}

export default { pushUrl, popUrl, markVisited, isVisited };