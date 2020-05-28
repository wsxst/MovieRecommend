<template>
  <div class="home">
      <span>开始时间</span>
      <label><input id="user-start-input"></label>
      <span>结束时间</span>
      <label><input id="user-end-input"></label>
      <button @click="search_user">查询</button>
      <div id="user_chart" style="height: 300px;width: 600px;left: 50%; transform: translate(-50%)"></div>
      <span>开始时间</span>
      <label><input id="movie-start-input"></label>
      <span>结束时间</span>
      <label><input id="movie-end-input"></label>
      <button @click="search_movie">查询</button>
      <div id="movie_chart" style="height: 300px;width: 600px;left: 50%; transform: translate(-50%)"></div>
  </div>
</template>

<script>
    // @ is an alias to /src
/* eslint-disable */
    import {get_movie_data, get_user_data} from "../api/controller";

    export default {
  name: 'Home',
  components: {
  },
    data(){
  	    return {
  	    	user_id_list:[],
            user_access_num_list:[],
            movie_id_list:[],
            movie_access_num_list:[]
        }
    },
    methods:{
  	    draw(chart_name){
  	    	if(chart_name==="user"){
		        // 基于准备好的dom，初始化echarts实例
		        let myChart = this.$echarts.init(document.getElementById('user_chart'));
		        // 绘制图表
		        myChart.setOption({
			        title: { text: '指定时段内访问量最多的10名用户' },
			        tooltip: {},
			        xAxis: {
				        data: this.user_id_list
			        },
			        yAxis: {},
			        series: [{
				        name: '访问量',
				        type: 'bar',
				        data: this.user_access_num_list
			        }]
		        });
            }else if(chart_name==="movie"){
		        let myChart = this.$echarts.init(document.getElementById('movie_chart'));
		        // 绘制图表
		        myChart.setOption({
			        title: { text: '指定时段内点击量最多的10部电影' },
			        tooltip: {},
			        xAxis: {
				        data: this.movie_id_list
			        },
			        yAxis: {},
			        series: [{
				        name: '点击量',
				        type: 'bar',
				        data: this.movie_access_num_list
			        }]
		        });
            }
        },
  	    search_user(){
  	    	const s=new Date(document.getElementById("user-start-input").value),e=new Date(document.getElementById("user-end-input").value);
  	    	const data={
  	    	    "start_time":s.getTime(),
		        "end_time":e.getTime()
            };
  	    	get_user_data(data)
            .then(res=>{
            	this.user_id_list = res.data.user_id_list;
            	this.user_access_num_list = res.data.user_access_num_list;
	            this.draw("user");
            })
            .catch(err=>{
            	alert(err);
            });
        },
        search_movie(){
  	    	const s=new Date(document.getElementById("movie-start-input").value),e=new Date(document.getElementById("movie-end-input").value);
	        const data={
		        "start_time":s.getTime(),
		        "end_time":e.getTime(),
	        };
	        get_movie_data(data)
		        .then(res=>{
			        this.movie_id_list = res.data.movie_id_list;
			        this.movie_access_num_list = res.data.movie_access_num_list;
			        this.draw("movie");
		        })
		        .catch(err=>{
			        alert(err);
		        });
        }
    }
}
</script>
