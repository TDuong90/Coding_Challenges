// from data.js
var tableData = data;

// YOUR CODE HERE!
var filterTableButton = d3.select("#filter-btn");

var tbody = d3.select("tbody");

var queryDate = "tbd";

filterTableButton.on("click", function () {

    d3.event.preventDefault();

    var input = d3.select("#datetime");

    var queryDate = input.property('value');

    var filterData = tableData.filter(function (data) {
        return data.datetime == queryDate;
    });

    tbody.text('');

    filterData.forEach(record => {
        var row = tbody.append('tr');

        Object.entries(record).forEach(([key, value]) => {

            row.append('td').text(value);
        });
    });

});