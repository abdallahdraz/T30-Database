# 🏆 دستور ومعمارية لعبة "تحدي الثلاثين" (T30 Master Architecture)

**ملاحظة للذكاء الاصطناعي (System Prompt):**
أنت الآن المحرك الأساسي والحكم للعبة "تحدي الثلاثين". هذا الملف يحتوي على القواعد القطعية، آليات اللعب، هندسة التلقين (Prompt Engineering)، والكود المعتمد. يمنع منعاً باتاً الخروج عن هذه القواعد أو تأليف معلومات غير موثقة (No Hallucinations). رياضة اللعبة هي **كرة القدم فقط**.

---

## 📋 1. قوانين الفقرات (Game Rounds)

### 1. ماذا تعرف (3 أسئلة)
- تبادل الإجابات بالدور. اللاعب الذي يخطئ، يكرر، أو يعجز عن الإجابة يحصل على "سترايك" (❌).
- **3 سترايكات** تعني ذهاب النقطة للخصم.
- **في حال انتهاء الإجابات:** اللاعب صاحب السترايكات الأقل يفوز بنقطة (أو نقطتين إذا لم يكن لديه أي سترايك). وإذا تعادلا بالسترايكات يحصل كل منهما على نقطة.
- الحد الأدنى للإجابات الممكنة لأي سؤال هو **15 إجابة**.
- **الأسئلة الترتيبية حصراً هنا:** (سجل الأبطال، الهدافين، الترتيب الأبجدي، أغلى الصفقات).

### 2. المزاد (5 أسئلة)
- اللاعبون يزايدون على عدد الإجابات التي يمكنهم ذكرها في **30 ثانية**.
- النقاط: (0-19 = نقطة)، (20-29 = نقطتين)، (30-39 = 3 نقاط).
- **زر القفل:** متاح مرة واحدة لكل لاعب لقفل المزاد فوراً.
- **العقوبات:** إذا كانت الإجابات الصحيحة أقل من الرقم المطلوب، تذهب النقطة للخصم. إذا تجاوزت الأخطاء 5 أخطاء، يُخصم من اللاعب نقطة وتذهب للخصم.
- الحد الأدنى للإجابات الممكنة لأي سؤال هو **30 إجابة**.

### 3. قصة (3 أسئلة)
- **3 تلميحات** (صعب = 3 نقاط، متوسط = نقطتين، سهل = نقطة). 
- لكل لاعب محاولتين (2) للتخمين. إذا استنفذ المحاولات يلغى مربع الإجابة.
- **هيكلة التلميحات الصارمة (لمنع تداخل المعلومات):**
  - **التلميح 1 (صعب - الزمالة حصراً):** 6 إلى 8 لاعبين زاملهم. (لاعبون غير مشهورين جداً أو في بداياته).
  - **التلميح 2 (متوسط - الأندية حصراً):** أندية لعب لها أو دربها. (أندية وسط أو بدايات).
  - **التلميح 3 (سهل - إنجازات وأحداث):** أحداث مشهورة، أرقام قياسية، أو أسماء أساطير معروفين جداً.

### 4. فقرة الجرس (10 أسئلة)
- أسئلة كروية سريعة. الأسرع بالضغط يجيب، إذا أجاب قبل انتهاء السؤال لا يُكمل السؤال ويجب أن يجيب.
- خطأ = يُكمل السؤال للخصم.
- **الزر الحصري:** مرة واحدة لكل لاعب بالفقرة. يحجز السؤال له ويسمعه كاملاً. خطأ = تذهب النقطة للخصم.

### 5. سين جيم (5 أسئلة)
- نفس قوانين الجرس ولكن أسئلة **أصعب بكثير**.
- **زر الحفرة:** مرة واحدة لكل لاعب. الإجابة الصحيحة = (+2 له، و -2 للخصم). خطأ = يذهب السؤال للخصم (إذا أجابه الخصم يحصل على +2 بدون خصم من الأول).

### 6. التعويض (6 أسئلة)
- مسيرة أندية بالترتيب الزمني (حالي أو معتزل). مسيرة مسحوبة **حرفياً** من ويكيبيديا (بدون نقص أو اختصار).
- إجابة قبل انتهاء السرد = نقطتين. بعد الانتهاء = نقطة.
- محاولتين لكل لاعب.
- **زر المسيرة الصعبة:** يعطي مسيرة صعبة (2 نقاط في أي وقت).

---

## 🛑 2. القواعد الصارمة للذكاء الاصطناعي (AI Constraints)

1. **الاستثناءات:** يمنع منعاً باتاً ذكر أو تضمين "إسرائيل" (جنسية، أندية، لاعبين).
2. **الدقة (Zero Hallucination):** يجب التحقق من مزاملة اللاعبين أو لعب اللاعب لمدرب معين بنسبة 100% قبل توليد السؤال.
3. **المصطلحات المعتمدة:** (Top 6 في إنجلترا، Top 3 في إسبانيا، الدوريات الخمسة الكبرى، الدوريات الثلاثة، الديربيات الشهيرة).
4. **القوائم المحفورة (Hardcoded DB):** يتم الاعتماد على قوائم دقيقة ومغلقة لـ (الكرة الذهبية، الحذاء الذهبي، الفتى الذهبي، ذا بيست) ولا تخضع لتوليد الـ AI.

---

## 💻 3. الكود المعتمد (React Frontend + Groq Integration)

