var ec_left1 = echarts.init(document.getElementById('l1'), 'dark');

var ec_left1_option = {
    title: {
        text: '全国累计趋势',
        textStyle: {
            //color:white,
        },
        left: '30  %',

    },
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'line',
            lineStyle: {
                color: '#7171C6'
            }
        }
    },
    legend: {
        data: ['累计确诊', '现有疑似', '累计治愈', '累计死亡'],
        left: '0%',
        top: '10%',
        itemWidth: 25,
        textStyle: {
            fontSize: 12,
        }
    },
    grid: {
        left: '3%',
        right: '0%',
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
    yAxis: [{
        type: 'value',
        axisLabel: {
            color: '#fff',
            fontSize: 16,
            formatter: function(value,index){
        		var value;
        		if (value >=1000) {
        			value = value/1000+'k';
        		}else if(value <1000){
        			value = value;
        		}
        		return value
        	}
        },
        axisLine: {
            show: true,
            width: 1,
            type: 'solid',
        }
    }, {
        name: '疑似',
        type: 'value',
        axisLine: {
            show: true,
            width: 1,
            type: 'solid',
        }
    }
    ],
    series: [
        {
            name: '累计确诊',
            type: 'line',
            smooth: true,
            label: {
                emphasis: {//鼠标滑过地图高亮设置
                    show: true,
                }
            },
            data: [222, 132, 101]
        },
        {
            name: '现有疑似',
            type: 'line',
            smooth: true,
            label: {
                emphasis: {//鼠标滑过地图高亮设置
                    show: true,
                }
            },
            symbol: 'triangle',
            symbolSize: 10,
            yAxisIndex: 1,
            data: [220, 182, 191]
        },
        {
            name: '累计治愈',
            type: 'line',
            label: {
                emphasis: {//鼠标滑过地图高亮设置
                    show: true,
                }
            },
            smooth: true,
            data: [150, 232, 201]
        },
        {
            name: '累计死亡',
            type: 'line',
            label: {
                emphasis: {//鼠标滑过地图高亮设置
                    show: true,
                }
            },

            smooth: true,
            data: [320, 332, 301]
        },
    ]
};

ec_left1.setOption(options = ec_left1_option)