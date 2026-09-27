// Socket.IO chat server: serves ../chat-client and stores messages in MongoDB.
// Requires Node.js, npm dependencies, and a valid MongoDB connection URI below.
const express = require("express");
const bodyParser = require("body-parser");
const path = require("path");
const app = express();


const http = require("http").Server(app);
const io = require("socket.io")(http);

const mongoose = require("mongoose");
const { error } = require("console");

app.use(express.static(path.join(__dirname, "../chat-client")));
app.use(bodyParser.urlencoded({extended: false}));

const dbUrl = "mongodb+srv://adullahjhamat:jhamat123@cluster0.bpqbloo.mongodb.net/?retryWrites=true&w=majority"


let Message = mongoose.model("Message",{
   name: String,
   message:String 
});


app.get("/meddelanden",(req, res)=>{
    Message.find()
    .then(item =>{
        res.send(item);
    }); 

});

app.post("/meddelanden",(req, res)=>{
    let message = new Message(req.body);
    message.save()
    .then(item =>{
        io.emit("message", req.body);
    })
    .catch(err =>{
        res.sendStatus(500).send("unable to save to data base");
    });
});

io.on("connection", (socket)=>{
    console.log("En användare anslöt")
})

try{
    mongoose.connect(dbUrl);
    console.log("Ansluten till MongoDB")
}
catch{
    console.log(error);
}


http.listen(3000, () => {
    console.log("Servern körs, besök http://localhost:3000")
})










