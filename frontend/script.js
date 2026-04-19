document.getElementById("uploadForm").addEventListener("submit", async function(e) {
    e.preventDefault();

    let fileInput = document.getElementById("resume").files[0];
    let jd = document.getElementById("jd").value;

    let formData = new FormData();
    formData.append("resume", fileInput);
    formData.append("job_description", jd);

    let response = await fetch("http://127.0.0.1:5000/analyze", {
        method: "POST",
        body: formData
    });

    let data = await response.json();

    document.getElementById("result").innerHTML =
        "Match Score: " + data.match_score + "%<br>Skills: " + data.skills.join(", ");
});
