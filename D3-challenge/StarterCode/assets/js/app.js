// @TODO: YOUR CODE HERE!

var svgHeight = 800;
var svgWidth = 800;

var margin ={
    top:20,
    right: 40,
    bottom: 80,
    left: 100
};

var height = svgHeight - margin.top - margin.bottom;
var width = svgWidth - margin.right - margin.left;

var svg = d3
    .select("#body")
    .append("svg")
    .attr("width", svgWidth)
    .attr("height", svgHeight);

var Chart = svg.append("g")
    .attr("transform", `translate(${margin.left}, ${margin.top})`);

d3.select("body").append("div").attr("class", "tooltip").style("opacity", 0);

//import data

d3.csv("data.csv", function(data, healthData){
    if (data) throw data;
    console.log(healthData)

        healthData.forEach(function(data){
            data.poverty = +data.poverty;
            data.healthcare = +data.heathcare;
        });

        var xLinearScale = d3.scaleLinear().range([0, width]);
        var yLinearScale = d3.scaleLinear().range([height, 0]);

        var bottomAxis = d3.axisBottom(xLinearScale);
        var leftAxis = d3.axisLeft(yLinearScale);

        var x_min;
        var x_max;
        var y_min;
        var y_max;

        x_min = d3.min(healthData, function(data){
            return data.heathcare;
        }); 
})
