import React from "react";
import Plot from "react-plotly.js";
import { Layout } from "plotly.js";

interface CategoryData {
  name: string;
  values: number[];
}

interface StackedBarChartProps {
  years: string[];
  data: CategoryData[];
  title?: string;
  legendNames?: { [key: string]: string }; // Mapping of original names to legend names
}

interface BarChartData {
  x: string[];
  y: number[];
  name: string; // This will hold the legend name
  type: "bar";
  text?: string;
}

const StackedBarChart: React.FC<StackedBarChartProps> = ({
  years,
  data,
  title = "Yearly Data by Category",
  legendNames = {}, // Default to empty object
}) => {
  const getSortedPlotData = (): BarChartData[] => {
    const yearData: { value: number; name: string }[][] = years.map(() => []);

    data.forEach((category) => {
      category.values.forEach((value, yearIndex) => {
        yearData[yearIndex].push({
          value,
          name: category.name, // Keep original name for sorting
        });
      });
    });

    yearData.forEach((year) => {
      year.sort((a, b) => b.value - a.value);
    });

    const sortedDataMap: { [key: string]: BarChartData } = {};

    yearData.forEach((yearValues, yearIndex) => {
      yearValues.forEach((item) => {
        if (!sortedDataMap[item.name]) {
          sortedDataMap[item.name] = {
            x: [],
            y: [],
            name: legendNames[item.name] || item.name, // Use legend name if provided, otherwise original
            type: "bar",
            text: item.name,
          };
        }
        sortedDataMap[item.name].x.push(years[yearIndex]);
        sortedDataMap[item.name].y.push(item.value);
      });
    });

    return Object.values(sortedDataMap);
  };

  const plotData: BarChartData[] = getSortedPlotData();

  const layout: Partial<Layout> = {
    barmode: "stack",
    title: title,
    xaxis: {
      title: "Year",
    },
    yaxis: {
      title: "Values",
    },
    legend: {
      font: {
        size: 10, // Smaller font size
      },
      x: 1, // Position to the right
      y: 1, // Align to the top
      xanchor: "left",
      yanchor: "top",
      orientation: "v", // Vertical orientation
      traceorder: "normal",
      itemwidth: 100, // Fixed width for each legend item (in pixels)
      itemsizing: "constant", // Uniform sizing
      bgcolor: "rgba(255, 255, 255, 0.8)", // Background for readability
      bordercolor: "gray",
      borderwidth: 1,
    },
    margin: {
      r: 120, // Increase right margin to accommodate legend
    },
    autosize: true,
    hoverlabel: {
      font: {
        size: 16,
      },
      namelength: -1,
      bgcolor: "rgba(0, 0, 0, 0.8)",
      bordercolor: "rgba(255, 255, 255, 0.5)",
      align: "left",
    },
  };

  const config: Partial<Plotly.Config> = {
    responsive: true,
  };

  return (
    <div>
      <Plot
        data={plotData}
        layout={layout}
        config={config}
        style={{ width: "calc(90vw)", height: "calc(90vh)" }}
      />
    </div>
  );
};

export default StackedBarChart;
