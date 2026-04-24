def housing_analysis():
    houses = {
        '001': {
            '房型': '3室1厅',
            '面积': 68.69,
            '装修情况': '简装',
            '挂牌价': 6124,
            '关注人数': 35
        },
        '002': {
            '房型': '2室2厅',
            '面积': 87.16,
            '装修情况': '精装',
            '挂牌价': 8375,
            '关注人数': 148
        },
        '003': {
            '房型': '3室1厅',
            '面积': 61.72,
            '装修情况': '精装',
            '挂牌价': 9266,
            '关注人数': 146
        },
        '004': {
            '房型': '3室2厅',
            '面积': 68.18,
            '装修情况': '精装',
            '挂牌价': 8496,
            '关注人数': 79
        },
        '005': {
            '房型': '2室2厅',
            '面积': 71.67,
            '装修情况': '简装',
            '挂牌价': 4871,
            '关注人数': 105
        },
        '006': {
            '房型': '3室1厅',
            '面积': 84.78,
            '装修情况': '简装',
            '挂牌价': 5782,
            '关注人数': 34
        }
    }
    sorted_by_popularity = sorted(houses.items(),
                                                     key=lambda x: x[1]['关注人数'],
                                                     reverse=True)

    for i,(house_id,info) in enumerate(sorted_by_popularity[:3],1):
        print(f"第{i}名 - 房源编号: {house_id}")
        print(f"  房型: {info['房型']}")
        print(f"  面积: {info['面积']}平方米")
        print(f"  装修情况: {info['装修情况']}")
        print(f"  挂牌价: {info['挂牌价']}元/平方米")
        print(f"  关注人数: {info['关注人数']}")
        print()
        
    print("=" * 50)
    print("总价最低的三套房源:")
    print("=" * 50)

    for house_id in houses:
        area = houses[house_id]['面积']
        price = houses[house_id]['挂牌价']
        houses[house_id]['总价'] = round(area * price, 2)

    sorted_by_total_price = sorted(houses.items(), key=lambda x: x[1]['总价'])
    
    for i, (house_id, info) in enumerate(sorted_by_total_price[:3], 1):
        print(f"第{i}名 - 房源编号: {house_id}")
        print(f"  房型: {info['房型']}")
        print(f"  面积: {info['面积']}平方米")
        print(f"  装修情况: {info['装修情况']}")
        print(f"  挂牌价: {info['挂牌价']}元/平方米")
        print(f"  关注人数: {info['关注人数']}")
        print(f"  总价: {info['总价']}元")
        print()


housing_analysis()        

        
