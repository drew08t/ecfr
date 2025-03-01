import React, { useState, useEffect } from "react";
import "./App.css";
import { agency, analysis } from "./types";

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
    fetch("/agencies")
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
    console.log(agencies);
    console.log(analysis);

    // agencies.map((agency) => {
    //   agencyCount += 1;
    //   // examples to check
    //   // title 1, chapter 3: Administrative Conference of the United States - 12.36k words
    //   // title 1, chapter IV, part 425: President's Commission on White House Fellowships - 1.43k words
    //   // TODO querying on chapter doesn't appear to be working!

    //   agency.cfr_references.map((reference) => {
    //     let countQueryArguments = "?date=2025-02-01&";
    //     Object.keys(reference).map((key) => {
    //       const value = reference[key as keyof cfr_reference];
    //       countQueryArguments += `${key}=${value}&`;
    //     });
    //     countQueryArguments = countQueryArguments.substring(
    //       0,
    //       countQueryArguments.length - 1
    //     );
    //     if (agencyCount <= totalAgenciesToTest) {
    //       fetch(`/count${countQueryArguments}`, {})
    //         .then((res) => res.json())
    //         .then((data) => {
    //           console.log({
    //             agency: agency.display_name,
    //             count: data.count,
    //             args: countQueryArguments,
    //           });
    //         });
    //     }
    //   });
    // });
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
