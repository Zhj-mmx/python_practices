
import jieba
from collections import Counter

# 设置matplotlib使用Agg后端
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

def get_chinese_font():
    """获取可用的中文字体路径"""
    # 在WSL中访问Windows字体
    windows_fonts = [
        # Windows系统中的中文字体路径
        '/mnt/c/Windows/Fonts/simhei.ttf',  # 黑体
        '/mnt/c/Windows/Fonts/simsun.ttc',  # 宋体
        '/mnt/c/Windows/Fonts/simkai.ttf',  # 楷体
        '/mnt/c/Windows/Fonts/MSYH.TTC',    # 微软雅黑
        # WSL系统中的中文字体
        '/usr/share/fonts/truetype/wqy/wqy-microhei.ttc',
        '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc',
        '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
    ]
    
    for font_path in windows_fonts:
        if os.path.exists(font_path):
            print(f"找到字体: {font_path}")
            return font_path
    
    print("未找到中文字体，将使用默认字体（可能显示方框）")
    return None

def water_margin_analysis_with_font():
    """水浒传人物分析 - 带字体修复版"""
    
    # 获取中文字体路径
    chinese_font = get_chinese_font()
    
    # 梁山好汉名单
    heroes = [
        "宋江", "卢俊义", "吴用", "公孙胜", "关胜", "林冲", "秦明", "呼延灼", "花荣", "柴进",
        "李应", "朱仝", "鲁智深", "武松", "董平", "张清", "杨志", "徐宁", "索超", "戴宗",
        "刘唐", "李逵", "史进", "穆弘", "雷横", "李俊", "阮小二", "张横", "阮小五", "张顺",
        "阮小七", "杨雄", "石秀", "解珍", "解宝", "燕青", "朱武", "黄信", "孙立", "宣赞",
        "郝思文", "韩滔", "彭玘", "单廷珪", "魏定国", "萧让", "裴宣", "欧鹏", "邓飞", "燕顺",
        "杨林", "凌振", "蒋敬", "吕方", "郭盛", "安道全", "皇甫端", "王英", "扈三娘", "鲍旭",
        "樊瑞", "孔明", "孔亮", "项充", "李衮", "金大坚", "马麟", "童威", "童猛", "孟康",
        "侯健", "陈达", "杨春", "郑天寿", "陶宗旺", "宋清", "乐和", "龚旺", "丁得孙", "穆春",
        "曹正", "宋万", "杜迁", "薛永", "施恩", "李忠", "周通", "汤隆", "杜兴", "邹渊",
        "邹润", "朱贵", "朱富", "蔡福", "蔡庆", "李立", "李云", "焦挺", "石勇", "孙新",
        "顾大嫂", "张青", "孙二娘", "P定六", "郁保四", "白胜", "时迁", "段景住"
    ]
    
    # 人物别名映射
    alias_mapping = {
        "宋江": ["宋押司", "宋公明", "黑三郎", "呼保义", "及时雨"],
        "李逵": ["黑旋风", "铁牛"],
        "武松": ["武都头", "武二郎", "行者"],
        "林冲": ["林教头", "豹子头"],
        "卢俊义": ["玉麒麟", "卢员外"],
        "燕青": ["燕小乙", "小乙哥"],
        "戴宗": ["神行太保", "戴院长"],
        "鲁智深": ["智深", "花和尚", "鲁提辖"],
        "柴进": ["柴大官人", "小放风"]
    }
    
    try:
        # 读取文件
        with open('shuihuzhuan.txt', 'r', encoding='utf-8') as f:
            text = f.read()
        
        print("文本预处理中...")
        # 文本预处理：替换别名
        for main_name, aliases in alias_mapping.items():
            for alias in aliases:
                text = text.replace(alias, main_name)
        
        print("分词中...")
        # 分词
        words = jieba.lcut(text)
        
        # 统计人物出场次数
        hero_count = {}
        for word in words:
            if word in heroes:
                hero_count[word] = hero_count.get(word, 0) + 1
        
        # 找出出场次数最多的前十位
        top_10 = Counter(hero_count).most_common(10)
        
        print("\n" + "=" * 60)
        print("出场次数最多的前十位水浒英雄:")
        print("=" * 60)
        for i, (hero, count) in enumerate(top_10, 1):
            print(f"第{i}名: {hero} - {count}次")
        
        # 生成柱状图（带字体修复）
        generate_bar_chart_with_font(hero_count, chinese_font)
        
        # 文本可视化
        generate_text_visualization(hero_count)
        
        # 生成词云（带字体修复）
        generate_wordcloud_with_font(hero_count, chinese_font)
        
    except FileNotFoundError:
        print("未找到水浒传文本文件 'shuihuzhuan.txt'")
    except Exception as e:
        print(f"分析过程中出错: {e}")

