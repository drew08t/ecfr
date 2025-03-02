import React, { useState, useEffect } from "react";
import "./App.css";
import { agency, analysis, year } from "./types";

function App() {
  const [currentTime, setCurrentTime] = useState(0);
  const [agencies, setAgencies] = useState<agency[]>([]);
  const [analysis, setAnalysis] = useState<analysis[]>([]);
  useEffect(() => {
    fetch("/time")
      .then((res) => res.json())
      .then((data) => {
        setCurrentTime(data.time);
      });
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
    // Pre-populate years
    analysis.map((row) => {
      const year = row.year;
      const matchingYearIndex = years.findIndex((item) => item.id === year);
      if (matchingYearIndex === -1) {
        years.push({ id: year, slugs: [], totalWords: 0 });
      }
    });

    years.sort((a, b) => a.id - b.id);

    // Organize data into year buckets
    analysis.map((row) => {
      const year = row.year;
      const matchingYearIndex = years.findIndex((item) => item.id === year);
      const slug = {
        slug: row.slug,
        totalWords: row.word_count ?? 0,
      };

      const currentCount = years[matchingYearIndex].totalWords;
      years[matchingYearIndex] = {
        ...years[matchingYearIndex],
        totalWords: currentCount + (row.word_count ?? 0),
      };
      // Look for existing slug
      const matchingSlugIndex = years[matchingYearIndex].slugs.findIndex(
        (item) => item.slug === row.slug
      );
      if (matchingSlugIndex > -1) {
        years[matchingYearIndex].slugs[matchingSlugIndex].totalWords +=
          row.word_count ?? 0;
      } else {
        years[matchingYearIndex].slugs.push(slug);
      }
    });

    console.log(years);
  }, [agencies, analysis]);

  return (
    <div className="App">
      <header className="App-header">
        <p>The current time is {currentTime}.</p>
      </header>
    </div>
  );
}

export default App;
