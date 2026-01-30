const BACKEND_URL = "https://smart-result-analytics-2.onrender.com";

function getTopper() {
  const branch = document.getElementById("branch").value;
  const tbody = document.querySelector("#result tbody");

  tbody.innerHTML = `<tr><td colspan="4">Loading...</td></tr>`;

  fetch(`${BACKEND_URL}/analytics/branch-top10?branch=${branch}`)
    .then(res => res.json())
    .then(data => {
      tbody.innerHTML = "";

      data.top_10_students.forEach((s, index) => {
        tbody.innerHTML += `
          <tr>
            <td>${index + 1}</td>
            <td>${s.name}</td>
            <td>${s.roll_no}</td>
            <td>${s.cgpa}</td>
          </tr>
        `;
      });
    })
    .catch(() => {
      tbody.innerHTML = `<tr><td colspan="4">Error loading data</td></tr>`;
    });
}
