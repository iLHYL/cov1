var ec_r1 = echarts.init(document.getElementById('r1'), 'dark');

var ec_r1_option = {
    title: {
        text: '今日境外输入',
        left: 'center',
        top: 2
    },
    legend: {
        top:27,
        right:'center'
    },
    tooltip: {},
    //缩放
    grid: {
        bottom: 50,
        right: 20
    },

    dataset: {
        source: [
            ['type', '累计', '新增', '治愈'],
            ['Matcha Latte', 43.3, 85.8, 93.7],
            ['Milk Tea', 83.1, 73.4, 55.1],
            ['Cheese Cocoa', 86.4, 65.2, 82.5],
            ['Walnut Brownie', 72.4, 53.9, 39.1]
        ]
    },
     dataZoom:  {
            show: true,
            type:'inside',
            realtime: true,
            start: 0,
            end: 30,
     },
    xAxis: {

        type: 'category',
        axisLabel: {
            show: true,
            // 强制显示所有坐标值
            interval:'0',
            // 坐标文字倾斜角度
            rotate:32,
            textStyle: {
                fontSize: '8',
                color: 'white',
            },
        },
    },
    yAxis: {},

    // Declare several bar series, each will be mapped
    // to a column of dataset.source by default.
    series: [
        {type: 'bar'},
        {type: 'bar'},
        {type: 'bar'}
    ]
};

ec_r1.setOption(options = ec_r1_option)