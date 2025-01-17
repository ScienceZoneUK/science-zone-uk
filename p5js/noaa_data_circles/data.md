# Using Global Temperature Data in p5.js

This guide explains how to use the `monthly.csv` dataset from the [Global Temperature dataset on GitHub](https://github.com/datasets/global-temp/blob/main/data/monthly.csv) in a p5.js project.

## Accessing the Data

The dataset is hosted on GitHub. Use the raw file link to access the CSV file:

```
https://raw.githubusercontent.com/datasets/global-temp/main/data/monthly.csv
```

## Loading CSV Data in p5.js

The `loadTable()` function in p5.js can be used to load and process the CSV file. Below is an example:

### Example Code

```javascript
let table; // Variable to store the CSV data

function preload() {
  // Load the CSV file from the raw GitHub link
  table = loadTable(
    "https://raw.githubusercontent.com/datasets/global-temp/main/data/monthly.csv",
    "csv",
    "header"
  );
}

function setup() {
  createCanvas(800, 600);
  background(220);

  // Display some data from the table
  console.log("Number of rows:", table.getRowCount());
  console.log("Number of columns:", table.getColumnCount());
  console.log("First row:", table.getRow(0).arr);
}
```

## Using the Data

Once the CSV is loaded, you can extract and visualize the data. For instance:

### Loop Through the Data

```javascript
function setup() {
  createCanvas(800, 600);
  background(220);

  // Loop through the table rows
  for (let i = 0; i < table.getRowCount(); i++) {
    let year = table.getString(i, "Date");
    let temp = table.getString(i, "Mean");

    // Example: Display year and temperature
    console.log(`Year: ${year}, Temperature: ${temp}`);
  }
}
```

### Visualizing Data (e.g., Line Graph)

```javascript
function setup() {
  createCanvas(800, 600);
  background(220);

  let xStep = width / table.getRowCount();

  // Plot temperature as a line graph
  beginShape();
  for (let i = 0; i < table.getRowCount(); i++) {
    let temp = table.getNum(i, "Mean");
    let x = i * xStep;
    let y = map(temp, -1, 1, height, 0); // Adjust y range as needed

    vertex(x, y);
  }
  endShape();
}
```

## Using the Data Offline

To use the dataset offline:
1. Download the `monthly.csv` file from GitHub.
2. Save it in your project folder (e.g., `data/monthly.csv`).
3. Update the `loadTable()` function to load the local file:

```javascript
table = loadTable("data/monthly.csv", "csv", "header");
```

## Running p5.js Sketches with External Data

When using `loadTable()` to fetch files from GitHub or other external sources, ensure:

- The sketch is served from a local server (not opened directly as a file).
- Use tools like [p5.js web editor](https://editor.p5js.org/), Python's `http.server`, or VSCode Live Server.

## License

This guide and example code are available for personal and educational use. If you use them in a project, credit is appreciated!
