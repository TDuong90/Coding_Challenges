// from data.js
var tableData = data;

// YOUR CODE HERE!
var filter = {};

var filterData = tableData;

var filterTableBtn = d3.select("#filter-btn");

var tbody = d3.select("tbody");

var Options = [{
        fieldName: 'Date',
        tableKey: 'date/time'
    },
    {
        fieldName: 'City',
        tableKey: 'city'
    },
    {
        fieldName: 'State',
        tableKey: 'state'
    },
    {
        fieldName: 'Country',
        tableKey: 'country'
    },
    {
        fieldName: 'Shape',
        tableKey: 'shape'
    }

];

Object.entries(Options).forEach(([key, value]) => Populate(value.fieldName, value.tableKey));

function Populate(fieldName, tableKey) {

    var menu = d3.select('#sel' + fieldName);

    var optionsArray = [...new]
}