import  {db} from  '../config/db.js';
import fs from "fs";
/*
register

columns: 
user_id
first_name
last_name
email - a unique
username
created_date (ie. date when the user registered)
last_login - date (ie. date when the user last logged in).

user_id, first_name, last_name, email, username, password, created_date, last_login

// Hash will always be 60 characters long.

create table register (
	user_id serial primary key,
	first_name varchar(50) not null,
        last_name varchar(50),
        email varchar(254) UNIQUE NOT NULL,
        username varchar(50) UNIQUE not null,
        password varchar(70) not null,
        created_date timestamp NOT NULL DEFAULT LOCALTIMESTAMP,
        last_login timestamp
)
*/


//all info
export const getAllUsers = () => {
    console.log('Received get req for all users');
    return db('register')
        .select('user_id', 'first_name', 'last_name', 'email', 'username', 'password','created_date', 'last_login')
        .orderBy('user_id')
}

//Create ADD NEW => recive data 
export const insertUser = (data) => {
    console.log("object to insert:", data)
    return db('register')
    .insert(data)
    .returning(['user_id', 'first_name', 'last_name', 'email', 'username','password','created_date', 'last_login'])
   
 }

 //search username
 export const checkLogin = (username, password) => {
    console.log("Models recive object to search: ", username, "and pasww", password)
    return db('register')
    .select('user_id', 'username', 'password')
    .where({username: username}) // sql req = ilike + % %, check knex documentation => whereIlike
    // console.log("result from DB:", result)
    // return result
 }
// update user login date
export const updateLastLogin = (user_id) => {
    let date_time = new Date();
    return db('register')
    .update({last_login: date_time})
    .where({user_id})
    .returning(['user_id','username','last_login'])
 }

/*
 login_id, username, password

// Hash will always be 60 characters long.

create table login (
	login_id serial primary key,
	username varchar(50) not null,
    password varchar(70) not null
)
*/

export const getAllLogins = () => {
    console.log('Received get req for all users');
    return db('login')
        .select('login_id', 'username', 'password')
        .orderBy('login_id')
}

//Create ADD NEW Login => recive data = username
export const insertLogin = ({username, password}) => {
    console.log("Models info login to insert:", {username, password})
    return db('login')
    .insert({username, password})
    .returning(['login_id', 'username', 'password'])
   
 }