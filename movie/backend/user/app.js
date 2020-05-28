const express = require('express')
var bodyParser = require('body-parser')
var cors = require('cors')

const app = express()
const port = 3000

app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())
app.use(cors())
const routers = require('./router')

app.use('/api', routers)

app.listen(port, () => console.log(`Server listening on port ${port}!`))
