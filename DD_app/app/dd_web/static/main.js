const form = document.querySelector("#dd-form");
const statusEl = document.querySelector("#status");
const submitBtn = document.querySelector("#submit");
const reportEl = document.querySelector("#report");
const evidenceEl = document.querySelector("#evidence");
const promptEl = document.querySelector("#prompt");
const noticeEl = document.querySelector("#notice");
const reportTitle = document.querySelector("#report-title");
const reportMeta = document.querySelector("#report-meta");
const historyList = document.querySelector("#history-list");
const copyBtn = document.querySelector("#copy-report");
const downloadPdfBtn = document.querySelector("#download-pdf");
const downloadMdBtn = document.querySelector("#download-md");
const downloadJsonBtn = document.querySelector("#download-json");
const clearHistoryBtn = document.querySelector("#clear-history");

let current = null;

function readHistory() {
  try {
    return JSON.parse(localStorage.getItem("mca_dd_history") || "[]");
  } catch {
    return [];
  }
}

function writeHistory(items) {
  localStorage.setItem("mca_dd_history", JSON.stringify(items.slice(0, 20)));
}

function renderHistory() {
  const items = readHistory();
  historyList.innerHTML = "";
  if (!items.length) {
    const empty = document.createElement("p");
    empty.textContent = "No saved reports yet.";
    historyList.appendChild(empty);
    return;
  }
  items.forEach((item, index) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "history-item";
    button.innerHTML = `${escapeHtml(item.company || "Untitled")}<span>${escapeHtml(item.created_at || "")}</span>`;
    button.addEventListener("click", () => loadResult(item));
    historyList.appendChild(button);
  });
}

function escapeHtml(value) {
  return String(value).replace(/[&<>"']/g, (char) => ({
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    '"': "&quot;",
    "'": "&#039;",
  }[char]));
}

function formPayload() {
  return Object.fromEntries(new FormData(form).entries());
}

function showNotice(message) {
  if (!message) {
    noticeEl.classList.add("hidden");
    noticeEl.textContent = "";
    return;
  }
  noticeEl.textContent = message;
  noticeEl.classList.remove("hidden");
}

function loadResult(result) {
  current = result;
  reportEl.value = result.report_markdown || "";
  evidenceEl.value = JSON.stringify(result.evidence_register || {}, null, 2);
  promptEl.value = result.prompt || "";
  const company = result.company || result.evidence_register?.company || "Company";
  const window = result.news_window ? `${result.news_window.start} to ${result.news_window.end}` : "";
  reportTitle.textContent = `${company} DD`;
  reportMeta.textContent = window || result.central_tension || "Generated report";
  showNotice(result.message || "");
  copyBtn.disabled = !reportEl.value;
  downloadPdfBtn.disabled = !reportEl.value;
  downloadMdBtn.disabled = !reportEl.value;
  downloadJsonBtn.disabled = !evidenceEl.value;
}

function saveResult(result, payload) {
  const company = result.company || payload.company || "Company";
  const item = {
    ...result,
    company,
    created_at: new Date().toLocaleString(),
  };
  const existing = readHistory();
  writeHistory([item, ...existing]);
  renderHistory();
  loadResult(item);
}

function slug(value) {
  return String(value || "company").toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "") || "company";
}

function download(filename, text, type) {
  const blob = new Blob([text], { type });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  a.remove();
  URL.revokeObjectURL(url);
}

async function checkHealth() {
  try {
    const response = await fetch("/api/health");
    const data = await response.json();
    statusEl.textContent = data.automation_ready ? `Automated with ${data.model}` : "Manual packet mode";
  } catch {
    statusEl.textContent = "Server unavailable";
  }
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const payload = formPayload();
  submitBtn.disabled = true;
  submitBtn.textContent = "Running...";
  showNotice("");
  reportTitle.textContent = "Researching";
  reportMeta.textContent = "This may take a few minutes when automation is enabled.";
  try {
    const response = await fetch("/api/generate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    const data = await response.json();
    if (!response.ok) {
      throw new Error(data.detail || "Request failed");
    }
    saveResult(data, payload);
  } catch (error) {
    showNotice(error.message);
    reportTitle.textContent = "Failed";
    reportMeta.textContent = "The request did not complete.";
  } finally {
    submitBtn.disabled = false;
    submitBtn.textContent = "Generate DD";
  }
});

document.querySelectorAll(".tab").forEach((tab) => {
  tab.addEventListener("click", () => {
    document.querySelectorAll(".tab").forEach((node) => node.classList.remove("active"));
    document.querySelectorAll(".output").forEach((node) => node.classList.remove("active"));
    tab.classList.add("active");
    document.querySelector(`[data-panel="${tab.dataset.tab}"]`).classList.add("active");
  });
});

copyBtn.addEventListener("click", async () => {
  await navigator.clipboard.writeText(reportEl.value);
});

downloadMdBtn.addEventListener("click", () => {
  download(`${slug(current?.company)}_dd_one_pager.md`, reportEl.value, "text/markdown;charset=utf-8");
});

downloadPdfBtn.addEventListener("click", async () => {
  downloadPdfBtn.disabled = true;
  downloadPdfBtn.textContent = "Building...";
  try {
    const response = await fetch("/api/export-pdf", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        company: current?.company || "company",
        report_markdown: reportEl.value,
      }),
    });
    if (!response.ok) {
      const data = await response.json().catch(() => ({}));
      throw new Error(data.detail || "PDF export failed");
    }
    const blob = await response.blob();
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `${slug(current?.company)}_dd_one_pager.pdf`;
    document.body.appendChild(a);
    a.click();
    a.remove();
    URL.revokeObjectURL(url);
  } catch (error) {
    showNotice(error.message);
  } finally {
    downloadPdfBtn.disabled = !reportEl.value;
    downloadPdfBtn.textContent = "PDF";
  }
});

downloadJsonBtn.addEventListener("click", () => {
  download(`${slug(current?.company)}_evidence.json`, evidenceEl.value, "application/json;charset=utf-8");
});

clearHistoryBtn.addEventListener("click", () => {
  writeHistory([]);
  renderHistory();
});

checkHealth();
renderHistory();
