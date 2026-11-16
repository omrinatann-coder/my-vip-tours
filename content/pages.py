"""Every content page on the site. Each URL keeps the language it had on the
old Base44 site; `alt` links a page to its version in the other language.

group: service | route | tour | city | vip | diaspora  (menus and footer)
"""
from services import SERVICES as _S

_SV = {s["slug"]: s for s in _S}


def _from(slug, lang, path, alt=None, group="service", vehicles=None, extra="", **over):
    """Page built from a text in services.py, with overrides."""
    x = dict(_SV[slug][lang])
    x.update(over)
    if extra:
        x["body"] = x["body"] + extra
    return {"path": path, "lang": lang, "alt": alt, "group": group,
            "vehicles": vehicles or _SV[slug]["vehicles"], **x}


def P(path, lang, group, nav, title, desc, h1, lead, body, vehicles, alt=None, related=(), articles=(), tours=False):
    return {"path": path, "lang": lang, "alt": alt, "group": group, "nav": nav, "title": title, "desc": desc,
            "h1": h1, "lead": lead, "body": body, "vehicles": vehicles, "related": list(related),
            "articles": list(articles), "tours": tours}


_ACCESS_HE = """
<h2>רכב ייעודי עם מעלון</h2>
<p>השירות ניתן ברכב ייעודי עם מעלון (Mercedes V-Class). לא כל רכב בצי מתאים לכל כיסא גלגלים, ולכן מתאמים מראש את סוג המעלון, את מידות הכיסא ומשקלו, את מספר הנוסעים והמלווים, ואת אמצעי העיגון והבטיחות.</p>
"""
_ACCESS_EN = """
<h2>A dedicated vehicle with a lift</h2>
<p>The service runs in a dedicated vehicle with a wheelchair lift (Mercedes V-Class). Not every vehicle in the fleet fits every wheelchair, so we agree in advance on the lift type, the chair's dimensions and weight, the number of passengers and companions, and the securing and safety equipment.</p>
"""

