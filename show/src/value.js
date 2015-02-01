// var a = "123";
// window.alert(a);
// news - 性别
var news_gender = new Array('男','女');
var news_genderNum = new Array(100,222);
var news_desc = new Array("人数");

// 展示的函数模板
function showChart(my_x,my_y,my_desc,myblock,myblock2,domId){
    // 路径配置
    require.config({
        paths: {
            echarts: '../echarts'
        }
    });

    // 使用
    require(
        [
            'echarts',
            'echarts/chart/bar', // 使用柱状图就加载bar模块，按需加载
            'echarts/chart/pie'
        ],
        function (ec) {
            var myChart = ec.init(document.getElementById(domId)); 
            myblock(my_x,my_y,my_desc,myChart);
            myblock2(myChart);
        }
    );

}
