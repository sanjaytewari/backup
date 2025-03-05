const express = require('express');
var mysql = require('mysql');

const conn = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "root",
    database: "practice"
})

conn.connect((err)=> {
    if (err) throw err;
    console.log('connected to database');
})

const app = express();
app.listen(3000, () => {
    console.log('connected port is 3000');
});

app.use(express.json());

app.get('/fetch',(req,res) => {
    conn.query('select * from practice.test_text',(err,result) =>{
        if(err) throw err;
        res.json(result);
    });
})


app.post('/insert',(req,res)=> {
    const {text1,id} = req.body;
    conn.query('insert into practice.test_text(text1,id) values(?,?)',[text1,id],(err,result)=>{
        if(err) throw err;
        res.json({success:"inserted successfully"});
    }
)})

app.put('/update',(req,res)=> {
    const {text1, id} = req.body;
    if(!id) {
        res.json({error:"id is required"});
    }
    conn.query("update practice.test_text set text1 = ? where id = ? order by id ",[text1,id], (err,result)=>{
        if(err) throw err;
        res.json({success: "Successfully updated"});
    })
}
)

app.delete('/delete',(req,res)=>{
    const{id} = req.body;
    if(!id) {
        res.json({error:"id is required"});
    }
    conn.query("delete from practice.test_text where id = ?",[id], (err,result)=> {
        if(err) throw err;
        res.json({success: "deleted successfully"});
    })
})