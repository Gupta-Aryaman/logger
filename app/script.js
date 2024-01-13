import fs from 'fs';
import { redis, connectRedis } from './db.js';

async function setupGears(){
    const requirements = ['rgsync', 'pymongo'];
    const writeBehindCode = fs
        .readFileSync('./write-behind.py', 'utf8')
        .toString()
        // .replace('%MONGODB_CONNECTION_URL%', process.env.MONGODB_URL);

    const params = [
        'RG.PYEXECUTE',
        writeBehindCode,
        'REQUIREMENTS',
        ...requirements,
    ];

    try{
        await redis?.sendCommand(params);
        console.log('RedisGers write behind setup complete');
    } catch(err){
        console.log('RedisGears write behind setup failed');
        console.log(JSON.stringify(err, Object.getOwnPropertyNames(err), 4));
    }
}

async function insertLog(log){
    await redis?.json.set(log);
    return;
}

try{
    await connectRedis();
    await redis.flushDb();
    await setupGears();

    await insertLog({
        "level": "error",
        "message": "Failed to connect to DB",
        "resourceId": "server-1234",
        "timestamp": "2023-09-15T08:00:00Z",
        "traceId": "abc-xyz-123",
        "spanId": "span-456",
        "commit": "5e5342f",
        "metadata": {
            "parentResourceId": "server-0987"
        }
    });

    await insertLog({
        "level": "error",
        "message": "Failed to connect to DB",
        "resourceId": "server-1234",
        "timestamp": "2023-09-15T08:00:00Z",
        "traceId": "abc-xyz-134",
        "spanId": "span-456",
        "commit": "5e5342f",
        "metadata": {
            "parentResourceId": "server-0987"
        }
    });

    await insertLog({
        "level": "error",
        "message": "Failed to connect to DB",
        "resourceId": "server-1234",
        "timestamp": "2023-09-15T08:00:00Z",
        "traceId": "abc-xyz-132",
        "spanId": "span-456",
        "commit": "5e5342f",
        "metadata": {
            "parentResourceId": "server-0987"
        }
    });

    process.exit();
} catch(e){
    console.log(e);
}