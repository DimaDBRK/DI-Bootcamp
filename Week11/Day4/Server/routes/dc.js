import express from 'express';
import { _getMessage,
        _anwserPostMessage 
        } from '../controllers/dc.js';

// it is trafic controller
const prouter = express.Router();

prouter.get('/hello', _getMessage);
prouter.post('/word', _anwserPostMessage);

export default prouter;