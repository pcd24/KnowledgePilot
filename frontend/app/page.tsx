"use client"

import { useState } from "react"

export default function Home() {
  const [status, setStatus] = useState("")

  async function checkBackend() {
    const response = await fetch("http://127.0.0.1:8000/health")
    const data = await response.json()

    setStatus(data.status)
  }

  return (
    <main>
      <h1>KnowledgePilot</h1>

      <p>Agentic RAG Research Platform</p>

      <button onClick={checkBackend}>
        Check Backend
      </button>

      <p>{status}</p>
    </main>
  )
}