import service from "./api";

export function get_user_data(data) {
	return service({
		url:"/user?s="+data.start_time+"&e="+data.end_time,
		method:"get"
	})
}

export function get_movie_data(data) {
	return service({
		url:"/movie?s="+data.start_time+"&e="+data.end_time,
		method:"get"
	})
}
