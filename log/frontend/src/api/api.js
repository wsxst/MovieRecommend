import axios from 'axios';

const service = axios.create({
	baseURL: 'http://121.36.133.80:16666', // url = base url + request url
});

export default service;
