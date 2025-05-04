async function summarize() {
    const chat_log = document.getElementById("chat_log").value;
    const res = await fetch('/summarize', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({chat_log})
    });
    const data = await res.json();
    document.getElementById("summary").innerText = data.answer;
}

async function ask() {
    const question = document.getElementById("question").value;
    const res = await fetch('/ask', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({question})
    });
    const data = await res.json();
    document.getElementById("answer").innerText = data.answer;
}

async function upload() {
    const fileInput = document.getElementById("file_input");
    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append('file', file);

    const res = await fetch('/upload', {
        method: 'POST',
        body: formData
    });
    const data = await res.json();
    document.getElementById("upload_result").innerText = JSON.stringify(data, null, 2);
}
