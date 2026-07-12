
import sys
sys.stdout.reconfigure(encoding='utf-8')
html = open(r'C:\Users\Charles\Documents\Psychology\study-planner\index.html', 'r', encoding='utf-8').read()
print('Length:', len(html))
print('Has 第一阶段:', '第一阶段' in html)
print('Has 西南交通大学:', '西南交通大学' in html)
print('Has 距2027:', '距2027' in html)
print('Has 2026:', '2026' in html)
