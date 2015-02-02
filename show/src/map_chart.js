// 地图
function myblock_map(my_x,my_y,my_desc,myChart){
    // 基于准备好的dom，初始化echarts图表
    var option = {
    title : {
        text: my_desc,
        subtext: '纯属虚构',
        x:'center'
    },
    tooltip : {
        trigger: 'item'
    },
    legend: {
        orient: 'vertical',
        x:'left',
        data:my_y
    },
    dataRange: {
        min: 0,
        max: 300,
        x: 'left',
        y: 'bottom',
        text:['高','低'],           // 文本，默认为数值文本
        calculable : true
    },
    toolbox: {
        show: true,
        orient : 'vertical',
        x: 'right',
        y: 'center',
        feature : {
            mark : {show: true},
            dataView : {show: true, readOnly: false},
            restore : {show: true},
            saveAsImage : {show: true}
        }
    },
    roamController: {
        show: true,
        x: 'right',
        mapTypeControl: {
            'china': true
        }
    },
    series : [{
            name: my_y[0],
            type: 'map',
            mapType: 'china',
            itemStyle:{
                normal:{label:{show:true}},
                emphasis:{label:{show:true}}
            },
            data:my_x
        }]
    };

    // 为echarts对象加载数据 
    myChart.setOption(option); 
}

function showMap(my_x,my_y,my_desc,myblock2_map){
    showChart(my_x,my_y,my_desc,myblock_map,myblock2_map,'MapChart');
}