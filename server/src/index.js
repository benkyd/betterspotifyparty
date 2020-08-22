const Logger = require('./logger.js');
const Database = require('./database.js');
const Server = require('./server.js');

module.exports.main = async function()
{
    Logger.init('./storage/logs.log');
    Logger.SetLevel(Logger.VERBOSE_LOGS);
    Logger.welcome();

    if (process.env.NODE_ENV == 'production')
    {
        Logger.info('Starting up in production mode');
    } else {
        Logger.debug('Starting up in development mode');
    }

    await Database.setup();
    await Server.init();

    Logger.ready();

}
