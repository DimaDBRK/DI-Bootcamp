// const express = require('express') -> in package we add "type": "module" and use import
import express from "express";
import dotenv from "dotenv";

import prouter from "./routes/register.js";

import path from 'path';
const __dirname = path.resolve();

const app = express();
dotenv.config(); // to read env file

//to index file
app.use('/', express.static(__dirname + "/public"));

// add parser
app.use(express.urlencoded({extended:true})); // ql
app.use(express.json());

app.use(prouter);

app.listen(process.env.PORT, ()=> {
    console.log(`run on port ${process.env.PORT}`);
});