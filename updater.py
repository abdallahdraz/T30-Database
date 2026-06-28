import os
import json
import requests
from datetime import datetime, timedelta
import time

print("🤖 بدأت أتمتة الروبوت الشاملة (نسخة الإضافة الآمنة)...")

# ==========================================
# 1. إعدادات الاتصال 
# ==========================================
API_KEY = os.environ.get("API_FOOTBALL_KEY")
HEADERS = {
    "x-apisports-key": API_KEY,
    "x-apisports-host": "v3.football.api-sports.io"
}

db_path = 'Tahadi_ULTIMATE_DB.json'
api_calls = 0

# ==========================================
# 2. القراءة الآمنة للداتابيز الحالية
# ==========================================
# نحن هنا نحمي البيانات القديمة. نقرأها أولاً، وإذا لم يكن الملف موجوداً ننشئ هيكل فارغ.
try:
    with open(db_path, 'r', encoding='utf-8') as f:
        db = json.load(f)
        print(f"📂 تم تحميل الداتابيز الحالية بنجاح. تحتوي على {len(db.get('dramatic_matches', []))} مباراة محفوظة.")
except FileNotFoundError:
    print("⚠️ لم يتم العثور على الداتابيز. سيتم إنشاء واحدة جديدة.")
    db = {"seen_jeem": [], "wc_2026_players": [], "dramatic_matches": []}
except json.JSONDecodeError:
    print("❌ خطأ قاتل: ملف الداتابيز الحالي تالف! سيتم إيقاف السكريبت لحماية البيانات.")
    exit(1) # نوقف السكريبت فوراً عشان ما نكتبش فوق الملف التالف ونضيعه

# ضمان وجود المفاتيح الأساسية حتى لا يتعطل الكود
for key in ['seen_jeem', 'wc_2026_players', 'dramatic_matches']:
    if key not in db:
        db[key] = []

# ==========================================
# 3. جلب الانتقالات (المرحلة الأولى)
# ==========================================
print("\n🔄 [1/2] جاري فحص أحدث الانتقالات...")
try:
    response = requests.get("https://v3.football.api-sports.io/transfers/latest", headers=HEADERS)
    api_calls += 1
    
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
                    
                    # التحقق من عدم وجود السؤال مسبقاً قبل الإضافة
                    if not any(item['q'] == new_q for item in db['seen_jeem']):
                        db['seen_jeem'].append({"q": new_q, "a": player_name})
                        print(f"🔥 إضافة انتقال جديد لسين جيم: {player_name}")
                        
                        # تحديث قائمة المونديال (تعديل وليس إضافة)
                        for p in db['wc_2026_players']:
                            if p['name'] == player_name:
                                p['club'] = team_in
                                print(f"🔄 تم تحديث نادي {player_name} في المونديال إلى {team_in}")
except Exception as e:
    print(f"❌ خطأ أثناء معالجة الانتقالات: {e}")

# ==========================================
# 4. جلب المباريات الدرامية (المرحلة الثانية)
# ==========================================
print("\n⚔️ [2/2] جاري فحص مباريات القمة لليوم الفائت...")

yesterday_date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

MAJOR_TOURNAMENTS = [1, 2, 4, 9, 10, 6] 
SECONDARY_CUPS = [3, 45, 137, 140, 135, 78, 61, 307] 
ELITE_TEAMS = [
    "Real Madrid", "Barcelona", "Atletico Madrid", "Liverpool", "Manchester United", 
    "Manchester City", "Arsenal", "Chelsea", "Tottenham", "Aston Villa", "Newcastle",
    "AC Milan", "Juventus", "Inter", "Napoli", "Bayern Munich", "Borussia Dortmund", 
    "Bayer Leverkusen", "Paris Saint Germain", "FC Porto", "Benfica", 
    "Al Nassr", "Al Hilal", "Al Ittihad", "Al Ahli Jeddah", 
    "Al Wehdat", "Al Faisaly", "Al Hussein", 
    "Al Ahly", "Zamalek", "Esperance", "Wydad", "Raja Casablanca"
]

def is_elite(team_name):
    if not team_name: return False
    return any(elite.lower() in str(team_name).lower() for elite in ELITE_TEAMS)

def is_knockout(round_name):
    if not round_name: return False
    keywords = ['Final', 'Semi', 'Quarter', 'Round of 16', 'Round of 8', 'Round of 32', 'Play-offs', 'Knockout']
    return any(keyword.lower() in str(round_name).lower() for keyword in keywords)

def is_elite_crushed(h_name, a_name, g_home, g_away):
    margin = abs(g_home - g_away)
    if margin >= 4:
        if (is_elite(h_name) and g_home < g_away) or (is_elite(a_name) and g_away < g_home): return True
    return False

def is_dramatic_comeback(score_data, h_name, a_name):
    try:
        ht_h, ht_a = score_data['halftime']['home'], score_data['halftime']['away']
        ft_h, ft_a = score_data['fulltime']['home'], score_data['fulltime']['away']
        if ht_h is None or ht_a is None or ft_h is None or ft_a is None: return False
        if is_elite(h_name) and (ht_h <= ht_a - 3) and (ft_h >= ft_a): return True
        if is_elite(a_name) and (ht_a <= ht_h - 3) and (ft_a >= ft_h): return True
    except: pass
    return False

