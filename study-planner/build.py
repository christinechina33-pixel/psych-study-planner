# -*- coding: utf-8 -*-
"""
西南交通大学 · 应用心理硕士(347) 备考学习系统 —— 单文件生成器。
index.html 由本脚本生成（单一事实来源）。
约定：JS 用模板字符串拼接 HTML，知识数据以 JSON 注入，避免引号转义类的语法错误。
运行： python build.py
"""
import json
import os

# ============================================================
# 知识数据（可作思维导图节点 + 卡片正反面）
#   t = 标题（导图节点 / 卡片正面）
#   m = 要点（详情 / 卡片背面）
#   tag = key(重点) | hard(难点) | easy(了解)
# ============================================================
KNOWLEDGE = {
    "psych347": {
        "name": "347 心理学专业综合",
        "short": "347心理",
        "icon": "📕",
        "chapters": [
            {"name": "心理学导论 · 普通心理学（黄希庭）", "points": [
                {"t": "心理学的性质与主要流派", "tag": "key",
                 "m": "构造主义（冯特、铁钦纳）、机能主义（詹姆斯、杜威）、行为主义（华生、斯金纳）、格式塔（韦特海默）、精神分析（弗洛伊德）、人本主义（马斯洛、罗杰斯）、认知心理学（奈瑟）。记忆要点：每个流派的代表人物 + 核心主张 + 研究方法。"},
                {"t": "心理的神经生理基础", "tag": "hard",
                 "m": "神经元与突触传递；神经系统分中枢与周围；大脑皮层分区（额叶、顶叶、枕叶、颞叶）及机能定位；大脑两半球分工与单侧化。"},
                {"t": "感觉：感受性与阈限", "tag": "key",
                 "m": "绝对感觉阈限与差别感觉阈限；韦伯定律 ΔI/I=K（常数）；费希纳对数定律 S=K·logR；感觉适应与感觉对比。"},
                {"t": "知觉的基本特性", "tag": "key",
                 "m": "选择性、整体性、理解性、恒常性（大小/形状/颜色/明度）；格式塔组织原则（接近、相似、连续、闭合）；深度知觉线索；错觉。"},
                {"t": "意识与注意", "tag": "key",
                 "m": "意识状态与睡眠阶段、梦；注意的种类（无意注意、有意注意、有意后注意）；注意理论：过滤器模型、衰减模型、后期选择模型、认知资源分配。"},
                {"t": "记忆系统", "tag": "key",
                 "m": "三级记忆：感觉记忆→短时记忆（容量 7±2）→长时记忆；工作记忆（巴德利）；加工水平说；编码策略：复述、组织、精细加工。"},
                {"t": "遗忘及其规律", "tag": "hard",
                 "m": "艾宾浩斯遗忘曲线（先快后慢）；遗忘理论：消退说、干扰说（前摄抑制/倒摄抑制）、提取失败说、动机性遗忘（压抑）。"},
                {"t": "思维与问题解决", "tag": "hard",
                 "m": "概念形成；推理（归纳/演绎）；问题解决策略（算法、启发式）；影响因素：定势、功能固着；创造性思维与发散思维。"},
                {"t": "情绪与情感", "tag": "key",
                 "m": "情绪三成分（主观体验、生理唤醒、外部表现）；情绪理论：詹姆斯-兰格（外周）、坎农-巴德（丘脑）、沙赫特-辛格（二因素）、阿诺德（评定-兴奋）、拉扎勒斯（认知评价）。"},
                {"t": "动机", "tag": "key",
                 "m": "需要与动机；马斯洛需要层次理论；内在动机与外在动机；成就动机（阿特金森）；耶克斯-多德森定律（中等动机水平效率最高，任务越难最佳动机越低）。"},
                {"t": "能力与智力", "tag": "key",
                 "m": "智力理论：斯皮尔曼二因素、瑟斯顿群因素、卡特尔流体/晶体智力、加德纳多元智能、斯滕伯格三元智力；IQ 与智力测验（比纳-西蒙、韦氏）。"},
                {"t": "人格", "tag": "key",
                 "m": "特质论：奥尔波特、卡特尔 16PF、大五人格（OCEAN）；精神分析：本我/自我/超我、防御机制；人本主义；人格测验：自陈量表（EPQ、MMPI）与投射测验（罗夏、TAT）。"},
                {"t": "学习心理", "tag": "key",
                 "m": "经典条件作用（巴甫洛夫：泛化、分化、消退）；操作条件作用（斯金纳：正/负强化、惩罚、消退）；观察学习（班杜拉：注意-保持-再现-动机）。"}
            ]},
            {"name": "发展心理学（林崇德）", "points": [
                {"t": "发展心理学概述与研究设计", "tag": "key",
                 "m": "研究设计：横断研究、纵向研究、聚合交叉研究；核心争论：遗传与环境、连续与阶段、早期经验与后期经验。"},
                {"t": "皮亚杰认知发展理论", "tag": "key",
                 "m": "核心概念：图式、同化、顺应、平衡化；四阶段：感知运动期(0-2)、前运算期(2-7)、具体运算期(7-11)、形式运算期(11岁以后)。"},
                {"t": "维果茨基社会文化理论", "tag": "key",
                 "m": "最近发展区（ZPD）、脚手架、社会中介与语言内化；强调文化与社会互动，对比皮亚杰的个体建构。"},
                {"t": "依恋理论", "tag": "key",
                 "m": "鲍尔比依恋理论；安斯沃斯陌生情境实验，依恋类型：安全型、回避型、矛盾型（反抗型）、混乱型。"},
                {"t": "埃里克森心理社会发展八阶段", "tag": "hard",
                 "m": "各阶段核心危机：信任对怀疑、自主对羞怯、主动对内疚、勤奋对自卑、同一性对角色混乱、亲密对孤独、繁殖对停滞、完善对绝望。"},
                {"t": "道德发展", "tag": "hard",
                 "m": "皮亚杰：从他律道德到自律道德；科尔伯格三水平六阶段（前习俗、习俗、后习俗），用道德两难故事测量。"},
                {"t": "青少年发展与自我同一性", "tag": "key",
                 "m": "青春期身心剧变；埃里克森的同一性任务；马西亚同一性四状态：同一性获得、延缓、早闭、扩散。"},
                {"t": "成年与老年心理发展", "tag": "easy",
                 "m": "卡特尔流体智力随年龄下降、晶体智力保持或上升；巴尔特斯毕生发展观（发展是一生的、多方向的、有可塑性）。"}
            ]},
            {"name": "心理与教育研究方法（董奇）", "points": [
                {"t": "研究的基本类型", "tag": "key",
                 "m": "定量研究与定性研究；实验研究、相关研究、描述研究（观察法、调查法、个案法）。相关不等于因果。"},
                {"t": "变量与操作定义", "tag": "key",
                 "m": "自变量、因变量、无关（额外）变量；操作定义把抽象概念转化为可测量、可操作的指标。"},
                {"t": "实验设计", "tag": "hard",
                 "m": "被试内设计、被试间设计、混合设计；控制额外变量：随机化、匹配、恒定法、平衡法（如 ABBA 抵消顺序效应）。"},
                {"t": "内部效度与外部效度", "tag": "hard",
                 "m": "内部效度威胁：历史、成熟、测验、工具、统计回归、被试流失、选择偏差；外部效度=结果的可推广性（总体、情境、时间）。"},
                {"t": "抽样方法", "tag": "key",
                 "m": "概率抽样：简单随机、分层、整群、系统抽样；非概率抽样：方便、目的、滚雪球抽样。"},
                {"t": "信度", "tag": "key",
                 "m": "信度=测量的一致性/稳定性：重测信度、复本信度、分半信度、同质性信度（克伦巴赫 α 系数）、评分者信度。"},
                {"t": "效度", "tag": "key",
                 "m": "效度=测量的准确性：内容效度、效标关联效度（预测效度/同时效度）、构念效度。信度是效度的必要而非充分条件。"},
                {"t": "心理测量与常用量表", "tag": "key",
                 "m": "标准化、常模、标准分数（Z、T）；常用量表：SCL-90、SDS（抑郁）、SAS（焦虑）、EPQ、MMPI、16PF、韦氏智力量表。"},
                {"t": "统计分析基础", "tag": "hard",
                 "m": "描述统计：集中趋势（均数/中数/众数）与离散趋势（方差/标准差）；推断统计：t 检验、方差分析（F）、相关与回归、卡方检验；显著性水平 α。"},
                {"t": "研究伦理", "tag": "easy",
                 "m": "知情同意、保密原则、最小伤害、避免欺骗（必要时事后说明 debriefing）、被试有随时退出的自由。"},
                {"t": "研究报告撰写", "tag": "easy",
                 "m": "遵循 APA 格式；IMRAD 结构：引言(Introduction)、方法(Method)、结果(Results)、讨论(Discussion)。"}
            ]}
        ]
    },
    "politics": {
        "name": "101 思想政治理论",
        "short": "政治",
        "icon": "📘",
        "chapters": [
            {"name": "马克思主义基本原理", "points": [
                {"t": "唯物论：物质与意识", "tag": "key",
                 "m": "物质决定意识，意识对物质具有能动的反作用；方法论：一切从实际出发、实事求是。"},
                {"t": "辩证法：对立统一规律", "tag": "hard",
                 "m": "矛盾是事物发展的动力与源泉；矛盾的普遍性与特殊性、同一性与斗争性；方法论：具体问题具体分析、两点论与重点论统一。"},
                {"t": "辩证法：三大规律", "tag": "key",
                 "m": "对立统一规律（实质与核心）、质量互变规律、否定之否定规律；五对基本范畴：原因与结果、必然与偶然、现象与本质、内容与形式、可能与现实。"},
                {"t": "认识论：实践与认识", "tag": "key",
                 "m": "实践是认识的基础，是认识的来源、动力、目的和检验真理的唯一标准；认识的两次飞跃：感性到理性、理性到实践。"},
                {"t": "唯物史观：社会存在与社会意识", "tag": "easy",
                 "m": "社会存在决定社会意识，社会意识具有相对独立性；生产力与生产关系、经济基础与上层建筑的矛盾运动推动社会发展。"}
            ]},
            {"name": "毛中特（毛泽东思想与中特理论）", "points": [
                {"t": "毛泽东思想活的灵魂", "tag": "key",
                 "m": "三个基本方面：实事求是、群众路线、独立自主。"},
                {"t": "新民主主义革命理论", "tag": "key",
                 "m": "革命的对象、动力、领导权与前途；三大法宝：统一战线、武装斗争、党的建设。"},
                {"t": "邓小平理论与社会主义本质", "tag": "key",
                 "m": "社会主义本质：解放生产力、发展生产力，消灭剥削、消除两极分化，最终达到共同富裕。"},
                {"t": "习近平新时代中国特色社会主义思想", "tag": "hard",
                 "m": "八个明确、十四个坚持；五位一体总体布局、四个全面战略布局；新发展理念（创新、协调、绿色、开放、共享）。"}
            ]},
            {"name": "中国近现代史纲要", "points": [
                {"t": "近代社会性质与两大历史任务", "tag": "key",
                 "m": "半殖民地半封建社会；两大任务：争取民族独立、人民解放，实现国家富强、人民幸福。"},
                {"t": "中国共产党的成立", "tag": "easy",
                 "m": "1919 五四运动是新民主主义革命开端；1921 中共一大成立；马克思主义与中国工人运动相结合。"},
                {"t": "新民主主义革命的胜利", "tag": "hard",
                 "m": "国共合作、土地革命、抗日战争、解放战争；重要节点：遵义会议、三大战役、七届二中全会。"},
                {"t": "社会主义改造", "tag": "key",
                 "m": "过渡时期总路线；对农业、手工业和资本主义工商业的社会主义改造（三大改造），确立社会主义基本制度。"}
            ]},
            {"name": "思想道德与法治", "points": [
                {"t": "理想信念与价值观", "tag": "easy",
                 "m": "个人价值与社会价值的统一；培育和践行社会主义核心价值观。"},
                {"t": "道德建设", "tag": "key",
                 "m": "社会公德、职业道德、家庭美德、个人品德；中华传统美德的创造性转化。"},
                {"t": "法治素养", "tag": "key",
                 "m": "宪法的地位与基本原则；公民的基本权利与义务；全面依法治国。"}
            ]}
        ]
    },
    "english": {
        "name": "204 英语（二）",
        "short": "英语",
        "icon": "📗",
        "chapters": [
            {"name": "词汇与语法基础", "points": [
                {"t": "考研核心词汇", "tag": "key",
                 "m": "约 5500 词；每天 100 词，先高频核心词再超纲词；按艾宾浩斯遗忘曲线循环复习，重视一词多义与熟词僻义。"},
                {"t": "长难句：三大从句", "tag": "hard",
                 "m": "定语从句、状语从句、名词性从句；先抓主干（主谓宾）再切分修饰成分，逐层翻译再整合。"},
                {"t": "长难句：非谓语与特殊结构", "tag": "hard",
                 "m": "非谓语动词 doing/done/to do 的作用；倒装、强调句、虚拟语气、插入语的识别。"}
            ]},
            {"name": "阅读理解（Part A）", "points": [
                {"t": "主旨大意题", "tag": "key",
                 "m": "关注首段、尾段及各段首句；警惕干扰项的以偏概全与过度推断。"},
                {"t": "细节理解题", "tag": "key",
                 "m": "回原文定位，识别同义替换；含 all / never / must 等绝对化词的选项通常为错误项。"},
                {"t": "推理判断题", "tag": "hard",
                 "m": "基于原文合理推断一步；与原文完全一致的直述内容一般不选（那属于细节题）。"},
                {"t": "词义猜测与观点态度题", "tag": "easy",
                 "m": "结合上下文逻辑关系推测词义；识别褒贬义词，判断作者的立场与情感倾向。"}
            ]},
            {"name": "完形填空与新题型", "points": [
                {"t": "完形填空：逻辑衔接", "tag": "hard",
                 "m": "先通读全文把握主线，再逐空填写；重点关注转折（but/yet）、因果（because/so）、并列（and/or）等逻辑关系。"},
                {"t": "新题型：信息匹配 / 小标题", "tag": "easy",
                 "m": "抓段落主题句（首句或末句），用关键词与选项匹配，注意同义改写。"}
            ]},
            {"name": "翻译与写作", "points": [
                {"t": "翻译：长句拆分", "tag": "hard",
                 "m": "遇到长句先拆分意群、分别翻译再重组，调整语序，保证中文通顺自然。"},
                {"t": "小作文：应用文", "tag": "key",
                 "m": "书信、通知、备忘录各背 1 个模板；注意称呼、正文、落款的格式规范。"},
                {"t": "大作文：图表 / 图画作文", "tag": "key",
                 "m": "三段式：描述现象/数据—分析原因或意义—总结建议；准备数据描述句式与高级替换词。"}
            ]}
        ]
    }
}

