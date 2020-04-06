var ec_left2 = echarts.init(document.getElementById('l2'),'dark');

var ec_left2_option = {
    title: {
        text: '全国新增趋势',
        textStyle:{
            //color:white,
        },
        left: '30 %',

    },
    tooltip: {
        trigger: 'axis',
        axisPointer:{
            type:'line',
            lineStyle:{
                color:'#7171C6'
            }
        }
    },
    legend: {
        data: ['新增确诊', '新增疑似', '新增治愈', '新增死亡'],
        left:'0%',
        top:'10%',
        itemWidth:30,
        textStyle:{
            fontSize:12,
        }
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    toolbox: {
        feature: {
            saveAsImage: {}
        }
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: ['01.20', '01.21', '01.22']
    },
    yAxis: {
        type: 'value',
        axisLine:{
            show:true,
            width:1,
            type:'solid',
        }
    },
    series: [
        {
            name: '新增确诊',
            type: 'line',
            smooth:true,
            label:{
                emphasis:{//鼠标滑过地图高亮设置
				    show:true,
			    }
            },
            data: [222, 132, 101]
        },
        {
            name: '新增疑似',
            type: 'line',
            smooth:true,
            label:{
                emphasis:{//鼠标滑过地图高亮设置
				    show:true,
			    }
            },
            data: [220, 182, 191]
        },
        {
            name: '新增治愈',
            type: 'line',
            label:{
                emphasis:{//鼠标滑过地图高亮设置
				    show:true,
			    }
            },
            smooth:true,
            data: [150, 232, 201]
        },
        {
            name:  '新增死亡',
            type: 'line',
            label:{
                emphasis:{//鼠标滑过地图高亮设置
				    show:true,
			    }
            },
            smooth:true,
            data: [320, 332, 301]
        },
    ]
};

ec_left2.setOption(options = ec_left2_option)