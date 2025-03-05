const express = require('express');
const mongoose = require('mongoose');
const userModel = require('./models/model.js')

const app = express();
app.listen(3000,()=>{
    console.log("app runnin on port 3000");
});

app.get('/api',(req,res)=>{
    res.send("hello world");
});

app.use(express.json());

mongoose.connect("mongodb://127.0.0.1:27017/myDb")
.then(()=>{
    console.log("connected to mongodb");
}).catch((error)=>{
    console.log(error);
})

app.post('/api/add_user',(req,res)=>{
    const {name, email} = req.body;
    const newuser = new userModel({name, email});
    newuser.save();
    res.json({succes:"data inserted successfully"});
});