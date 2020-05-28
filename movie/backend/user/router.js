var express = require('express')
var router = express.Router()


var mysql      = require('mysql');
var connection = mysql.createConnection({
  host     : '121.36.152.15',
  user     : 'root',
  password : '123456',
  database : 'recommend',
  port     : '9777',
});
 
connection.connect();
var crypto = require('crypto');
function cryptPwd(password) {
    var md5 = crypto.createHash('md5');
    return md5.update(password).digest('hex');
}
router.post('/login', function (req, res) {
    let username = req.body.username,
        password = cryptPwd(req.body.password)

    console.log(`username ${username} password ${password}`)
    connection.query(`SELECT * FROM user where username='${username}'`, function (error, results, fields) {
        if (error){
            res.send(false)
            console.log(error)
            return
        }
        if(results.length == 0){
            res.send(false)
            console.log(`username ${username} not exist`)
            return
        }else if(results[0]['password'] == password){
            let userObject = {
                username: username,
                userid: results[0]['userid'],
            }
            console.log("good")
            res.send(userObject)
            return
        }else if(results[0]['password'] != password){
            res.send(false)
            console.log("password should be" + results[0]['password'])
            return
        }else{
            res.send(false)
            console.log('unknown')
            return
        }

    });
    //if(email == userObject.email && password == userObject.password){
        //res.send(true)
    //} else {
        //res.send(false)
    //}
    //res.send(true)

})

router.post('/register', function (req, res) {
	let username = req.body.username,
	password = cryptPwd(req.body.password)
    connection.query(`INSERT INTO user(username,password) VALUES('${username}','${password}')`, function (error, results, fields) {
        if (error){
            res.send(false)
            console.log(error)
            return
        }
        res.send(true)
        return
    })
})

module.exports = router
