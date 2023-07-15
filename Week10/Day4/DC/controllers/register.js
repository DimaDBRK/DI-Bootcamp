import { getAllUsers, insertUser, getAllLogins, insertLogin, checkLogin, updateLastLogin} from "../models/register.js";

import * as p4ssw0rd from 'p4ssw0rd';


//READ - GET get all Users  -> _ before it 
export const _getAllUsers = (req, res) => {
    console.log('Controller received get req for all users')
    getAllUsers() // it is function, return promise
    .then(data => {
        res.json(data)
    })
    .catch(e => {
        console.log("ERROR CONTROLLER:", e);
        res.status(404).json({ msg: "not found" }); // or e.message
    })
}

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
        if (data.length === 0 ) {
            console.log(`username ${userLoginUsername} doesn't exist.`);
            result = `username ${userLoginUsername} doesn't exist.`;
            res.json({result, login: false});
        } else {
            const dbHashPassword = data[0].password;
            const userRegisterId = data[0].user_id;
            console.log("DB hash password: ", dbHashPassword);
            const checkPassword = p4ssw0rd.check(userLoginPassword, dbHashPassword);
            console.log("p4ssw0rd check password result: ", checkPassword);
            if (checkPassword) {
                console.log(`Check OK, welcome ${userLoginUsername}`);
                result = `Check OK, welcome ${userLoginUsername}`;
                res.json({result, login: true})
                // update data in DB for Login  -> directly from here
                insertLogin({username: userLoginUsername, password: dbHashPassword})
                .then(data => {
                    console.log("in login added info:",data)
                    // _getAllUsers(req,res) // return all with update
                })
                .catch(e => {
                    console.log("ERROR CONTROLLER", e, "detail:", e.detail);
                    // "problem with insert" or e.message
                })

                // update date in Register DB
                // res = OK
                updateLastLogin(userRegisterId).then(data => {
                    console.log("update login date info from DB:",data)
                })
                .catch(e => {
                    console.log("error update login date:", e.msg);
                })
            
            } else { 
                console.log(`Password for user ${userLoginUsername} is incorrect.`);
                result = `Password for user ${userLoginUsername} is incorrect.`;
                res.json({result, login: false})
            }
        }
      
    })
    .catch(e => {
        console.log(e);
        res.status(404).json({ msg: e.message }); // or e.message
    })
}

// update date




//read all logins
//READ - GET get all  -> _ before it 
export const _getAllLogins = (req, res) => {
    console.log('Controller received get req for all logins', res)
    getAllLogins() // it is function, rturn promise
    .then(data => {
        res.json(data)
    })
    .catch(e => {
        console.log("ERROR CONTROLLER LOGIN:", e.message);
        res.status(404).json({ msg: "not found logins" }); // or e.message
    })
}

// ADD Login
export const _insertLogin = (req, res) => {
    console.log('Controller received post req to add Login', req.body)
    //modify password:
    // console.log("PASS before modify:", req.body.password);
    // const hash = p4ssw0rd.hash(req.body.password);
    // console.log("PASS after p4ssw0rd:", hash);
    // req.body.password = hash;
    // console.log("PASS decode check:", (p4ssw0rd.check("req.body.password", hash)));
    
    insertLogin(req.body)
    .then(data => {
        res.json(data)
        // _getAllUsers(req,res) // return all with update
    })
    .catch(e => {
        console.log("ERROR CONTROLLER", e, "detail:", e.detail);
        res.status(404).json({ msg: e.message });
        // "problem with insert" or e.message
    })
}
