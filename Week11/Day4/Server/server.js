import express from "express";
import dotenv from "dotenv";
import prouter from "./routes/dc.js";
import cors from "cors";



const app = express();
dotenv.config();


// add parser
app.use(express.urlencoded({extended:true})); // ql
app.use(express.json());

app.use(cors());

app.use('/api', prouter);



app.listen(process.env.PORT, () => {
console.log(`run on port ${process.env.PORT}`);
});