PAGES = [
# ------------------------------------------------------------------ Hebrew services
_from("ben-gurion-airport-transfers", "he", "/hasaot-menatbag", alt="/ben-gurion-airport-transfers",
      related=["/monit-tel-aviv-natbag", "/monit-yerushalayim-natbag", "/nahag-prati"],
      articles=["/blog/6ade3177ac824cd0a53548ab", "/blog/ben-gurion-transfer-guide"],
      extra="""
<h2>טרמינל 1 או 3</h2>
<p>כתבו בהזמנה מאיזה טרמינל אתם טסים או נוחתים. בנחיתה, הנהג מגיע לפי שעת הנחיתה בפועל, גם כשהטיסה מתעכבת.</p>
"""),
_from("private-driver-israel", "he", "/nahag-prati", alt="/private-driver-israel",
      related=["/rechavei-yukra", "/siur-yerushalayim", "/monit-yerushalayim-tel-aviv"],
      articles=["/blog/private-day-tours-from-tel-aviv"],
      extra="""
<h2>לשעה, לחצי יום או ליום שלם</h2>
<p>אפשר להזמין נהג לשעה, לחצי יום (4 שעות), ליום שלם (8 שעות) או לכמה ימים. הנהגים דוברים עברית, אנגלית ורוסית, כך שהשירות מתאים גם לאורחים מחו"ל.</p>
"""),
_from("israel-private-tours", "he", "/siurim-pratiyim", alt="/israel-private-tours", group="tour", tours=True,
      related=["/siur-yerushalayim", "/tiyul-yam-hamelach", "/tiyul-galil", "/tiyul-eilat"],
      articles=["/blog/private-day-tours-from-tel-aviv", "/blog/israel-family-trip-tips"]),
_from("private-transportation-israel", "he", "/hasaot-beisrael", alt="/israel-transportation-services",
      nav="הסעות בכל הארץ", h1="הסעות בכל הארץ",
      title="הסעות בכל הארץ | מונית, ואן, מיניבוס ואוטובוס עם נהג | Tour VIP",
      related=["/hasaot-tel-aviv", "/hasaot-yerushalayim", "/hasaot-haifa", "/hasaot-beer-sheva", "/hasaot-netanya",
               "/hasaot-ashdod", "/hasaot-rishon-lezion", "/hasaot-petah-tikva"],
      articles=["/blog/choosing-vehicle-size", "/blog/event-transportation-checklist"]),
_from("accessible-transportation", "he", "/accessible-transportation", alt="/en/accessible-transportation",
      vehicles=["van6"], extra=_ACCESS_HE,
      related=["/hasaot-menatbag", "/nahag-prati"], articles=["/blog/accessible-ride-planning"]),
_from("19-passenger-minibus-israel", "he", "/minibus-hashara", alt="/19-passenger-minibus-israel",
      nav="השכרת מיניבוס", h1="השכרת מיניבוס עם נהג",
      title="השכרת מיניבוס עם נהג | 16, 19 ו-22 מקומות | Tour VIP",
      desc="השכרת מיניבוס עם נהג ל-16, 19 או 22 נוסעים: לפי שעה, חצי יום או יום שלם. לטיולים, אירועים, הסעות עובדים ואיסוף מנתב\"ג. הזמנה בוואטסאפ 054-283-1111.",
      lead="מיניבוס של 16, 19 או 22 מקומות עם נהג, לפי שעה, לחצי יום או ליום שלם. כל הקבוצה ברכב אחד, ממקום למקום בכל הארץ.",
      related=["/hasaot-iruvim", "/tiyul-galil", "/tiyul-eilat"],
      articles=["/blog/choosing-vehicle-size", "/blog/event-transportation-checklist"]),
_from("hasaot-iruvim", "he", "/hasaot-iruvim", alt="/en/event-transportation",
      related=["/hasaot-chasuna", "/hasaot-bar-mitzva", "/minibus-hashara"],
      articles=["/blog/event-transportation-checklist"]),

# ------------------------------------------------------------------ Hebrew routes
P("/monit-tel-aviv-natbag", "he", "route", "מונית מתל אביב לנתב\"ג",
  "מונית מתל אביב לנתב\"ג | הסעה פרטית 24/7 | Tour VIP",
  "מונית והסעה פרטית מתל אביב לנתב\"ג ובחזרה, 24/7 כולל שבת וחגים. כ-20 ק\"מ ו-20–30 דקות בלי עומס. מונית, ואן ומיניבוס. 054-283-1111.",
  "מונית מתל אביב לנתב\"ג",
  "איסוף מהבית, מהמלון או מהמשרד בתל אביב, ישר לטרמינל. גם בלילה, בשבת ובחגים.",
  """
<h2>כמה זמן לוקחת הנסיעה</h2>
<p>המרחק מתל אביב לנתב"ג הוא כ-20 ק"מ. בלי עומסים הנסיעה אורכת 20–30 דקות, ובשעות העומס עד 45–60 דקות. לטיסה בינלאומית מקובל להגיע לטרמינל כשלוש שעות לפני ההמראה, ולפי זה קובעים את שעת האיסוף.</p>
<h2>מאיפה אוספים</h2>
<p>מכל כתובת בתל אביב-יפו: דירות, מלונות על קו החוף, משרדים ויפו. אם אתם במלון, כתבו את שם המלון ונאסוף מהכניסה.</p>
<h2>גם מהשדה הביתה</h2>
<p>בנחיתה, הנהג עוקב אחרי מספר הטיסה ומגיע לפי שעת הנחיתה בפועל. כתבו בהזמנה את מספר הטיסה ואת הטרמינל: 1 או 3.</p>
<h2>איזה רכב</h2>
<ul><li>עד 4 נוסעים: מונית.</li><li>משפחה עם מזוודות: ואן 6 או 7 מקומות.</li><li>קבוצה: מיניבוס 16, 19 או 22 מקומות.</li></ul>
""", ["taxi4", "van6", "van7", "mini16"],
  related=["/monit-yerushalayim-natbag", "/hasaot-menatbag", "/hasaot-tel-aviv"],
  articles=["/blog/ben-gurion-transfer-guide"]),

P("/monit-yerushalayim-natbag", "he", "route", "מונית מירושלים לנתב\"ג",
  "מונית מירושלים לנתב\"ג ובחזרה | הסעה פרטית 24/7 | Tour VIP",
  "מונית והסעה פרטית מירושלים לנתב\"ג ומנתב\"ג לירושלים, 24/7 כולל שבת וחגים. כ-50 ק\"מ, 45–50 דקות בלי עומס. תשלום במזומן, אשראי, Bit ופייבוקס.",
  "מונית מירושלים לנתב\"ג",
  "נסיעה ישירה מכל כתובת בירושלים לנמל התעופה, ומהשדה חזרה לבית או למלון בירושלים.",
  """
<h2>זמן הנסיעה</h2>
<p>המרחק כ-50 ק"מ. בתנאי תנועה רגילים הנסיעה אורכת 45–50 דקות, ובבוקר ובערבי חג כביש 1 עמוס יותר. לכן קובעים איתכם שעת יציאה עם מרווח.</p>
<h2>בשני הכיוונים</h2>
<p>לטיסה יוצאת אוספים מהכתובת בירושלים. בנחיתה, הנהג ממתין באולם הנכנסים ועוקב אחרי שעת הנחיתה בפועל. מסרו מספר טיסה וטרמינל (1 או 3).</p>
<h2>תשלום</h2>
<p>אפשר לשלם במזומן, בכרטיס אשראי, ב-Bit ובפייבוקס. ציינו את אופן התשלום בהזמנה.</p>
<h2>איזה רכב</h2>
<ul><li>עד 4 נוסעים: מונית.</li><li>משפחה עם הרבה מזוודות: ואן 6 או 7 מקומות.</li><li>קבוצה: מיניבוס.</li></ul>
""", ["taxi4", "van6", "van7", "mini19"],
  related=["/monit-tel-aviv-natbag", "/monit-yerushalayim-tel-aviv", "/hasaot-yerushalayim"],
  articles=["/blog/6ade3177ac824cd0a53548ab", "/blog/ben-gurion-transfer-guide"]),

P("/monit-yerushalayim-tel-aviv", "he", "route", "מונית מירושלים לתל אביב",
  "מונית מירושלים לתל אביב ובחזרה | מדלת לדלת | Tour VIP",
  "מונית והסעה פרטית בין ירושלים לתל אביב, מדלת לדלת, 24/7 כולל שישי-שבת וחגים. נסיעה הלוך-חזור במחיר מיוחד. מונית, ואן ומיניבוס. 054-283-1111.",
  "מונית מירושלים לתל אביב",
  "מכתובת לכתובת בין שתי הערים, בלי החלפות ובלי לסחוב מזוודות לרכבת.",
  """
<h2>למה לא רכבת</h2>
<p>הרכבת מגיעה לתחנה, לא לכתובת. במונית פרטית נוסעים ישר מהדלת לדלת, עם המזוודות ברכב ובלי החלפות. זה משמעותי כשיש ילדים, מטען, או פגישה שאסור לאחר אליה.</p>
<h2>הלוך-חזור</h2>
<p>אפשר להזמין נסיעה הלוך-חזור, במחיר מיוחד. לימי פגישות עם כמה עצירות, עדיף <a href="/nahag-prati">נהג צמוד</a> שנשאר איתכם כל היום.</p>
<h2>מתי</h2>
<p>השירות פועל 24/7, כולל שישי-שבת וחגים. בשעות העומס הנסיעה ארוכה יותר, ולכן לפגישה בשעה קבועה כדאי לצאת עם מרווח.</p>
""", ["taxi4", "van6", "van7", "mini16"],
  related=["/nahag-prati", "/hasaot-yerushalayim", "/hasaot-tel-aviv"]),

# ------------------------------------------------------------------ Hebrew events
P("/hasaot-chasuna", "he", "service", "הסעות לחתונה",
  "הסעות לחתונה | אוטובוסים ומיניבוסים לאורחים | Tour VIP",
  "הסעות אורחים לחתונה מהבית לאולם ובחזרה: מיניבוסים 19-22 מקומות ואוטובוסים 35, 50 ו-60 מקומות, מסלולים לפי כתובות האורחים. הזמנה בוואטסאפ 054-283-1111.",
  "הסעות לחתונה",
  "האורחים מגיעים יחד ובזמן לחופה, וחוזרים הביתה בלי לנהוג אחרי האירוע.",
  """
<h2>מהבית לאולם ובחזרה</h2>
<p>אנחנו מסיעים את האורחים מהבית לאולם ובחזרה, ובונים את המסלולים לפי כתובות האורחים. אפשר אוטובוס אחד מאזור מרכזי, או כמה מיניבוסים מכמה אזורים.</p>
<h2>הנהגים</h2>
<p>הנהגים מגיעים בלבוש מכובד: חולצה לבנה ומכנסיים שחורים.</p>
<h2>מתי להזמין</h2>
<p>מומלץ להזמין חודש עד שלושה חודשים מראש, במיוחד בעונת החתונות בקיץ.</p>
<h2>רכב לזוג ולהורים</h2>
<p>לחתן ולכלה, להורים או לאורחים מכובדים אפשר להזמין <a href="/rechavei-yukra">רכב יוקרה עם נהג</a> לכל הערב.</p>
""", ["mini19", "mini22", "bus35", "bus50", "bus60"],
  related=["/hasaot-iruvim", "/hasaot-bar-mitzva", "/rechavei-yukra"],
  articles=["/blog/event-transportation-checklist"]),

P("/hasaot-bar-mitzva", "he", "service", "הסעות לבר מצווה",
  "הסעות לבר מצווה ובת מצווה | לכותל ולאולם | Tour VIP",
  "הסעות לבר מצווה ובת מצווה: לכותל, לבית הכנסת ולאולם, מכל הארץ. מיניבוסים ואוטובוסים לכל המשפחה, ואיסוף מנתב\"ג לאורחים מחו\"ל. 054-283-1111.",
  "הסעות לבר מצווה",
  "כל המשפחה מגיעה יחד לכותל, לבית הכנסת ולאולם, בלי לחפש חניה בירושלים.",
  """
<h2>עלייה לתורה בכותל</h2>
<p>הנהיגה והחניה ליד העיר העתיקה מסובכות, במיוחד בבוקר של שני וחמישי. ההסעה מורידה את כולם בנקודה הקרובה ביותר שמותרת לרכבים, ואוספת שוב בסיום.</p>
<h2>יום שלם, לוח זמנים אחד</h2>
<p>אפשר לבנות את כל היום כמסלול אחד: איסוף בבוקר, הטקס בכותל, סעודה במסעדה או באולם, וחזרה הביתה. ספרו לנו את סדר היום ונבנה את לוח הזמנים.</p>
<h2>אורחים מחו"ל ומבוגרים</h2>
<p>לאורחים שמגיעים במיוחד מחו"ל אפשר לשלב <a href="/hasaot-menatbag">איסוף מנתב"ג</a>. לסבים ולסבתות, ספרו לנו מראש אם צריך עזרה בעלייה לרכב או <a href="/accessible-transportation">רכב נגיש</a>.</p>
""", ["van7", "mini16", "mini19", "mini22", "bus50"],
  related=["/hasaot-iruvim", "/hasaot-chasuna", "/siur-yerushalayim"],
  articles=["/blog/event-transportation-checklist"]),

# ------------------------------------------------------------------ Hebrew tours
P("/siur-yerushalayim", "he", "tour", "סיור בירושלים",
  "סיור בירושלים עם נהג פרטי | העיר העתיקה, הכותל והר הזיתים | Tour VIP",
  "סיור פרטי בירושלים עם נהג צמוד: העיר העתיקה, הכותל המערבי, הר הזיתים ושוק מחנה יהודה. יום שלם בקצב שלכם, לזוגות, משפחות וקבוצות.",
  "סיור בירושלים עם נהג פרטי",
  "יום שלם בירושלים בקצב שלכם: העיר העתיקה, הכותל המערבי, הר הזיתים ושוק מחנה יהודה.",
  """
<h2>מסלול מוצע ליום אחד</h2>
<ul>
<li><strong>בוקר: העיר העתיקה והכותל המערבי.</strong> מתחילים מוקדם, לפני העומס.</li>
<li><strong>צהריים: תצפית מהר הזיתים</strong> על העיר העתיקה.</li>
<li><strong>אחר הצהריים: שוק מחנה יהודה</strong>, או מוזיאון ישראל ויד ושם, לפי מה שמעניין אתכם.</li>
</ul>
<p>אתם בוחרים את האתרים, והנהג מוריד אתכם בכניסה הנוחה ביותר לכל אחד ומחכה בסיום.</p>
<h2>לפני שקובעים תאריך</h2>
<ul>
<li>מומלץ להזמין לפחות 48 שעות מראש.</li>
<li>ביום שישי השוק עמוס ונסגר לקראת שבת, ובשבת חלק גדול מהעיר סגור.</li>
<li>במקומות קדושים נדרש לבוש צנוע: כתפיים וברכיים מכוסות.</li>
</ul>
""", ["taxi4", "van7", "mini19", "bus50"],
  related=["/siurim-pratiyim", "/tiyul-yam-hamelach", "/hasaot-yerushalayim"],
  articles=["/blog/private-day-tours-from-tel-aviv"]),

P("/tiyul-yam-hamelach", "he", "tour", "טיול לים המלח",
  "טיול לים המלח ומצדה עם נהג פרטי | עין גדי | Tour VIP",
  "טיול פרטי לים המלח, מצדה ועין גדי עם נהג צמוד: יציאה מוקדמת, עצירות בקצב שלכם וחזרה ישר למלון. למשפחות, זוגות וקבוצות. 054-283-1111.",
  "טיול לים המלח ומצדה",
  "יום מלא בדרום: מצדה, עין גדי וציפה בים המלח, עם נהג שמחכה בכל עצירה.",
  """
<h2>איך נראה היום</h2>
<p>מתל אביב זה בערך שעתיים נסיעה לכל כיוון, ומירושלים פחות. לכן יוצאים מוקדם, עולים למצדה לפני החום הכבד, עוצרים בעין גדי, ומסיימים בציפה בים המלח.</p>
<h2>מה לקחת</h2>
<ul><li>הרבה מים, כובע וקרם הגנה.</li><li>נעליים נוחות למצדה ולעין גדי.</li><li>בגד ים ומגבת, ונעלי מים לחוף.</li></ul>
<h2>לקבוצות ולמשפחות</h2>
<p>משפחה מורחבת או קבוצה נוסעות יחד במיניבוס או באוטובוס. בסוף היום חוזרים ישר למלון או הביתה, בלי לנהוג אחרי יום ארוך בשמש.</p>
""", ["van7", "mini16", "mini19", "bus50"],
  related=["/siurim-pratiyim", "/siur-yerushalayim", "/tiyul-eilat"],
  articles=["/blog/private-day-tours-from-tel-aviv"]),

P("/tiyul-galil", "he", "tour", "טיול לגליל",
  "טיול לגליל ולצפון עם נהג פרטי | כנרת, צפת וראש הנקרה | Tour VIP",
  "טיול פרטי לגליל ולצפון עם נהג צמוד: הכנרת, צפת, ראש הנקרה ותצפיות ברמת הגולן. מסלול גמיש, ומיניבוס לקבוצות ומשפחות מורחבות.",
  "טיול לגליל ולצפון",
  "הכנרת, צפת וראש הנקרה ביום אחד, עם נהג צמוד שמכיר את הדרכים בצפון.",
  """
<h2>מה רואים</h2>
<ul><li><strong>הכנרת</strong> וטבריה.</li><li><strong>צפת</strong> העתיקה וסמטאות האמנים.</li><li><strong>ראש הנקרה</strong> והנקרות שעל הים.</li></ul>
<p>אפשר גם לשלב תצפיות ברמת הגולן או ביקור ביקב.</p>
<h2>לא לנסות לראות הכול</h2>
<p>לטבריה זה בערך שעתיים מהמרכז, והאתרים בצפון רחוקים זה מזה. יום טוב כולל שניים או שלושה יעדים, לא חמישה. ספרו לנו מה הכי חשוב לכם ונבנה מסלול שמשאיר זמן ליהנות.</p>
<h2>קבוצות</h2>
<p>לקבוצות ולמשפחות מורחבות יש <a href="/minibus-hashara">מיניבוס עם נהג</a>, שעוצר בכל מקום שתבקשו.</p>
""", ["van7", "mini16", "mini19", "mini22"],
  related=["/siurim-pratiyim", "/minibus-hashara", "/hasaot-haifa"],
  articles=["/blog/private-day-tours-from-tel-aviv"]),

P("/tiyul-eilat", "he", "tour", "נסיעה לאילת",
  "נסיעה וטיול לאילת עם נהג | מיניבוס וואן למשפחות וקבוצות | Tour VIP",
  "נסיעה לאילת עם נהג, מכל מקום בארץ ועד המלון: עצירות בדרך, מכתש רמון ושדה בוקר, מקום לכל המזוודות. ואנים, מיניבוסים ואוטובוסים. 054-283-1111.",
  "נסיעה לאילת עם נהג",
  "מהבית עד המלון באילת, בלי שעות של נהיגה בערבה. החופשה מתחילה כבר ברכב.",
  """
<h2>הדרך</h2>
<p>מהמרכז זה כארבע עד חמש שעות נסיעה, תלוי בעצירות. הנהג קובע איתכם עצירות התרעננות, ואם רוצים, אפשר להפוך את הדרך לטיול: מכתש רמון, עבדת ושדה בוקר נמצאים על הדרך.</p>
<h2>מזוודות וציוד</h2>
<p>לחופשה משפחתית יש הרבה ציוד. כתבו בהזמנה כמה מזוודות, עגלות וציוד ים יש, ונתאים רכב עם מקום לכולם.</p>
<h2>כמה משפחות יחד</h2>
<p>כשכמה משפחות נוסעות יחד, <a href="/minibus-hashara">מיניבוס עם נהג</a> זול ונוח יותר מכמה רכבים. אפשר להזמין גם את הנסיעה חזרה.</p>
""", ["van6", "van7", "mini16", "mini19", "bus35"],
  related=["/tiyul-yam-hamelach", "/siurim-pratiyim", "/minibus-hashara"],
  articles=["/blog/israel-family-trip-tips"]),

# ------------------------------------------------------------------ Hebrew VIP
P("/rechavim-memugnay-yeri", "he", "vip", "רכבים ממוגני ירי",
  "רכבים ממוגני ירי עם נהג ומאבטח | הסעות מאובטחות | Tour VIP",
  "רכבים ממוגני ירי עם נהג מקצועי ואפשרות למאבטח חמוש: לאישי ציבור, דיפלומטים, מנהלים ומשלחות. איסוף מנתב\"ג, סיורים והסעות מאובטחות בכל הארץ.",
  "רכבים ממוגני ירי עם נהג",
  "נסיעה מאובטחת לאישי ציבור, דיפלומטים, מנהלים ואורחים שצריכים רמת ביטחון גבוהה.",
  """
<h2>מה זה רכב ממוגן ירי</h2>
<p>רכב שעבר התאמה מלאה: פלדות מיגון, זכוכיות משוריינות רב-שכבתיות וצמיגי Run-Flat, בתקן מיגון מוכר. מבחוץ הוא נראה כמו רכב VIP רגיל.</p>
<h2>שירות מלא</h2>
<p>רכב ממוגן, נהג מקצועי מוסמך, ולפי הצורך ליווי של מאבטח בעל רישיון נשק. המסלול, הרכב, הנהג והמאבטח מתואמים מראש לפי דרישות האבטחה שלכם.</p>
<h2>מה אפשר להזמין</h2>
<ul><li>איסוף VIP מנתב"ג בליווי מאבטח.</li><li>סיורים מאובטחים בירושלים ובכל הארץ.</li><li>הסעות יומיות בין מלונות, משרדים ופגישות.</li></ul>
""", ["armored"],
  related=["/rechavei-yukra", "/hasaot-meforsamim", "/nahag-prati"]),

P("/rechavei-yukra", "he", "vip", "רכבי יוקרה עם נהג",
  "רכבי יוקרה עם נהג | הסעות VIP למנהלים ולאירועים | Tour VIP",
  "רכבי יוקרה עם נהג פרטי: מיניוואנים ומיניבוסים מאובזרים, Wi-Fi ומים ברכב, עזרה במזוודות ודיסקרטיות מלאה. למנהלים, משלחות, חתונות ואורחים. 24/7.",
  "רכבי יוקרה עם נהג",
  "רכב VIP מאובזר ונהג מקצועי, לנסיעה אחת, ליום שלם או לכל הביקור.",
  """
<h2>מה כלול</h2>
<ul><li>רכב VIP מאובזר ונהג פרטי לבוש היטב.</li><li>מים מינרליים, Wi-Fi ומטענים ברכב.</li><li>עזרה במזוודות ודיסקרטיות מלאה.</li></ul>
<h2>הרכבים</h2>
<p>מיניוואני VIP ומיניבוסים יוקרתיים עם מושבי עור, תאורת אווירה, מזגן אישי ומרווח רגליים מוגדל.</p>
<h2>למי זה מתאים</h2>
<p>מנהלים ואנשי עסקים שנוסעים בין פגישות, משלחות עסקיות, חתן וכלה ביום החתונה, ואורחים מכובדים מחו"ל. ללקוחות שצריכים גם אבטחה יש <a href="/rechavim-memugnay-yeri">רכבים ממוגני ירי</a>.</p>
<h2>מחיר</h2>
<p>המחיר נקבע לפי סוג הרכב, משך ההזמנה והמסלול. מסלול של יום שלם כולל נהג צמוד לכל היום.</p>
""", ["van6", "van7", "mini19", "armored"], alt="/vip-transportation-israel",
  related=["/rechavim-memugnay-yeri", "/hasaot-meforsamim", "/nahag-prati"]),

P("/hasaot-meforsamim", "he", "vip", "הסעות לאמנים ומפורסמים",
  "הסעות לאמנים, מפורסמים ואישי ציבור | דיסקרטיות מלאה | Tour VIP",
  "הסעות דיסקרטיות לאמנים, זמרים, שחקנים ואישי ציבור: איסוף מנתב\"ג, הופעות, צילומים והפקות. נהגים חתומים על סודיות, ואפשרות לרכב ממוגן ומאבטח.",
  "הסעות לאמנים ומפורסמים",
  "נסיעות להופעות, לצילומים ולראיונות, בפרטיות מלאה ובלי חשיפה מיותרת.",
  """
<h2>דיסקרטיות</h2>
<p>הנהגים חתומים על הסכם סודיות, הרכבים בלוחיות רישוי רגילות, ויוצאים מכניסות צד כשצריך. בלי פרסום ובלי חשיפה.</p>
<h2>איסוף מנתב"ג</h2>
<p>מעקב אחרי הטיסה, המתנה בנקודת מפגש פרטית, עזרה במזוודות ויציאה מהירה מהשדה.</p>
<h2>הפקות וסבבי הופעות</h2>
<p>צוותי הפקה וטכנאים נוסעים במיניבוסים ובאוטובוסים, והאמנים ברכבי VIP נפרדים. מתאמים בין אולמות, אולפנים ומלונות לאורך כל הסבב.</p>
<h2>אבטחה</h2>
<p>כשצריך, משלבים <a href="/rechavim-memugnay-yeri">רכב ממוגן ירי</a> ומאבטח חמוש, בתיאום מראש עם צוות ההפקה.</p>
""", ["van7", "mini19", "bus50", "armored"],
  related=["/rechavei-yukra", "/rechavim-memugnay-yeri", "/hasaot-iruvim"]),
]

