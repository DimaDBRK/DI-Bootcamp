// sometimes we nedd to import again in every file
import dotenv from "dotenv";
dotenv.config();

import knex from 'knex';

//export
export const db = knex({
    client: 'pg',
    connection: {
      host : process.env.DB_HOST,
      port : process.env.DB_PORT,
      user : process.env.DB_USER,
      password : process.env.DB_PASS,
      database : process.env.DB_NAME
    }
});