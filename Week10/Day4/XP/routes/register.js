import express from 'express';
import { _getAllUsers,
        _insertUser,
        _getAllLogins,
        _insertLogin,
        _checkLogin
        } from '../controllers/register.js';

// it is traffic controller
const prouter = express.Router();

prouter.get('/api/users', _getAllUsers),
prouter.post("/api/users", _insertUser),
prouter.get("/api/logins", _getAllLogins),
prouter.post("/api/logins", _insertLogin),
prouter.post("/api/login", _checkLogin)

export default prouter;