# ------------------------------------------------------------------ Hebrew city pages
_CITIES = [
    ("/hasaot-tel-aviv", "תל אביב", "כ-20 ק\"מ, 20–30 דקות בלי עומס",
     "<p>מתל אביב יוצאים הרבה לנתב\"ג, לפגישות בירושלים ולימי טיול. אוספים מדירות, ממלונות על קו החוף, ממשרדים ומיפו.</p>"
     "<p>לאירועים ולמסיבות אפשר להזמין הסעה חזרה בסוף הערב, כך שאף אחד לא נוהג אחרי שתייה.</p>",
     ["/monit-tel-aviv-natbag", "/monit-yerushalayim-tel-aviv", "/hasaot-iruvim"]),
    ("/hasaot-yerushalayim", "ירושלים", "כ-50 ק\"מ, 45–50 דקות בלי עומס",
     "<p>בירושלים יש הרבה אירוח: מלונות, אורחים מחו\"ל, עליות לתורה בכותל וסיורים בעיר העתיקה. החניה ליד העיר העתיקה קשה, ולכן הסעה שמורידה ואוספת חוסכת זמן ועצבים.</p>"
     "<p>אוספים מכל שכונות העיר, לנתב\"ג, לתל אביב, לים המלח ולכל יעד אחר.</p>",
     ["/monit-yerushalayim-natbag", "/siur-yerushalayim", "/hasaot-bar-mitzva"]),
    ("/hasaot-haifa", "חיפה", "כ-100 ק\"מ, שעה ורבע עד שעה וחצי בלי עומס",
     "<p>מחיפה הנסיעה לנתב\"ג ארוכה יחסית, ולכן כדאי לתאם אותה מראש ועם מרווח. אוספים מהכרמל, מהעיר התחתית, מהקריות ומנמל חיפה.</p>"
     "<p>חיפה היא גם נקודת יציאה טובה לטיולים: הגנים הבהאיים והכרמל, עכו, ראש הנקרה והגליל.</p>",
     ["/tiyul-galil", "/hasaot-menatbag", "/minibus-hashara"]),
    ("/hasaot-beer-sheva", "באר שבע", "כ-100 ק\"מ, כשעה ורבע בלי עומס",
     "<p>מבאר שבע נוסעים לנתב\"ג, למרכז, ולבתי חולים ולטיפולים. אוספים מכל שכונות העיר ומהיישובים סביבה.</p>"
     "<p>הדרום קרוב: ים המלח, מכתש רמון ואילת נמצאים במרחק נסיעה קצר יותר מאשר מהמרכז.</p>",
     ["/tiyul-yam-hamelach", "/tiyul-eilat", "/accessible-transportation"]),
    ("/hasaot-netanya", "נתניה", "כ-50 ק\"מ, 40–50 דקות בלי עומס",
     "<p>בנתניה נופשים תיירים רבים במלונות שעל הצוק, ולכן איסוף מנתב\"ג למלון ובחזרה מבוקש מאוד. אוספים גם מכל שכונות העיר.</p>"
     "<p>מנתניה קל לצאת צפונה: קיסריה, זכרון יעקב וחיפה.</p>",
     ["/hasaot-menatbag", "/nahag-prati", "/siurim-pratiyim"]),
    ("/hasaot-ashdod", "אשדוד", "כ-50 ק\"מ, כ-45 דקות בלי עומס",
     "<p>באשדוד מרבים בשמחות ובאירועים משפחתיים גדולים, והסעת אורחים במיניבוס או באוטובוס מתאימה במיוחד. אוספים מכל רובעי העיר.</p>"
     "<p>גם לנתב\"ג, לירושלים ולטיולים בדרום.</p>",
     ["/hasaot-chasuna", "/hasaot-bar-mitzva", "/minibus-hashara"]),
    ("/hasaot-rishon-lezion", "ראשון לציון", "כ-20 ק\"מ, 20–25 דקות בלי עומס",
     "<p>ראשון לציון קרובה לנתב\"ג, ויש בה אולמות אירועים רבים. אנחנו מסיעים אורחים לאולמות בעיר מכל הארץ, ומהעיר לכל יעד.</p>",
     ["/hasaot-iruvim", "/hasaot-chasuna", "/hasaot-menatbag"]),
    ("/hasaot-petah-tikva", "פתח תקווה", "כ-15 ק\"מ, כ-20 דקות בלי עומס",
     "<p>מפתח תקווה נוסעים לנתב\"ג, לפגישות במרכז, ולבתי החולים בעיר לטיפולים ולביקורים. לנוסעים עם כיסא גלגלים יש <a href=\"/accessible-transportation\">רכב נגיש עם מעלון</a>, בתיאום מראש.</p>",
     ["/accessible-transportation", "/hasaot-menatbag", "/nahag-prati"]),
]

