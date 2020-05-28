import axios from 'axios'
let baseUrl = "http://121.36.137.213:18999";

const service = axios.create({
	baseURL: baseUrl, // url = base url + request url
	timeout: 5000 // request timeout
});

export default service;
