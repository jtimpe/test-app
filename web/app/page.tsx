'use client';

import { useState } from "react";

const API_URI = 'http://localhost:5000'

export default function Home() {
  const [temperature, setTemperature] = useState('')
  const [condition, setCondition] = useState('')
  const [city, setCity] = useState('')
  const [reported_by, setReported_by] = useState('')
  
  const onSubmit = (e) => {
    e.preventDefault()
    console.log('data submitted')

    console.log('temperature', temperature)
    console.log('condition', condition)
    console.log('city', city)
    console.log('reported_by', reported_by)

    fetch(
      `${API_URI}/report_weather`,
      {
        method: "POST",
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ temperature, condition, city, reported_by }),
      }
    )
    // does sending this request to the nextjs server before the api save us some CORS setup?
  }

  // render list of submitted weather reports using search params + prefetch - https://nextjs.org/learn/dashboard-app/adding-search-and-pagination

  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <form onSubmit={onSubmit}>
        <input type="number" name="temperature" placeholder="Temperature" value={temperature} onChange={(e) => setTemperature(e.target.value)} /> <br/>
        <input type="text" name="condition" placeholder="Weather condition" value={condition} onChange={(e) => setCondition(e.target.value)} /> <br/>
        <input type="text" name="city" placeholder="City" value={city} onChange={(e) => setCity(e.target.value)} /> <br/>
        <input type="text" name="reported_by" placeholder="Reported by" value={reported_by} onChange={(e) => setReported_by(e.target.value)} /> <br/>
        <input type="submit" />
      </form>
    </div>
  );
}