# ============================================================
# 三阶段复习计划（任务 id 保持不变以兼容已保存进度）
# ============================================================
PHASES = [
    {"id": "p1", "title": "第一阶段 · 基础夯实", "dates": "7月12日 - 8月31日", "tasks": [
        {"id": "p1_1", "name": "政治：完成马原、毛中特第一轮听课", "desc": "徐涛/腿姐强化班，同步做笔记"},
        {"id": "p1_2", "name": "政治：完成1000题马原部分", "desc": "每天30题，错题标记"},
        {"id": "p1_3", "name": "英语：考研核心词一轮背诵完成", "desc": "墨墨背单词/不背单词，每天100词"},
        {"id": "p1_4", "name": "英语：长难句分析训练", "desc": "田静/何凯文长难句，每天5句"},
        {"id": "p1_5", "name": "英语：2010-2014年阅读真题精做", "desc": "每篇精读，分析错题"},
        {"id": "p1_6", "name": "347：心理学导论通读完第一遍", "desc": "黄希庭版，做章节框架笔记"},
        {"id": "p1_7", "name": "347：发展心理学通读完第一遍", "desc": "林崇德版，做章节框架笔记"},
        {"id": "p1_8", "name": "347：心理与教育研究方法通读完第一遍", "desc": "董奇版，理解研究方法论"}
    ]},
    {"id": "p2", "title": "第二阶段 · 强化提升", "dates": "9月1日 - 10月31日", "tasks": [
        {"id": "p2_1", "name": "政治：完成史纲、思修、当代第一轮", "desc": "听课+1000题对应部分"},
        {"id": "p2_2", "name": "政治：1000题二刷错题", "desc": "重点关注一刷错题"},
        {"id": "p2_3", "name": "英语：考研核心词二轮巩固", "desc": "每天100词，重点记忆生词"},
        {"id": "p2_4", "name": "英语：2015-2019年阅读真题精做", "desc": "限时训练，每篇15-20分钟"},
        {"id": "p2_5", "name": "英语：完形+翻译+新题型专项训练", "desc": "每周各2篇"},
        {"id": "p2_6", "name": "347：三本教材二轮复习", "desc": "整理背诵笔记，建立知识体系"},
        {"id": "p2_7", "name": "347：核心知识点一轮背诵", "desc": "每天2章，利用艾宾浩斯表格"},
        {"id": "p2_8", "name": "347：收集历年347真题", "desc": "分析题型、考点分布"}
    ]},
    {"id": "p3", "title": "第三阶段 · 冲刺模考", "dates": "11月1日 - 12月考前", "tasks": [
        {"id": "p3_1", "name": "政治：肖秀荣八套卷选择题", "desc": "限时做，错题回归知识点"},
        {"id": "p3_2", "name": "政治：肖秀荣四套卷全真模拟", "desc": "大题背诵，每天2-3题"},
        {"id": "p3_3", "name": "政治：时政热点整理背诵", "desc": "关注年度重大事件"},
        {"id": "p3_4", "name": "英语：2020-2025年真题全真模拟", "desc": "严格计时，模拟考试环境"},
        {"id": "p3_5", "name": "英语：作文模板整理与背诵", "desc": "大作文+小作文各5篇模板"},
        {"id": "p3_6", "name": "347：二轮知识点背诵", "desc": "查漏补缺，重点突破薄弱章节"},
        {"id": "p3_7", "name": "347：全真模拟考试至少3次", "desc": "限时3小时，模拟答题卡"},
        {"id": "p3_8", "name": "347：三轮快速回顾", "desc": "框架式复习，保持状态"},
        {"id": "p3_9", "name": "全科：考前一周调整状态", "desc": "轻复习，调整作息"}
    ]}
]

