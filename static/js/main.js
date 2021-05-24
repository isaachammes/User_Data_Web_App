
function handleSubmit() {
  //Gets file or text with priority going to files. Then calls getStatistics using the proper request options.
  let requestOptions

  if (document.getElementById('fileSubmission').files[0]) {
    let file = document.getElementById("fileSubmission").files[0]
    let formData = new FormData()
    formData.append("file", file)
    requestOptions = {method: "POST",
                      headers: {
                        'Accept': 'application/json'
                      }, 
                      body: formData}
  }
  else if (isJsonString(document.getElementById('textSubmission').value)) {
    let data = document.getElementById('textSubmission').value
    requestOptions = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
      body: data,
    }
  }

  getStatistics(requestOptions)
}

function femaleVsMale() {
  //Generates a pie chart for female vs male percent
  let statistics = window.statistics
  let malePercent = (100 - statistics['percent_female_vs_male'])
  let femalePercent = statistics['percent_female_vs_male']
  let data = [{name: "Male " + malePercent + "%", share: malePercent}, 
  {name: "Female " + femalePercent + "%", share: femalePercent}]
  let colors = ["#0000FF", "#FF1493"]

  createPieChart(data, colors)
}

function firstNamePercent() {
  //Generates a pie chart for first names A-M vs N-Z
  let statistics = window.statistics
  let amPercent = statistics['percent_first_names_start_a_to_m']
  let nzPercent = (100 - statistics['percent_first_names_start_a_to_m'])
  let data = [{name: "First Name A-M " + amPercent + "%", share: amPercent}, 
  {name: "First Name N-Z " + nzPercent + "%", share: nzPercent}]
  let colors = ["#FF0000	", "#008000"]

  createPieChart(data, colors)
}

function lastNamePercent() {
  //Generates a pie chart for last names A-M vs N-Z
  let statistics = window.statistics
  let amPercent = statistics['percent_last_names_start_a_to_m']
  let nzPercent = (100 - statistics['percent_last_names_start_a_to_m'])
  let data = [{name: "Last Name A-M " + amPercent + "%", share: amPercent}, 
  {name: "Last Name N-Z " + nzPercent + "%", share: nzPercent}]
  let colors = ["#FF0000	", "#008000"]

  createPieChart(data, colors)
}

function percentEachState() {
  //Generates a bar chart for percent of population in each state
  let statistics = window.statistics
  createBarChart(statistics["percent_by_state"])
}

function percentFemaleEachState() {
  //Generates a bar chart for percent female in each state
  let statistics = window.statistics
  createBarChart(statistics["percent_female_by_state"])
}

function percentMaleEachState() {
  //Generates a bar chart for percent male in each state
  let statistics = window.statistics
  createBarChart(statistics["percent_male_by_state"])
}

function agePercent() {
  //Generates a bar chart for percent of population by age
  let statistics = window.statistics
  createBarChart(statistics["percent_by_age"])
}

function getStatistics(requestOptions) {
  //Makes api call to retrieve statistics and calls renderChartsPage to setup the charts page
  fetch('/get_statistics', requestOptions)
      .then(response => response.json())
      .then(json => renderChartsPage(json))
      .catch(error => console.log('Request Failed', error))
      .then(alert('Please only submit valid json as input'))
}

function renderChartsPage(statistics) {
  //Changes html page to display charts and displays female vs male chart initially
  document.body.innerHTML = `
    <div id="svgChart">
      <svg class="chart"></svg>
    </div>
    <div id="buttonContainer">
      <input class="buttons" id="femaleVsMale" type="button" value="Female vs Male" onclick="femaleVsMale();" />
      <input class="buttons" id="firstNamePercent" type="button" value="First Name" onclick="firstNamePercent();" />
      <input class="buttons" id="lastNamePercent" type="button" value="Last Name" onclick="lastNamePercent();" />
      <input class="buttons" id="percentEachState" type="button" value="By State" onclick="percentEachState();" />
      <input class="buttons" id="percentFemaleEachState" type="button" value="Female by State" onclick="percentFemaleEachState();" />
      <input class="buttons" id="percentMaleEachState" type="button" value="Male by State" onclick="percentMaleEachState();" />
      <input class="buttons" id="agePercent" type="button" value="By Age" onclick="agePercent();" />
    </div>
  `
  window.statistics = statistics

  femaleVsMale()
}

function createPieChart(data, colors) {
  d3.select("svg").remove()
  document.getElementById("svgChart").innerHTML = '<svg class="chart" width="1000" height="600"></svg>'

  let svg = d3.select("svg"),
            width = svg.attr("width"),
            height = svg.attr("height"),
            radius = 300

  let g = svg.append("g")
            .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");
  
  let ordScale = d3.scaleOrdinal()
                      .domain(data)
                      .range(colors)

                      var pie = d3.pie().value(function(d) { 
                        return d.share; 
                    })
        
  let arc = g.selectAll("arc")
                  .data(pie(data))
                  .enter()

  let path = d3.arc()
                     .outerRadius(radius)
                     .innerRadius(0);

  arc.append("path")
      .attr("d", path)
      .attr("fill", function(d) { return ordScale(d.data.name) })

  let label = d3.arc()
      .outerRadius(radius)
      .innerRadius(0);

  arc.append("text")
      .attr("transform", function(d) { return "translate(" + label.centroid(d) + ")" })
      .attr("text-anchor", "middle")
      .text(function(d) { return d.data.name; })
      .style("font-family", "arial")
      .style("font-size", 15)
}

function createBarChart(data) {
  d3.select("svg").remove()
  document.getElementById("svgChart").innerHTML = '<svg class="chart" width="1200" height="500"></svg>'

  let margin = {top: 200, right: 20, bottom: 30, left: 40};
  let svg = d3.select("svg"),
          svgWidth = svg.attr("width"),
          svgHeight = svg.attr("height")
  let height = svgHeight- margin.top- margin.bottom, width = svgWidth - margin.left - margin.right;
  let sourceNames = [], sourceCount = [];

  let x = d3.scaleBand().rangeRound([0, width]).padding(0.1),
      y = d3.scaleLinear().rangeRound([height, 0]);
  for(let key in data){
    if(data.hasOwnProperty(key)){
        sourceNames.push(key);
        sourceCount.push(parseInt(data[key]));
    }
  }
  x.domain(sourceNames);
  y.domain([0, d3.max(sourceCount, function(d) { return d; })]);

  svg = svg.append("g")
         .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  svg.append("g")
    .attr("class", "axis axis--x")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x));

  svg.append("g")
    .attr("class", "axis axis--y")
    .call(d3.axisLeft(y).ticks(5))

  let bars = svg.selectAll('.bar')
    .data(sourceNames)
    .enter()
    .append("g");

  bars.append('rect')
    .attr('class', 'bar')
    .attr("x", function(d) { return x(d); })
    .attr("y", function(d) { return y(data[d]); })
    .attr("width", x.bandwidth())
    .attr("height", function(d) { return height - y(data[d]); });
    
  bars.append("text")
    .text(function(d) { 
        return data[d];
    })
    .attr("x", function(d){
        return x(d) + x.bandwidth()/2;
    })
    .attr("y", function(d){
        return y(data[d]) - 5;
    })
    .attr("font-family" , "sans-serif")
    .attr("font-size" , "14px")
    .attr("fill" , "black")
    .attr("text-anchor", "middle");
}


function isJsonString(str) {
  try {
      JSON.parse(str);
  } catch (e) {
      return false;
  }
  return true;
}