```jsx
import React, { useState, useEffect, useRef } from 'react';

// ==========================================
// 1. الثوابت العامة والمفاتيح
// ==========================================
const CONFIG = {
  GROQ_API_KEY: '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',
  GOOGLE_KEY: 'AIzaSyADvnZu031JT07jEvdje0SNAq1QxrksVOc',
  GOOGLE_CX: 'c629c80fa3d884b36',
  ROUNDS: ['ماذا تعرف', 'المزاد', 'قصة', 'فقرة الجرس', 'سين جيم', 'التعويض'],
  ROUND_LIMITS: { 'ماذا تعرف': 3, 'المزاد': 5, 'قصة': 3, 'فقرة الجرس': 10, 'سين جيم': 5, 'التعويض': 6 }
};

// ==========================================
// 2. قاعدة البيانات المحلية (صفر هبد) لسين جيم والجرس
// ==========================================
const TRIVIA_DB = [
  { type: "الجرس", q: "من هو اللاعب الذي سجل هدف فوز إسبانيا بكأس العالم 2010؟", a: "أندريس إنييستا" },
  { type: "الجرس", q: "من هو أول منتخب عربي يتأهل لنصف نهائي كأس العالم؟", a: "المغرب" },
  { type: "الجرس", q: "من هو أغلى مدافع في تاريخ كرة القدم حتى عام 2024؟", a: "جوسكو جفارديول (أو هاري ماجواير)" },
  { type: "سين جيم", q: "نادي فاز بدوري أبطال أوروبا مرتين متتاليتين عامي 1979 و 1980، من هو؟", a: "نوتنغهام فورست" },
  { type: "سين جيم", q: "من هو اللاعب الذي يحمل الرقم القياسي كأكثر من سجل في نسخة واحدة من كأس العالم (13 هدف)؟", a: "جوست فونتين" },
  { type: "سين جيم", q: "ما هو المنتخب الذي فاز بأول نسخة من كأس العالم عام 1930؟", a: "الأوروغواي" },
  { type: "الجرس", q: "من هو النادي الوحيد الذي توج بدوري أبطال أوروبا دون أن يخسر أي مباراة في البطولة نسخة 2020؟", a: "بايرن ميونخ" },
  { type: "سين جيم", q: "من هو اللاعب العربي الوحيد الذي فاز بجائزة الكرة الذهبية الأفريقية عام 1982؟", a: "محمود الخطيب" }
  // سيتم توسيع هذه القائمة لاحقاً من سكريبت API
];

// ==========================================
// 3. دوائر البحث (ويكيبيديا وجوجل)
// ==========================================
const searchWikipedia = async (query) => {
  try {
    const url = `https://ar.wikipedia.org/w/api.php?action=query&list=search&srsearch=${encodeURIComponent(query)}&utf8=&format=json&origin=*`;
    const response = await fetch(url);
    const data = await response.json();
    return data.query?.search?.slice(0, 2).map(item => item.snippet.replace(/(<([^>]+)>)/gi, "")).join(" | ") || "لا توجد نتائج.";
  } catch (e) {
    return "خطأ اتصال.";
  }
};

const searchGoogle = async (query) => {
  try {
    const url = `https://www.googleapis.com/customsearch/v1?key=${CONFIG.GOOGLE_KEY}&cx=${CONFIG.GOOGLE_CX}&q=${encodeURIComponent(query)}`;
    const response = await fetch(url);
    const data = await response.json();
    return data.items?.slice(0, 3).map(item => item.snippet).join(" | ") || "لا توجد نتائج.";
  } catch (e) {
    return "خطأ اتصال.";
  }
};

const fetchPlayerWikiData = async (playerName) => {
  try {
    const url = `https://ar.wikipedia.org/w/api.php?action=parse&prop=wikitext&page=${encodeURIComponent(playerName)}&format=json&origin=*`;
    const res = await fetch(url);
    const data = await res.json();
    const wikitext = data.parse?.wikitext['*'] || "";
    return wikitext.substring(0, 8000);
  } catch(e) { return ""; }
};

// ==========================================
// 4. محرك الاتصال بـ Groq
// ==========================================
const callGroq = async (prompt, systemInstruction) => {
  try {
    const response = await fetch('[https://api.groq.com/openai/v1/chat/completions](https://api.groq.com/openai/v1/chat/completions)', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${CONFIG.GROQ_API_KEY}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        model: 'llama-3.3-70b-versatile',
        messages: [
          { role: 'system', content: systemInstruction },
          { role: 'user', content: prompt }
        ],
        response_format: { type: "json_object" },
        temperature: 0.7
      })
    });
    const data = await response.json();
    if (!response.ok) throw new Error(data.error?.message || "خطأ من سيرفر Groq.");
    return data.choices[0].message.content;
  } catch (err) {
    throw err;
  }
};

const extractJson = (text) => {
  try { return JSON.parse(text); }
  catch (err) {
    try {
      const jsonMatch = text.match(/{[\s\S]*}/);
      if (jsonMatch) return JSON.parse(jsonMatch[0]);
      throw new Error();
    } catch(e) { throw new Error("مشكلة في قراءة البيانات."); }
  }
};

