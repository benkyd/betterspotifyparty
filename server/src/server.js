const Logger = require('./logger.js')

const Express = require('express')

const App = Express();

module.exports.init = async function()
{
    App.listen(process.env.SERVER_PORT, () => {
        Logger.info(`Server listening on port ${process.env.SERVER_PORT}`);
    });


    App.get('/api/', (req, res, next) => {
        res.send('bruh');
    });

}
