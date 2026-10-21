(async () => {
  // Grab the course ID from the URL (e.g. /courses/704/modules -> 704)
  const match = location.pathname.match(/\/courses\/(\d+)/);
  if (!match) {
    console.error("Open a page inside a course first (the URL should contain /courses/<number>).");
    return;
  }
  const courseId = match[1];

  // Fetch the course name and make it safe to use in a filename
  const courseRes = await fetch(`/api/v1/courses/${courseId}`, { credentials: "same-origin" });
  let courseInfo = {};
  try {
    courseInfo = JSON.parse((await courseRes.text()).replace(/^while\s*\(1\)\s*;\s*/, ""));
  } catch {
    console.warn("Could not read course info; using a generic filename.");
  }
  const safeName = (courseInfo.name || "course")
    .replace(/[\\/:*?"<>|]/g, "")   // remove characters not allowed in filenames
    .replace(/\s+/g, "_")           // spaces -> underscores
    .slice(0, 80);                  // keep it a reasonable length
  const fileName = `${safeName}_Course_Code_${courseId}.json`;

  // Fetches every page of a list endpoint by following the Link header
  const getAll = async (path) => {
    let url = new URL(path, location.origin).href;
    const out = [];
    while (url) {
      const r = await fetch(url, { credentials: "same-origin" });
      if (!r.ok) { console.warn(r.status, url); break; }
      const t = (await r.text()).replace(/^while\s*\(1\)\s*;\s*/, "");
      const j = JSON.parse(t);
      Array.isArray(j) ? out.push(...j) : out.push(j);
      const next = (r.headers.get("Link") || "").match(/<([^>]+)>;\s*rel="next"/);
      url = next ? next[1] : null;
    }
    return out;
  };

  // HTML -> readable text, keeping bullets and line breaks
  const htmlToText = (html) => {
    const doc = new DOMParser().parseFromString(html || "", "text/html");
    doc.querySelectorAll("br").forEach(br => br.replaceWith("\n"));
    doc.querySelectorAll("li").forEach(li => li.prepend("• "));
    doc.querySelectorAll("p, div, li, h1, h2, h3, h4, h5, h6, ul, ol, tr")
      .forEach(el => el.append("\n"));
    return doc.body.textContent
      .replace(/\u00a0/g, " ")
      .replace(/[ \t]+\n/g, "\n")
      .replace(/\n{3,}/g, "\n\n")
      .trim();
  };

  // Every link in the description: anchors, embedded videos, media
  const extractLinks = (html) => {
    const doc = new DOMParser().parseFromString(html || "", "text/html");
    const links = new Set();
    doc.querySelectorAll("a[href]").forEach(a => links.add(new URL(a.getAttribute("href"), location.origin).href));
    doc.querySelectorAll("iframe[src], video[src], video source[src]")
      .forEach(el => links.add(new URL(el.getAttribute("src"), location.origin).href));
    doc.querySelectorAll("[data-media-id]")
      .forEach(el => links.add("canvas-media-id:" + el.getAttribute("data-media-id")));
    return [...links];
  };

  // Fetch assignments and modules
  const assignments = await getAll(`/api/v1/courses/${courseId}/assignments?per_page=100`);
  const byId = new Map(assignments.map(a => [a.id, a]));
  const modules = await getAll(`/api/v1/courses/${courseId}/modules?per_page=100`);

  // Build rows in module order
  const rows = [];
  const seen = new Set();
  const addRow = (a, moduleName) => {
    rows.push({
      name: a.name,
      module: moduleName,
      description: htmlToText(a.description),
      links: extractLinks(a.description)
    });
    seen.add(a.id);
  };

  for (const m of modules) {
    const items = await getAll(`/api/v1/courses/${courseId}/modules/${m.id}/items?per_page=100`);
    for (const it of items) {
      if (it.type === "Assignment" && byId.has(it.content_id) && !seen.has(it.content_id)) {
        addRow(byId.get(it.content_id), m.name);
      }
    }
  }
  assignments.filter(a => !seen.has(a.id)).forEach(a => addRow(a, "(not in a module)"));

  window.challenges = rows;

  // Draw the table on the page
  document.getElementById("challenge-overlay")?.remove();
  const overlay = document.createElement("div");
  overlay.id = "challenge-overlay";
  overlay.style.cssText = "position:fixed;inset:0;z-index:999999;background:#fff;color:#000;overflow:auto;padding:16px;font:14px/1.4 sans-serif;";

  const bar = document.createElement("div");
  bar.style.cssText = "margin-bottom:12px;display:flex;gap:8px;align-items:center;";

  const copyBtn = document.createElement("button");
  copyBtn.textContent = "Copy for Excel / Sheets";
  copyBtn.onclick = async () => {
    const clean = s => s.replace(/\s*\n\s*/g, " ").replace(/\t/g, " ");
    const tsv = ["Challenge\tModule\tDescription\tLinks",
      ...rows.map(r => [r.name, r.module, clean(r.description), r.links.join(" | ")].map(clean).join("\t"))
    ].join("\n");
    await navigator.clipboard.writeText(tsv);
    copyBtn.textContent = "Copied!";
    setTimeout(() => (copyBtn.textContent = "Copy for Excel / Sheets"), 1500);
  };

  const jsonBtn = document.createElement("button");
  jsonBtn.textContent = "Download JSON";
  jsonBtn.onclick = () => {
    const blob = new Blob([JSON.stringify(rows, null, 2)], { type: "application/json" });
    const dl = document.createElement("a");
    dl.href = URL.createObjectURL(blob);
    dl.download = fileName;
    document.body.append(dl);
    dl.click();
    dl.remove();
    setTimeout(() => URL.revokeObjectURL(dl.href), 1000);
    jsonBtn.textContent = "Downloaded!";
    setTimeout(() => (jsonBtn.textContent = "Download JSON"), 1500);
  };

  const closeBtn = document.createElement("button");
  closeBtn.textContent = "Close";
  closeBtn.onclick = () => overlay.remove();

  const count = document.createElement("span");
  count.textContent = `${courseInfo.name || "Course"} (${courseId}): ${rows.length} challenges`;
  bar.append(copyBtn, jsonBtn, closeBtn, count);

  const table = document.createElement("table");
  table.style.cssText = "border-collapse:collapse;width:100%;";
  const cell = (tag, content) => {
    const c = document.createElement(tag);
    c.style.cssText = "border:1px solid #bbb;padding:6px 8px;vertical-align:top;text-align:left;white-space:pre-wrap;word-break:break-word;";
    if (content instanceof Node) c.append(content); else c.textContent = content;
    return c;
  };

  const head = document.createElement("tr");
  ["Challenge", "Module", "Description", "Links"].forEach(h => {
    const th = cell("th", h);
    th.style.background = "#eee";
    head.append(th);
  });
  table.append(head);

  rows.forEach(r => {
    const tr = document.createElement("tr");
    const linkCell = document.createElement("div");
    if (!r.links.length) linkCell.textContent = "none";
    r.links.forEach(l => {
      const a = document.createElement("a");
      a.href = l; a.textContent = l; a.target = "_blank";
      a.style.display = "block";
      linkCell.append(a);
    });
    tr.append(cell("td", r.name), cell("td", r.module), cell("td", r.description), cell("td", linkCell));
    table.append(tr);
  });

  overlay.append(bar, table);
  document.body.append(overlay);

  console.log(`Done: ${courseInfo.name || "course"} (${courseId}), ${rows.length} challenges. Data is in window.challenges.`);
})();
