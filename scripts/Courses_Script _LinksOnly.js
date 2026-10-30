
(async () => {
  // Get the course ID from the current Canvas URL
  const match = location.pathname.match(/\/courses\/(\d+)/);

  if (!match) {
    console.error("Open a page inside a course first (the URL should contain /courses/<number>).");
    return;
  }

  const courseId = match[1];

  // Fetch course information for the filename and preview
  const courseRes = await fetch(
    `/api/v1/courses/${courseId}`,
    { credentials: "same-origin" }
  );

  let courseInfo = {};

  try {
    courseInfo = JSON.parse(
      (await courseRes.text()).replace(/^while\s*\(1\)\s*;\s*/, "")
    );
  } catch {
    console.warn("Could not read course info; using a generic filename.");
  }

  const safeName = (courseInfo.name || "course")
    .replace(/[\\/:*?"<>|]/g, "")
    .replace(/\s+/g, "_")
    .slice(0, 80);

  const fileName = `${safeName}_Course_Challenges_${courseId}.json`;

  // Fetch all pages of a Canvas API endpoint
  const getAll = async (path) => {
    let url = new URL(path, location.origin).href;
    const out = [];

    while (url) {
      const response = await fetch(url, {
        credentials: "same-origin"
      });

      if (!response.ok) {
        console.warn(`Request failed (${response.status}):`, url);
        break;
      }

      const text = (await response.text())
        .replace(/^while\s*\(1\)\s*;\s*/, "");

      const data = JSON.parse(text);

      Array.isArray(data)
        ? out.push(...data)
        : out.push(data);

      const next = (response.headers.get("Link") || "")
        .match(/<([^>]+)>;\s*rel="next"/);

      url = next ? next[1] : null;
    }

    return out;
  };

  // Fetch assignments and modules
  const assignments = await getAll(
    `/api/v1/courses/${courseId}/assignments?per_page=100`
  );

  const byId = new Map(
    assignments.map(assignment => [assignment.id, assignment])
  );

  const modules = await getAll(
    `/api/v1/courses/${courseId}/modules?per_page=100`
  );

  // Build challenge rows in module order
  // Only export name, module, and challenge page URL
  const rows = [];
  const seen = new Set();

  const addRow = (assignment, moduleName) => {
    const url = assignment.html_url ||
      new URL(
        `/courses/${courseId}/assignments/${assignment.id}`,
        location.origin
      ).href;

    rows.push({
      name: assignment.name,
      module: moduleName,
      url: url
    });

    seen.add(assignment.id);
  };

  // Process assignments in module order
  for (const module of modules) {
    const items = await getAll(
      `/api/v1/courses/${courseId}/modules/${module.id}/items?per_page=100`
    );

    for (const item of items) {
      if (
        item.type === "Assignment" &&
        byId.has(item.content_id) &&
        !seen.has(item.content_id)
      ) {
        addRow(byId.get(item.content_id), module.name);
      }
    }
  }

  // Include assignments that aren't listed in a module
  assignments
    .filter(assignment => !seen.has(assignment.id))
    .forEach(assignment => {
      addRow(assignment, "(not in a module)");
    });

  // Keep results available in the browser console
  window.challenges = rows;

  // Create the local preview overlay
  document.getElementById("challenge-overlay")?.remove();

  const overlay = document.createElement("div");
  overlay.id = "challenge-overlay";

  overlay.style.cssText =
    "position:fixed;inset:0;z-index:999999;" +
    "background:#fff;color:#000;overflow:auto;" +
    "padding:16px;font:14px/1.4 sans-serif;";

  const bar = document.createElement("div");

  bar.style.cssText =
    "margin-bottom:12px;display:flex;gap:8px;" +
    "align-items:center;flex-wrap:wrap;";

  // Copy button for Excel / Google Sheets
  const copyBtn = document.createElement("button");
  copyBtn.textContent = "Copy for Excel / Sheets";

  copyBtn.onclick = async () => {
    const clean = value =>
      String(value ?? "")
        .replace(/[\t\r\n]+/g, " ")
        .trim();

    const tsv = [
      "Challenge\tModule\tChallenge URL",
      ...rows.map(row =>
        [row.name, row.module, row.url]
          .map(clean)
          .join("\t")
      )
    ].join("\n");

    await navigator.clipboard.writeText(tsv);

    copyBtn.textContent = "Copied!";

    setTimeout(() => {
      copyBtn.textContent = "Copy for Excel / Sheets";
    }, 1500);
  };

  // Download JSON button
  const jsonBtn = document.createElement("button");
  jsonBtn.textContent = "Download JSON";

  jsonBtn.onclick = () => {
    const blob = new Blob(
      [JSON.stringify(rows, null, 2)],
      { type: "application/json" }
    );

    const objectUrl = URL.createObjectURL(blob);

    const downloadLink = document.createElement("a");
    downloadLink.href = objectUrl;
    downloadLink.download = fileName;

    document.body.append(downloadLink);
    downloadLink.click();
    downloadLink.remove();

    setTimeout(() => {
      URL.revokeObjectURL(objectUrl);
    }, 1000);

    jsonBtn.textContent = "Downloaded!";

    setTimeout(() => {
      jsonBtn.textContent = "Download JSON";
    }, 1500);
  };

  // Close button
  const closeBtn = document.createElement("button");
  closeBtn.textContent = "Close";
  closeBtn.onclick = () => overlay.remove();

  // Challenge count
  const count = document.createElement("span");

  count.textContent =
    `${courseInfo.name || "Course"} (${courseId}): ` +
    `${rows.length} challenges`;

  bar.append(copyBtn, jsonBtn, closeBtn, count);

  // Create preview table
  const table = document.createElement("table");

  table.style.cssText =
    "border-collapse:collapse;width:100%;";

  const cell = (tag, content) => {
    const element = document.createElement(tag);

    element.style.cssText =
      "border:1px solid #bbb;padding:6px 8px;" +
      "vertical-align:top;text-align:left;" +
      "white-space:pre-wrap;word-break:break-word;";

    if (content instanceof Node) {
      element.append(content);
    } else {
      element.textContent = content;
    }

    return element;
  };

  // Table headings
  const header = document.createElement("tr");

  ["Challenge", "Module", "Challenge URL"].forEach(label => {
    const th = cell("th", label);
    th.style.background = "#eee";
    header.append(th);
  });

  table.append(header);

  // Table rows
  rows.forEach(row => {
    const tr = document.createElement("tr");

    const link = document.createElement("a");
    link.href = row.url;
    link.textContent = row.url;
    link.target = "_blank";
    link.rel = "noopener noreferrer";

    tr.append(
      cell("td", row.name),
      cell("td", row.module),
      cell("td", link)
    );

    table.append(tr);
  });

  overlay.append(bar, table);
  document.body.append(overlay);

  console.log(
    `Done: ${courseInfo.name || "course"} ` +
    `(${courseId}), ${rows.length} challenges. ` +
    `Data is in window.challenges.`
  );
})();
