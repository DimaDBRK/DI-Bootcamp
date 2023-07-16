import {  insertUser, checkLogin } from "../models/register.js";

import * as p4ssw0rd from 'p4ssw0rd';



// ADD User
export const _insertUser = (req, res) => {
    console.log('Controller received post req to add users', req.body)
    //modify password:
    console.log("PASS before modify:", req.body.password);
    const hash = p4ssw0rd.hash(req.body.password);
    console.log("PASS after p4ssw0rd:", hash);
    req.body.password = hash;

    // console.log("PASS decode check:", (p4ssw0rd.check("req.body.password", hash)));
    
    insertUser(req.body)
    .then(data => {
        console.log("controller res:", data);
        res.json([data])
        // _getAllUsers(req,res) // return all with update
    })
    .catch(e => {
        console.log("ERROR CONTROLLER", e);
        res.status(404).json({ msg: e.message });//e.message });
         // "problem with insert" or e.message
    })
}

//check login = search by username and password
export const _checkLogin = (req, res) => {
    console.log('Controller received post check login users:', "1-", req.body.username, "2-", req.body.password)
    const userLoginPassword = req.body.password;
    const userLoginUsername = req.body.username;
    let result = '';
    checkLogin(userLoginUsername, userLoginPassword)
    .then(data => {
        console.log("response from db:", data)
        if (!data) {
            console.log(`username ${userLoginUsername} doesn't exist.`);
            result = `username ${userLoginUsername} doesn't exist.`;
            res.json({result, login: false});
        } else {
          
                console.log(`Check OK, welcome ${userLoginUsername}`);
                result = `Check OK, welcome ${userLoginUsername}`;
                res.json({result, login: true})
        }
    })
    .catch(e => {
        console.log(e);
        res.status(404).json({ msg: e.message }); // or e.message
    })
}

// update date



