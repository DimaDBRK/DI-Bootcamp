import express from 'express';
import { 
        _insertUser,
        
     
        _checkLogin
        } from '../controllers/register.js';

// it is traffic controller
const prouter = express.Router();


prouter.post("/api/users", _insertUser),
prouter.post("/api/login", _checkLogin)

export default prouter;