// 柱状图

function myblock_lineBar(my_x,my_y,my_desc,myChart){
    // 基于准备好的dom，初始化echarts图表

    var option = {
        tooltip: {
            show: true
        },
        toolbox: {
        show : true,
        feature : {
            mark : {show: true},
            dataView : {show: true, readOnly: false},
            magicType : {show: true, type: ['line', 'bar']},
            restore : {show: true},
            saveAsImage : {show: true}
        }
    },
        legend: {
            data:my_desc,
            
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


function showLineBar(my_x,my_y,my_desc,myblock2_lineBar){
    showChart(my_x,my_y,my_desc,myblock_lineBar,myblock2_lineBar,'LineBarChart');
}


