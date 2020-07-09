function getPlots(id) {
    d3.json("static/js/samples.json").then((data) => {
        console.log(data)

        var ids = data.samples[0].otu_ids;
        console.log(ids)
        var sampleValues = data.samples[0].sample_values.slice(0, 10).reverse();
        console.log(sampleValues)
        var labels = data.samples[0].otu_labels.slice(0, 10);
        console.log(labels)
        console.log(`OTU_labels: ${labels}`)
        var OTU_TopID = (data.samples[0].otu_ids.slice(0, 10)).reverse();
        console.log(OTU_TopID);
        var OTU_ID = OTU_TopID.map(id => "OTU" + id);
        console.log(`OTU IDS: ${OTU_ID}`)

        var trace = {
            x: sampleValues,
            y: OTU_ID,
            text: labels,
            marker: {
                color: 'blue'
            },
            type: "bar",
            orientation: "h"
        }
        var data = [trace];

        var layout = {
            title: "Top 10 OTU",
            yaxis: {
                tickmode: "linear",
            },
            margin: {
                l: 100,
                r: 100,
                t: 100,
                b: 30
            }
        };

        Plotly.newPlot("bar", data, layout)
    });
}

function DemoInfo(id) {


    d3.json("static/js/samples.json").then((data) => {

        var metadata = data.metadata;
        console.log(metadata)

        var result = metadata.filter(x => x.id.toString === id)[0];

        var demographic = d3.select("#sample-metadata");

        demographic.html("");

        Object.entries(result).forEach((key) => {
            demographic.append("h5").text(key[0].toUpperCase() + ": " + key[1] + "\n");
        });
    });
}

function optionChanged(id) {
    getPlots(id);
    getDemoInfo(id);
}

function init() {

    var dropdown = d3.select('#selDataset');

    d3.json("static/js/samples.json").then((data) => {
        console.log(data)

        data.names.forEach(function (name) {
            dropdown.append("option").text(name).property("value");
        })

        getPlots(data.names[0]);
        getDemoInfo(data.names[0]);
    });

}

init();