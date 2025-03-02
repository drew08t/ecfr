import React, { useState, useEffect } from "react";
import "./App.css";
import { agency, analysis, year, chartData } from "./types";
import StackedBarChart from "./components/Plot";

function App() {
  const [agencies, setAgencies] = useState<agency[]>([]);
  const [analysis, setAnalysis] = useState<analysis[]>([]);
  const [plotYears, setPlotYears] = useState<string[]>([]);
  const [plotData, setPlotData] = useState<chartData[]>([]);
  const [legend, setLegend] = useState<{ [key: string]: string }>({});

  useEffect(() => {
    fetch("/agencies-unique")
      .then((res) => res.json())
      .then((data) => {
        setAgencies(data);
      });
    fetch("/analysis")
      .then((res) => res.json())
      .then((data) => {
        setAnalysis(data);
      });
  }, []);

  useEffect(() => {
    const years: year[] = [];
    const uniqueSlugs: string[] = [];
    const yearStrings: string[] = [];
    const legendNames: { [key: string]: string } = {};
    // Pre-populate years
    analysis.map((row) => {
      const year = row.year;
      const matchingYearIndex = years.findIndex((item) => item.id === year);
      if (matchingYearIndex === -1) {
        years.push({ id: year, slugs: [], totalWords: 0 });
      }
    });

    years.sort((a, b) => a.id - b.id);
    years.map((year) => {
      yearStrings.push(year.id.toString());
    });

    // Organize data into year buckets
    analysis.map((row) => {
      const year = row.year;
      const matchingYearIndex = years.findIndex((item) => item.id === year);
      const slugName = row.slug;
      if (!uniqueSlugs.includes(slugName)) {
        uniqueSlugs.push(slugName);
      }
      const slug = {
        slug: slugName,
        totalWords: row.word_count ?? 0,
      };

      const currentCount = years[matchingYearIndex].totalWords;
      years[matchingYearIndex] = {
        ...years[matchingYearIndex],
        totalWords: currentCount + (row.word_count ?? 0),
      };
      // Look for existing slug
      const matchingSlugIndex = years[matchingYearIndex].slugs.findIndex(
        (item) => item.slug === slug.slug
      );
      if (matchingSlugIndex > -1) {
        years[matchingYearIndex].slugs[matchingSlugIndex].totalWords +=
          row.word_count ?? 0;
      } else {
        years[matchingYearIndex].slugs.push(slug);
      }
    });

    // Transform data to fit plot structure
    const chartData: chartData[] = [];
    uniqueSlugs.map((slug) => {
      const values = yearStrings.map((year) => {
        const yearData = years.find((obj) => obj.id.toString() === year);
        const slugValue = yearData?.slugs.find((s) => s.slug === slug);
        return slugValue?.totalWords ?? 0;
      });
      const agencyData =
        agencies.find((agency) => agency.slug === slug) ?? agencies[0];
      chartData.push({ name: slug, values });
      // Get unique legend names for each slug
      legendNames[slug] = agencyData.short_name ?? agencyData.display_name;
    });
    setPlotYears(yearStrings);
    setPlotData(chartData);
    setLegend(legendNames);
  }, [agencies, analysis]);

  return (
    <div className="App">
      <StackedBarChart
        years={plotYears}
        data={plotData}
        title="My Custom Data"
        legendNames={legend}
      />
    </div>
  );
}

export default App;
