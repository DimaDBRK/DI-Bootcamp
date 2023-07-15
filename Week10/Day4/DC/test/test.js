
import fs from "fs";
let usernameFromUser = "Den";
let emailFromUser = "asg";
let  first_name =  "dd";
let last_name = "s";
let password = "123";

let date_time = new Date();

fs.readFile('../data/register.json', 'utf-8', (err, data) => {
    if (err) return console.log(err);
    const users = JSON.parse(data);
    console.log("result",data);
    //find max user_Id
    // const index = users.findIndex(item => item.user_id == 3); // -1
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
        return console.log("User name or email already registered.");
    };

    //chek length
    let checkLength = true;

    if (checkLength) {
        // write to file
        
        const newUserInfo = {
            user_id: user_id, 
            first_name: first_name,
            last_name: last_name,
            email: emailFromUser,
            username: usernameFromUser,
            password: password,
            created_date: date_time,
            last_login: "",
           
        };
        users.push(newUserInfo);

        fs.writeFile('../data/register.json', JSON.stringify(users), 'utf-8', (err) => {
            if (err) return console.log(err);
            return newUserInfo;
            });

    } else {
        return console.log("Check length of data.");
    }

    console.log("max id:", userIdMax);
    console.log(date_time);


});


// //v2
// /Create ADD NEW => recive data 
// export const insertUser = async (dataFromUser) => {
//     console.log("object to insert:", dataFromUser)
//     //logic to check data before store
//     let first_name =  dataFromUser.first_name;
//     let last_name = dataFromUser.last_name;
//     let usernameFromUser = dataFromUser.username;
//     let emailFromUser = dataFromUser.email;
//     let password = dataFromUser.password;
//     let date_time = new Date();
//      //check length
//     let checkLength = true;
//     let newUserInfo = {};
//     // DI_Bootcamp_April2023\DI-Bootcamp\Week10\Day4\DC\data\register.json
//     if (checkLength) {

//         return  Promise.resolve( 
//             fs.readFile('../dc/data/register.json', 'utf-8', (err, data) => { 
//             if (err) return console.log(err);
//             const users = JSON.parse(data);
//             console.log("users OK:");
//             //find max user_Id
//             // const index = users.findIndex(item => item.user_id == 3); // -1
//             let user_id = 1;
//             let userIdMax = 1;
//             if (users.length > 0) {
//                 //find max user_id
//                 userIdMax = users.reduce(
//                     (acc, value) => {
//                     return (acc = acc > value.user_id ? acc : value.user_id)
//                     }, 0);
//                     user_id = userIdMax + 1;
//             }

//             //check username and email
//             if (users.findIndex(item => item.username === usernameFromUser) >= 0 || users.findIndex(item => item.email === emailFromUser) >= 0) {
//                 console.log("User name or email already registered.");
//                 return  new Error("User name or email already registered."); 
//             };       
//             // write to file
//             newUserInfo = {
//                 user_id: user_id, 
//                 first_name: first_name,
//                 last_name: last_name,
//                 email: emailFromUser,
//                 username: usernameFromUser,
//                 password: password,
//                 created_date: date_time,
//                 last_login: "",
//             }
            
//             users.push(newUserInfo);

//             fs.writeFile('../dc/data/register.json', JSON.stringify(users), 'utf-8', (err) => {
//                 if (err) return console.log(err);
//                 return console.log("write to file:", newUserInfo);
//                 });

    
//             console.log("max id:", userIdMax);
//             console.log(date_time);
//             return newUserInfo;
//         })
        
        
//     );
    
//         // return [newUserInfo];
//     } else {
//         console.log("Check length of data.");
//         return Promise.reject(new Error("Check length of data.")); 
//     }
// }
