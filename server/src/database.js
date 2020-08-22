const Logger = require('./logger.js');

const Sequelize = require('sequelize');

let Database;

module.exports.setup = async function()
{
    Logger.info('Setting up database');

    if (process.env.NODE_ENV == 'production')
    {
        Logger.database('Setting up production database');
        Database = new Sequelize(`mariadb://${process.env.PROD_DATABASE_HOST}:${process.env.PROD_DATABASE_PORT}/${process.env.PROD_DATABASE_DB}?user=${process.env.PROD_DATABASE_USER}&password=${process.env.PROD_DATABASE_PASS}`, {
            dialect: 'mariadb',
            logging: Logger.database
        });
    } else
    {
        Logger.database('Setting up production database');
        Database = new Sequelize({
            dialect: 'sqlite',
            storage: process.env.DEV_DATABASE_LOC,
            logging: Logger.database
        });
    }

    // ORM definitions here


    try {
        await Database.authenticate();
        await Database.sync();
        Logger.info('Database connection successfull');
    } catch (e)
    {
        Logger.panic('Unable to connect to database: ' + e)
    }

}