// ==========================================
// 5. خوارزمية التوليد لـ (المزاد وماذا تعرف)
// ==========================================
const generateQuestionPrompt = (roundType, randomSeed) => {
  const getRnd = (arr) => arr[Math.floor(Math.random() * arr.length)];
  const getTwo = (arr) => { let a = getRnd(arr), b = getRnd(arr); while(a===b) b = getRnd(arr); return [a, b]; };

  const teams = ["ريال مدريد", "برشلونة", "مانشستر يونايتد", "ليفربول", "يوفنتوس", "ميلان", "بايرن ميونخ", "آرسنال", "تشيلسي", "الإنتر", "أياكس", "نوتنغهام فورست", "أستون فيلا"];
  const leagues = ["الدوري الإنجليزي", "الدوري الإسباني", "الدوري الإيطالي", "الدوري الألماني", "الدوري الفرنسي"];
  const tournaments = ["دوري أبطال أوروبا", "كأس العالم", "كأس أمم أوروبا", "كوبا أمريكا"];
  const nationalities = ["البرازيل", "الأرجنتين", "فرنسا", "إسبانيا", "إيطاليا", "ألمانيا", "المغرب", "الجزائر", "مصر", "السعودية"];
  const continents = ["أوروبا", "أمريكا الجنوبية", "أفريقيا", "آسيا"];
  const positions = ["مهاجم", "جناح", "صانع ألعاب", "خط وسط", "مدافع", "ظهير", "حارس مرمى"];
  const managers = ["جوزيه مورينيو", "بيب جوارديولا", "كارلو أنشيلوتي", "يورجن كلوب", "زين الدين زيدان", "دييجو سيميوني"];
  const stars = ["ميسي", "كريستيانو رونالدو", "نيمار", "دي بروين", "محمد صلاح", "بيليه", "مارادونا"];
  const decades = ["الثمانينات", "السبعينات", "التسعينات"];
  const stadiums = ["ويمبلي", "سانتياغو برنابيو", "كامب نو", "سان سيرو", "ستاد لوسيل"];

  const [tA, tB] = getTwo(teams);
  const [lA, lB] = getTwo(leagues);
  const [natA, natB] = getTwo(nationalities);
  const contA = getRnd(continents);
  const posA = getRnd(positions);
  const manA = getRnd(managers);
  const tournA = getRnd(tournaments);
  const starA = getRnd(stars);
  const decade = getRnd(decades);
  const stadium = getRnd(stadiums);

  const timeEnding = Math.random() > 0.5 ? "في الموسم الحالي" : "عبر التاريخ";

  const generalPool = [
    `لاعبين لعبوا لنادي ${tA} ${timeEnding}`,
    `لاعبين لعبوا في نادي ${tA} و ${tB} خلال مسيرتهم`,
    `لاعب من قارة ${contA} لعب في دوري ${lA} ${timeEnding}`,
    `لاعب يلعب بمركز ${posA} لعب بفريق ${tA} ${timeEnding}`,
    `لاعب تدرب تحت قيادة المدرب ${manA} في فريق ${tA} ${timeEnding}`,
    `لاعب سجل هدفاً على الأقل في بطولة ${tournA} ${timeEnding}`,
    `فريق شارك في بطولة ${tournA} ${timeEnding}`,
    `لاعب زامل اللاعب ${starA} في النادي أو المنتخب (الذي يمثله ${starA} فقط)`,
    `لاعبين لعبوا لأحد أندية لندن ${timeEnding}`,
    `لاعبين لعبوا في الدوري الألماني والفرنسي عدا بايرن ميونخ وباريس سان جيرمان`,
    `لاعب سجل في نهائي بطولة ${tournA} وفاز فيه`,
    `لاعبون عرب سجلوا في دوري أبطال أوروبا عبر التاريخ`
  ];

  const orderPool = [
    `سجل أبطال بطولة ${tournA} بالترتيب مع ذكر سنة التتويج`,
    `سجل هدافين دوري ${lA} بالترتيب`,
    `أعلى صفقات قيمة لبطولة ${tournA} في ملعب ${stadium} بالترتيب`
  ];

  let selectedIdea = roundType === 'ماذا تعرف' ? getRnd([...generalPool, ...orderPool]) : getRnd(generalPool);
  let minAnswersRequired = roundType === 'المزاد' ? 30 : 15;

  const prompt = `أنت صانع أسئلة كروية لتحدي الثلاثين. استخدم قالب السؤال التالي حرفياً: [${selectedIdea}]

قواعد صارمة:
1. يمنع منعاً باتاً استحضار إسرائيل.
2. الحد الأدنى للإجابات هو (${minAnswersRequired}). وسّع نطاق السؤال كروياً إن لزم الأمر ليحقق الشرط.

أرجع JSON فقط:
{
  "question": "نص السؤال الدقيق",
  ${roundType === 'ماذا تعرف' ? `"max_answers": العدد الفعلي` : `"estimated_max": الحد الأقصى التقريبي`} 
}`;

  return prompt;
};

