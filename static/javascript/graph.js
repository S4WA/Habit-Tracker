function gen_graph(calendar, math_d) {
  math_data = math_d;
  document.getElementById("title").innerText = ` in ${moment().format("MMMM YYYY")}`;

  let graph = document.getElementById("graph"),
      weekdays = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];

  for (let row = 0; row < calendar.length; row++) {
    let row_el = document.createElement("tr")

    for (let cell = 0; cell < calendar[row].length; cell++) {
      if (cell == 0) {
        let label = document.createElement("td");
        label.classList.add("label");
        label.innerText = weekdays[row];
        row_el.append(label);
      }

      let cell_el = document.createElement("td"),
          date = moment(calendar[row][cell], "MM/DD/YYYY"),
          head = `${date.month()+1}/${date.date()}/${date.year()}`,
          percentage = math_d[head] != null && math_d[head].length != 0 ? Math.round(math_d[head][0]/math_d[head][1]*100) : 0;

      cell_el.title = head;
      cell_el.classList.add("cldr_cell");
      cell_el.classList.add(`p${Math.ceil(percentage/25)*25}`); // Background color for each cell in the graph
      if (date.isSame(moment(), "day")) {
        cell_el.id = "today";
      }
      cell_el.setAttribute("p", percentage);

      if (percentage > 0) {
        cell_el.title += ` | ${percentage}%`;
        cell_el.title += ` | ${math_d[head][0]}/${math_d[head][1]}`;
      }

      row_el.append(cell_el);
    }
    graph.append(row_el);
  }
}

function gen_pure_log(cl_names, data) {
  var table = document.getElementById("pure_log"), tr = document.createElement("tr");
  // Fill L1
  for (let i = 0; i < cl_names.length; i++) {
    let th = document.createElement("th");
    th.innerText = cl_names[i];
    tr.append(th);
  }
  table.append(tr);

  // Fill L2 ~ Last
  for (var i = 0; i < data.length; i++) {
    let tr = document.createElement("tr");
    for (let o in data[i]) {
      let th = document.createElement("th");
      th.innerText = data[i][o];
      tr.append(th)
    }
    if (math_data[data[i]["Date"]]) {
      table.append(tr);      
    }
  }
}

var math_data;