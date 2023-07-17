import express from "express"
import {promises  as fsPromises} from "fs" 


// for dirname
import path from "path";

// read

const __dirname = path.resolve();

const app = express();

app.use(express.json());
app.use(express.urlencoded({extended: true}));
//add static
app.use("/",express.static(__dirname + "/public"));

app.get("/registeruser", (request, response) => {
    response.sendFile(__dirname + "/public/register.html")
})

app.post("/registeruser", async (request, res) => {
    // console.log("req", request);
    const dataBody = request.body;
    console.log("rerq data", dataBody);
    const readFileResponse = await readuser(dataBody); // call ssync function - add await
    res.status(200).json(readFileResponse);
})


// read // auto return data from file
async function readuser (currentUser) {
    const data = await fsPromises.readFile(__dirname + '/public/data2.json',  "utf8")
    .catch((err) => console.error('Failed to read file', err));
    console.log("data before:", data);
    const datausers = JSON.parse(data);
   
    const findUser = datausers.findIndex(element => element.username === currentUser.username);
    
    console.log(findUser);

    if (findUser >= 0) {
        console.log("User already exist")
        return "User already exist"
    } else {
        datausers.push(currentUser);
        console.log("Info to add - 1 element:", datausers[0]);
        //VERY IMPORTANT TO STRINGIFY THE DATA SENT TO WRITE FILES
        await fsPromises.writeFile(__dirname + "/public/data2.json", JSON.stringify(datausers),
        'utf-8');
        console.log('Ok');
        return "User added successfully";
    } 
}
// auto return data from file


app.listen("3000", () => {
    console.log("server listening")
})