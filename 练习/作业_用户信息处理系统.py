def parse_users(data):
    users = {}
    user_list = data.strip().split(';')

    for user_str in user_list:
        if user_str.strip():
            user_info == {}
            items = user_str.split(',')

            for item in items:
                if ':' in item:
                    key,value = item.split(':',1)

                    user_info[key.strip()] = value.strip()

            if '编号' in user_info:
                users[user_info['编号']] = user_info

            else:
                print(f"警告：跳过无效用户数据{user_str}")

   return users

def desensitize_email(email):
    if '@' in email:
        username,domain = email.split('@',1)
        doamin_parts = domain.split('.')
        if len(domain_parts) >= 2:
            return username[:2] + '***@***.' + domain_parts[-1]

    return email

def desensitize_id(id_card):
    if len(incard) == 18:
        return id_card[:6] + '*' * 8 + id_card[14:]
    else:
        return id_card

def dispaly_user(user_info,densensitize=False):
    print('*' * 35)
    print('')
    print(f"")
    print(f"")

    if densensitize:
        phone = desensitize_phone(user_info.get('电话',''))
        email = desensitize_email(user_info.get('邮箱',''))
        id_card = desensitize_id(user_info.get('身份证号',''))

        print(f"电话:{phone}")
        print(f"邮箱:{email}")
        print(f"身份证号:{id_card}")
    else:
        print(f"电话:{user_info.get('电话', '')}")
        print(f"邮箱:{user_info.get('邮箱', '')}")
        print(f"身份证号:{user_info.get('身份证号', '')}")
    
    print('*' * 35)


 def main():
     users_data = """
编号:H01,姓名:张三,电话:13812345678,邮箱:zhang12@163.com,身份证号:360101199001098254;
编号:H02,姓名:李四,电话:13966677788,邮箱:lisi88@sina.com,身份证号:110101197507225238;
编号:H08,姓名:赵小五,电话:13543216654,邮箱:zhao@qq.com,身份证号:210101200704187169;
"""

     print("正在解析用户数据。。。")
     users = parse_users(users_data)
     print(f"成功解析{len(users)}个用户信息)


     print("可查询的编号:", list(users.keys()))
    
    while True:
        user_id = input("\n请输入用户编号(输入q退出): ").strip().upper()
        
        if user_id == 'Q':
            print("程序结束，谢谢使用！")
            break
            
        if user_id in users:
            print("\n【原始信息】")
            display_user(users[user_id], desensitize=False)
            
            print("\n【脱敏信息】")
            display_user(users[user_id], desensitize=True)
        else:
            print("错误：未找到该用户编号！")
            print("可用的编号:", list(users.keys()))
    