try:
    url_yesterday = f"https://v3.football.api-sports.io/fixtures?date={yesterday_date}"
    response_yesterday = requests.get(url_yesterday, headers=HEADERS).json()
    api_calls += 1

    matches_to_deep_fetch = []

    if response_yesterday.get('response'):
        for match in response_yesterday['response']:
            league_id = match['league']['id']
            round_name = match['league']['round']
            home_name = match['teams']['home']['name']
            away_name = match['teams']['away']['name']
            
            if match['fixture']['status']['short'] not in ['FT', 'AET', 'PEN']: continue
            if match['goals']['home'] is None or match['goals']['away'] is None: continue

            goals_home, goals_away = match['goals']['home'], match['goals']['away']
            keep_match, reason = False, ""

            if league_id in MAJOR_TOURNAMENTS and is_knockout(round_name):
                keep_match, reason = "دور إقصائي في بطولة كبرى"
            elif league_id in SECONDARY_CUPS and is_knockout(round_name) and ((goals_home + goals_away) > 5):
                keep_match, reason = "مباراة إقصائية غزيرة الأهداف"
            elif is_elite(home_name) and is_elite(away_name):
                keep_match, reason = "مواجهة قمة مباشرة"
            elif is_elite_crushed(home_name, away_name, goals_home, goals_away):
                keep_match, reason = "سقوط مدوي لفريق نخبوي"
            elif is_dramatic_comeback(match['score'], home_name, away_name):
                keep_match, reason = "ريمونتادا بعد تأخر بـ 3 أهداف"

            if keep_match:
                matches_to_deep_fetch.append((match['fixture']['id'], reason))

    # سحب التفاصيل وإضافتها للداتابيز
    if matches_to_deep_fetch:
        print(f"🔥 تم صيد {len(matches_to_deep_fetch)} مباراة درامية! جاري الجلب والإضافة...")
        
        for fix_id, reason in matches_to_deep_fetch:
            if api_calls >= 95: break
            
            # التحقق قبل استهلاك طلب API: هل المباراة موجودة مسبقاً في الداتابيز؟
            if any(item.get('id') == fix_id for item in db['dramatic_matches']):
                print(f"⚠️ المباراة (ID: {fix_id}) محفوظة مسبقاً. سيتم تخطيها.")
                continue

            detail_url = f"https://v3.football.api-sports.io/fixtures?id={fix_id}"
            match_data = requests.get(detail_url, headers=HEADERS).json()['response'][0]
            api_calls += 1
            
            venue = f"{match_data['fixture']['venue']['name'] or 'مجهول'} ({match_data['fixture']['venue']['city'] or 'مجهول'})"
            
            goals_list = []
            red_cards_list = []
            if match_data.get('events'):
                for event in match_data['events']:
                    time_str = f"{event['time']['elapsed']}{f'+{event['time']['extra']}' if event['time']['extra'] else ''}'"
                    if event['type'] == 'Goal' and event['detail'] != 'Missed Penalty':
                        scorer = event['player']['name'] or "مجهول"
                        assist = event['assist']['name']
                        goals_list.append(f"{scorer} {time_str} (أسيست: {assist if assist else 'بدون'})")
                    elif event['type'] == 'Card' and 'Red' in str(event['detail']):
                        red_cards_list.append(f"{event['player']['name'] or 'مجهول'} {time_str}")

            lineups_data = {}
            if match_data.get('lineups'):
                for team_lineup in match_data['lineups']:
                    t_name = team_lineup['team']['name']
                    lineups_data[t_name] = {
                        "coach": team_lineup['coach']['name'] or "مجهول",
                        "starters": [p['player']['name'] for p in team_lineup['startXI']],
                        "substitutes": [p['player']['name'] for p in team_lineup['substitutes']]
                    }

            # تجميع الحدث وإضافته لمتغير الداتابيز (db)
            full_match_record = {
                "id": fix_id,
                "saved_by_filter": reason,
                "tournament": match_data['league']['name'],
                "date": match_data['fixture']['date'][:10],
                "venue": venue,
                "score": f"{match_data['teams']['home']['name']} {match_data['goals']['home']} - {match_data['goals']['away']} {match_data['teams']['away']['name']}",
                "match_events": {"goals": goals_list, "red_cards": red_cards_list},
                "lineups": lineups_data
            }
            
            db['dramatic_matches'].append(full_match_record)
            print(f"✅ تمت إضافة مباراة جديدة: {full_match_record['score']}")
            time.sleep(0.5)
    else:
        print("😴 لا توجد مباريات مطابقة للشروط الكبرى ليوم أمس.")

except Exception as e:
    print(f"❌ خطأ أثناء معالجة المباريات: {e}")

# ==========================================
# 5. الحفظ الآمن (Safe Save)
# ==========================================
try:
    # نقوم بالكتابة مرة واحدة في النهاية، فقط بعد اكتمال كل عمليات الإضافة الناجحة
    with open(db_path, 'w', encoding='utf-8') as f:
        json.dump(db, f, ensure_ascii=False, indent=4)
    print(f"\n💾 تم حفظ الداتابيز بأمان! الإجمالي الآن {len(db.get('dramatic_matches', []))} مباراة. (الطلبات المستهلكة: {api_calls})")
except Exception as e:
    print(f"❌ خطأ قاتل أثناء حفظ الملف النهائي: {e}")
