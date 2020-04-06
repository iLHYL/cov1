var ec_r2 = echarts.init(document.getElementById('r2'),'dark')

var ec_r2_option = {
    title:{
        text:"今日疫情热搜",
        textStyle:{
            color:'white',
        },
        left:'left',
    },
    tooltip:{
        show:false
    },
    series:[{
        type:'wordCloud',
        gridSize:1,
        sizeRange: [12,55],
        rotationRange: [-45,0,45,90],
        textStyle:{
            normal:{
                color:function () {
                    return 'rgb('+
                        Math.round(Math.random()*255)+','+
                        Math.round(Math.random()*255)+','+
                         Math.round(Math.random()*255)+')'

                }
            }
        },

        right:null,
        bottom:null,
        data:[{'name': '动态', 'value': '1268575'}, {'name': '新型', 'value': '1268575'}, {'name': '实时', 'value': '1268575'}, {'name': '肺炎', 'value': '1268575'}, {'name': '美国', 'value': '1041823'}, {'name': '滞留', 'value': '1041823'}, {'name': '哭诉', 'value': '1041823'}, {'name': '想家', 'value': '1041823'}, {'name': '张伟丽', 'value': '1041823'}, {'name': '英国', 'value': '696628'}, {'name': '外出', 'value': '696628'}, {'name': '确诊', 'value': '696628'}, {'name': '口罩', 'value': '696628'}, {'name': '抵京', 'value': '696628'}, {'name': '未戴', 'value': '696628'}, {'name': '中国', 'value': '642850'}, {'name': '有效', 'value': '642850'}, {'name': '暂停', 'value': '642850'}, {'name': '外国人', 'value': '642850'}, {'name': '入境', 'value': '642850'}, {'name': '签证', 'value': '642850'}, {'name': '感染', 'value': '617475'}, {'name': '演员', 'value': '617475'}, {'name': '疑似', 'value': '617475'}, {'name': '朵儿', 'value': '617475'}, {'name': '新冠', 'value': '617475'}, {'name': '逃走', 'value': '579251'}, {'name': '乘客', 'value': '579251'}, {'name': '飞行员', 'value': '579251'}, {'name': '打喷嚏', 'value': '579251'}],
    }]
}

