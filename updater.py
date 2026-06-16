import os
import json
import requests

print("🤖 الروبوت بدأ العمل: جاري جلب التحديثات من API-Football...")

# قراءة المفتاح السري من GitHub Secrets
API_KEY = os.environ.get("API_FOOTBALL_KEY")
headers = {
    "x-rapidapi-host": "v3.football.api-sports.io",
    "x-rapidapi-key": API_KEY
}

# قراءة الداتابيز الحالية
db_path = 'Tahadi_ULTIMATE_DB.json'
with open(db_path, 'r', encoding='utf-8') as f:
    db = json.load(f)

# ---------------------------------------------------------
# مثال لتحديث حقيقي: سحب أحدث الانتقالات (Transfers)
# ---------------------------------------------------------
# سحب أحدث الانتقالات من الـ API (كمثال مبدئي لتجربة الربط)
try:
    response = requests.get("https://v3.football.api-sports.io/transfers/latest", headers=headers)
    data = response.json()
    
    if "response" in data and len(data["response"]) > 0:
        latest_transfers = data["response"][:5] # نأخذ أحدث 5 انتقالات
        for transfer_data in latest_transfers:
            player_name = transfer_data.get('player', {}).get('name', 'لاعب غير معروف')
            transfers_list = transfer_data.get('transfers', [])
            
            if transfers_list:
                latest_move = transfers_list[0]
                team_in = latest_move.get('teams', {}).get('in', {}).get('name')
                team_out = latest_move.get('teams', {}).get('out', {}).get('name')
                
                # إضافة سؤال جديد لفقرة سين جيم
                new_q = f"انتقل اللاعب {player_name} حديثاً من نادي {team_out} إلى نادي {team_in}. (تحديث تلقائي)"
                # نتأكد إن السؤال مش مكرر
                if not any(item['q'] == new_q for item in db['seen_jeem']):
                    db['seen_jeem'].append({"q": new_q, "a": player_name})
                    print(f"✅ تمت إضافة انتقال جديد: {player_name} إلى {team_in}")

    # حفظ الداتابيز بعد التحديث
    with open(db_path, 'w', encoding='utf-8') as f:
        json.dump(db, f, ensure_ascii=False, indent=4)
    print("💾 تم حفظ التحديثات بنجاح!")

except Exception as e:
    print(f"❌ حدث خطأ أثناء جلب البيانات: {e}")
