import  {db} from  '../config/db.js';
import fs from "fs";
import * as p4ssw0rd from 'p4ssw0rd';
/*
register.json

columns: 
user_id
first_name
last_name
email - a unique
username - a unique
created_date (ie. date when the user registered)
last_login - date (ie. date when the user last logged in).

user_id, first_name, last_name, email, username, password, created_date, last_login

// Hash will always be 60 characters long.

[{user_id, first_name, last_name, email, username, password, created_date, last_login}]
	
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


//Create ADD NEW => recive data 
export const insertUser = async (dataFromUser) => {
    console.log("object to insert:", dataFromUser)
    //logic to check data before store
    let first_name =  dataFromUser.first_name;
    let last_name = dataFromUser.last_name;
    let usernameFromUser = dataFromUser.username;
    let emailFromUser = dataFromUser.email;
    let password = dataFromUser.password;
    let date_time = new Date();
     //check length
    let checkLength = true;
    let newUserInfo = {};
    let users;
    // DI_Bootcamp_April2023\DI-Bootcamp\Week10\Day4\DC\data\register.json
   
    try {
        //read file
        //check if file exist
    
        const data = fs.readFileSync('../dc/data/register.json', 'utf-8');
        users = JSON.parse(data);
        console.log("users OK:");
        
 
        // data analyses 

        //find max user_Id
        let user_id = 1;
        let userIdMax = 1;
        if (users.length > 0) {
            //find max user_id
            userIdMax = users.reduce(
                (acc, value) => {
                return (acc = acc > value.user_id ? acc : value.user_id)
                }, 0);
            user_id = userIdMax + 1;
        }

        //check username and email
        if (users.findIndex(item => item.username === usernameFromUser) >= 0 || users.findIndex(item => item.email === emailFromUser) >= 0) {
            console.log("User name or email already registered.");
            throw  new Error("User name or email already registered."); 
            
        };       
        
        // write to file
        // add user data to users arr
        newUserInfo = {
            user_id: user_id, 
            first_name: first_name,
            last_name: last_name,
            email: emailFromUser,
            username: usernameFromUser,
            password: password,
            created_date: date_time,
            last_login: "",
            }
            
        users.push(newUserInfo);
        // write sync

        fs.writeFileSync('../dc/data/register.json', JSON.stringify(users), 'utf-8', (err) => {
            console.log("write to file");
            if (err) return console.log(err);
            return console.log("write to file:", newUserInfo);
            });

    
        console.log("max id:", userIdMax);
        console.log(date_time);
        return newUserInfo;
     
          


        } catch (error) {
                console.error('Error writing to file:', error.message);
                throw new Error(error.message);
        }  
    
      
}

 //search username
 export const checkLogin = async (username, password) => {
    console.log("Models recive object to search: ", username, "and pasww", password)
    //read data from register file
    let users;
    let login = false;
    try {
        //read file
        //check if file exist
    
        const data = fs.readFileSync('../dc/data/register.json', 'utf-8');
        users = JSON.parse(data);
        console.log("read from file users OK:");
        
 
        // data analyses 

        const userInfoIndex = users.findIndex(item => item.username === username)
        //check username and email
        if (userInfoIndex > 0) {
            const dbHashPassword = users[userInfoIndex]["password"]
            console.log("passw:", dbHashPassword);
            // check password
            if (p4ssw0rd.check(password, dbHashPassword)) {
                login = true;
                insertLogin(username, dbHashPassword);
            } else {
                console.log("Password no Ok");
                throw  new Error("Password no Ok"); 
            }

        } else {
            console.log("User name is registered.");
            throw  new Error("User name doesn't."); 
        };

    } catch (error) {
        console.error('Error writing to file:', error.message);
        throw new Error(error.message);
    } 

    return login
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


//Create ADD NEW Login => recive data = username
export const insertLogin = async (username, password) => {
    console.log("Models info login to insert:", {username, password})
    let logins = [];
    let date_time = new Date();
    try { 
        const data = fs.readFileSync('../dc/data/login.json', 'utf-8');
        logins = JSON.parse(data);
        console.log("read from file users OK:", logins);
        // add info
        logins.push({username, password, date_time})
        //write to file
        
        fs.writeFileSync('../dc/data/login.json', JSON.stringify(logins), 'utf-8', (err) => {
            console.log("write to file");
            if (err) return console.log(err);
            return console.log("write to file login:", username, date_time);
            });

    } catch (error) {
        console.error('Error writing to file:', error.message);
        throw new Error(error.message);
    } 

   
 }