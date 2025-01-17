# Using Global Temperature Data in p5.js

This guide explains how to use the `monthly.csv` dataset from the [Global Temperature dataset on GitHub](https://github.com/datasets/global-temp/blob/main/data/monthly.csv) in a p5.js project. Additionally, it includes instructions to convert the data into JSON format for structured storage and easy manipulation.

## Accessing the Data

The dataset is hosted on GitHub. Use the raw file link to access the CSV file:

The Global Climate at a Glance (GCAG) is a dataset that provides global temperature data from 1850 to the present. The GCAG data is available from the National Centers for Environmental Information (NCEI). 


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

## Converting CSV to JSON

To store and manipulate the data in a structured format, you can convert the CSV data into JSON. This allows you to group the data by year, with each year containing an array of 12 months of data.

### Example Code to Convert CSV to JSON

```javascript
let table; // Variable to hold the CSV data
let jsonData = {}; // Object to store JSON data

function preload() {
  // Load the CSV file
  table = loadTable(
    "https://raw.githubusercontent.com/datasets/global-temp/main/data/monthly.csv",
    "csv",
    "header",
    onLoadSuccess,
    onLoadError
  );
}

function setup() {
  createCanvas(400, 400);
  background(220);

  if (table && table.getRowCount() > 0) {
    jsonData = processCSVToJSON(table);
    console.log(jsonData);
    saveJSON(jsonData, "temperature_data.json");
  } else {
    console.error("No data to process.");
  }
}

function processCSVToJSON(table) {
  let data = {};

  for (let i = 0; i < table.getRowCount(); i++) {
    let year = table.getString(i, "Year"); // Use "Year" instead of "Date"
    let meanTemp = table.getString(i, "Mean"); // No change needed for "Mean"

    // Ensure the year exists in the data object
    if (!data[year]) {
      data[year] = [];
    }

    // Populate with mean temperatures (assuming one entry per year in this file)
    data[year].push(parseFloat(meanTemp));
  }

  return data;
}

function onLoadSuccess() {
  console.log("CSV loaded successfully!");
}

function onLoadError(err) {
  console.error("Error loading CSV:", err);
}

```

### JSON Output Format

The resulting JSON file will look like this:

```json
{
  "1850": [-0.7, -0.6, -0.4, -0.5, -0.2, 0.1, 0.3, 0.2, -0.1, -0.4, -0.5, -0.6],
  "1851": [-0.6, -0.5, -0.3, -0.2, -0.1, 0.0, 0.2, 0.1, -0.2, -0.3, -0.4, -0.5],
  ...
}
```

### Accessing JSON Data

To access specific years or months:

```javascript
let year = "1850";
let januaryTemp = jsonData[year][0]; // January temperature for 1850
let julyTemp = jsonData[year][6];   // July temperature for 1850
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
