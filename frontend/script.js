const BACKEND_URL = "https://smart-result-analytics-2.onrender.com";

function getTopper() {
  const branch = document.getElementById("branch").value;

  fetch(`${BACKEND_URL}/analytics/branch-top10?branch=${branch}`)
    .then(res => res.json())
    .then(data => {
      const tbody = document.querySelector("#result tbody");
      tbody.innerHTML = "";

      data.top_10_students.forEach(s => {
        tbody.innerHTML += `
          <tr>
            <td>${s.name}</td>
            <td>${s.roll_no}</td>
            <td>${s.cgpa}</td>
          </tr>
        `;
      });
    });
}
