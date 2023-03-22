function gen_graph(calendar, data) {
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
          percentage = data[head] != null && data[head].length != 0 ? Math.round(data[head][0]/data[head][1]*100) : 0;

      cell_el.title = `${head}`;
      cell_el.classList.add("cldr_cell");
      cell_el.classList.add(`p${Math.ceil(percentage/25)*25}`); // Background color for each cell in the graph
      cell_el.setAttribute("p", percentage);

      if (percentage > 0) {
        cell_el.title += ` | ${percentage}%`;
        cell_el.title += ` | ${data[head][0]}/${data[head][1]}`;
      }

      row_el.append(cell_el);
    }
    graph.append(row_el);
  }
}