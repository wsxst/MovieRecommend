import axios from 'axios'
let baseUrl = `http://47.97.200.236:3000/api`

const client = axios.create({
    baseURL: baseUrl,
});

export default {
    async callApi(method, uri, data){
        try {
            let req =await client({
                method,
                url : uri,
                data : data
            })

            return req.data
        } catch (err) {
            console.log('Error in getting Server uri')
            console.log(err)
        }
    }
}