QUOTES = [
    "🌸 每一页笔记，都是未来的底气。",
    "✨ 慢慢来，比较快。今天也在靠近梦想。",
    "🌿 你不必完美，只要今天比昨天多懂一点点。",
    "☕ 专注当下这一小时，就已经很棒了。",
    "🌷 稳稳地走，交大在等你。",
    "💪 别怕难，难的地方正是拉开差距的地方。",
    "🌈 状态会起伏，坚持的人最后都赢了。",
    "📖 心之所向，素履以往。"
]

# ============================================================
# 页面模板（CSS 内联；__SCRIPT__ 由脚本注入）
# ============================================================
HTML = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<meta name="theme-color" content="#F4A6C0">
<title>应用心理硕士 · 备考学习系统</title>
<link rel="manifest" href="manifest.json">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
--rose:#E76A97;--rose-light:#F4A6C0;--rose-bg:#FDEFF4;
--lav:#A98BE0;--lav-bg:#F1EAFB;
--mint:#3FC6AE;--cream:#FFF9FB;
--ink:#463A47;--muted:#9C93A6;--line:#F3E5EE;
--warn:#F0A020;--danger:#F2718C;
}
body{font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",sans-serif;background:var(--cream);color:var(--ink);line-height:1.6;padding-bottom:40px;-webkit-tap-highlight-color:transparent}
.app-header{background:linear-gradient(135deg,#F4A6C0 0%,#C9A7EB 100%);color:#fff;padding:22px 18px 18px;border-radius:0 0 22px 22px;box-shadow:0 6px 20px rgba(201,167,235,0.35)}
.app-header h1{font-size:19px;font-weight:800;letter-spacing:.5px}
.app-header .subtitle{font-size:12px;opacity:.92;margin-top:4px}
.app-header .countdown{margin-top:12px;background:rgba(255,255,255,0.22);border-radius:12px;padding:8px 14px;font-size:14px;display:flex;align-items:center;gap:6px}
.app-header .countdown strong{font-size:20px}
.app-header .quote{margin-top:8px;font-size:12px;opacity:.95}
.tab-bar{display:flex;gap:8px;overflow-x:auto;background:#fff;padding:10px 12px;position:sticky;top:0;z-index:9;box-shadow:0 2px 10px rgba(231,106,151,0.06);scrollbar-width:none;-ms-overflow-style:none}
.tab-bar::-webkit-scrollbar{display:none}
.tab-btn{flex:0 0 auto;padding:8px 16px;font-size:14px;font-weight:600;color:var(--muted);background:var(--rose-bg);border:none;border-radius:999px;cursor:pointer;transition:all .2s;white-space:nowrap}
.tab-btn.active{color:#fff;background:linear-gradient(135deg,var(--rose-light),var(--lav));box-shadow:0 4px 12px rgba(233,106,151,0.3)}
.content{padding:16px;max-width:640px;margin:0 auto}
.section{display:none;animation:fade .35s ease}
.section.active{display:block}
@keyframes fade{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}
.card{background:#fff;border-radius:18px;box-shadow:0 6px 20px rgba(231,106,151,0.08);padding:16px;margin-bottom:14px}
.card-title{font-size:15px;font-weight:700;color:var(--ink);margin-bottom:10px;display:flex;align-items:center;gap:6px}
.badge{display:inline-block;font-size:11px;font-weight:600;padding:2px 9px;border-radius:10px;margin-left:6px}
.badge-blue{background:var(--lav-bg);color:var(--lav)}
.badge-green{background:#DEF7EF;color:#1F9D82}
.badge-yellow{background:#FEF1D6;color:#B07A11}
.badge-red{background:#FCE4EC;color:#C24A6B}
.progress-bar{height:8px;background:var(--rose-bg);border-radius:6px;margin:8px 0;overflow:hidden}
.progress-fill{height:100%;border-radius:6px;transition:width .6s ease;background:linear-gradient(90deg,var(--rose-light),var(--lav))}
.progress-text{font-size:13px;color:var(--muted)}
.stats-row{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:16px}
.stat-box{background:#fff;border-radius:16px;box-shadow:0 6px 18px rgba(231,106,151,0.08);padding:14px 10px;text-align:center}
.stat-num{font-size:24px;font-weight:800;background:linear-gradient(135deg,var(--rose),var(--lav));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.stat-label{font-size:12px;color:var(--muted);margin-top:2px}
.task-item{display:flex;align-items:flex-start;gap:10px;padding:11px 0;border-bottom:1px solid var(--line)}
.task-item:last-child{border-bottom:none}
.task-check{width:22px;height:22px;border:2px solid var(--rose-light);border-radius:50%;flex-shrink:0;cursor:pointer;margin-top:2px;display:flex;align-items:center;justify-content:center;transition:all .2s}
.task-check.done{background:linear-gradient(135deg,var(--rose-light),var(--lav));border-color:transparent;color:#fff;font-size:13px;font-weight:bold}
.task-info{flex:1}
.task-name{font-size:14px;color:var(--ink)}
.task-name.done{text-decoration:line-through;color:var(--muted)}
.task-desc{font-size:12px;color:var(--muted);margin-top:2px}
.phase-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:10px}
.phase-title{font-size:16px;font-weight:800;color:var(--ink)}
.phase-dates{font-size:12px;color:var(--muted)}
.btn{border:none;border-radius:12px;cursor:pointer;font-family:inherit;font-weight:600}
.btn-primary{background:linear-gradient(135deg,var(--rose-light),var(--lav));color:#fff;padding:11px 22px;font-size:14px;box-shadow:0 4px 12px rgba(233,106,151,0.28)}
.btn-ghost{background:var(--rose-bg);color:var(--rose);padding:8px 16px;font-size:13px}
.btn-reset{display:block;width:100%;padding:11px;background:var(--rose-bg);border:none;border-radius:12px;color:var(--muted);font-size:13px;cursor:pointer;margin-top:6px;font-family:inherit}
.notes-area{width:100%;border:1px solid var(--line);border-radius:12px;padding:11px;font-size:13px;font-family:inherit;resize:vertical;min-height:64px;margin-top:8px;outline:none;background:var(--cream)}
.notes-area:focus{border-color:var(--rose-light)}
.info-box{background:linear-gradient(135deg,var(--rose-bg),var(--lav-bg));border-radius:16px;padding:14px;margin-bottom:14px;font-size:13px;line-height:1.9}
.info-box strong{color:var(--rose)}
.resource-list{list-style:none}
.resource-list li{padding:10px 0;border-bottom:1px solid var(--line);font-size:14px}
.resource-list li:last-child{border-bottom:none}
.resource-list .book-title{font-weight:600}
.resource-list .book-author{color:var(--muted);font-size:13px}
.review-date{font-size:13px;color:var(--muted);margin-bottom:10px;padding-bottom:8px;border-bottom:1px solid var(--line)}
.review-item{padding:9px 0;display:flex;justify-content:space-between;align-items:center}
.review-rating span{transition:transform .15s}
.review-rating span:active{transform:scale(1.25)}
.search-box{width:100%;padding:11px 14px;border:1px solid var(--line);border-radius:12px;font-size:14px;font-family:inherit;outline:none;margin-bottom:12px;background:#fff}
.search-box:focus{border-color:var(--rose-light)}
.mastery-star{cursor:pointer;color:#E7DDE5;transition:color .2s;font-size:16px}
.mastery-star.active{color:var(--warn)}
.save-indicator{position:fixed;bottom:20px;left:50%;transform:translateX(-50%);background:var(--ink);color:#fff;padding:9px 18px;border-radius:20px;font-size:13px;opacity:0;transition:opacity .3s;z-index:200;pointer-events:none}
.save-indicator.show{opacity:.92}
/* 知识点速查（列表） */
.kb-subject{margin-bottom:14px}
.kb-subject-head{background:linear-gradient(135deg,var(--rose-light),var(--lav));color:#fff;padding:12px 16px;border-radius:14px;font-size:15px;font-weight:700;cursor:pointer;display:flex;justify-content:space-between;align-items:center}
.kb-chapter{border:1px solid var(--line);border-radius:12px;margin:8px 0 8px 10px;overflow:hidden}
.kb-chapter-head{background:var(--rose-bg);padding:10px 14px;font-size:13px;font-weight:700;cursor:pointer;display:flex;justify-content:space-between;align-items:center;color:var(--ink)}
.kb-body{padding:8px 12px;display:none}
.kb-body.open{display:block}
.kb-point{background:var(--cream);border-left:3px solid var(--rose-light);padding:10px 12px;margin-bottom:8px;border-radius:0 10px 10px 0}
.kb-point-title{font-size:13px;font-weight:700;color:var(--ink);margin-bottom:4px}
.kb-point-method{font-size:12px;color:#6E6472;line-height:1.75}
.arrow{transition:transform .3s;font-size:12px}
.arrow.open{transform:rotate(90deg)}
.k-tag{display:inline-block;font-size:11px;padding:1px 8px;border-radius:10px;margin-left:4px}
.k-tag-key{background:#FEF1D6;color:#B07A11}
.k-tag-hard{background:#FCE4EC;color:#C24A6B}
.k-tag-easy{background:#DEF7EF;color:#1F9D82}
/* 思维导图 */
.mm-toolbar{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-bottom:10px}
.mm-sbtn{padding:7px 14px;border:none;border-radius:999px;font-size:13px;font-weight:600;font-family:inherit;background:var(--rose-bg);color:var(--muted);cursor:pointer}
.mm-sbtn.active{background:linear-gradient(135deg,var(--rose-light),var(--lav));color:#fff}
.mm-zoom{margin-left:auto;display:flex;gap:6px}
.mm-zbtn{width:34px;height:34px;border:none;border-radius:10px;background:var(--rose-bg);color:var(--rose);font-size:18px;cursor:pointer;font-weight:700}
.mm-hint{font-size:11px;color:var(--muted);margin-bottom:8px}
.mm-wrap{border:1px solid var(--line);border-radius:16px;background:radial-gradient(circle at 1px 1px,rgba(201,167,235,0.18) 1px,transparent 0);background-size:22px 22px;background-color:#fff;overflow:auto;height:64vh;-webkit-overflow-scrolling:touch;position:relative}
.mm-node{box-sizing:border-box;height:100%;width:100%;display:flex;align-items:center;justify-content:center;text-align:center;font-size:12px;line-height:1.25;padding:4px 8px;border-radius:12px;overflow:hidden;cursor:pointer;font-weight:600}
.mm-root{background:linear-gradient(135deg,var(--rose),var(--lav));color:#fff;font-size:14px;font-weight:800;box-shadow:0 4px 12px rgba(233,106,151,0.4)}
.mm-chapter{background:linear-gradient(135deg,var(--rose-light),#D8B4F0);color:#fff;box-shadow:0 3px 8px rgba(201,167,235,0.35)}
.mm-point{background:#fff;color:var(--ink);border:1.5px solid var(--rose-light);box-shadow:0 2px 6px rgba(231,106,151,0.12);font-weight:500}
.mm-point.mastered{border-color:var(--mint);background:#F2FBF8}
.mm-point.tag-hard{border-color:var(--danger)}
.sheet{position:fixed;left:0;right:0;bottom:0;background:#fff;border-radius:20px 20px 0 0;box-shadow:0 -8px 30px rgba(70,58,71,0.18);padding:18px 18px 26px;z-index:150;transform:translateY(110%);transition:transform .3s ease;max-height:70vh;overflow:auto}
.sheet.show{transform:translateY(0)}
.sheet-head{display:flex;justify-content:space-between;align-items:center;margin-bottom:8px}
.sheet-close{cursor:pointer;color:var(--muted);font-size:18px;padding:4px 8px}
.sheet-title{font-size:16px;font-weight:800;margin-bottom:8px}
.sheet-body{font-size:14px;color:#5B5160;line-height:1.85}
.sheet-master{margin-top:14px;font-size:13px;color:var(--muted);display:flex;align-items:center;gap:8px}
.sheet-master .mastery-star{font-size:22px}
/* 卡片 */
.fc-filters{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-bottom:12px}
.fc-scene{perspective:1400px;margin:4px 0 14px}
.fc{position:relative;width:100%;height:270px;transform-style:preserve-3d;transition:transform .55s;cursor:pointer}
.fc.flipped{transform:rotateY(180deg)}
.fc-face{position:absolute;inset:0;backface-visibility:hidden;-webkit-backface-visibility:hidden;border-radius:20px;padding:24px;display:flex;flex-direction:column;justify-content:center;box-shadow:0 10px 30px rgba(231,106,151,0.16)}
.fc-front{background:linear-gradient(135deg,var(--rose-light),var(--lav));color:#fff}
.fc-front .fc-q{font-size:20px;font-weight:800;text-align:center;line-height:1.5}
.fc-front .fc-sub{position:absolute;top:16px;left:18px;font-size:12px;opacity:.9}
.fc-front .fc-tip{position:absolute;bottom:16px;left:0;right:0;text-align:center;font-size:12px;opacity:.85}
.fc-back{background:#fff;color:var(--ink);transform:rotateY(180deg);overflow:auto;justify-content:flex-start}
.fc-back .fc-a-title{font-size:15px;font-weight:800;margin-bottom:8px;color:var(--rose)}
.fc-back .fc-a{font-size:14px;line-height:1.85;color:#5B5160}
.fc-rate{display:flex;gap:10px;margin-top:6px}
.fc-rate button{flex:1;padding:13px 0;font-size:14px}
.fc-forgot{background:#FCE4EC;color:#C24A6B}
.fc-vague{background:#FEF1D6;color:#B07A11}
.fc-known{background:#DEF7EF;color:#1F9D82}
.fc-progress{text-align:center;font-size:13px;color:var(--muted);margin-bottom:10px}
.fc-empty{text-align:center;padding:40px 10px;color:var(--muted)}
.fc-done{text-align:center;padding:30px 10px}
.fc-done .big{font-size:40px}
select.fc-select{padding:8px 12px;border:1px solid var(--line);border-radius:10px;font-family:inherit;font-size:13px;background:#fff;color:var(--ink);outline:none}
.toggle-weak{display:flex;align-items:center;gap:6px;font-size:13px;color:var(--muted);cursor:pointer}
.empty-tip{text-align:center;padding:40px;color:var(--muted)}
</style>
</head>
<body>
<div class="app-header">
<h1>🌸 应用心理硕士 · 备考系统</h1>
<div class="subtitle">西南交通大学 · 045400 应用心理（全日制 / 非全日制）</div>
<div class="countdown" id="countdown">距 2026 考研还有 <strong id="daysLeft">--</strong> 天</div>
<div class="quote" id="quote"></div>
</div>
<div class="tab-bar">
<button class="tab-btn active" data-tab="plan">📋 计划</button>
<button class="tab-btn" data-tab="mind">🧠 导图</button>
<button class="tab-btn" data-tab="cards">🎴 卡片</button>
<button class="tab-btn" data-tab="review">🌱 回顾</button>
<button class="tab-btn" data-tab="info">📖 资料</button>
</div>
<div class="content">

<div class="section active" id="tab-plan">
<div class="stats-row">
<div class="stat-box"><div class="stat-num" id="statTotal">0</div><div class="stat-label">总任务</div></div>
<div class="stat-box"><div class="stat-num" id="statDone">0</div><div class="stat-label">已完成</div></div>
<div class="stat-box"><div class="stat-num" id="statPct">0%</div><div class="stat-label">完成率</div></div>
</div>
<div id="planContent"></div>
<button class="btn-reset" onclick="resetAll()">重置所有任务进度</button>
</div>

<div class="section" id="tab-mind">
<div class="mm-toolbar" id="mmSubjects"></div>
<div class="mm-toolbar">
<button class="mm-sbtn" onclick="mmExpandAll(true)">展开全部</button>
<button class="mm-sbtn" onclick="mmExpandAll(false)">收起知识点</button>
<div class="mm-zoom">
<button class="mm-zbtn" onclick="mmZoom(-1)">－</button>
<button class="mm-zbtn" onclick="mmZoom(1)">＋</button>
</div>
</div>
<div class="mm-hint">💡 点章节可展开/收起 · 点知识点看详情 · 拖动可平移 · ＋/－ 缩放</div>
<div class="mm-wrap" id="mmCanvas"></div>
</div>

<div class="section" id="tab-cards">
<div class="fc-filters">
<select class="fc-select" id="cardSubject" onchange="onCardFilter()">
<option value="all">全部科目</option>
<option value="psych347">347 心理学</option>
<option value="politics">政治</option>
<option value="english">英语</option>
</select>
<label class="toggle-weak"><input type="checkbox" id="cardWeak" onchange="onCardFilter()"> 只看未掌握</label>
<button class="btn btn-ghost" onclick="startCards()">重新开始</button>
</div>
<div class="fc-progress" id="cardProgress"></div>
<div id="cardArea"></div>
</div>

<div class="section" id="tab-review">
<div class="card"><div class="card-title">📊 总体进度</div>
<div style="display:flex;align-items:center;gap:12px"><div style="flex:1"><div class="progress-bar"><div class="progress-fill" id="overallBar" style="width:0%"></div></div></div><span class="progress-text" id="overallPct">0%</span></div>
<div id="phaseProgressCards" style="margin-top:6px"></div>
<div style="margin-top:6px;font-size:13px;color:var(--muted)">🎴 知识掌握：<span id="masteryStat">0 / 0</span></div>
</div>
<div class="card"><div class="card-title">🌱 每日回顾</div><div class="review-date" id="todayDate"></div><div id="dailyReview"></div></div>
<div class="card"><div class="card-title">📈 本周复习</div><div id="weekStats"></div></div>
<div class="card"><div class="card-title">📝 备考笔记</div><textarea class="notes-area" id="notesArea" placeholder="记录学习心得、重点难点、疑问..."></textarea></div>
</div>

<div class="section" id="tab-info">
<div class="info-box"><strong>西南交通大学 · 心理研究与咨询中心</strong><br>专业代码：<strong>045400 应用心理</strong><br>全日制 27 人（含推免 3 人）｜ 非全日制 20 人</div>
<div class="card"><div class="card-title">📝 考试科目</div><ul class="resource-list">
<li><span class="book-title">101 思想政治理论</span><br><span class="book-author">全国统考 · 满分 100 分</span></li>
<li><span class="book-title">204 英语（二）</span><br><span class="book-author">全国统考 · 满分 100 分</span></li>
<li><span class="book-title">347 心理学专业综合</span><br><span class="book-author">学校自命题 · 满分 300 分</span></li>
</ul></div>
<div class="card"><div class="card-title">📚 347 参考书目</div><ul class="resource-list">
<li><span class="book-title">《心理学导论》第三版</span><br><span class="book-author">黄希庭 著，人民教育出版社</span></li>
<li><span class="book-title">《发展心理学》第三版</span><br><span class="book-author">林崇德 著，人民教育出版社</span></li>
<li><span class="book-title">《心理与教育研究方法》</span><br><span class="book-author">董奇 著，北京师范大学出版社</span></li>
</ul></div>
<div class="card"><div class="card-title">🔍 知识点速查</div>
<input class="search-box" id="kbSearch" placeholder="🔍 搜索知识点关键词..." oninput="renderKb()">
<div id="kbList"></div>
</div>
<div class="card"><div class="card-title">🔗 重要链接</div><ul class="resource-list">
<li><a href="https://yz.swjtu.edu.cn" target="_blank" style="color:var(--rose);text-decoration:none">西南交大研究生招生网</a></li>
<li><a href="https://yz.chsi.com.cn" target="_blank" style="color:var(--rose);text-decoration:none">中国研究生招生信息网</a></li>
</ul></div>
</div>

</div>
<div class="sheet" id="mmDetail"></div>
<div class="save-indicator" id="saveIndicator">已自动保存 🌸</div>
__SCRIPT__
</body></html>'''

JS = r'''<script>
var KNOWLEDGE = __KNOWLEDGE__;
var PHASES = __PHASES__;
var QUOTES = __QUOTES__;
var SUBJECT_ORDER = ["psych347","politics","english"];

var state = null;

function mkey(sk,ci,pi){ return sk + "_" + ci + "_" + pi; }

function getDefaultState(){
  var s = {tasks:{}, notes:"", reviews:[], knowledge:{}, cards:{}};
  PHASES.forEach(function(p){ p.tasks.forEach(function(t){ s.tasks[t.id]=false; }); });
  return s;
}

function loadState(){
  try{
    var raw = localStorage.getItem("psych_study_state");
    if(raw){
      var p = JSON.parse(raw);
      p.tasks = p.tasks || {};
      p.knowledge = p.knowledge || {};
      p.cards = p.cards || {};
      p.reviews = p.reviews || [];
      if(typeof p.notes !== "string") p.notes = "";
      PHASES.forEach(function(ph){ ph.tasks.forEach(function(t){ if(p.tasks[t.id]===undefined) p.tasks[t.id]=false; }); });
      return p;
    }
  }catch(e){}
  return getDefaultState();
}

function saveState(){
  localStorage.setItem("psych_study_state", JSON.stringify(state));
  var el = document.getElementById("saveIndicator");
  el.classList.add("show");
  clearTimeout(el._t);
  el._t = setTimeout(function(){ el.classList.remove("show"); }, 1400);
}

function todayKey(){ return new Date().toISOString().split("T")[0]; }
function getReview(key){
  for(var i=0;i<state.reviews.length;i++){ if(state.reviews[i].date===key) return state.reviews[i]; }
  return null;
}
function ensureReview(key){
  var r = getReview(key);
  if(!r){ r = {date:key, politics:0, english:0, psych347:0, hours:0, summary:""}; state.reviews.push(r); }
  return r;
}

function updateCountdown(){
  var exam = new Date(2026, 11, 21);
  var diff = Math.ceil((exam - new Date())/(1000*60*60*24));
  document.getElementById("daysLeft").textContent = diff>0 ? diff : "已开考";
}

/* ---------------- 复习计划 ---------------- */
function toggleTask(id){
  state.tasks[id] = !state.tasks[id];
  saveState(); renderPlan();
}
function renderPlan(){
  var total=0, done=0, html="";
  PHASES.forEach(function(p){
    var phaseDone=0, tasksHtml="";
    p.tasks.forEach(function(t){
      total++;
      var isDone = !!state.tasks[t.id];
      if(isDone){ done++; phaseDone++; }
      tasksHtml += `<div class="task-item"><div class="task-check${isDone?' done':''}" onclick="toggleTask('${t.id}')">${isDone?'✓':''}</div>`
        + `<div class="task-info"><div class="task-name${isDone?' done':''}">${t.name}</div><div class="task-desc">${t.desc}</div></div></div>`;
    });
    var pct = p.tasks.length ? Math.round(phaseDone/p.tasks.length*100) : 0;
    var badge = pct===100?'badge-green':(pct>50?'badge-blue':(pct>0?'badge-yellow':'badge-red'));
    html += `<div class="card"><div class="phase-header"><div><div class="phase-title">${p.title}</div><div class="phase-dates">${p.dates}</div></div><span class="badge ${badge}">${pct}%</span></div>`
      + `<div class="progress-bar"><div class="progress-fill" style="width:${pct}%"></div></div>${tasksHtml}</div>`;
  });
  document.getElementById("planContent").innerHTML = html;
  document.getElementById("statTotal").textContent = total;
  document.getElementById("statDone").textContent = done;
  document.getElementById("statPct").textContent = total ? Math.round(done/total*100)+"%" : "0%";
}
function resetAll(){
  if(confirm("确定重置所有任务进度吗？（每日回顾、卡片掌握度会保留）")){
    PHASES.forEach(function(p){ p.tasks.forEach(function(t){ state.tasks[t.id]=false; }); });
    saveState(); renderPlan(); renderProgress();
  }
}

/* ---------------- 进度 + 回顾 ---------------- */
function calcOverall(){
  var total=0, done=0;
  PHASES.forEach(function(p){ p.tasks.forEach(function(t){ total++; if(state.tasks[t.id]) done++; }); });
  return total ? Math.round(done/total*100) : 0;
}
function masteryCount(){
  var total=0, got=0;
  SUBJECT_ORDER.forEach(function(sk){
    KNOWLEDGE[sk].chapters.forEach(function(ch,ci){
      ch.points.forEach(function(pt,pi){ total++; if((state.knowledge[mkey(sk,ci,pi)]||0)>=3) got++; });
    });
  });
  return {total:total, got:got};
}
function renderProgress(){
  var pct = calcOverall();
  document.getElementById("overallBar").style.width = pct+"%";
  document.getElementById("overallPct").textContent = pct+"%";
  var html="";
  PHASES.forEach(function(p){
    var d=0; p.tasks.forEach(function(t){ if(state.tasks[t.id]) d++; });
    var pp = p.tasks.length ? Math.round(d/p.tasks.length*100) : 0;
    html += `<div style="margin-bottom:10px"><div style="display:flex;justify-content:space-between;font-size:13px;margin-bottom:4px"><span>${p.title}</span><span style="font-weight:700">${d}/${p.tasks.length}</span></div><div class="progress-bar"><div class="progress-fill" style="width:${pp}%"></div></div></div>`;
  });
  document.getElementById("phaseProgressCards").innerHTML = html;
  var mc = masteryCount();
  document.getElementById("masteryStat").textContent = mc.got + " / " + mc.total;
  document.getElementById("notesArea").value = state.notes || "";
}
function renderReview(){
  var today = new Date();
  document.getElementById("todayDate").textContent = "📌 " + today.toLocaleDateString("zh-CN",{year:"numeric",month:"long",day:"numeric",weekday:"long"});
  var subjects = [{id:"politics",name:"思想政治"},{id:"english",name:"英语（二）"},{id:"psych347",name:"347 心理学"}];
  var key = todayKey();
  var r = getReview(key);
  var emojis = ["😞","😐","🙂","😊"];
  var html = `<div style="font-size:13px;color:var(--muted);margin-bottom:8px">今天各科学习状态</div>`;
  subjects.forEach(function(sub){
    var val = r ? (r[sub.id]||0) : 0;
    var stars="";
    for(var j=0;j<emojis.length;j++){
      stars += `<span style="font-size:22px;cursor:pointer;opacity:${val===j+1?'1':'0.3'}" onclick="setRating('${sub.id}',${j+1})">${emojis[j]}</span>`;
    }
    html += `<div class="review-item"><span style="font-size:14px">${sub.name}</span><div class="review-rating">${stars}</div></div>`;
  });
  var hours = r ? (r.hours||0) : 0;
  html += `<div class="review-item"><span style="font-size:14px">今日学习时长</span><div style="display:flex;align-items:center;gap:8px">`
    + `<button class="mm-zbtn" onclick="adjHours(-0.5)">－</button><span style="font-size:16px;font-weight:700;min-width:46px;text-align:center">${hours}h</span>`
    + `<button class="mm-zbtn" onclick="adjHours(0.5)">＋</button></div></div>`;
  var summary = r ? (r.summary||"") : "";
  html += `<div style="margin-top:12px"><div style="font-size:13px;color:var(--muted);margin-bottom:4px">今日学习小结</div>`
    + `<textarea class="notes-area" id="dailyNotes" style="min-height:52px" placeholder="今天学了什么？有什么收获？">${summary}</textarea></div>`
    + `<button class="btn btn-primary" style="margin-top:10px" onclick="saveDailyReview()">保存今日回顾</button>`;
  document.getElementById("dailyReview").innerHTML = html;
  renderWeekStats();
  renderProgress();
}
function setRating(subject, rating){
  var r = ensureReview(todayKey());
  r[subject] = rating;
  saveState(); renderReview();
}
function adjHours(delta){
  var r = ensureReview(todayKey());
  r.hours = Math.max(0, Math.round((r.hours+delta)*10)/10);
  saveState(); renderReview();
}
function saveDailyReview(){
  var r = ensureReview(todayKey());
  var el = document.getElementById("dailyNotes");
  if(el) r.summary = el.value;
  saveState();
}
function renderWeekStats(){
  var data=[], today=new Date();
  for(var i=6;i>=0;i--){
    var d=new Date(today); d.setDate(d.getDate()-i);
    var key=d.toISOString().split("T")[0];
    var r=getReview(key);
    data.push({day:d.toLocaleDateString("zh-CN",{weekday:"short"}), hours:r?(r.hours||0):0, status:r?[r.politics,r.english,r.psych347].filter(Boolean).length:0});
  }
  var html = `<div style="display:flex;gap:4px;justify-content:space-between">`;
  var totalHours=0;
  data.forEach(function(d){
    totalHours += d.hours;
    var barH = Math.min(d.hours/8*100,100);
    html += `<div style="flex:1;text-align:center"><div style="font-size:11px;color:var(--muted)">${d.day}</div>`
      + `<div style="margin:4px 0;height:44px;background:var(--rose-bg);border-radius:6px;position:relative;overflow:hidden">`
      + `<div style="position:absolute;bottom:0;width:100%;border-radius:6px;height:${barH}%;background:linear-gradient(180deg,var(--lav),var(--rose-light))"></div></div>`
      + `<div style="font-size:12px;font-weight:700">${d.hours}h</div><div style="font-size:10px;color:var(--muted)">${d.status}/3科</div></div>`;
  });
  html += `</div><div style="font-size:12px;color:var(--muted);margin-top:8px;text-align:center">本周总学习：${totalHours}h</div>`;
  document.getElementById("weekStats").innerHTML = html;
}

/* ---------------- 思维导图 ---------------- */
var mmSubject = "psych347";
var mmScale = 1;
var mmCollapsed = {};
var GAPX = 46, GAPY = 12;
var W_ROOT=100, W_CH=150, W_PT=210, H_ROOT=56, H_CH=50, H_PT=48;
var _cursor=0, _maxX=0;

function renderMmSubjects(){
  var html="";
  SUBJECT_ORDER.forEach(function(sk){
    html += `<button class="mm-sbtn${sk===mmSubject?' active':''}" onclick="mmSelect('${sk}')">${KNOWLEDGE[sk].icon} ${KNOWLEDGE[sk].short}</button>`;
  });
  document.getElementById("mmSubjects").innerHTML = html;
}
function mmSelect(sk){ mmSubject=sk; renderMmSubjects(); renderMind(); }
function mmZoom(dir){ mmScale = Math.min(1.8, Math.max(0.5, Math.round((mmScale + dir*0.15)*100)/100)); renderMind(); }
function mmToggle(sk,ci){ var k=sk+"_"+ci; mmCollapsed[k]=(mmCollapsed[k]===false); renderMind(); }
function mmExpandAll(open){
  KNOWLEDGE[mmSubject].chapters.forEach(function(ch,ci){ mmCollapsed[mmSubject+"_"+ci] = !open; });
  renderMind();
}
function buildTree(sk){
  var sd = KNOWLEDGE[sk];
  var root = {type:"root", label:sd.short, w:W_ROOT, h:H_ROOT, children:[]};
  sd.chapters.forEach(function(ch,ci){
    var chNode = {type:"chapter", label:ch.name, w:W_CH, h:H_CH, ci:ci, collapsed:(mmCollapsed[sk+"_"+ci] !== false), children:[]};
    ch.points.forEach(function(pt,pi){
      chNode.children.push({type:"point", label:pt.t, w:W_PT, h:H_PT, ci:ci, pi:pi, tag:pt.tag});
    });
    root.children.push(chNode);
  });
  return root;
}
function assignY(node){
  var kids = node.collapsed ? [] : (node.children||[]);
  if(kids.length===0){ node.y = _cursor + node.h/2; _cursor += node.h + GAPY; }
  else { kids.forEach(assignY); node.y = (kids[0].y + kids[kids.length-1].y)/2; }
}
function assignX(node){
  if(node.type==="root") node.x = 16;
  else if(node.type==="chapter") node.x = 16 + W_ROOT + GAPX;
  else node.x = 16 + W_ROOT + GAPX + W_CH + GAPX;
  _maxX = Math.max(_maxX, node.x + node.w);
  (node.collapsed?[]:(node.children||[])).forEach(assignX);
}
function conn(p,c){
  var x1=p.x+p.w, y1=p.y, x2=c.x, y2=c.y, mx=(x1+x2)/2;
  return `M${x1},${y1} C${mx},${y1} ${mx},${y2} ${x2},${y2}`;
}
function renderMind(){
  var sk = mmSubject;
  var root = buildTree(sk);
  _cursor = 16; _maxX = 0;
  assignY(root); assignX(root);
  var W = _maxX + 16, H = _cursor + 8;
  var paths="", nodes="";
  function walk(node){
    var kids = node.collapsed ? [] : (node.children||[]);
    kids.forEach(function(c){ paths += `<path d="${conn(node,c)}" fill="none" stroke="#E7B7CF" stroke-width="2" opacity="0.7"/>`; walk(c); });
  }
  walk(root);
  function drawNode(node){
    var cls="mm-root", click="", label=node.label, arrow="";
    if(node.type==="chapter"){
      cls="mm-chapter";
      click = `onclick="mmToggle('${sk}',${node.ci})"`;
      arrow = node.collapsed ? " ▸" : " ▾";
    } else if(node.type==="point"){
      cls = "mm-point tag-" + node.tag;
      var m = state.knowledge[mkey(sk,node.ci,node.pi)]||0;
      if(m>=3){ cls += " mastered"; label = "✅ " + label; }
      click = `onclick="mmShowPoint('${sk}',${node.ci},${node.pi})"`;
    }
    nodes += `<foreignObject x="${node.x}" y="${node.y-node.h/2}" width="${node.w}" height="${node.h}">`
      + `<div xmlns="http://www.w3.org/1999/xhtml" class="mm-node ${cls}" ${click}>${label}${arrow}</div></foreignObject>`;
    (node.collapsed?[]:(node.children||[])).forEach(drawNode);
  }
  drawNode(root);
  var svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" width="${Math.round(W*mmScale)}" height="${Math.round(H*mmScale)}" style="display:block">${paths}${nodes}</svg>`;
  document.getElementById("mmCanvas").innerHTML = svg;
}
function mmShowPoint(sk,ci,pi){
  var pt = KNOWLEDGE[sk].chapters[ci].points[pi];
  var tagMap = {key:'<span class="k-tag k-tag-key">⭐ 重点</span>', hard:'<span class="k-tag k-tag-hard">🔥 难点</span>', easy:'<span class="k-tag k-tag-easy">✅ 了解</span>'};
  var el = document.getElementById("mmDetail");
  el.innerHTML = `<div class="sheet-head"><div style="font-size:12px;color:var(--muted)">${KNOWLEDGE[sk].chapters[ci].name}</div><span class="sheet-close" onclick="hideSheet()">✕</span></div>`
    + `<div class="sheet-title">${pt.t} ${tagMap[pt.tag]||''}</div>`
    + `<div class="sheet-body">${pt.m}</div>`
    + `<div class="sheet-master">掌握程度：<span id="sheetStars"></span></div>`;
  renderSheetStars(sk,ci,pi);
  el.classList.add("show");
}
function renderSheetStars(sk,ci,pi){
  var key = mkey(sk,ci,pi);
  var m = state.knowledge[key]||0;
  var html="";
  for(var s=1;s<=3;s++){ html += `<span class="mastery-star${s<=m?' active':''}" onclick="setMastery('${key}',${s},true)">★</span>`; }
  var el = document.getElementById("sheetStars");
  if(el) el.innerHTML = html;
}
function hideSheet(){ document.getElementById("mmDetail").classList.remove("show"); }
function setMastery(key, level, fromSheet){
  state.knowledge[key] = (state.knowledge[key]===level) ? 0 : level;
  saveState();
  if(fromSheet){ var p=key.split("_"); renderSheetStars(p[0], parseInt(p[1]), parseInt(p[2])); renderMind(); }
}

/* 拖动平移 */
function initMmDrag(){
  var wrap = document.getElementById("mmCanvas");
  var down=false, sx, sy, sl, st;
  wrap.addEventListener("mousedown", function(e){
    if(e.target.closest(".mm-node")) return;
    down=true; sx=e.clientX; sy=e.clientY; sl=wrap.scrollLeft; st=wrap.scrollTop; e.preventDefault();
  });
  window.addEventListener("mousemove", function(e){
    if(!down) return;
    wrap.scrollLeft = sl-(e.clientX-sx); wrap.scrollTop = st-(e.clientY-sy);
  });
  window.addEventListener("mouseup", function(){ down=false; });
}

/* ---------------- 卡片自测 ---------------- */
var cardQueue=[], cardIdx=0, cardFlipped=false, cardSessionDone=0;
function buildCardPool(){
  var subj = document.getElementById("cardSubject").value;
  var onlyWeak = document.getElementById("cardWeak").checked;
  var pool=[];
  SUBJECT_ORDER.forEach(function(sk){
    if(subj!=="all" && subj!==sk) return;
    KNOWLEDGE[sk].chapters.forEach(function(ch,ci){
      ch.points.forEach(function(pt,pi){
        var key = mkey(sk,ci,pi);
        if(onlyWeak && (state.knowledge[key]||0)>=3) return;
        pool.push({sk:sk,ci:ci,pi:pi,key:key,front:pt.t,back:pt.m,tag:pt.tag,chapter:ch.name,subject:KNOWLEDGE[sk].short});
      });
    });
  });
  return pool;
}
function shuffle(a){ for(var i=a.length-1;i>0;i--){ var j=Math.floor(Math.random()*(i+1)); var t=a[i]; a[i]=a[j]; a[j]=t; } return a; }
function onCardFilter(){ startCards(); }
function startCards(){
  cardQueue = shuffle(buildCardPool());
  cardIdx = 0; cardFlipped=false; cardSessionDone=0;
  renderCard();
}
function renderCard(){
  var area = document.getElementById("cardArea");
  var prog = document.getElementById("cardProgress");
  if(cardQueue.length===0){
    prog.textContent = "";
    area.innerHTML = `<div class="fc-empty">🌼 这个筛选下没有卡片啦，换个科目或取消"只看未掌握"试试～</div>`;
    return;
  }
  if(cardIdx>=cardQueue.length){
    var mc = masteryCount();
    prog.textContent = "";
    area.innerHTML = `<div class="fc-done"><div class="big">🎉</div><div style="font-size:16px;font-weight:800;margin:8px 0">本轮完成！复习了 ${cardSessionDone} 张</div>`
      + `<div style="color:var(--muted);font-size:13px;margin-bottom:16px">累计已掌握 ${mc.got}/${mc.total} 个知识点</div>`
      + `<button class="btn btn-primary" onclick="startCards()">再来一轮</button></div>`;
    return;
  }
  var c = cardQueue[cardIdx];
  prog.textContent = `第 ${cardIdx+1} / ${cardQueue.length} 张 · ${c.subject}`;
  var tagMap = {key:'⭐ 重点', hard:'🔥 难点', easy:'✅ 了解'};
  area.innerHTML = `<div class="fc-scene"><div class="fc${cardFlipped?' flipped':''}" id="fcCard" onclick="flipCard()">`
    + `<div class="fc-face fc-front"><div class="fc-sub">${c.subject} · ${tagMap[c.tag]||''}</div><div class="fc-q">${c.front}</div><div class="fc-tip">👆 点击卡片看答案</div></div>`
    + `<div class="fc-face fc-back"><div class="fc-a-title">${c.front}</div><div class="fc-a">${c.back}</div></div>`
    + `</div></div>`
    + `<div class="fc-rate"><button class="btn fc-forgot" onclick="rateCard(1)">忘记了</button>`
    + `<button class="btn fc-vague" onclick="rateCard(2)">有点模糊</button>`
    + `<button class="btn fc-known" onclick="rateCard(3)">认识！</button></div>`;
}
function flipCard(){ cardFlipped=!cardFlipped; var el=document.getElementById("fcCard"); if(el) el.classList.toggle("flipped"); }
function rateCard(level){
  var c = cardQueue[cardIdx];
  state.knowledge[c.key] = level;
  var box = (state.cards[c.key] && state.cards[c.key].box) || 0;
  box = level===3 ? Math.min(box+1,5) : (level===2 ? box : 0);
  state.cards[c.key] = {box:box, last:todayKey()};
  saveState();
  cardSessionDone++;
  cardIdx++; cardFlipped=false;
  renderCard();
}

/* ---------------- 知识点速查（列表） ---------------- */
function renderKb(){
  var search = (document.getElementById("kbSearch").value||"").toLowerCase();
  var html="";
  SUBJECT_ORDER.forEach(function(sk){
    var sd = KNOWLEDGE[sk], subjectHtml="", any=false;
    sd.chapters.forEach(function(ch,ci){
      var pointsHtml="", hit=false;
      ch.points.forEach(function(pt,pi){
        if(search && pt.t.toLowerCase().indexOf(search)===-1 && pt.m.toLowerCase().indexOf(search)===-1 && ch.name.toLowerCase().indexOf(search)===-1) return;
        hit=true; any=true;
        var tagMap = {key:'<span class="k-tag k-tag-key">⭐ 重点</span>', hard:'<span class="k-tag k-tag-hard">🔥 难点</span>', easy:'<span class="k-tag k-tag-easy">✅ 了解</span>'};
        pointsHtml += `<div class="kb-point"><div class="kb-point-title">${pt.t} ${tagMap[pt.tag]||''}</div><div class="kb-point-method">${pt.m}</div></div>`;
      });
      if(hit){
        subjectHtml += `<div class="kb-chapter"><div class="kb-chapter-head" onclick="toggleKbBody(this)"><span>${ch.name}</span><span class="arrow">▶</span></div><div class="kb-body${search?' open':''}">${pointsHtml}</div></div>`;
      }
    });
    if(any){
      html += `<div class="kb-subject"><div class="kb-subject-head" onclick="toggleKbSubject(this)"><span>${sd.icon} ${sd.name}</span><span class="arrow open">▶</span></div><div class="kb-subject-body" style="display:block">${subjectHtml}</div></div>`;
    }
  });
  if(!html) html = `<div class="empty-tip">没有找到匹配的知识点，换个关键词试试～</div>`;
  document.getElementById("kbList").innerHTML = html;
}
function toggleKbBody(el){
  var body = el.nextElementSibling;
  var arrow = el.querySelector(".arrow");
  body.classList.toggle("open");
  arrow.classList.toggle("open");
}
function toggleKbSubject(el){
  var body = el.nextElementSibling;
  var arrow = el.querySelector(".arrow");
  var open = body.style.display !== "none";
  body.style.display = open ? "none" : "block";
  if(open) arrow.classList.remove("open"); else arrow.classList.add("open");
}

/* ---------------- 初始化 ---------------- */
(function(){
  state = loadState();
  document.querySelectorAll(".tab-btn").forEach(function(btn){
    btn.addEventListener("click", function(){
      document.querySelectorAll(".tab-btn").forEach(function(b){ b.classList.remove("active"); });
      document.querySelectorAll(".section").forEach(function(s){ s.classList.remove("active"); });
      this.classList.add("active");
      var tab = this.dataset.tab;
      document.getElementById("tab-"+tab).classList.add("active");
      if(tab==="plan") renderPlan();
      else if(tab==="review") renderReview();
      else if(tab==="mind") renderMind();
      else if(tab==="cards"){ if(cardQueue.length===0) startCards(); else renderCard(); }
      else if(tab==="info") renderKb();
    });
  });
  document.addEventListener("input", function(e){
    if(e.target && e.target.id==="notesArea"){ state.notes = e.target.value; saveState(); }
  });
  document.getElementById("quote").textContent = QUOTES[Math.floor(Math.random()*QUOTES.length)];
  updateCountdown();
  renderPlan();
  renderMmSubjects();
  initMmDrag();
  if("serviceWorker" in navigator){ navigator.serviceWorker.register("sw.js").catch(function(){}); }
})();
</script>'''


def build():
    js = (JS
          .replace("__KNOWLEDGE__", json.dumps(KNOWLEDGE, ensure_ascii=False))
          .replace("__PHASES__", json.dumps(PHASES, ensure_ascii=False))
          .replace("__QUOTES__", json.dumps(QUOTES, ensure_ascii=False)))
    html = HTML.replace("__SCRIPT__", js)
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("OK: written {} bytes to {}".format(len(html), path))


if __name__ == "__main__":
    build()
