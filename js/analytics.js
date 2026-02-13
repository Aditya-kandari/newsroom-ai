// Topic Distribution (ML-style clustering output)
new Chart(document.getElementById("topicChart"), {
  type: "doughnut",
  data: {
    labels: [
      "Data Security",
      "Government Policy",
      "Geopolitics",
      "Internet Access",
      "Technology Impact"
    ],
    datasets: [{
      data: [42, 28, 22, 18, 18],
      backgroundColor: [
        "#2563eb",
        "#f59e0b",
        "#ef4444",
        "#22c55e",
        "#6366f1"
      ],
      borderWidth: 3,
      borderColor: "#ffffff"
    }]
  },
  options: {
    cutout: "72%",
    plugins: {
      legend: {
        position: "bottom",
        labels: {
          padding: 14,
          boxWidth: 12,
          font: { size: 12 }
        }
      }
    }
  }
});

// Sentiment Breakdown
new Chart(document.getElementById("sentimentChart"), {
  type: "bar",
  data: {
    labels: ["Positive", "Neutral", "Concerned"],
    datasets: [{
      data: [22, 32, 74],
      backgroundColor: ["#22c55e", "#eab308", "#ef4444"]
    }]
  },
  options: {
    plugins: {
      legend: { display: false }
    },
    scales: {
      y: {
        beginAtZero: true,
        ticks: { stepSize: 10 }
      }
    }
  }
});