for path, city, natbag, body, related in _CITIES:
    PAGES.append(P(
        path, "he", "city", f"הסעות ב{city}",
        f"הסעות ב{city} ומ{city} | מונית, ואן, מיניבוס ואוטובוס | Tour VIP",
        f"הסעות פרטיות ב{city}: לנתב\"ג ({natbag}), בין ערים, לאירועים ולטיולים. מונית 4 מקומות, ואנים, מיניבוסים 16-22 ואוטובוסים עד 60 מקומות. 054-283-1111.",
        f"הסעות ב{city}",
        f"מונית, ואן, מיניבוס או אוטובוס עם נהג, מכל כתובת ב{city} לכל מקום בארץ.",
        f"""
<h2>הסעות מ{city}</h2>
{body}
<h2>לנתב"ג</h2>
<p>מ{city} לנתב"ג: {natbag}. השירות פועל 24/7, כולל לילות, שבתות וחגים. מסרו מספר טיסה, ונתאים את שעת האיסוף או נעקוב אחרי הנחיתה.</p>
<h2>רכב לפי גודל הקבוצה</h2>
<ul><li>עד 4 נוסעים: מונית.</li><li>6–7 נוסעים או הרבה מזוודות: ואן.</li><li>16–22 נוסעים: מיניבוס.</li><li>35–60 נוסעים: אוטובוס.</li></ul>
""", ["taxi4", "van7", "mini19", "bus50"], related=related + ["/hasaot-beisrael"]))

