function myblock_pieBar(mypie_x,mypie_y,mypie_desc,myChart){
    // 基于准备好的dom，初始化echarts图表

    var option = {
    title : {
        text: mypie_desc,
        subtext: '数据',
        x:'center'
    },
    tooltip : {
        trigger: 'item',
        formatter: "{a} <br/>{b} : {c} ({d}%)"
    },
    legend: {
        orient : 'vertical',
        x : 'left',
        data:mypie_x
    },
    toolbox: {
        show : true,
        feature : {
            mark : {show: true},
            dataView : {show: true, readOnly: false},
            magicType : {
                show: true, 
                type: ['pie', 'funnel'],
                option: {
                    funnel: {
                        x: '25%',
                        width: '50%',
                        funnelAlign: 'left',
                        max: 1548
                    }
                }
            },
            restore : {show: true},
            saveAsImage : {show: true}
        }
    },
    calculable : true,
    series : [
        {
            name:'微博数据',
            type:'pie',
            radius : '55%',
            center: ['50%', '60%'],
            data:mypie_y
        }
    ]
};
                    
    // 为echarts对象加载数据 
    myChart.setOption(option); 
}

function showPie(my_x,my_y,my_desc,myblock2_pieBar){
    showChart(my_x,my_y,my_desc,myblock_pieBar,myblock2_pieBar,'PieChart');
}