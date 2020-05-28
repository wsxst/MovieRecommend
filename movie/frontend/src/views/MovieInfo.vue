<template>
    <div class="main">
        <el-row>
            <img alt="" :src="url" style="width:50%; height:50%;">
        </el-row>
        <el-row>
            <span>电影名称：{{movieInfo.moviename}}</span>
        </el-row>
        <el-row>
            <span>电影上映时间🗓：{{movieInfo.moviename}}</span>
        </el-row>
        <el-row>
            <span>导演🎬：{{movieInfo.director}}</span>
        </el-row>
        <el-row>
            <span>领衔主演🕴：{{movieInfo.leadactors}}</span>
        </el-row>
        <el-row>
            <span>平均得分🌟：{{movieInfo.averating}}</span>
        </el-row>
        <el-row>
            <span>评分人数：{{movieInfo.numrating}}</span>
        </el-row>
        <el-row>
            <span>简介：{{movieInfo.description}}</span>
        </el-row>
        <el-row>
            <span>类型：{{movieInfo.typelist}}</span>
        </el-row>
        <el-row v-if="!movieInfo.review">
            <label for="rating-input"></label><input id="rating-input" type="number">
            <el-button type="primary" @click="rate" style="margin:10px;">评分</el-button>
        </el-row>
        <el-row v-else>
            <span>您对这部电影的评分为：{{movieInfo.user_rating}}</span>
        </el-row>
    </div>
</template>

<script>
	/* eslint-disable */
	import {getMovieInfo,rateMovie} from "../controller/movieController";

	export default {
		name: "MoviceInfo",
		data(){
			return{
				movieid:0,
				userDetail: {},
				movieInfo:{},
                url:"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590516462968&di=d171b302972acff95c18f4f85ae5eb4d&imgtype=0&src=http%3A%2F%2Fwww.oct-cts.com%2Fimages%2Fup_scenery%2FUploadImage%2F36961%2FlargeImg%2F2014010309528e0e-cc0.jpg"
			}
		},
		mounted() {
			// console.log(this.$cookie.get("userid"))

		},
		created() {
			this.movieid=this.$route.params.movieid;
			this.userDetail = this.$root.$data.userDetail;
			if(!this.$cookie.get("userid")){
				this.$router.push({path: 'login'})
			}
			getMovieInfo({"movieid":this.movieid,"userid":this.userDetail.userid})
				.then(res=>{
					this.movieInfo=res.data.data;
				})
				.catch(err=>{
					alert(err);
				})
		},
        methods:{
			rate(){
				const data={
					"userid":this.userDetail.userid,
                    "movieid":this.movieid,
                    "star":parseInt(document.getElementById("rating-input").value)
				};
				rateMovie(data)
                .then(res=>{
                	alert("评分成功！");
                	this.movieInfo.review=true;
                	this.movieInfo.user_rating=parseInt(document.getElementById("rating-input").value);
                })
                .catch(err=>{
                	alert(err);
                })
            }
        }
	}
</script>

<style scoped>
.main{
    padding-top:50px;
    padding-left:300px;
    padding-right:300px;
    text-align:left;
}

</style>
