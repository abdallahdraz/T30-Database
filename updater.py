import os
import json
import requests

print("🤖 بدأت أتمتة الروبوت: جاري فحص التحديثات وربط داتا كأس العالم...")

API_KEY = os.environ.get("API_FOOTBALL_KEY")
headers = {
    "x-apisports-key": API_KEY
}

db_path = 'Tahadi_ULTIMATE_DB.json'

# فتح الداتابيز المدمجة بحذر
try:
    with open(db_path, 'r', encoding='utf-8') as f:
        db = json.load(f)
except FileNotFoundError:
    db = {"seen_jeem": [], "wc_2026_players": []}

# التأكد من وجود الأقسام الجديدة عشان السكريبت ما يضرب
if 'seen_jeem' not in db:
    db['seen_jeem'] = []
if 'wc_2026_players' not in db:
    db['wc_2026_players'] = []

try:
    # جلب أحدث الانتقالات العالمية للحفاظ على ديناميكية الأسئلة
    response = requests.get("https://v3.football.api-sports.io/transfers/latest", headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        if "response" in data and len(data["response"]) > 0:
            latest_transfers = data["response"][:10]
            
            for transfer_data in latest_transfers:
                player_name = transfer_data.get('player', {}).get('name', '').strip()
                transfers_list = transfer_data.get('transfers', [])
                
                if player_name and transfers_list:
                    latest_move = transfers_list[0]
                    team_in = latest_move.get('teams', {}).get('in', {}).get('name')
                    team_out = latest_move.get('teams', {}).get('out', {}).get('name')
                    
                    new_q = f"انتقل اللاعب {player_name} حديثاً من نادي {team_out} إلى نادي {team_in}. (تحديث تلقائي)"
                    
                    # الفحص ومنع التكرار
                    if not any(item['q'] == new_q for item in db['seen_jeem']):
                        db['seen_jeem'].append({"q": new_q, "a": player_name})
                        print(f"🔥 تم رصد انتقال حي وتحديثه: {player_name}")
                        
                        # تحديث ناديه الحالي في قائمة كأس العالم لو كان موجوداً هناك
                        for p in db['wc_2026_players']:
                            if p['name'] == player_name:
                                p['club'] = team_in
                                print(f"🔄 تم تحديث نادي اللاعب {player_name} في قائمة كأس العالم إلى {team_in}")

    # حفظ الملف النهائي مع الحفاظ على الترتيب والترميز العربي
    with open(db_path, 'w', encoding='utf-8') as f:
        json.dump(db, f, ensure_ascii=False, indent=4)
    print("💾 تم حفظ ومزامنة الداتابيز بنجاح على السيرفر!")

except Exception as e:
    print(f"❌ حدث خطأ غير متوقع أثناء المعالجة: {e}")