# ------------------------------------------------------------------ English
PAGES += [
_from("ben-gurion-airport-transfers", "en", "/ben-gurion-airport-transfers", alt="/hasaot-menatbag",
      related=["/private-driver-israel", "/israel-family-transportation", "/vip-transportation-israel"],
      articles=["/en/blog/ben-gurion-transfer-guide", "/en/blog/choosing-vehicle-size"]),
_from("private-driver-israel", "en", "/private-driver-israel", alt="/nahag-prati",
      related=["/vip-transportation-israel", "/israel-private-tours", "/ben-gurion-airport-transfers"],
      articles=["/en/blog/private-day-tours-from-tel-aviv"]),
_from("israel-private-tours", "en", "/israel-private-tours", alt="/siurim-pratiyim", tours=True,
      related=["/private-driver-israel", "/israel-family-transportation", "/19-passenger-minibus-israel"],
      articles=["/en/blog/private-day-tours-from-tel-aviv", "/en/blog/israel-family-trip-tips"]),
_from("private-transportation-israel", "en", "/private-transportation-israel",
      related=["/israel-transportation-services", "/ben-gurion-airport-transfers", "/19-passenger-minibus-israel"],
      articles=["/en/blog/choosing-vehicle-size"]),
_from("israel-family-transportation", "en", "/israel-family-transportation",
      related=["/ben-gurion-airport-transfers", "/israel-private-tours", "/private-driver-israel"],
      articles=["/en/blog/israel-family-trip-tips", "/en/blog/ben-gurion-transfer-guide"]),
_from("19-passenger-minibus-israel", "en", "/19-passenger-minibus-israel", alt="/minibus-hashara",
      related=["/en/event-transportation", "/israel-private-tours", "/ben-gurion-airport-transfers"],
      articles=["/en/blog/choosing-vehicle-size", "/en/blog/event-transportation-checklist"]),
_from("accessible-transportation", "en", "/en/accessible-transportation", alt="/accessible-transportation",
      vehicles=["van6"], extra=_ACCESS_EN,
      related=["/ben-gurion-airport-transfers", "/private-driver-israel"],
      articles=["/en/blog/accessible-ride-planning"]),
_from("hasaot-iruvim", "en", "/en/event-transportation", alt="/hasaot-iruvim",
      related=["/19-passenger-minibus-israel", "/vip-transportation-israel", "/israel-transportation-services"],
      articles=["/en/blog/event-transportation-checklist"]),

P("/israel-transportation-services", "en", "service", "All transportation services",
  "Transportation Services in Israel | Airport, Private, Group & Events | Tour VIP",
  "All our transportation services in Israel in one place: Ben Gurion Airport transfers, private drivers, private tours, group minibuses and coaches, events and VIP. 24/7, nationwide.",
  "Transportation services in Israel",
  "One company for every ride in Israel: from a single airport pickup to moving a 60-person group, door to door, 24/7.",
  """
<h2>What we do</h2>
<ul>
<li><a href="/ben-gurion-airport-transfers">Ben Gurion Airport transfers</a>: pickups and drop-offs, any hour.</li>
<li><a href="/private-driver-israel">Private drivers</a>: by the hour, the day or your whole trip.</li>
<li><a href="/israel-private-tours">Private tours</a>: Jerusalem, the Dead Sea, the Galilee and more.</li>
<li><a href="/19-passenger-minibus-israel">Group minibuses</a> and coaches of up to 60 seats.</li>
<li><a href="/en/event-transportation">Events</a>: weddings, bar and bat mitzvahs, conferences.</li>
<li><a href="/vip-transportation-israel">VIP transportation</a>, including armored vehicles.</li>
<li><a href="/en/accessible-transportation">Accessible transportation</a> with a wheelchair lift.</li>
</ul>
<h2>How booking works</h2>
<p>Send the pickup point, destination, date, number of passengers and luggage. We reply with a quote and confirm availability.</p>
""", ["taxi4", "van7", "mini19", "bus60", "armored"], alt="/hasaot-beisrael",
  related=["/private-transportation-israel", "/israel-family-transportation", "/vip-transportation-israel"],
  articles=["/en/blog/choosing-vehicle-size"]),

P("/vip-transportation-israel", "en", "service", "VIP transportation",
  "VIP Transportation in Israel | Chauffeur, Meet & Greet, Armored | Tour VIP",
  "VIP transportation in Israel: premium vehicles with a professional chauffeur, meet-and-greet at Ben Gurion, Wi-Fi and water on board, full discretion, and armored vehicles on request.",
  "VIP transportation in Israel",
  "A premium vehicle and a professional chauffeur, for one ride, a full day or your entire stay.",
  """
<h2>What is included</h2>
<ul><li>A well-presented professional chauffeur.</li><li>Mineral water, Wi-Fi and chargers on board.</li><li>Help with luggage and full discretion.</li></ul>
<h2>Meet and greet at Ben Gurion</h2>
<p>Your driver meets you in the arrivals hall, helps with your bags, and takes you straight to your hotel, apartment or office, at any hour.</p>
<h2>The vehicles</h2>
<p>VIP vans and luxury minibuses with leather seats, ambient lighting, individual air conditioning and extra legroom. For executives, delegations, wedding parties and guests of honour.</p>
<h2>Security</h2>
<p>When security comes first, we provide armored vehicles, and an armed security escort can be arranged in advance.</p>
""", ["van6", "van7", "mini19", "armored"], alt="/rechavei-yukra",
  related=["/private-driver-israel", "/ben-gurion-airport-transfers", "/israel-transportation-services"]),
]

