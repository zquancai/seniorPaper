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
        'echarts/chart/bar' // 使用柱状图就加载bar模块，按需加载
    ],
    function (ec) {
        // 基于准备好的dom，初始化echarts图表
        var myChart = ec.init(document.getElementById('LineBarChart')); 
        
        var option = {
            tooltip: {
                show: true
            },
            legend: {
                data:my_desc
            },
            xAxis : [
                {
                    type : 'category',
                    data : my_x
                }
            ],
            yAxis : [
                {
                    type : 'value'
                }
            ],
            series : [
                {
                    "name":my_desc,
                    "type":"bar",
                    "data":my_y
                }
            ]
        };

        // 为echarts对象加载数据 
        myChart.setOption(option); 
    }
);