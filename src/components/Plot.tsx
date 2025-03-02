import React from "react";
import Plot from "react-plotly.js";
import { Data, Layout } from "plotly.js";

// Define the interface for individual category data
interface CategoryData {
  name: string;
  values: number[];
  color?: string; // Optional color property
}

// Define props interface
interface StackedBarChartProps {
  years: string[];
  data: CategoryData[];
  title?: string; // Optional title
}

const StackedBarChart: React.FC<StackedBarChartProps> = ({
  years,
  data,
  title = "Yearly Data by Category",
}) => {
  // Transform the input data into Plotly format
  const plotData: Data[] = data.map((category, index) => ({
    x: years,
    y: category.values,
    name: category.name,
    type: "bar" as const,
    marker: {
      // Use provided color or fallback to a default palette
      color: category.color || getDefaultColor(index),
    },
  }));

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
      x: 1,
      y: 1,
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

// Helper function for default colors
const getDefaultColor = (index: number): string => {
  const colors = [
    "#1f77b4", // blue
    "#ff7f0e", // orange
    "#2ca02c", // green
    "#d62728", // red
    "#9467bd", // purple
  ];
  return colors[index % colors.length];
};

export default StackedBarChart;