// ==========================================
// 6. المكون البرمجي الرئيسي للعبة
// ==========================================
export default function App() {
  const [setupNames, setSetupNames] = useState({ p1: 'اللاعب 1', p2: 'اللاعب 2' });
  const [isSetup, setIsSetup] = useState(true);

  const [players, setPlayers] = useState({
    p1: { name: '', score: 0, strikes: 0, attempts: 2, passUsed: false, auctionSpecUsed: false, exclusiveUsed: false, hofraUsed: false, hardCareerUsed: false },
    p2: { name: '', score: 0, strikes: 0, attempts: 2, passUsed: false, auctionSpecUsed: false, exclusiveUsed: false, hofraUsed: false, hardCareerUsed: false }
  });

  const [currentRound, setCurrentRound] = useState('ماذا تعرف');
  const [roundQuestionIndex, setRoundQuestionIndex] = useState(1);
  const [question, setQuestion] = useState(null);
  const [loading, setLoading] = useState(false);
  const [varVerdict, setVarVerdict] = useState('');

  const [userInput, setUserInput] = useState('');
  const [roundInputs, setRoundInputs] = useState({ p1: '', p2: '' });
  const [guessedAnswers, setGuessedAnswers] = useState([]);

  const [rawWikiCareerText, setRawWikiCareerText] = useState('');
  const [showWikiCareer, setShowWikiCareer] = useState(false);
  const [updatedCareer, setUpdatedCareer] = useState('');

  const [timer, setTimer] = useState(30);
  const [isTimerActive, setIsTimerActive] = useState(false);
  const [apiCooldown, setApiCooldown] = useState(0);

  const countdownRef = useRef(null);
  const cooldownRef = useRef(null);

  const [bids, setBids] = useState({ p1: 0, p2: 0, winner: null, targetValue: 0 });
  const [auctionCounters, setAuctionCounters] = useState({ correct: 0, errors: 0 });
  const [storyHintLevel, setStoryHintLevel] = useState(1);
  const [roundModifiers, setRoundModifiers] = useState({ exclusiveActive: null, hofraActive: null, hardCareerActive: false });

  const startGame = () => {
    if (!setupNames.p1.trim() || !setupNames.p2.trim()) return;
    setPlayers(prev => ({
      p1: { ...prev.p1, name: setupNames.p1 },
      p2: { ...prev.p2, name: setupNames.p2 }
    }));
    setIsSetup(false);
  };

  useEffect(() => {
    if (isTimerActive && timer > 0) {
      countdownRef.current = setTimeout(() => setTimer(prev => prev - 1), 1000);
    } else if (timer === 0 && isTimerActive) {
      setIsTimerActive(false);
      handleTimeOutEvent();
    }
    return () => clearTimeout(countdownRef.current);
  }, [isTimerActive, timer]);

  useEffect(() => {
    if (apiCooldown > 0) {
      cooldownRef.current = setTimeout(() => setApiCooldown(prev => prev - 1), 1000);
    }
    return () => clearTimeout(cooldownRef.current);
  }, [apiCooldown]);

  const triggerCooldown = () => setApiCooldown(3);

  const clearQuestionState = (targetRound = currentRound) => {
    setQuestion(null);
    setVarVerdict('');
    setUserInput('');
    setRoundInputs({ p1: '', p2: '' });
    setGuessedAnswers([]);
    setRawWikiCareerText('');
    setShowWikiCareer(false);
    setTimer(30);
    setIsTimerActive(false);
    setAuctionCounters({ correct: 0, errors: 0 });
    setStoryHintLevel(1);
    setRoundModifiers({ exclusiveActive: null, hofraActive: null, hardCareerActive: false });

    const startingAttempts = (targetRound === 'سين جيم' || targetRound === 'فقرة الجرس') ? 1 : 2;
    setPlayers(prev => ({
      ...prev,
      p1: { ...prev.p1, strikes: 0, attempts: startingAttempts },
      p2: { ...prev.p2, strikes: 0, attempts: startingAttempts }
    }));
  };

  const handleTimeOutEvent = () => {
    if (currentRound === 'المزاد' && bids.winner) {
      const loser = bids.winner === 'p1' ? 'p2' : 'p1';
      adjustScore(loser, 1, "انتهى الوقت بالمزاد! تذهب نقطة للخصم.");
    } else {
      setVarVerdict("❌ انتهى الوقت! يلغى السؤال.");
    }
  };

  const adjustScore = (playerKey, value, msg) => {
    setPlayers(prev => ({
      ...prev,
      [playerKey]: { ...prev[playerKey], score: prev[playerKey].score + value }
    }));
    if(msg) setVarVerdict(msg);
  };

  const handleManualStrike = (playerKey, customMsg = null) => {
    setPlayers(prev => {
      let next = { ...prev };
      const opp = playerKey === 'p1' ? 'p2' : 'p1';
      next[playerKey].strikes += 1;
      if (next[playerKey].strikes >= 3) {
        next[playerKey].strikes = 0;
        next[opp].score += 1;
        setVarVerdict(customMsg || `❌ 3 سترايكات على ${next[playerKey].name}! النقطة تحولت للخصم.`); 
      } else { 
        setVarVerdict(customMsg || `⚠️ سترايك تم تسجيله على ${next[playerKey].name}.`);
      }
      return next;
    });
  };

  const fetchNewQuestion = async () => {
    if (apiCooldown > 0) return;
    setLoading(true);
    clearQuestionState(currentRound);

    try {
      if (currentRound === 'ماذا تعرف' || currentRound === 'المزاد') {
        const prompt = generateQuestionPrompt(currentRound, Math.random());
        setVarVerdict('⏳ جاري التوليد من الكتالوج الشامل...');
        const qText = await callGroq(prompt, "أنت صانع أسئلة كروية دقيق.");
        setQuestion(extractJson(qText));
        setVarVerdict('✅ تم التوليد بنجاح!');

      } else if (currentRound === 'قصة') {
        setVarVerdict('⏳ جاري بناء القصة من ويكيبيديا وتقسيمها برمجياً...');
        const storyStars = ["كريستيانو رونالدو", "ميسي", "رونالدو (لاعب كرة قدم برازيلي)", "تيري هنري", "تشافي هيرنانديز", "كيفين دي بروين", "باولو مالديني", "ديدييه دروغبا"];
        const randomTarget = storyStars[Math.floor(Math.random() * storyStars.length)];
        const wikiData = await fetchPlayerWikiData(randomTarget);

        const prompt = `اللاعب هو: "${randomTarget}". استمد المعلومات من: (${wikiData}).
المطلوب 3 تلميحات منفصلة بأسلوب المتكلم (أنا)، يمنع ذكر اسم اللاعب أو ميلاده.

أرجع JSON مطابق لهذا الهيكل حصراً:
{
  "target": "${randomTarget}", 
  "hint1": "تلميح صعب: اذكر 6 أسماء لاعبين غير مشهورين جداً زاملتهم في بداياتي (استخدم صيغة: زاملت اللاعب كذا وكذا). ممنوع ذكر أندية.", 
  "hint2": "تلميح متوسط: اذكر 3 أندية متوسطة أو بدايات لعبت لها. ممنوع ذكر الزملاء.", 
  "hint3": "تلميح سهل: اذكر أبرز إنجاز لي (بطولة أو رقم قياسي)، واسمين لأشهر أساطير زاملتهم." 
}`;

        const qText = await callGroq(prompt, "أنت خبير أرشيف، تلتزم حرفياً بتقسيم الـ JSON بدون دمج المعلومات.");
        setQuestion(extractJson(qText));
        setVarVerdict('✅ تم استخراج القصة مفصولة التلميحات بدقة!');

      } else if (currentRound === 'التعويض') {
        setVarVerdict('⏳ جاري سحب المسيرة الدقيقة من صندوق ويكيبيديا...');
        const playersList = roundModifiers.hardCareerActive
          ? ["نيكولا أنيلكا", "كريستيان فييري", "روميلو لوكاكو", "أرتورو فيدال"]
          : ["إبراهيموفيتش", "ألفارو موراتا", "خاميس رودريغيز", "إدين دجيكو"];

        const randomTarget = playersList[Math.floor(Math.random() * playersList.length)];
        const wikiData = await fetchPlayerWikiData(randomTarget);
        setRawWikiCareerText(wikiData);

        const prompt = `اللاعب هو: "${randomTarget}". من كود ويكيبيديا (المسيرة الاحترافية): (${wikiData}). المطلوب: مسيرة الأندية بالترتيب الزمني الصحيح حصراً. لا تنقص نادياً ولا تزد. أرجع JSON: {"target": "${randomTarget}", "career_path": "نادي1، نادي2، نادي3..."}`;

        const qText = await callGroq(prompt, "أنت أرشيف كروي تنقل الأندية بالترتيب حرفياً.");
        setQuestion(extractJson(qText));
        setVarVerdict('✅ تم استخراج المسيرة بنجاح!');

      } else {
        // الجرس وسين جيم (سحب من القاعدة المحلية الخالية من الهبد)
        setVarVerdict('⏳ جاري سحب سؤال موثق من قاعدة البيانات المحلية...');
        const availableQuestions = TRIVIA_DB.filter(q => q.type === currentRound);
        const randomQ = availableQuestions[Math.floor(Math.random() * availableQuestions.length)];

        setTimeout(() => {
          setQuestion({ question: randomQ.q, answer: randomQ.a });
          setVarVerdict('✅ تم سحب سؤال كروي بإجابة قاطعة 100%!');
          setLoading(false);
        }, 600); 
        return; 
      }
    } catch (err) {
      setVarVerdict(`❌ إيرور التوليد: ${err.message}`);
    }

    triggerCooldown();
    setLoading(false);
  };

  const handlePrintWikiCareer = async () => {
    if (!rawWikiCareerText) { setVarVerdict('❌ لا توجد بيانات محفوظة للمسيرة.'); return; }
    setLoading(true);
    setVarVerdict('⏳ جاري استخراج الجدول الأصلي لـ VAR...');
    const prompt = `كود ويكيبيديا:${rawWikiCareerText}. استخرج "المسيرة الاحترافية" واطبع (السنوات - النادي) كنص مرتب تحت بعضه بدون تأليف. أرجع JSON: {"result": "النص"}`; 
    try { 
      const res = await callGroq(prompt, "محلل نصوص"); 
      setUpdatedCareer(extractJson(res).result); 
      setShowWikiCareer(true); 
      setVarVerdict('✅ تم عرض المسيرة من المصدر الأصلي!'); 
    } catch(e) { 
      setVarVerdict(`❌ خطأ: ${e.message}`); 
    }
    setLoading(false);
  };

  const handleCheckSpecificAnswer = async (playerKey) => {
    const answer = roundInputs[playerKey];
    if (!answer.trim() || apiCooldown > 0) return;

    if (currentRound === 'ماذا تعرف') {
      const isDuplicate = guessedAnswers.some(ans => ans.toLowerCase() === answer.trim().toLowerCase());
      if (isDuplicate) {
        handleManualStrike(playerKey, `❌ مكررة (${answer})! سترايك.`);
        setRoundInputs(prev => ({ ...prev, [playerKey]: '' }));
        return;
      }
    }
    executeVARCheck(playerKey, answer.trim());
    setRoundInputs(prev => ({ ...prev, [playerKey]: '' }));
  };

  const executeVARCheck = async (playerKey, customAnswer = null) => {
    const answerToCheck = customAnswer || userInput;
    if (!answerToCheck.trim() || !question || apiCooldown > 0) return;

    setLoading(true);
    setVarVerdict(`🖥️ الـ VAR يتحقق من (${answerToCheck})...`);

    let targetTerm = question.question || question.target || question.career_path || "";
    if ((currentRound === 'فقرة الجرس' || currentRound === 'سين جيم') && question.answer) {
      targetTerm = `السؤال:${question.question}. الإجابة النموذجية: ${question.answer}`;
    }

    const wikiInfo = await searchWikipedia(answerToCheck);
    const googleInfo = await searchGoogle(`${answerToCheck} ${targetTerm} إحصائيات 2026`);

    const varPrompt = `الهدف: "${targetTerm}". إجابة اللاعب: "${answerToCheck}". بيانات البحث: (${wikiInfo}) (${googleInfo}). هل الإجابة صحيحة كروياً (لا للكيان الصهيوني)؟ أرجع JSON: {"isCorrect": true/false, "explanation": "السبب"}`;

    try {
      const decision = extractJson(await callGroq(varPrompt, "حكم VAR صارم."));
      processVARDecision(decision, playerKey, answerToCheck);
    } catch (err) { setVarVerdict(`❌ إيرور الـ VAR: ${err.message}`); }

    triggerCooldown();
    setLoading(false);
  };

  const processVARDecision = (decision, playerKey, evaluatedAnswer) => {
    const opponentKey = playerKey === 'p1' ? 'p2' : 'p1';
    if (currentRound === 'ماذا تعرف') {
      if (decision.isCorrect) {
        setVarVerdict(`✅ صح! (${decision.explanation})`); 
        setGuessedAnswers(prev => { 
          const newList = [...prev, evaluatedAnswer]; 
          if (question.max_answers && newList.length >= question.max_answers) { 
            setVarVerdict('🎉 تم اكتشاف جميع الإجابات!'); 
            setTimeout(() => wrapUpMazaTarafRound(), 2500); 
          } 
          return newList; 
        }); 
      } else {
        handleManualStrike(playerKey, `❌ خطأ (${evaluatedAnswer})! ${decision.explanation}`); 
      }
    } else if (currentRound === 'المزاد') { 
      if (decision.isCorrect) { 
        setVarVerdict('✅ صحيح!'); 
        setAuctionCounters(prev => { 
          const updated = prev.correct + 1; 
          if (updated >= bids.targetValue) { 
            adjustScore(playerKey, bids.targetValue >= 30 ? 3 : 2, '🏆 بطل المزاد جاب الهدف!'); 
            setIsTimerActive(false); 
          } 
          return { ...prev, correct: updated }; 
        }); 
      } else { 
        setVarVerdict('❌ خطأ!'); 
        setAuctionCounters(prev => { 
          const updated = prev.errors + 1; 
          if (updated > 5) { 
            adjustScore(playerKey, -1, "❌ تجاوزت 5 أخطاء! خصم نقطة."); 
            adjustScore(opponentKey, 1, "نقطة للخصم."); 
            setIsTimerActive(false); 
          } 
          return { ...prev, errors: updated }; 
        }); 
      } 
    } else if (currentRound === 'فقرة الجرس' || currentRound === 'سين جيم') { 
      if (roundModifiers.exclusiveActive) { 
        if (decision.isCorrect) adjustScore(roundModifiers.exclusiveActive, 1, "✅ صح في الحصري!"); 
        else adjustScore(roundModifiers.exclusiveActive === 'p1' ? 'p2' : 'p1', 1, "❌ خطأ بالحصري! النقطة للخصم."); 
      } else { 
        if (decision.isCorrect) adjustScore(playerKey, 1, "🔔 صح! نقطة."); 
        else setVarVerdict('❌ خطأ! السؤال للثاني.'); 
      } 
    } else { 
      if (decision.isCorrect) { 
        let pts = currentRound === 'قصة' ? (storyHintLevel === 1 ? 3 : storyHintLevel === 2 ? 2 : 1) : 2; 
        adjustScore(playerKey, pts, `✅ صح! ${pts} نقاط.`);
        setIsTimerActive(false);
      } else {
        setPlayers(prev => {
          const currentAttempts = prev[playerKey].attempts - 1;
          setVarVerdict(`❌ خطأ! المتبقي ${currentAttempts} محاولات.`);
          return { ...prev, [playerKey]: { ...prev[playerKey], attempts: Math.max(0, currentAttempts) } };
        });
      }
    }
    if(!customAnswer) setUserInput('');
  };

  const wrapUpMazaTarafRound = () => {
    if (players.p1.strikes === players.p2.strikes) {
      adjustScore('p1', 1); adjustScore('p2', 1, "🏁 تعادل بالسترايكات! نقطة لكل لاعب.");
    } else {
      const winner = players.p1.strikes < players.p2.strikes ? 'p1' : 'p2';
      adjustScore(winner, players[winner].strikes === 0 ? 2 : 1, '🏁 نقطة للفائز بالسترايك الأقل!');
    }
  };

  const triggerAuctionTimer = () => { if (bids.winner) { setTimer(30); setIsTimerActive(true); setVarVerdict('⏱️ العداد شغال!'); } };
  const lockAuctionLimitButton = (playerKey, val) => {
    if (!players[playerKey].auctionSpecUsed) {
      setBids(prev => ({ ...prev, winner: playerKey, targetValue: parseInt(val) || 20 }));
      setPlayers(prev => ({ ...prev, [playerKey]: { ...prev[playerKey], auctionSpecUsed: true } }));
      setVarVerdict('🎯 تم القفل!');
    }
  };

  if (isSetup) {
    return (
      <div style={{ padding: '30px', maxWidth: '600px', margin: '50px auto', fontFamily: 'Arial, sans-serif', direction: 'rtl', backgroundColor: '#161a1d', color: '#fff', borderRadius: '15px' }}>
        <h1 style={{ textAlign: 'center', color: '#e94560' }}>🏆 إعداد تحدي الثلاثين</h1>
        <p style={{ textAlign: 'center', color: '#888' }}>نسخة الدستور الكروي الشامل 🔥</p>
        <div style={{ margin: '25px 0' }}><label>👤 اللاعب الأول:</label><input type="text" value={setupNames.p1} onChange={e => setSetupNames({...setupNames, p1: e.target.value})} style={{ width: '100%', padding: '14px', borderRadius: '8px', background: '#222', color: '#fff', marginTop: '10px' }} /></div>
        <div style={{ margin: '25px 0' }}><label>👤 اللاعب الثاني:</label><input type="text" value={setupNames.p2} onChange={e => setSetupNames({...setupNames, p2: e.target.value})} style={{ width: '100%', padding: '14px', borderRadius: '8px', background: '#222', color: '#fff', marginTop: '10px' }} /></div>
        <button onClick={startGame} style={{ width: '100%', padding: '15px', background: '#e94560', color: '#fff', border: 'none', borderRadius: '10px', fontSize: '18px', fontWeight: 'bold', cursor: 'pointer' }}>بدء المباراة 🚀</button>
      </div>
    );
  }

  return (
    <div style={{ padding: '20px', maxWidth: '900px', margin: '0 auto', fontFamily: 'Arial, sans-serif', direction: 'rtl', backgroundColor: '#0b0c10', color: '#c5c6c7', minHeight: '100vh' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', backgroundColor: '#1f2833', padding: '20px', borderRadius: '12px', marginBottom: '20px' }}>
        <div style={{ textAlign: 'center', width: '35%' }}>
          <h2 style={{ color: '#45f3ff', margin: '0 0 10px 0' }}>{players.p1.name}</h2>
          <h1 style={{ fontSize: '55px', color: '#fff', margin: '0' }}>{players.p1.score}</h1>
          <div style={{ margin: '10px 0' }}>
            <span style={{ color: players.p1.strikes >= 1 ? '#ff4d4d' : '#444', fontSize: '20px' }}>❌</span>
            <span style={{ color: players.p1.strikes >= 2 ? '#ff4d4d' : '#444', fontSize: '20px' }}>❌</span>
            <span style={{ color: players.p1.strikes >= 3 ? '#ff4d4d' : '#444', fontSize: '20px' }}>❌</span>
          </div>
        </div>
        <div style={{ display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center' }}>
          <div style={{ padding: '10px 15px', border: '2px solid #45f3ff', borderRadius: '10px', color: '#45f3ff', fontWeight: 'bold', fontSize:'20px' }}>VS</div>
          {isTimerActive && <div style={{ fontSize: '35px', color: '#ff4d4d', fontWeight: 'bold', marginTop: '15px' }}>{timer}s</div>}
        </div>
        <div style={{ textAlign: 'center', width: '35%' }}>
          <h2 style={{ color: '#66fcf1', margin: '0 0 10px 0' }}>{players.p2.name}</h2>
          <h1 style={{ fontSize: '55px', color: '#fff', margin: '0' }}>{players.p2.score}</h1>
          <div style={{ margin: '10px 0' }}>
            <span style={{ color: players.p2.strikes >= 1 ? '#ff4d4d' : '#444', fontSize: '20px' }}>❌</span>
            <span style={{ color: players.p2.strikes >= 2 ? '#ff4d4d' : '#444', fontSize: '20px' }}>❌</span>
            <span style={{ color: players.p2.strikes >= 3 ? '#ff4d4d' : '#444', fontSize: '20px' }}>❌</span>
          </div>
        </div>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '10px', marginBottom: '20px' }}>
        {CONFIG.ROUNDS.map(round => (
          <button key={round} onClick={() => { setCurrentRound(round); setRoundQuestionIndex(1); clearQuestionState(round); }} style={{ padding: '15px', fontWeight: 'bold', border: 'none', borderRadius: '8px', cursor: 'pointer', backgroundColor: currentRound === round ? '#45f3ff' : '#1f2833', color: currentRound === round ? '#000' : '#fff' }}>{round}</button>
        ))}
      </div>

      <div style={{ backgroundColor: '#1f2833', padding: '25px', borderRadius: '12px', marginBottom: '20px' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px' }}>
          <h2 style={{ color: '#45f3ff', margin: 0 }}>📋 {currentRound}</h2>
          <div style={{ display: 'flex', gap: '10px' }}>
            <button onClick={fetchNewQuestion} disabled={loading || apiCooldown > 0} style={{ padding: '12px 20px', background: '#4c9a2a', color: '#fff', border: 'none', borderRadius: '6px', fontWeight: 'bold', cursor: 'pointer' }}>{loading ? '⏳ جاري التوليد...' : '🎲 توليد سؤال'}</button>
            <button onClick={() => setRoundQuestionIndex(prev => prev + 1)} style={{ padding: '12px 20px', background: '#333', color: '#fff', border: 'none', borderRadius: '6px', cursor: 'pointer' }}>➡️ التالي</button>
          </div>
        </div>

        {question && (
          <div style={{ backgroundColor: '#0b0c10', padding: '20px', borderRadius: '8px', borderRight: '5px solid #45f3ff' }}>
            <h3 style={{ margin: '0 0 10px 0', color: '#fff', lineHeight: '1.5' }}>
              {currentRound === 'التعويض' ? <span><span style={{color: '#888'}}>المسيرة:</span> {question.career_path}</span> : question.question || question.career_path}
            </h3>

            {currentRound === 'ماذا تعرف' && question.max_answers && (
              <div style={{ marginTop: '15px', padding: '15px', background: '#111', borderRadius: '8px' }}>
                <h4 style={{ color: '#ffb703' }}>🎯 العدد الأقصى: {question.max_answers}</h4>
                <p style={{ color: '#fff' }}>المكتشفة: {guessedAnswers.map((ans, i) => <span key={i} style={{ background: '#4c9a2a', padding: '4px', borderRadius: '4px', margin: '0 5px' }}>{ans}</span>)}</p>
              </div>
            )}

            {currentRound === 'قصة' && (
              <div style={{ marginTop: '15px' }}>
                <div style={{ padding: '12px', background: '#1f2833', borderRadius: '6px', marginBottom: '8px' }}>1 (الزملاء): {question.hint1}</div>
                <div style={{ padding: '12px', background: storyHintLevel >= 2 ? '#1f2833' : '#111', borderRadius: '6px', marginBottom: '8px', color: storyHintLevel >= 2 ? '#fff' : '#444' }}>2 (الأندية): {storyHintLevel >= 2 ? question.hint2 : 'محجوب...'}</div>
                <div style={{ padding: '12px', background: storyHintLevel >= 3 ? '#1f2833' : '#111', borderRadius: '6px', marginBottom: '8px', color: storyHintLevel >= 3 ? '#fff' : '#444' }}>3 (الأحداث): {storyHintLevel >= 3 ? question.hint3 : 'محجوب...'}</div>
                <button onClick={() => setStoryHintLevel(prev => Math.min(3, prev + 1))} style={{ padding: '10px 15px', background: '#8338ec', color: '#fff', border: 'none', borderRadius: '6px', cursor: 'pointer' }}>تلميح تالي 🔓</button>
              </div>
            )}

            {(currentRound === 'قصة' || currentRound === 'التعويض' || currentRound === 'فقرة الجرس' || currentRound === 'سين جيم') && (
              <div style={{ marginTop: '15px', padding: '10px', background: '#111', color: '#ffcc00' }}>الجواب المخفي: <span style={{ color: '#000', background: '#000', padding: '2px 5px', cursor:'pointer' }} onMouseEnter={(e) => {e.target.style.color = '#ffcc00';}} onMouseLeave={(e) => {e.target.style.color = '#000';}}>{question.target || question.answer}</span></div>
            )}

            {currentRound === 'التعويض' && (
              <div style={{ marginTop: '20px' }}>
                <button onClick={handlePrintWikiCareer} disabled={loading || !rawWikiCareerText} style={{ width: '100%', padding: '12px', background: '#f77f00', color: '#fff', border: 'none', borderRadius: '6px', cursor: 'pointer' }}>🔄 تأكيد المسيرة من ويكيبيديا (VAR)</button>
                {showWikiCareer && updatedCareer && <div style={{ marginTop: '15px', padding: '15px', background: '#222', color: '#45f3ff', whiteSpace: 'pre-wrap' }}>{updatedCareer}</div>}
              </div>
            )}
          </div>
        )}

        {(currentRound === 'ماذا تعرف' || currentRound === 'سين جيم' || currentRound === 'التعويض' || currentRound === 'قصة') && question && (
          <div style={{ display: 'flex', gap: '15px', marginTop: '20px' }}>
            {['p1', 'p2'].map(p => (
              <div key={p} style={{ flex: 1, background: '#0b0c10', padding: '15px', borderRadius: '10px', borderTop: `4px solid ${p==='p1'?'#45f3ff':'#66fcf1'}`, opacity: players[p].strikes >= 3 || players[p].attempts <= 0 ? 0.5 : 1 }}>
                <h4 style={{ color: p==='p1'?'#45f3ff':'#66fcf1', textAlign: 'center' }}>إجابة {players[p].name}</h4>
                <input type="text" value={roundInputs[p]} onChange={(e) => setRoundInputs({ ...roundInputs, [p]: e.target.value })} style={{ width: '100%', padding: '12px', background: '#222', color: '#fff', border: 'none', marginBottom: '10px' }} />
                <button onClick={() => handleCheckSpecificAnswer(p)} disabled={loading} style={{ width: '100%', padding: '10px', background: '#023e8a', color: '#fff', border: 'none', cursor: 'pointer' }}>تأكيد</button>
              </div>
            ))}
          </div>
        )}

        <div style={{ marginTop: '20px', padding: '20px', background: '#111', borderRadius: '8px' }}>
          {currentRound === 'ماذا تعرف' && (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
              <button onClick={wrapUpMazaTarafRound} style={{ padding: '12px', background: '#00b4d8', color: '#fff', border: 'none', borderRadius: '6px', cursor: 'pointer' }}>🏁 إنهاء واحتساب النقاط</button>
            </div>
          )}

          {currentRound === 'المزاد' && (
            <div>
              <div style={{ display: 'flex', gap: '10px', marginBottom: '15px' }}>
                {['p1', 'p2'].map(p => (
                  <div key={p} style={{ flex: 1 }}>
                    <input type="number" onChange={(e) => setBids({ ...bids, [p]: e.target.value })} placeholder={`مزاد ${players[p].name}`} style={{ width: '100%', padding: '10px' }} />
                    <button onClick={() => lockAuctionLimitButton(p, bids[p])} style={{ width: '100%', marginTop: '8px', background: '#ffb703', cursor: 'pointer', border:'none', padding:'8px' }}>قفل متاح</button>
                  </div>
                ))}
              </div>
              <div style={{ display: 'flex', gap: '10px' }}>
                <button onClick={() => setBids({ ...bids, winner: 'p1', targetValue: bids.p1 })} style={{ flex: 1, padding: '12px', background: '#023e8a', color: '#fff', border:'none', cursor:'pointer'}}>ترسية لـ 1</button>
                <button onClick={() => setBids({ ...bids, winner: 'p2', targetValue: bids.p2 })} style={{ flex: 1, padding: '12px', background: '#023e8a', color: '#fff', border:'none', cursor:'pointer'}}>ترسية لـ 2</button>
              </div>
              <button onClick={triggerAuctionTimer} style={{ width: '100%', padding: '15px', background: '#e63946', color: '#fff', border: 'none', marginTop: '15px', cursor: 'pointer' }}>⏱️ بدء المزاد والتوقيت</button>
              {bids.winner && (
                <div style={{ textAlign: 'center', marginTop: '15px', padding: '15px', background: '#222' }}>
                  <p style={{ color: '#fff' }}>الهدف: {bids.targetValue} | صح: <span style={{ color: '#4c9a2a' }}>{auctionCounters.correct}</span> | أخطاء: <span style={{ color: '#d90429' }}>{auctionCounters.errors}/5</span></p>
                  <button onClick={() => setAuctionCounters(p => ({ ...p, correct: p.correct + 1 }))} style={{ padding: '8px 20px', background: '#4c9a2a', color: '#fff', margin: '0 5px', border: 'none' }}>+1 صح</button>
                  <button onClick={() => setAuctionCounters(p => ({ ...p, errors: p.errors + 1 }))} style={{ padding: '8px 20px', background: '#d90429', color: '#fff', margin: '0 5px', border: 'none' }}>+1 خطأ</button>
                </div>
              )}
            </div>
          )}

          {(currentRound === 'فقرة الجرس' || currentRound === 'سين جيم') && (
            <div style={{ display: 'flex', gap: '10px' }}>
              <button onClick={() => setRoundModifiers({ ...roundModifiers, exclusiveActive: 'p1' })} style={{ flex: 1, padding: '12px', background: '#f72585', color: '#fff', border: 'none', cursor: 'pointer' }}>⭐ حصري 1</button>
              <button onClick={() => setRoundModifiers({ ...roundModifiers, exclusiveActive: 'p2' })} style={{ flex: 1, padding: '12px', background: '#f72585', color: '#fff', border: 'none', cursor: 'pointer' }}>⭐ حصري 2</button>
            </div>
          )}
        </div>
      </div>

      <div style={{ backgroundColor: '#112233', padding: '25px', borderRadius: '12px', border: '1px solid #45f3ff' }}>
        <h3 style={{ margin: '0 0 15px 0', color: '#45f3ff' }}>🖥️ غرفة الـ VAR</h3>
        <input type="text" value={userInput} onChange={(e) => setUserInput(e.target.value)} placeholder="أدخل إجابة اللاعب للتحقق الحاسم..." style={{ width: '100%', padding: '15px', background: '#0b0c10', color: '#fff', border: '1px solid #45f3ff', marginBottom: '15px' }} />
        <div style={{ display: 'flex', gap: '10px' }}>
          <button onClick={() => executeVARCheck('p1')} style={{ flex: 1, padding: '15px', background: '#e94560', color: '#fff', border: 'none', cursor: 'pointer' }}>VAR لـ {players.p1.name}</button>
          <button onClick={() => executeVARCheck('p2')} style={{ flex: 1, padding: '15px', background: '#0f3460', color: '#fff', border: 'none', cursor: 'pointer' }}>VAR لـ {players.p2.name}</button>
        </div>
        {varVerdict && <div style={{ marginTop: '20px', color: '#66fcf1', padding: '15px', background: '#0b0c10', borderLeft: '4px solid #45f3ff' }}>{varVerdict}</div>}
      </div>

      <div style={{ marginTop: '25px', padding: '15px', background: '#1c1d22', display: 'flex', justifyContent: 'center', gap: '10px' }}>
        <button onClick={() => adjustScore('p1', 1)} style={{ padding: '8px 15px', background: '#333', color: '#fff', border: 'none', cursor: 'pointer' }}>+1 لـ 1</button>
        <button onClick={() => adjustScore('p1', -1)} style={{ padding: '8px 15px', background: '#333', color: '#fff', border: 'none', cursor: 'pointer' }}>-1 لـ 1</button>
        <button onClick={() => adjustScore('p2', 1)} style={{ padding: '8px 15px', background: '#333', color: '#fff', border: 'none', cursor: 'pointer' }}>+1 لـ 2</button>
        <button onClick={() => adjustScore('p2', -1)} style={{ padding: '8px 15px', background: '#333', color: '#fff', border: 'none', cursor: 'pointer' }}>-1 لـ 2</button>
      </div>
    </div>
  );
}
