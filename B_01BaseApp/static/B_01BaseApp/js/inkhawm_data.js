console.log(`value from html file's script tag is: `);
console.log(json_data_js);
console.log(json_data_js[0].pk);

// here we use the json data passed from django view to html to js
    // g chart 
    // Load the Visualization API and the corechart package.
    google.charts.load("current", { packages: ["corechart"] });
    // Set a callback to run when the Google Visualization API is loaded.
    google.charts.setOnLoadCallback(drawChart);
    // Callback that creates and populates a data table,
    // instantiates the pie chart, passes in the data and
    // draws it.
    function drawChart() {
      // Create the data table.
      var data = new google.visualization.DataTable();
      data.addColumn("string", "Date");
        data.addColumn("number", "nos.");
        for (let key in json_data_js) {
        // for (let key in api_data) {
          data.addRows([["Matthaia", json_data_js[key].mat_grp_cmt]]);
          data.addRows([["Marka", json_data_js[key].marka_grp_cmt]]);
          data.addRows([["Luka", json_data_js[key].luka_grp_cmt]]);
          data.addRows([["Johana", json_data_js[key].johan_grp_cmt]]);
        }
        // Set chart options
        var options = {
          title: "KTP inkhawm inchhiarna",
          width: 500,
          // width: 400,
          height: 300,
        };
        
        // Instantiate and draw our chart, passing in some options.
        // var chart = new google.visualization.PieChart(
          var chart = new google.visualization.BarChart(
            document.getElementById("chart_div")
            );
            chart.draw(data, options);
          }
          // g chart ends

// using api fromt he js script direetly
  fetch("http://127.0.0.1:8060/api/list/")
  .then((response) => response.json())
  .then((api_data) => {
    // Handle the data returned from the API
    // g chart
    // Load the Visualization API and the corechart package.
    google.charts.load("current", { packages: ["corechart"] });
    // Set a callback to run when the Google Visualization API is loaded.
    google.charts.setOnLoadCallback(drawChart);
    // Callback that creates and populates a data table,
    // instantiates the pie chart, passes in the data and
    // draws it.
    function drawChart() {
      // Create the data table.
      var data2 = new google.visualization.DataTable();
      data2.addColumn("string", "Date");
        data2.addColumn("number", "nos.");
        for (let key in api_data) {
          data2.addRows([["Matthaia", api_data[key].mat_grp_cmt]]);
          data2.addRows([["Marka", api_data[key].marka_grp_cmt]]);
          data2.addRows([["Luka", api_data[key].luka_grp_cmt]]);
          data2.addRows([["Johana", api_data[key].johan_grp_cmt]]);
          console.log(api_data[key].pk);
        }
        // Set chart options
        var options = {
          title: "KTP inkhawm inchhiarna (via api fetched from js)",
          width: 500,
          height: 300,
        };
        // Instantiate and draw our chart, passing in some options.
        // var chart = new google.visualization.PieChart(
          var chart = new google.visualization.BarChart(
            document.getElementById("chart_div2")
            );
            chart.draw(data2, options);
          }
          // g chart ends
        })
        .catch((error) => {
          // Handle any errors that occurred during the request
      console.error(error);
    });

// using chart js
let json_labels = [];
// let json_data = [];
// let json_data2 = [];
let json_mat_grp = [];
let json_mat_mem = [];
let json_mar_grp = [];
let json_mar_mem = [];
let json_lk_grp = [];
let json_lk_mem = [];
let json_jh_grp = [];
let json_jh_mem = [];
let json_total = [];

console.log("json obj are")

for (let key in json_data_js) {
    // console.log(json_data_js[key]);
    // console.log(json_data_js[key].inkhawm_ni);
    json_labels.push(json_data_js[key].inkhawm_ni);
    json_mat_grp.push(json_data_js[key].mat_grp_cmt);
    json_mat_mem.push(json_data_js[key].mat_members);
    json_mar_grp.push(json_data_js[key].marka_grp_cmt);
    json_mar_mem.push(json_data_js[key].marka_members);
    json_lk_grp.push(json_data_js[key].luka_grp_cmt);
    json_lk_mem.push(json_data_js[key].luka_members);
    json_jh_grp.push(json_data_js[key].johan_grp_cmt);
    json_jh_mem.push(json_data_js[key].johan_members);
    // json_data.push(json_data_js[key].johan_members);
}
console.log(json_labels)
// console.log(json_data)
// console.log(json_data2)
console.log(json_mat_grp)
console.log(json_mat_mem)
console.log(json_lk_grp)
console.log(json_lk_mem)
console.log(json_mar_grp)
console.log(json_mar_mem)
console.log(json_jh_grp)
console.log(json_jh_mem)

// data: mat grp,  mark grp, luk grp, jh grp
// data2: mat mem, mark mem, lk mem, jh mem

const ctx = document.getElementById("myChart2");

      new Chart(ctx, {
        type: "bar",
        data: {
          labels: json_labels, //x-axis
        //   labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"], //x-axis
          datasets: [
            {
              label: 'Mat grp',
              data: json_mat_grp,
              backgroundColor: '#B82D2D',
              borderColor: '#EEE1E1',
              borderWidth: 2,
              stack: 'Stack 1'
            },
            {
              label: 'Mat member',
              data: json_mat_mem,
              backgroundColor: '#DFD298',
              borderColor: '#EEE1E1',
              borderWidth: 2,
              stack: 'Stack 1'
            },
            {
              label: 'Marka grp',
              data: json_mar_grp,
              backgroundColor: '#B82D2D',
              borderColor: '#6979CB',
              borderWidth: 1,
              stack: 'Stack 2'
            },
            {
              label: 'Mar mem',
              data: json_mar_mem,
              backgroundColor: '#DFD298',
              borderColor: '#6979CB',
              borderWidth: 1,
              stack: 'Stack 2'
            },
            {
              label: 'Luka grp',
              data: json_lk_grp,
              backgroundColor: '#B82D2D',
              borderColor: '#497F37',
              borderWidth: 1,
              stack: 'Stack 3'
            },
            {
              label: 'Luka mem',
              data: json_lk_mem,
              backgroundColor: '#DFD298',
              borderColor: '#497F37',
              borderWidth: 1,
              stack: 'Stack 3'
            },
            {
              label: 'Johana Grp',
              data: json_jh_grp,
              backgroundColor: '#B82D2D',
              borderColor: '#BA4949',
              borderWidth: 1,
              stack: 'Stack 4'
            },
            {
              label: 'Johana mem',
              data: json_jh_mem,
              backgroundColor: '#DFD298',
              borderColor: '#BA4949',
              borderWidth: 1,
              stack: 'Stack 4'
            },
          ]
        },
        options: {
          scales: {
            y: {
              // beginAtZero: true,
              stacked: true,
            },
            x: {
              beginAtZero: true,
              stacked: true,
            },
          },
        //   below is to enable zoom and pan, ofcourse after putting appropriate js
          plugins: {
            zoom: {
            pan: {
                // pan options and/or events
                enabled: true,
                modifierKey: 'shift',
                overScaleMode: 'xy'
                },
            zoom: {
            wheel: {
                enabled: true,
            },
            pinch: {
                enabled: true
            },
            mode: 'xy',
            }
            }
          }
        },
      });