def generate_bar_chart_with_font(hero_count, font_path):
    """生成带字体修复的柱状图"""
    try:
        # 设置字体
        if font_path:
            plt.rcParams['font.family'] = ['sans-serif']
            plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']  # 黑体优先
            plt.rcParams['axes.unicode_minus'] = False
        else:
            # 如果没有中文字体，使用默认字体
            plt.rcParams['font.family'] = ['DejaVu Sans']
        
        # 取前15个人物
        top_15 = Counter(hero_count).most_common(15)
        names = [item[0] for item in top_15]
        counts = [item[1] for item in top_15]
        
        # 创建柱状图
        plt.figure(figsize=(14, 8))
        bars = plt.bar(range(len(names)), counts, color='steelblue', alpha=0.7)
        
        plt.title('《水浒传》梁山好汉出场次数TOP15', fontsize=16, pad=20, fontproperties=get_font_properties(font_path))
        plt.xlabel('人物姓名', fontsize=12, fontproperties=get_font_properties(font_path))
        plt.ylabel('出场次数', fontsize=12, fontproperties=get_font_properties(font_path))
        
        # 设置x轴标签
        plt.xticks(range(len(names)), names, rotation=45, ha='right', fontproperties=get_font_properties(font_path))
        
        # 在柱子上显示数字
        for bar, count in zip(bars, counts):
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 10, 
                    str(count), ha='center', va='bottom', fontsize=10)
        
        # 调整布局
        plt.tight_layout()
        
        # 保存图片
        plt.savefig('water_margin_bar_chart_fixed.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        print("✓ 柱状图已保存为 'water_margin_bar_chart_fixed.png'")
        
    except Exception as e:
        print(f"生成柱状图时出错: {e}")

def get_font_properties(font_path):
    """获取字体属性"""
    if font_path:
        from matplotlib.font_manager import FontProperties
        return FontProperties(fname=font_path)
    return None

def generate_text_visualization(hero_count):
    """生成文本可视化"""
    print("\n" + "=" * 60)
    print("文本可视化 - 人物出场次数分布")
    print("=" * 60)
    
    # 排序并取前20名
    top_20 = Counter(hero_count).most_common(20)
    
    # 找到最大次数用于比例计算
    max_count = top_20[0][1]
    
    print("\n排名  人物    次数  可视化")
    print("-" * 50)
    
    for i, (hero, count) in enumerate(top_20, 1):
        # 计算条形长度
        bar_length = int((count / max_count) * 40)
        bar = "█" * bar_length
        
        print(f"{i:2d}   {hero:3}   {count:4d}  {bar}")
    
    # 保存详细结果
    save_detailed_results(hero_count)

def save_detailed_results(hero_count):
    """保存详细结果"""
    try:
        with open('水浒传人物分析结果.txt', 'w', encoding='utf-8') as f:
            f.write("《水浒传》梁山好汉出场次数统计\n")
            f.write("=" * 50 + "\n\n")
            
            f.write("出场次数最多的前十位水浒英雄:\n")
            f.write("-" * 40 + "\n")
            top_10 = Counter(hero_count).most_common(10)
            for i, (hero, count) in enumerate(top_10, 1):
                f.write(f"第{i}名: {hero} - {count}次\n")
            
            f.write("\n所有108将出场次数统计:\n")
            f.write("-" * 30 + "\n")
            sorted_heroes = sorted(hero_count.items(), key=lambda x: x[1], reverse=True)
            
            # 分组显示
            f.write("\n第一梯队 (500次以上):\n")
            for hero, count in sorted_heroes:
                if count >= 500:
                    f.write(f"  {hero}: {count}次\n")
            
            f.write("\n第二梯队 (200-499次):\n")
            for hero, count in sorted_heroes:
                if 200 <= count < 500:
                    f.write(f"  {hero}: {count}次\n")
            
            f.write("\n第三梯队 (100-199次):\n")
            for hero, count in sorted_heroes:
                if 100 <= count < 200:
                    f.write(f"  {hero}: {count}次\n")
            
            f.write("\n第四梯队 (100次以下):\n")
            for hero, count in sorted_heroes:
                if count < 100:
                    f.write(f"  {hero}: {count}次\n")
            
            # 统计信息
            f.write(f"\n统计信息:\n")
            f.write(f"总统计人物数: {len(hero_count)}位\n")
            f.write(f"总出场次数: {sum(hero_count.values())}次\n")
            f.write(f"平均出场次数: {sum(hero_count.values()) / len(hero_count):.1f}次\n")
            f.write(f"最高出场次数: {max(hero_count.values())}次 (宋江)\n")
            f.write(f"最低出场次数: {min(hero_count.values())}次\n")
        
        print("✓ 详细结果已保存为 '水浒传人物分析结果.txt'")
        
    except Exception as e:
        print(f"保存结果时出错: {e}")

def generate_wordcloud_with_font(hero_count, font_path):
    """生成带字体修复的词云"""
    try:
        from wordcloud import WordCloud
        
        if font_path:
            print(f"使用字体生成词云: {font_path}")
            wc = WordCloud(
                font_path=font_path,
                width=1000,
                height=700,
                background_color='white',
                max_words=50,
                colormap='viridis',
                relative_scaling=0.5
            )
        else:
            print("未找到中文字体，尝试生成英文词云...")
            # 如果没有中文字体，尝试使用拼音
            hero_count_pinyin = {}
            for hero, count in hero_count.items():
                # 简单的拼音映射（仅用于演示）
                pinyin_map = {
                    "宋江": "SongJiang", "李逵": "LiKui", "武松": "WuSong", 
                    "林冲": "LinChong", "鲁智深": "LuZhiShen", "吴用": "WuYong",
                    "卢俊义": "LuJunYi", "柴进": "ChaiJin", "戴宗": "DaiZong",
                    "公孙胜": "GongSunSheng"
                }
                hero_count_pinyin[pinyin_map.get(hero, hero)] = count
            
            wc = WordCloud(
                width=1000,
                height=700,
                background_color='white',
                max_words=50,
                colormap='viridis'
            )
            hero_count = hero_count_pinyin
        
        # 生成词云
        wc.generate_from_frequencies(hero_count)
        
        # 保存词云
        if font_path:
            filename = 'water_margin_wordcloud_chinese.png'
        else:
            filename = 'water_margin_wordcloud_pinyin.png'
        
        wc.to_file(filename)
        print(f"✓ 词云图已保存为 '{filename}'")
        
        # 同时生成HTML版本作为备用
        generate_html_cloud(hero_count)
            
    except Exception as e:
        print(f"词云生成失败: {e}")
        print("创建HTML文本版词云...")
        generate_html_cloud(hero_count)

def generate_html_cloud(hero_count):
    """生成HTML文本版词云"""
    try:
        # 根据频率生成不同大小的文本
        top_30 = Counter(hero_count).most_common(30)
        
        html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>水浒传人物词云</title>
            <style>
                body { font-family: "Microsoft YaHei", Arial, sans-serif; margin: 40px; background: #f5f5f5; }
                .cloud { text-align: center; line-height: 2.5; padding: 20px; }
                .large { font-size: 36px; color: #e74c3c; font-weight: bold; margin: 10px; display: inline-block; }
                .medium { font-size: 24px; color: #3498db; margin: 8px; display: inline-block; }
                .small { font-size: 18px; color: #2ecc71; margin: 6px; display: inline-block; }
                .xsmall { font-size: 14px; color: #95a5a6; margin: 4px; display: inline-block; }
                .title { text-align: center; color: #2c3e50; margin-bottom: 30px; }
                .info { text-align: center; color: #7f8c8d; margin-top: 30px; }
            </style>
        </head>
        <body>
            <div class="title">
                <h1>《水浒传》人物出场次数词云</h1>
                <p>字体大小代表出场次数多少</p>
            </div>
            <div class="cloud">
        """
        
        # 添加人物名称
        max_count = top_30[0][1]
        for hero, count in top_30:
            ratio = count / max_count
            if ratio > 0.7:
                size_class = "large"
            elif ratio > 0.4:
                size_class = "medium"
            elif ratio > 0.2:
                size_class = "small"
            else:
                size_class = "xsmall"
            
            html_content += f'<span class="{size_class}" title="出场{count}次">{hero}</span>\n'
        
        html_content += """
            </div>
            <div class="info">
                <p>鼠标悬停在名字上查看具体出场次数</p>
                <p>生成时间: """ + __import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S') + """</p>
            </div>
        </body>
        </html>
        """
        
        with open('water_margin_text_cloud.html', 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print("✓ 文本版词云已保存为 'water_margin_text_cloud.html'")
        print("   请在浏览器中打开此文件查看效果")
        
    except Exception as e:
        print(f"生成HTML词云时出错: {e}")

def main():
    """主函数"""
    print("开始分析《水浒传》人物出场次数...")
    print("正在检测中文字体...")
    water_margin_analysis_with_font()
    print("\n" + "=" * 60)
    print("分析完成！生成的文件：")
    print("  ✓ water_margin_bar_chart_fixed.png - 修复版柱状图")
    print("  ✓ 水浒传人物分析结果.txt - 详细统计数据")
    print("  ✓ water_margin_wordcloud_*.png - 词云图")
    print("  ✓ water_margin_text_cloud.html - 文本版词云")
    print("=" * 60)

if __name__ == "__main__":
    main()
