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
}

interface BarChartData {
  x: string[];
  y: number[];
  name: string;
  type: "bar";
}

const StackedBarChart: React.FC<StackedBarChartProps> = ({
  years,
  data,
  title = "Yearly Data by Category",
}) => {
  const getSortedPlotData = (): BarChartData[] => {
    const yearData: { value: number; name: string }[][] = years.map(() => []);

    data.forEach((category) => {
      category.values.forEach((value, yearIndex) => {
        yearData[yearIndex].push({
          value,
          name: category.name,
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
            name: item.name,
            type: "bar",
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
      x: 1,
      y: 1,
    },
    autosize: true,
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
