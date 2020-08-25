const Logger = require('./logger.js');
const Helpers = require('./helpers.js');

const Express = require('express');

const App = Express();

module.exports.init = async function()
{
    App.use(Logger.middleware);

    // This is only needed for the "host" queue
    App.get('/api/auth', AuthenticateHandle);
    App.get('/api/authcallback', AuthenticatedHandle);
    
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


async function AuthenticateHandle(req, res, next)
{
    let scopes = 'user-read-private user-read-email streaming user-read-playback-state user-modify-playback-state user-read-currently-playing';
    res.redirect('https://accounts.spotify.com/authorize' +
        '?response_type=code' +
        '&client_id=' + process.env.SPOTIFY_APP_ID +
        (scopes ? '&scope=' + encodeURIComponent(scopes) : '') +
        '&redirect_uri=' + encodeURIComponent('http://' + process.env.SERVER_HOST + '/api/authcallback') + '&show_dialog=true');
}

async function AuthenticatedHandle(req, res, next)
{
    console.log('New spotify auth');
    console.log(Helpers.SafeJSONStringify(req, 4));
    // Database time
    res.send('Authenticated with spotify');
}
