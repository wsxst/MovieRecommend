<template>
<div>
    <h1>电影推荐系统</h1>
    <p>用户名：{{userDetail.username}}</p>
    <p>用户ID：{{userDetail.userid}} </p>
    <el-button type="primary" @click="logout">
        Logout
    </el-button>
    <el-row :gutter="20">
        <el-col :xs="24" :sm="6" :md="6" v-for="movie in movieList" :key="movie.movieid" style="text-align:center; margin:50px;">
          <el-card class="video-card"@click.native="viewMovieInfo(movie.movieid)">
            <img class="video-avatar" :src="url">
            <div>
              <div class="video-title">{{movie.moviename}}</div>
              <div class="video-bottom clearfix">
                <span>🗓：</span>
                <span>{{movie.showyear.substring(0,17)}}</span>
                <br>
                <span>🎬：</span>
                <span>{{movie.director}}</span>
                <br>
                <span>🕴：</span>
                <span v-if="movie.leadactors.length<=10">{{movie.leadactors}}</span>
                <span v-else>{{movie.leadactors.substr(0,10)+"..."}}</span>
                <br>
                <span>🌟：</span>
                <span>{{movie.averating}}/5</span>
                <br>
                <span>ℹ️：</span>
                <span>{{movie.typelist}}</span>
              </div>
            </div>
          </el-card>
        </el-col>
      </el-row>


<!--
<el-row :gutter="20">
        <el-col :xs="24" :sm="8" :md="8" v-for="video in videos" :key="video.id">
          <el-card class="video-card" @click.native="goVideo(video)">
            <img class="video-avatar" :src="video.avatar">
            <div>
              <div class="video-title">{{video.title}}</div>
              <div class="video-bottom clearfix">
                <span class="video-info">{{video.info.substring(0, 40)}}</span>
              </div>
            </div>
          </el-card>
        </el-col>
      </el-row>
-->

<!--    <el-row :gutter="20">
        <el-col :span="8" v-for="(movie, index) in this.movieList" :key="movie.movieid" :offset="index > 0 ? 2 : 0">
            <el-card :body-style="{ padding: '0px' }">
                <img :src="movie.picture" class="image" alt="">
                <div style="padding: 14px;">
                    <span>{{movie.moviename}}</span>
                    <div class="bottom clearfix">
                        <span>{{movie.showyear}}</span>
                        <span>{{movie.director}}</span>
                        <span v-if="movie.leadactors.length<=10">{{movie.leadactors}}</span>
                        <span v-else>{{movie.leadactors.substr(0,10)+"..."}}</span>
                        <span>{{movie.averating}}</span>
                        <span>{{movie.typelist}}</span>
                        <el-button type="text" class="button" @click="viewMovieInfo(movie.movieid)">查看详情</el-button>
                    </div>
                </div>
            </el-card>
        </el-col>
    </el-row>

-->
</div>
</template>

<script>
	/* eslint-disable */
    import {getMovieInfo, getRecommendList} from "../controller/movieController";
    export default {
        name: "Profile",
        data(){
            return{
                userDetail: {},
                movieList:[],
                url:"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590516462968&di=d171b302972acff95c18f4f85ae5eb4d&imgtype=0&src=http%3A%2F%2Fwww.oct-cts.com%2Fimages%2Fup_scenery%2FUploadImage%2F36961%2FlargeImg%2F2014010309528e0e-cc0.jpg"
            }
        },
        mounted() {
            // console.log(this.$cookie.get("userid"))

        },
        created() {
	        this.userDetail = this.$root.$data.userDetail
	        if(!this.$cookie.get("userid")){
		        this.$router.push({path: 'login'})
	        }
        	getRecommendList({"userid":this.userDetail.userid})
            .then(res=>{
            	this.movieList=res.data.data;
            })
            .catch(err=>{
            	alert(err);
            })
        },
	    methods:{
            logout: function () {
                this.$root.$data.userDetail = null
                this.$cookie.delete("userid")
                this.$cookie.delete("username")
                this.$router.push({path: '/'})
            },
		    viewMovieInfo(movieid){
			    this.$router.push({name: "movie_info", params:{movieid:movieid}});
            }
        }
    }
</script>

<style scoped>
.video-avatar {
  width: 50%;
}
.video-title {
  margin: 4px 0px 4px 0px;
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
  font-size:20px;
  font-weight:bold;
}
.video-bottom {
  margin-top: 4px;
  padding-left:33%;
  text-align:left;
}
.video-info {
  color: #909399;
}
.video-card {
  margin-bottom: 14px;
  cursor: pointer;
}

</style>
