import os
import json

def write_html():
    path = r"C:\Users\Charles\Documents\Psychology\study-planner\index.html"
    parts = []
    
    parts.append('<!DOCTYPE html>')
    parts.append('<html lang="zh-CN">')
    parts.append('<head>')
    parts.append('<meta charset="UTF-8">')
    parts.append('<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">')
    parts.append('<title>应用心理硕士 · 备考学习管理系统</title>')
    parts.append('<style>')
    parts.append('*{margin:0;padding:0;box-sizing:border-box}')
    parts.append(':root{--primary:#4F46E5;--primary-light:#818CF8;--primary-bg:#EEF2FF;--success:#10B981;--warning:#F59E0B;--danger:#EF4444;--gray-50:#F9FAFB;--gray-100:#F3F4F6;--gray-200:#E5E7EB;--gray-300:#D1D5DB;--gray-500:#6B7280;--gray-700:#374151;--gray-900:#111827}')
    parts.append('body{font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",sans-serif;background:var(--gray-50);color:var(--gray-900);line-height:1.6;padding-bottom:80px}')
    parts.append('.app-header{background:linear-gradient(135deg,var(--primary),#7C3AED);color:white;padding:24px 16px 20px;position:sticky;top:0;z-index:10}')
    parts.append('.app-header h1{font-size:20px;font-weight:700}')
    parts.append('.app-header .subtitle{font-size:13px;opacity:0.85;margin-top:4px}')
    parts.append('.app-header .countdown{margin-top:10px;background:rgba(255,255,255,0.15);border-radius:8px;padding:8px 12px;display:flex;align-items:center;gap:8px;font-size:14px}')
    parts.append('.tab-bar{display:flex;background:white;border-bottom:1px solid var(--gray-200);position:sticky;top:108px;z-index:9}')
    parts.append('.tab-btn{flex:1;text-align:center;padding:12px 8px;font-size:14px;font-weight:500;color:var(--gray-500);background:none;border:none;cursor:pointer;border-bottom:2px solid transparent}')
    parts.append('.tab-btn.active{color:var(--primary);border-bottom-color:var(--primary)}')
    parts.append('.content{padding:16px;max-width:600px;margin:0 auto}')
    parts.append('.section{display:none}')
    parts.append('.section.active{display:block}')
    parts.append('.card{background:white;border-radius:12px;box-shadow:0 1px 3px rgba(0,0,0,0.08);padding:16px;margin-bottom:12px}')
    parts.append('.card-title{font-size:15px;font-weight:600;color:var(--gray-900);margin-bottom:8px}')
    parts.append('.badge{display:inline-block;font-size:11px;font-weight:500;padding:2px 8px;border-radius:10px;margin-left:6px}')
    parts.append('.badge-blue{background:var(--primary-bg);color:var(--primary)}')
    parts.append('.badge-green{background:#D1FAE5;color:#065F46}')
    parts.append('.badge-yellow{background:#FEF3C7;color:#92400E}')
    parts.append('.badge-red{background:#FEE2E2;color:#991B1B}')
    parts.append('.progress-bar{height:6px;background:var(--gray-200);border-radius:3px;margin:8px 0;overflow:hidden}')
    parts.append('.progress-fill{height:100%;border-radius:3px;transition:width 0.5s ease}')
    parts.append('.progress-text{font-size:13px;color:var(--gray-500)}')
    parts.append('.task-item{display:flex;align-items:flex-start;gap:10px;padding:10px 0;border-bottom:1px solid var(--gray-100)}')
    parts.append('.task-check{width:20px;height:20px;border:2px solid var(--gray-300);border-radius:50%;flex-shrink:0;cursor:pointer;margin-top:2px;display:flex;align-items:center;justify-content:center}')
    parts.append('.task-check.done{background:var(--success);border-color:var(--success);color:white;font-size:14px;font-weight:bold}')
    parts.append('.task-info{flex:1}')
    parts.append('.task-name{font-size:14px;color:var(--gray-700)}')
    parts.append('.task-name.done{text-decoration:line-through;color:var(--gray-300)}')
    parts.append('.task-desc{font-size:12px;color:var(--gray-500);margin-top:2px}')
    parts.append('.phase-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:12px}')
    parts.append('.phase-title{font-size:16px;font-weight:700;color:var(--gray-900)}')
    parts.append('.phase-dates{font-size:13px;color:var(--gray-500)}')
    parts.append('.stats-row{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:16px}')
    parts.append('.stat-box{background:white;border-radius:12px;box-shadow:0 1px 3px rgba(0,0,0,0.08);padding:14px 12px;text-align:center}')
    parts.append('.stat-num{font-size:22px;font-weight:700;color:var(--primary)}')
    parts.append('.stat-label{font-size:12px;color:var(--gray-500);margin-top:2px}')
    parts.append('.review-date{font-size:13px;color:var(--gray-500);margin-bottom:12px;padding-bottom:8px;border-bottom:1px solid var(--gray-200)}')
    parts.append('.review-item{padding:8px 0;display:flex;justify-content:space-between;align-items:center}')
    parts.append('.review-rating{display:flex;gap:4px}')
    parts.append('.info-box{background:var(--primary-bg);border-radius:12px;padding:14px;margin-bottom:12px;font-size:13px;line-height:1.8}')
    parts.append('.info-box strong{color:var(--primary)}')
    parts.append('.resource-list{list-style:none}')
    parts.append('.resource-list li{padding:10px 0;border-bottom:1px solid var(--gray-100);font-size:14px}')
    parts.append('.resource-list .book-title{font-weight:600}')
    parts.append('.resource-list .book-author{color:var(--gray-500);font-size:13px}')
    parts.append('.save-indicator{position:fixed;bottom:16px;left:50%;transform:translateX(-50%);background:var(--gray-900);color:white;padding:8px 16px;border-radius:20px;font-size:13px;opacity:0;transition:opacity 0.3s;z-index:100;pointer-events:none}')
    parts.append('.save-indicator.show{opacity:1}')
    parts.append('.btn-reset{display:block;width:100%;padding:10px;background:var(--gray-100);border:none;border-radius:8px;color:var(--gray-500);font-size:13px;cursor:pointer;margin-top:8px}')
    parts.append('.notes-area{width:100%;border:1px solid var(--gray-200);border-radius:8px;padding:10px;font-size:13px;font-family:inherit;resize:vertical;min-height:60px;margin-top:8px;outline:none}')
    parts.append('.notes-area:focus{border-color:var(--primary)}')
    parts.append('</style></head><body>')
    
    parts.append('<div class="app-header">')
    parts.append('<h1> 应用心理硕士 · 备考系统</h1>')
    parts.append('<div class="subtitle">西南交通大学 · 045400 应用心理（全日制/非全日制）</div>')
    parts.append('<div class="countdown" id="countdown">距2026考研还有 <strong id="daysLeft">--</strong> 天</div>')
    parts.append('</div>')
    
    parts.append('<div class="tab-bar">')
    parts.append('<button class="tab-btn active" data-tab="plan">复习计划</button>')
    parts.append('<button class="tab-btn" data-tab="progress">进度追踪</button>')
    parts.append('<button class="tab-btn" data-tab="review">学习回顾</button>')
    parts.append('<button class="tab-btn" data-tab="info">考试信息</button>')
    parts.append('</div>')
    
    parts.append('<div class="content">')
    
    # Tab 1: Plan
    parts.append('<div class="section active" id="tab-plan">')
    parts.append('<div class="stats-row"><div class="stat-box"><div class="stat-num" id="statTotal">0</div><div class="stat-label">总任务</div></div><div class="stat-box"><div class="stat-num" id="statDone">0</div><div class="stat-label">已完成</div></div><div class="stat-box"><div class="stat-num" id="statPct">0%</div><div class="stat-label">完成率</div></div></div>')
    parts.append('<div id="planContent"></div>')
    parts.append('<button class="btn-reset" onclick="resetAll()">重置所有进度</button>')
    parts.append('</div>')
    
    # Tab 2: Progress
    parts.append('<div class="section" id="tab-progress">')
    parts.append('<div class="card"><div class="card-title">总体进度</div><div style="display:flex;align-items:center;gap:12px"><div style="flex:1"><div class="progress-bar"><div class="progress-fill" id="overallBar" style="width:0%;background:var(--primary)"></div></div></div><span class="progress-text" id="overallPct">0%</span></div></div>')
    parts.append('<div class="card" id="phaseProgressCards"></div>')
    parts.append('<div class="card"><div class="card-title">备考笔记</div><textarea class="notes-area" id="notesArea" placeholder="记录学习心得、重点难点、疑问..."></textarea></div>')
    parts.append('</div>')
    
    # Tab 3: Review
    parts.append('<div class="section" id="tab-review">')
    parts.append('<div class="card"><div class="card-title">每日回顾</div><div class="review-date" id="todayDate"></div><div id="dailyReview"></div></div>')
    parts.append('<div class="card"><div class="card-title">本周复习统计</div><div id="weekStats"></div></div>')
    parts.append('</div>')
    
    # Tab 4: Info
    parts.append('<div class="section" id="tab-info">')
    parts.append('<div class="info-box"><strong>西南交通大学 · 心理研究与咨询中心</strong><br>专业代码：<strong>045400 应用心理</strong><br>全日制 27人（含推免3人）| 非全日制 20人</div>')
    parts.append('<div class="card"><div class="card-title">考试科目</div><ul class="resource-list"><li><span class="book-title">101 思想政治理论</span><br><span class="book-author">全国统考 · 满分100分</span></li><li><span class="book-title">204 英语（二）</span><br><span class="book-author">全国统考 · 满分100分</span></li><li><span class="book-title">347 心理学专业综合</span><br><span class="book-author">学校自命题 · 满分300分</span></li></ul></div>')
    parts.append('<div class="card"><div class="card-title">347参考书目</div><ul class="resource-list"><li><span class="book-title">《心理学导论》第三版</span><br><span class="book-author">黄希庭 著，人民教育出版社，2015</span></li><li><span class="book-title">《发展心理学》第三版</span><br><span class="book-author">林崇德 著，人民教育出版社，2018</span></li><li><span class="book-title">《心理与教育研究方法》第二版</span><br><span class="book-author">董奇 著，北京师范大学出版社，2019</span></li></ul></div>')
    parts.append('<div class="card"><div class="card-title">研究方向</div><ul class="resource-list"><li>心理健康与大数据应用</li><li>临床与咨询心理</li><li>人机交互与用户体验</li></ul></div>')
    parts.append('<div class="card"><div class="card-title">重要链接</div><ul class="resource-list"><li><a href="https://yz.swjtu.edu.cn" target="_blank" style="color:var(--primary);text-decoration:none">西南交大研究生招生网</a></li><li><a href="https://yz.chsi.com.cn" target="_blank" style="color:var(--primary);text-decoration:none">中国研究生招生信息网</a></li></ul></div>')
    parts.append('</div>')
    parts.append('</div>')
    parts.append('<div class="save-indicator" id="saveIndicator">已自动保存</div>')
    
    # JavaScript
    js = '''<script>
var PHASES = [
  {id:"p1",title:"第一阶段 · 基础夯实",dates:"7月12日 - 8月31日",
   tasks:[
    {id:"p1_1",name:"政治：完成马原、毛中特第一轮听课",desc:"徐涛/腿姐强化班，同步做笔记"},
    {id:"p1_2",name:"政治：完成1000题马原部分",desc:"每天30题，错题标记"},
    {id:"p1_3",name:"英语：考研核心词一轮背诵完成",desc:"墨墨背单词/不背单词，每天100词"},
    {id:"p1_4",name:"英语：长难句分析训练",desc:"田静/何凯文长难句，每天5句"},
    {id:"p1_5",name:"英语：2010-2014年阅读真题精做",desc:"每篇精读，分析错题"},
    {id:"p1_6",name:"347：心理学导论通读完第一遍",desc:"黄希庭版，做章节框架笔记"},
    {id:"p1_7",name:"347：发展心理学通读完第一遍",desc:"林崇德版，做章节框架笔记"},
    {id:"p1_8",name:"347：心理与教育研究方法通读完第一遍",desc:"董奇版，理解研究方法论"}
  ]},
  {id:"p2",title:"第二阶段 · 强化提升",dates:"9月1日 - 10月31日",
   tasks:[
    {id:"p2_1",name:"政治：完成史纲、思修、当代第一轮",desc:"听课+1000题对应部分"},
    {id:"p2_2",name:"政治：1000题二刷错题",desc:"重点关注一刷错题"},
    {id:"p2_3",name:"英语：考研核心词二轮巩固",desc:"每天100词，重点记忆生词"},
    {id:"p2_4",name:"英语：2015-2019年阅读真题精做",desc:"限时训练，每篇15-20分钟"},
    {id:"p2_5",name:"英语：完形+翻译+新题型专项训练",desc:"每周各2篇"},
    {id:"p2_6",name:"347：三本教材二轮复习",desc:"整理背诵笔记，建立知识体系"},
    {id:"p2_7",name:"347：核心知识点一轮背诵",desc:"每天2章，利用艾宾浩斯表格"},
    {id:"p2_8",name:"347：收集历年347真题",desc:"分析题型、考点分布"}
  ]},
  {id:"p3",title:"第三阶段 · 冲刺模考",dates:"11月1日 - 12月考前",
   tasks:[
    {id:"p3_1",name:"政治：肖秀荣八套卷选择题",desc:"限时做，错题回归知识点"},
    {id:"p3_2",name:"政治：肖秀荣四套卷全真模拟",desc:"大题背诵，每天2-3题"},
    {id:"p3_3",name:"政治：时政热点整理背诵",desc:"关注年度重大事件"},
    {id:"p3_4",name:"英语：2020-2025年真题全真模拟",desc:"严格计时，模拟考试环境"},
    {id:"p3_5",name:"英语：作文模板整理与背诵",desc:"大作文+小作文各5篇模板"},
    {id:"p3_6",name:"347：二轮知识点背诵",desc:"查漏补缺，重点突破薄弱章节"},
    {id:"p3_7",name:"347：全真模拟考试至少3次",desc:"限时3小时，模拟答题卡"},
    {id:"p3_8",name:"347：三轮快速回顾",desc:"框架式复习，保持状态"},
    {id:"p3_9",name:"全科：考前一周调整状态",desc:"轻复习，调整作息"}
  ]}
];

var state = null;

function getDefaultState() {
  var s = {tasks:{},notes:"",reviews:[]};
  for (var i=0;i<PHASES.length;i++) {
    for (var j=0;j<PHASES[i].tasks.length;j++) {
      s.tasks[PHASES[i].tasks[j].id] = false;
    }
  }
  return s;
}

function loadState() {
  try {
    var raw = localStorage.getItem("psych_study_state");
    if (raw) {
      var parsed = JSON.parse(raw);
      for (var i=0;i<PHASES.length;i++) {
        for (var j=0;j<PHASES[i].tasks.length;j++) {
          if (parsed.tasks[PHASES[i].tasks[j].id] === undefined) {
            parsed.tasks[PHASES[i].tasks[j].id] = false;
          }
        }
      }
      return parsed;
    }
  } catch(e) {}
  return getDefaultState();
}

function saveState() {
  localStorage.setItem("psych_study_state", JSON.stringify(state));
  var el = document.getElementById("saveIndicator");
  el.classList.add("show");
  clearTimeout(el._timer);
  el._timer = setTimeout(function(){el.classList.remove("show");}, 1500);
}

function updateCountdown() {
  var exam = new Date(2026, 11, 21);
  var today = new Date();
  var diff = Math.ceil((exam - today) / (1000 * 60 * 60 * 24));
  document.getElementById("daysLeft").textContent = diff > 0 ? diff : "已开考";
}

function toggleTask(id) {
  state.tasks[id] = !state.tasks[id];
  saveState();
  renderPlan();
  renderProgress();
}

function calcOverall() {
  var total = 0, done = 0;
  for (var i=0;i<PHASES.length;i++) {
    for (var j=0;j<PHASES[i].tasks.length;j++) {
      total++;
      if (state.tasks[PHASES[i].tasks[j].id]) done++;
    }
  }
  return total ? Math.round(done/total*100) : 0;
}

function renderPlan() {
  var container = document.getElementById("planContent");
  var html = "";
  var total = 0, done = 0;
  
  for (var i=0;i<PHASES.length;i++) {
    var p = PHASES[i];
    var phaseDone = 0;
    var tasksHtml = "";
    for (var j=0;j<p.tasks.length;j++) {
      var t = p.tasks[j];
      total++;
      var isDone = state.tasks[t.id];
      if (isDone) { done++; phaseDone++; }
      var checkClass = isDone ? " task-check done" : " task-check";
      var nameClass = isDone ? " task-name done" : " task-name";
      var checkMark = isDone ? "\\u2713" : "";
      tasksHtml += "<div class=\\"task-item\\"><div class=\\"" + checkClass + "\\" onclick=\\"toggleTask('" + t.id + "')\\">" + checkMark + "</div><div class=\\"task-info\\"><div class=\\"" + nameClass + "\\">" + t.name + "</div><div class=\\"task-desc\\">" + t.desc + "</div></div></div>";
    }
    var pct = p.tasks.length ? Math.round(phaseDone/p.tasks.length*100) : 0;
    var badgeClass = "badge-red";
    if (pct === 100) badgeClass = "badge-green";
    else if (pct > 50) badgeClass = "badge-blue";
    else if (pct > 0) badgeClass = "badge-yellow";
    var barColor = pct === 100 ? "var(--success)" : "var(--primary)";
    html += "<div class=\\"card\\"><div class=\\"phase-header\\"><div><div class=\\"phase-title\\">" + p.title + "</div><div class=\\"phase-dates\\">" + p.dates + "</div></div><span class=\\"badge " + badgeClass + "\\">" + pct + "%</span></div><div class=\\"progress-bar\\"><div class=\\"progress-fill\\" style=\\"width:" + pct + "%;background:" + barColor + ";\\"></div></div>" + tasksHtml + "</div>";
  }
  
  container.innerHTML = html;
  document.getElementById("statTotal").textContent = total;
  document.getElementById("statDone").textContent = done;
  document.getElementById("statPct").textContent = total ? Math.round(done/total*100) + "%" : "0%";
}

function renderProgress() {
  var pct = calcOverall();
  document.getElementById("overallBar").style.width = pct + "%";
  document.getElementById("overallPct").textContent = pct + "%";
  
  var html = "";
  for (var i=0;i<PHASES.length;i++) {
    var p = PHASES[i];
    var phaseDone = 0;
    for (var j=0;j<p.tasks.length;j++) {
      if (state.tasks[p.tasks[j].id]) phaseDone++;
    }
    var phasePct = p.tasks.length ? Math.round(phaseDone/p.tasks.length*100) : 0;
    var barColor = phasePct === 100 ? "var(--success)" : "var(--primary)";
    html += "<div style=\\"margin-bottom:12px\\"><div style=\\"display:flex;justify-content:space-between;font-size:14px;margin-bottom:4px\\"><span>" + p.title + "</span><span style=\\"font-weight:600\\">" + phaseDone + "/" + p.tasks.length + "</span></div><div class=\\"progress-bar\\"><div class=\\"progress-fill\\" style=\\"width:" + phasePct + "%;background:" + barColor + ";\\"></div></div></div>";
  }
  document.getElementById("phaseProgressCards").innerHTML = html;
  document.getElementById("notesArea").value = state.notes || "";
}

function renderReview() {
  var today = new Date();
  var dateStr = today.toLocaleDateString("zh-CN", {year:"numeric",month:"long",day:"numeric",weekday:"long"});
  document.getElementById("todayDate").textContent = "\\ud83d\\udccc " + dateStr;

  var subjects = [
    {id:"politics", name:"思想政治"},
    {id:"english", name:"英语（二）"},
    {id:"psych347", name:"347心理学专业综合"}
  ];

  var todayKey = today.toISOString().split("T")[0];
  var todayReview = null;
  for (var i=0;i<state.reviews.length;i++) {
    if (state.reviews[i].date === todayKey) { todayReview = state.reviews[i]; break; }
  }
  
  var html = "<div style=\\"font-size:14px;color:var(--gray-500);margin-bottom:8px\\">今天各科学习状态</div>";
  for (var i=0;i<subjects.length;i++) {
    var sub = subjects[i];
    var val = todayReview ? (todayReview[sub.id] || 0) : 0;
    var emojis = ["\\ud83d\\ude1e","\\ud83d\\ude10","\\ud83d\\ude42","\\ud83d\\ude0a"];
    var stars = "";
    for (var j=0;j<emojis.length;j++) {
      var opacity = val === j+1 ? "1" : "0.3";
      stars += "<span style=\\"font-size:20px;cursor:pointer;opacity:" + opacity + ";\\" onclick=\\"setRating('" + todayKey + "','" + sub.id + "'," + (j+1) + ")\\">" + emojis[j] + "</span>";
    }
    html += "<div class=\\"review-item\\"><span style=\\"font-size:14px\\">" + sub.name + "</span><div class=\\"review-rating\\">" + stars + "</div></div>";
  }

  var hours = todayReview ? (todayReview.hours || 0) : 0;
  html += "<div class=\\"review-item\\"><span style=\\"font-size:14px\\">今日学习时长</span><div style=\\"display:flex;align-items:center;gap:8px\\"><button onclick=\\"adjHours(-0.5)\\" style=\\"width:28px;height:28px;border:1px solid var(--gray-200);border-radius:50%;background:white;cursor:pointer;font-size:16px\\">-</button><span style=\\"font-size:16px;font-weight:600;min-width:40px;text-align:center\\">" + hours + "h</span><button onclick=\\"adjHours(0.5)\\" style=\\"width:28px;height:28px;border:1px solid var(--gray-200);border-radius:50%;background:white;cursor:pointer;font-size:16px\\">+</button></div></div>";
  
  var summary = todayReview ? (todayReview.summary || "") : "";
  html += "<div style=\\"margin-top:12px\\"><div style=\\"font-size:13px;color:var(--gray-500);margin-bottom:4px\\">今日学习小结</div><textarea class=\\"notes-area\\" id=\\"dailyNotes\\" style=\\"min-height:50px\\" placeholder=\\"今天学了什么？有什么收获？\\">" + summary + "</textarea></div><button onclick=\\"saveDailyReview()\\" style=\\"margin-top:8px;padding:8px 20px;background:var(--primary);color:white;border:none;border-radius:8px;font-size:14px;cursor:pointer\\">保存今日回顾</button>";

  document.getElementById("dailyReview").innerHTML = html;
  renderWeekStats();
}

function renderWeekStats() {
  var weekData = [];
  var today = new Date();
  for (var i=6;i>=0;i--) {
    var d = new Date(today);
    d.setDate(d.getDate() - i);
    var key = d.toISOString().split("T")[0];
    var r = null;
    for (var k=0;k<state.reviews.length;k++) {
      if (state.reviews[k].date === key) { r = state.reviews[k]; break; }
    }
    var dayLabel = d.toLocaleDateString("zh-CN", {weekday:"short"});
    var hrs = r ? (r.hours || 0) : 0;
    var status = r ? [r.politics,r.english,r.psych347].filter(Boolean).length : 0;
    weekData.push({day:dayLabel, hours:hrs, status:status});
  }

  var html = "<div style=\\"display:flex;gap:4px;justify-content:space-between\\">";
  for (var i=0;i<weekData.length;i++) {
    var d = weekData[i];
    var barH = Math.min(d.hours/8*100, 100);
    html += "<div style=\\"flex:1;text-align:center\\"><div style=\\"font-size:11px;color:var(--gray-500)\\">" + d.day + "</div><div style=\\"margin:4px 0;height:40px;background:var(--gray-100);border-radius:4px;position:relative;overflow:hidden\\"><div style=\\"position:absolute;bottom:0;width:100%;background:var(--primary);border-radius:4px;height:" + barH + "%\\"></div></div><div style=\\"font-size:12px;font-weight:600\\">" + d.hours + "h</div><div style=\\"font-size:10px;color:var(--gray-500)\\">" + d.status + "/3科</div></div>";
  }
  var totalHours = 0;
  for (var i=0;i<weekData.length;i++) totalHours += weekData[i].hours;
  html += "</div><div style=\\"font-size:12px;color:var(--gray-500);margin-top:8px;text-align:center\\">本周总学习：" + totalHours + "h</div>";
  document.getElementById("weekStats").innerHTML = html;
}

function setRating(dateKey, subject, rating) {
  var r = null;
  for (var i=0;i<state.reviews.length;i++) {
    if (state.reviews[i].date === dateKey) { r = state.reviews[i]; break; }
  }
  if (!r) {
    r = {date:dateKey, politics:0, english:0, psych347:0, hours:0, summary:""};
    state.reviews.push(r);
  }
  r[subject] = rating;
  saveState();
  renderReview();
}

function adjHours(delta) {
  var todayKey = new Date().toISOString().split("T")[0];
  var r = null;
  for (var i=0;i<state.reviews.length;i++) {
    if (state.reviews[i].date === todayKey) { r = state.reviews[i]; break; }
  }
  if (!r) {
    r = {date:todayKey, politics:0, english:0, psych347:0, hours:0, summary:""};
    state.reviews.push(r);
  }
  r.hours = Math.max(0, Math.round((r.hours + delta) * 10) / 10);
  saveState();
  renderReview();
}

function saveDailyReview() {
  var todayKey = new Date().toISOString().split("T")[0];
  var r = null;
  for (var i=0;i<state.reviews.length;i++) {
    if (state.reviews[i].date === todayKey) { r = state.reviews[i]; break; }
  }
  if (!r) {
    r = {date:todayKey, politics:0, english:0, psych347:0, hours:0, summary:""};
    state.reviews.push(r);
  }
  r.summary = document.getElementById("dailyNotes").value;
  saveState();
}

document.addEventListener("input", function(e) {
  if (e.target && e.target.id === "notesArea") {
    state.notes = e.target.value;
    saveState();
  }
});

function resetAll() {
  if (confirm("确定要重置所有学习进度吗？（每日回顾数据会保留）")) {
    for (var i=0;i<PHASES.length;i++) {
      for (var j=0;j<PHASES[i].tasks.length;j++) {
        state.tasks[PHASES[i].tasks[j].id] = false;
      }
    }
    state.notes = "";
    saveState();
    renderPlan();
    renderProgress();
  }
}

(function(){
  var btns = document.querySelectorAll(".tab-btn");
  for (var i=0;i<btns.length;i++) {
    btns[i].addEventListener("click", function() {
      var btns2 = document.querySelectorAll(".tab-btn");
      for (var k=0;k<btns2.length;k++) btns2[k].classList.remove("active");
      var secs = document.querySelectorAll(".section");
      for (var k=0;k<secs.length;k++) secs[k].classList.remove("active");
      this.classList.add("active");
      document.getElementById("tab-" + this.dataset.tab).classList.add("active");
      if (this.dataset.tab === "review") renderReview();
      if (this.dataset.tab === "progress") renderProgress();
      if (this.dataset.tab === "plan") renderPlan();
    });
  }
  
  state = loadState();
  updateCountdown();
  renderPlan();
})();
</script>'''
    
    parts.append(js)
    parts.append('</body></html>')
    
    result = '\n'.join(parts)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(result)
    print(f"OK: written {len(result)} bytes to {path}")

write_html()
