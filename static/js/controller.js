function gettime() {
    $.ajax({
        url: "/time",

        timeout: 10000,
        success: function (data) {
            $("#time").html(data)
        },
        error: function (xhr, type, errorThrown) {

        }
    });
}

function get_c1_data() {
    $.ajax({
        url: '/c1',
        success: function (data) {
            $(".num h1").eq(0).text(data.confirm);
            $(".num h1").eq(1).text(data.suspect);
            $(".num h1").eq(2).text(data.heal);
            $(".num h1").eq(3).text(data.dead);
        },
        error: function () {

        }
    })
}

function get_c2_data(){
    $.ajax({
        url :'/c2',
        success:function (data) {
            ec_center_option.series[0].data = data.data
            // console.log(data.data)
            ec_center.setOption(ec_center_option)
        },
        error:function () {

        }
    })
}

function get_l1_data(){
    $.ajax({
        url :'/l1',
        success:function (data) {
            ec_left1_option.xAxis.data = data.day
            ec_left1_option.series[0].data = data.confirm
            ec_left1_option.series[1].data = data.suspect
            ec_left1_option.series[2].data = data.heal
            ec_left1_option.series[3].data = data.dead
            ec_left1.setOption(ec_left1_option)
        },
        error:function () {

        }
    })
}

function get_l2_data(){
    $.ajax({
        url :'/l2',
        success:function (data) {
            ec_left2_option.xAxis.data = data.day
            ec_left2_option.series[0].data = data.confirm
            ec_left2_option.series[1].data = data.suspect
            ec_left2_option.series[2].data = data.heal
            ec_left2_option.series[3].data = data.dead
            ec_left2.setOption(ec_left2_option)
        },
        error:function () {

        }
    })
}

function get_r1_data(){
    // console.log('r1')
    $.ajax({
        url:'/r1',
        success:function (data) {
            var res = []
            res.push(['type','累计','新增','治愈'])
            res = res.concat(data.data)
            ec_r1_option.dataset.source = res
            ec_r1.setOption(ec_r1_option)
        },
        error:function () {

        }
    })
}

function get_r2_data(){
    console.log('r2')
    $.ajax({
        url:'/r2',
        success:function (data) {
            console.log(ec_r2_option.series.data)
            console.log(data.kws);
            ec_r2_option.series.data = data.kws;
            console.log(ec_r2_option.series.data)

            ec_r2.setOption(ec_r2_option)
        }
    })
}

setInterval(gettime,1000)
get_r2_data()
get_c1_data()
get_c2_data()
get_l1_data()
get_l2_data()
get_r1_data()

