import service from "./movieapi";

export function getRecommendList(data) {
	return service({
		url:"/get_recommend?userid="+data.userid,
		method:"get"
	})
}

export function getMovieInfo(data) {
	return service({
		url:"/get_movie?movieid="+data.movieid+"&userid="+data.userid,
		method:"get"
	})
}

export function rateMovie(data) {
	return service({
		url:"/user_rate?userid="+data.userid+"&movieid="+data.movieid+"&star="+data.star,
		method:"get"
	})
}
