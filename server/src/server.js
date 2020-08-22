const Logger = require('./logger.js')

const Express = require('express')

const App = Express();

module.exports.init = async function()
{
    App.get('/api/', (req, res, next) => {
        res.send('bruh');
    });
    
    return new Promise((resolve, reject) => {
        try
        {
            App.listen(process.env.SERVER_PORT, () => {
                resolve();
                Logger.info(`Server listening on port ${process.env.SERVER_PORT}`);
            });
        } catch (e)
        {
            Logger.panic(`Cannot listen on port ${process.env.SERVER_PORT}: ${e}`);
            reject();
        }
    });
}
