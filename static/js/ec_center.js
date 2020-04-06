var ec_center = echarts.init(document.getElementById('c2'),"dark");

var mydata = [{"name":"上海","value":237},{"name":"浙江","value":67}]

var ec_center_option = {
	title:{
		text:'',
		subtext:'',
		x:'left'
	},
	tooltip:{
		trigger:'item'
	},
	//左侧导航图标
	visualMap: {
			show:true,
			x:'left',
			y:'bottom',
			textStyle:{
				fontSize:8
			},
			splitList:[{ start: 0,end: 9},
				{ start: 10,end: 50},
				{ start: 51,end: 100},
				{ start: 101,end: 200},
			{ start: 201}],
		color:['#8A3310','#C64918','#E55B25','#F2AD92','#F9DCD1']
	},

	//配置属性
	series:[{
		name:'现存确诊人数',
		type:'map',
		mapType:'china',
        roam:false,//拖动和缩放
        itemStyle:{
		    normal:{
		        borderWidth:.3,//区域边框宽度
                borderColor:'#009fe8',//区域边框颜色
                areaColor:"#ffefd5",//区域颜色
            },
			emphasis:{//鼠标滑过地图高亮设置
				borderWidth:.3,
				borderColor:'#4b0082',
				areaColor:'#fff',
			}
        },
		label:{
			normal:{
			   show:true,//省份名称
			   fontSize:8,
			},
			emphasis:{//鼠标滑过地图高亮设置
				show:true,
				fontSize:8,
			}
		},
		data:mydata//数据
	}]
};
ec_center.setOption(ec_center_option)