_DIASPORA = [
    ("/israel-vip-transportation-new-york", "New York",
     "Many New York families come to Israel for a bar or bat mitzvah at the Western Wall, a wedding, or the holidays. "
     "We handle the whole visit: the airport pickup after the overnight flight, the ride to Jerusalem, the day of the ceremony with guests, and touring days.",
     "Planning a bar or bat mitzvah in Israel? Send us the dates and the number of guests, and we will build the transportation plan around the day."),
    ("/israel-vip-transportation-miami", "Miami",
     "Travelers from Miami and South Florida often come for family visits, winter holidays and celebrations. "
     "After a long flight, the last thing you need is a taxi queue: your driver waits in the arrivals hall and the vehicle is sized for your family and luggage.",
     "Staying for a few weeks? Book the airport pickup, day trips and the ride back to the airport in one booking."),
    ("/israel-vip-transportation-canada", "Canada",
     "Visitors from Toronto, Montreal and across Canada come for family visits, tours and simchas. "
     "We cover the airport transfers, a private driver for touring days, and group transportation when the whole family gathers.",
     "Coming with a large family or a community group? A 16, 19 or 22 seat minibus keeps everyone together."),
    ("/israel-vip-transportation-russia", "Russia",
     "Our drivers speak Hebrew, English and Russian, so travelers from Russia and Russian-speaking countries can talk to their driver in their own language from the moment they land. "
     "We provide airport transfers, private drivers by the hour or the day, and private tours across Israel.",
     "Tell us in your booking if you prefer a Russian-speaking driver."),
]
for path, place, intro, tip in _DIASPORA:
    PAGES.append(P(
        path, "en", "diaspora", f"Travelers from {place}",
        f"Israel VIP Transportation for Travelers from {place} | Tour VIP",
        f"VIP transportation in Israel for travelers from {place}: Ben Gurion Airport meet-and-greet, private drivers, private tours and family events. Book on WhatsApp +972-54-283-1111.",
        f"Israel VIP transportation for travelers from {place}",
        "From the arrivals hall at Ben Gurion to every stop of your visit, with a professional driver and a vehicle that fits your party.",
        f"""
<h2>Your visit, door to door</h2>
<p>{intro}</p>
<h2>What we can book for you</h2>
<ul>
<li><a href="/ben-gurion-airport-transfers">Ben Gurion Airport transfers</a>, tracked to your actual landing time.</li>
<li><a href="/private-driver-israel">A private driver</a> by the hour, the day or the whole trip.</li>
<li><a href="/israel-private-tours">Private tours</a>: Jerusalem, the Dead Sea, the Galilee.</li>
<li><a href="/vip-transportation-israel">VIP</a> and armored vehicles.</li>
</ul>
<p>{tip}</p>
""", ["taxi4", "van7", "mini19", "armored"],
        related=["/ben-gurion-airport-transfers", "/private-driver-israel", "/vip-transportation-israel"]))
