"""The service pages. Slugs must stay exactly as on the old site (SEO)."""

SERVICES = [
{
"slug": "ben-gurion-airport-transfers", "icon": "plane",
"vehicles": ["taxi4", "van6", "van7", "mini16", "mini19", "mini22"],
"articles": ["ben-gurion-transfer-guide", "choosing-vehicle-size"],
"he": {
"nav": "הסעות לנתב\"ג",
"title": "הסעות לנתב\"ג ומנתב\"ג | מונית, ואן ומיניבוס | Tour VIP",
"desc": "הסעה פרטית לנמל התעופה בן גוריון ובחזרה, מכל מקום בארץ. מונית, ואן 6-7 מקומות ומיניבוסים לקבוצות. הזמנה מהירה בוואטסאפ 054-283-1111.",
"h1": "הסעות לנתב\"ג ומנתב\"ג",
"lead": "נסיעה פרטית לנמל התעופה בן גוריון ובחזרה, מהבית, מהמלון או מהמשרד, עם רכב שמתאים לכמות הנוסעים והמזוודות.",
"body": """
<h2>איך זה עובד</h2>
<ol>
<li>שולחים לנו בוואטסאפ את התאריך, שעת הטיסה, כתובת האיסוף, מספר הנוסעים והמזוודות.</li>
<li>אנחנו מתאימים רכב ושולחים אישור עם המחיר לפני הנסיעה.</li>
<li>הנהג מגיע בזמן שנקבע. בנחיתה, הנהג מחכה לכם באולם הנכנסים.</li>
</ol>
<h2>לטיסה יוצאת</h2>
<p>לטיסות בינלאומיות מקובל להגיע לנתב\"ג כשלוש שעות לפני ההמראה. כדאי לקחת בחשבון גם עומסי תנועה בשעות הבוקר ובערבי חג, ולכן נקבע איתכם שעת איסוף שמשאירה מרווח.</p>
<h2>לטיסה נכנסת</h2>
<p>אם תשלחו לנו את מספר הטיסה, נוכל לעקוב אחרי שעת הנחיתה בפועל. כך שינויים ועיכובים לא יפתיעו אף אחד, והנהג יגיע כשאתם יוצאים עם המזוודות.</p>
<h2>איזה רכב להזמין</h2>
<ul>
<li><strong>עד 4 נוסעים</strong> עם מזוודות רגילות: מונית.</li>
<li><strong>משפחה עם הרבה מזוודות</strong>, עגלה או ציוד ספורט: ואן 6 או 7 מקומות.</li>
<li><strong>קבוצה</strong>: מיניבוס 16, 19 או 22 מקומות, כולם יחד ברכב אחד.</li>
</ul>
<p>לא בטוחים? כתבו לנו את מספר הנוסעים והמזוודות ונמליץ.</p>
"""},
"en": {
"nav": "Ben Gurion Airport transfers",
"title": "Ben Gurion Airport Transfers | Taxi, Van & Minibus | Tour VIP",
"desc": "Private transfers to and from Ben Gurion Airport (TLV) from anywhere in Israel. Taxis, 6-7 seat vans and group minibuses. Book on WhatsApp +972-54-283-1111.",
"h1": "Ben Gurion Airport transfers",
"lead": "A private ride to and from Ben Gurion Airport (TLV): from your home, hotel or office, in a vehicle sized for your passengers and luggage.",
"body": """
<h2>How it works</h2>
<ol>
<li>Send us on WhatsApp your date, flight time, pickup address, number of passengers and suitcases.</li>
<li>We match a vehicle and send you a confirmation with the price before the ride.</li>
<li>Your driver arrives at the agreed time. On arrival flights, the driver waits for you in the arrivals hall.</li>
</ol>
<h2>Departing flights</h2>
<p>For international flights the usual advice is to be at Ben Gurion about three hours before take-off. Morning rush hour and holiday eves add traffic, so we agree a pickup time that leaves a margin.</p>
<h2>Arriving flights</h2>
<p>Send us your flight number and we can follow the actual landing time. Delays and changes then surprise no one, and your driver is there when you come out with your bags.</p>
<h2>Which vehicle to book</h2>
<ul>
<li><strong>Up to 4 passengers</strong> with regular luggage: a taxi.</li>
<li><strong>A family with lots of luggage</strong>, a stroller or sports gear: a 6 or 7 seat van.</li>
<li><strong>A group</strong>: a 16, 19 or 22 seat minibus, everyone in one vehicle.</li>
</ul>
<p>Not sure? Tell us how many passengers and suitcases and we will recommend.</p>
"""}},
{
"slug": "private-driver-israel", "icon": "driver",
"vehicles": ["taxi4", "van6", "van7", "armored"],
"articles": ["private-day-tours-from-tel-aviv", "choosing-vehicle-size"],
"he": {
"nav": "נהג צמוד",
"title": "נהג צמוד בישראל | נהג פרטי לפי שעות או ימים | Tour VIP",
"desc": "נהג פרטי צמוד לפגישות עסקיות, ימי טיול, אירועים ואורחים מחו\"ל. לפי שעות, יום או כמה ימים, ברכב לבחירתכם. הזמנה בוואטסאפ 054-283-1111.",
"h1": "נהג צמוד בישראל",
"lead": "נהג פרטי שנשאר איתכם לאורך כל היום: לפגישות, לסידורים, לטיול או לאירוח אורחים מחו\"ל. אתם קובעים את הלו\"ז, אנחנו נוהגים.",
"body": """
<h2>למי זה מתאים</h2>
<ul>
<li><strong>אנשי עסקים ומשלחות</strong>: כמה פגישות ביום בערים שונות, בלי לחפש חניה ובלי לחכות למונית.</li>
<li><strong>אורחים מחו\"ל</strong>: נהג שמחכה בנתב\"ג ומלווה את כל הביקור.</li>
<li><strong>משפחות ביום טיול</strong>: עוצרים איפה שרוצים, כמה שרוצים.</li>
<li><strong>אירועים</strong>: נהג לחתן ולכלה, להורים או לאורחים מכובדים.</li>
</ul>
<h2>איך מזמינים</h2>
<p>שלחו לנו את התאריך, שעת ההתחלה, הנקודות שאתם מתכננים לעבור בהן ומספר הנוסעים. נציע רכב ומחיר לפי שעות או לפי יום מלא, ונאשר מראש מה כלול.</p>
<h2>רכב ממוגן</h2>
<p>למי שצריך רמת ביטחון גבוהה יותר, אפשר להזמין נהג צמוד ברכב ממוגן. ציינו זאת בהזמנה ונבדוק זמינות.</p>
"""},
"en": {
"nav": "Private driver",
"title": "Private Driver in Israel | Chauffeur by the Hour or Day | Tour VIP",
"desc": "A private driver for business meetings, day trips, events and visitors from abroad. By the hour, day or several days, in the vehicle you choose. Book on WhatsApp +972-54-283-1111.",
"h1": "Private driver in Israel",
"lead": "A private driver who stays with you all day: meetings, errands, sightseeing or hosting guests from abroad. You set the schedule, we drive.",
"body": """
<h2>Who it is for</h2>
<ul>
<li><strong>Executives and delegations</strong>: several meetings a day in different cities, no parking, no waiting for taxis.</li>
<li><strong>Visitors from abroad</strong>: a driver who meets you at Ben Gurion and stays with you through the visit.</li>
<li><strong>Families on a day out</strong>: stop wherever you like, for as long as you like.</li>
<li><strong>Events</strong>: a driver for the couple, the parents or guests of honour.</li>
</ul>
<h2>How to book</h2>
<p>Send us the date, start time, the places you plan to visit and the number of passengers. We offer a vehicle and a price by the hour or for a full day, and confirm in advance what is included.</p>
<h2>Armored vehicle</h2>
<p>If you need a higher level of security, you can book a private driver with an armored vehicle. Mention it when booking and we will check availability.</p>
"""}},
{
"slug": "israel-private-tours", "icon": "map",
"vehicles": ["taxi4", "van7", "mini19", "bus50"],
"articles": ["private-day-tours-from-tel-aviv", "israel-family-trip-tips"],
"he": {
"nav": "סיורים פרטיים",
"title": "סיורים פרטיים בישראל | ירושלים, ים המלח, הגליל | Tour VIP",
"desc": "סיורים פרטיים בישראל עם נהג: ירושלים, ים המלח ומצדה, הגליל והגולן, קיסריה, חיפה ועכו. למשפחות ולקבוצות, בקצב שלכם. הזמנה בוואטסאפ 054-283-1111.",
"h1": "סיורים פרטיים בישראל",
"lead": "יום טיול שבנוי סביבכם: איסוף מהמלון, מסלול שתואם מראש, ועצירות בקצב שלכם. רכב לזוג, למשפחה או לקבוצה שלמה.",
"body": """
<h2>יעדים מבוקשים</h2>
<ul>
<li><strong>ירושלים</strong>: העיר העתיקה, הכותל, הר הזיתים ושוק מחנה יהודה.</li>
<li><strong>ים המלח ומצדה</strong>: יום מלא בדרום, עם עצירה לרחצה.</li>
<li><strong>הגליל והגולן</strong>: הכנרת, צפת ונופי הצפון.</li>
<li><strong>החוף הצפוני</strong>: קיסריה, חיפה והגנים הבהאיים, ועכו העתיקה.</li>
</ul>
<h2>איך בונים את היום</h2>
<p>ספרו לנו מאיפה יוצאים, מה חשוב לכם לראות ומי מגיע. נציע מסלול שאפשר לעשות ביום אחד בלי לבלות את רובו בכביש, ונתאים רכב לגודל הקבוצה.</p>
<p>שימו לב: חלק מהאתרים בישראל סגורים או מצמצמים שעות בימי שישי, בשבת ובחגים. נבדוק את זה איתכם לפני שקובעים תאריך.</p>
"""},
"en": {
"nav": "Private tours",
"title": "Israel Private Tours | Jerusalem, Dead Sea, Galilee | Tour VIP",
"desc": "Private tours of Israel with a driver: Jerusalem, the Dead Sea and Masada, Galilee and the Golan, Caesarea, Haifa and Akko. For families and groups, at your pace. Book on WhatsApp +972-54-283-1111.",
"h1": "Private tours in Israel",
"lead": "A day out built around you: hotel pickup, a route agreed in advance, and stops at your pace. Vehicles for a couple, a family or a whole group.",
"body": """
<h2>Popular destinations</h2>
<ul>
<li><strong>Jerusalem</strong>: the Old City, the Western Wall, the Mount of Olives and Mahane Yehuda market.</li>
<li><strong>The Dead Sea and Masada</strong>: a full day in the south, with time for a float.</li>
<li><strong>The Galilee and the Golan</strong>: the Sea of Galilee, Safed and the northern landscapes.</li>
<li><strong>The northern coast</strong>: Caesarea, Haifa and the Bahá'í Gardens, and old Akko.</li>
</ul>
<h2>How we plan the day</h2>
<p>Tell us where you start, what matters to you and who is coming. We suggest a route that fits in one day without spending most of it on the road, and match the vehicle to your group.</p>
<p>Note: some sites in Israel close or shorten their hours on Fridays, Saturdays and holidays. We check this with you before fixing a date.</p>
"""}},
{
"slug": "private-transportation-israel", "icon": "car",
"vehicles": ["taxi4", "van6", "van7", "mini16", "mini19", "mini22", "bus35", "bus50", "bus60", "armored"],
"articles": ["choosing-vehicle-size", "event-transportation-checklist"],
"he": {
"nav": "הסעות פרטיות",
"title": "הסעות פרטיות בכל הארץ | מונית, ואן, מיניבוס ואוטובוס | Tour VIP",
"desc": "הסעות פרטיות בין ערים ובכל הארץ: מונית 4 מקומות, ואנים 6-7, מיניבוסים 16-22, אוטובוסים 35-60 ורכבים ממוגנים. הזמנה בוואטסאפ 054-283-1111.",
"h1": "הסעות פרטיות בכל הארץ",
"lead": "מנסיעה אחת של זוג ועד הסעה של קבוצה גדולה: רכב פרטי עם נהג, מכל נקודה לכל נקודה בישראל.",
"body": """
<h2>מה אפשר להזמין</h2>
<ul>
<li>נסיעות בין ערים, לנתב\"ג ולמלונות.</li>
<li>הסעות עובדים, צוותים וכנסים.</li>
<li>הסעות לאירועים, חתונות ובר מצוות.</li>
<li>הסעות לקבוצות תיירים, טיולים ונופשים.</li>
</ul>
<h2>צי שמתאים לכל גודל</h2>
<p>מונית 4 מקומות, ואן 6 ו-7 מקומות, מיניבוסים של 16, 19 ו-22 מקומות, אוטובוסים של 35, 50 ו-60 מקומות ורכבים ממוגנים. אם הקבוצה גדולה מרכב אחד, נשלב כמה רכבים באותה הזמנה.</p>
<h2>מה צריך לשלוח לנו</h2>
<p>תאריך ושעה, נקודת איסוף ויעד, מספר נוסעים, כמות מזוודות או ציוד, והאם צריך גם נסיעה חזרה. נחזור עם הצעה מסודרת.</p>
"""},
"en": {
"nav": "Private transportation",
"title": "Private Transportation in Israel | Taxi, Van, Minibus, Coach | Tour VIP",
"desc": "Private transportation anywhere in Israel: 4-seat taxis, 6-7 seat vans, 16-22 seat minibuses, 35-60 seat coaches and armored vehicles. Book on WhatsApp +972-54-283-1111.",
"h1": "Private transportation in Israel",
"lead": "From a single ride for two to moving a large group: a private vehicle with a driver, from any point to any point in Israel.",
"body": """
<h2>What you can book</h2>
<ul>
<li>City-to-city rides, airport runs and hotel transfers.</li>
<li>Staff shuttles, team transport and conferences.</li>
<li>Events, weddings and bar/bat mitzvahs.</li>
<li>Tour groups, day trips and retreats.</li>
</ul>
<h2>A fleet for every size</h2>
<p>A 4-seat taxi, 6 and 7 seat vans, 16, 19 and 22 seat minibuses, 35, 50 and 60 seat coaches, and armored vehicles. If your group is bigger than one vehicle, we combine several in one booking.</p>
<h2>What to send us</h2>
<p>Date and time, pickup point and destination, number of passengers, luggage or equipment, and whether you need a return trip. We will come back with a clear quote.</p>
"""}},
{
"slug": "accessible-transportation", "icon": "access",
"vehicles": ["van6", "van7", "mini16"],
"articles": ["accessible-ride-planning"],
"he": {
"nav": "הסעות נגישות",
"title": "הסעות נגישות | נסיעה עם כיסא גלגלים ולבני גיל הזהב | Tour VIP",
"desc": "הסעות נגישות לבעלי מוגבלויות, נוסעים עם כיסא גלגלים ובני גיל הזהב: לנתב\"ג, לטיפולים, לאירועים ולטיולים. ספרו לנו מה צריך ונתאים רכב. 054-283-1111.",
"h1": "הסעות נגישות",
"lead": "נסיעה בטוחה ונוחה לנוסעים עם מוגבלות, כיסא גלגלים, הליכון או קושי בעלייה לרכב. מתאימים את הרכב והזמן לצרכים שלכם.",
"body": """
<h2>לפני ההזמנה, ספרו לנו</h2>
<ul>
<li>האם הנוסע עובר מהכיסא למושב, או נוסע בכיסא עצמו.</li>
<li>סוג הכיסא: מתקפל, ידני או ממונע, ומשקל משוער.</li>
<li>האם יש מלווה, ציוד רפואי או צורך בעזרה בעלייה ובירידה.</li>
<li>כתובת האיסוף: קומה, מעלית ומדרגות בכניסה.</li>
</ul>
<p>עם הפרטים האלה נוכל להגיד לכם מראש איזה רכב מתאים, ולקבוע זמן איסוף שלא לוחץ על אף אחד.</p>
<h2>לאן נוסעים</h2>
<p>לנתב\"ג, לבתי חולים ולטיפולים, לאירועים משפחתיים ולטיולים. גם קבוצות של בני גיל הזהב ומוסדות.</p>
"""},
"en": {
"nav": "Accessible transportation",
"title": "Accessible Transportation in Israel | Wheelchair & Senior Rides | Tour VIP",
"desc": "Accessible rides for passengers with disabilities, wheelchair users and seniors: airport, medical appointments, events and trips. Tell us what you need and we match the vehicle. +972-54-283-1111.",
"h1": "Accessible transportation",
"lead": "Safe, comfortable rides for passengers with a disability, a wheelchair or walker, or difficulty getting into a car. We match the vehicle and timing to your needs.",
"body": """
<h2>Before you book, tell us</h2>
<ul>
<li>Whether the passenger transfers from the chair to a seat, or travels in the chair.</li>
<li>The type of chair: folding, manual or powered, and roughly its weight.</li>
<li>Whether there is a companion, medical equipment, or a need for help getting in and out.</li>
<li>The pickup address: floor, lift and any steps at the entrance.</li>
</ul>
<p>With these details we can tell you in advance which vehicle fits, and set a pickup time that rushes no one.</p>
<h2>Where we go</h2>
<p>Ben Gurion Airport, hospitals and treatments, family events and day trips. Senior groups and institutions too.</p>
"""}},
{
"slug": "israel-family-transportation", "icon": "family",
"vehicles": ["van6", "van7", "mini16"],
"articles": ["israel-family-trip-tips", "ben-gurion-transfer-guide"],
"he": {
"nav": "הסעות למשפחות",
"title": "הסעות למשפחות בישראל | ואן 6-7 מקומות ומיניבוס | Tour VIP",
"desc": "הסעות למשפחות: נתב\"ג, טיולים, חופשות ואירועים משפחתיים. ואנים 6-7 מקומות עם מקום למזוודות ולעגלות, ומיניבוסים למשפחות מורחבות. 054-283-1111.",
"h1": "הסעות למשפחות",
"lead": "כל המשפחה ברכב אחד, עם מקום לילדים, למזוודות ולעגלה. לנתב\"ג, לחופשה, לטיול או לאירוע משפחתי.",
"body": """
<h2>למה ואן ולא שתי מוניות</h2>
<p>משפחה של 5 ומעלה עם מזוודות בדרך כלל לא נכנסת למונית אחת. ואן של 6 או 7 מקומות שומר על כולם יחד, עם מקום לעגלה ולמזוודות. למשפחות מורחבות יש מיניבוס של 16 מקומות.</p>
<h2>נוסעים עם ילדים</h2>
<p>כתבו לנו בהזמנה את מספר הילדים והגילים שלהם, ואם אתם מביאים כיסאות בטיחות משלכם. כך נדע להתאים את הרכב ואת המקום.</p>
<h2>חופשה בארץ</h2>
<p>אפשר להזמין איסוף מנתב\"ג, נסיעה למלון, ימי טיול באמצע החופשה והחזרה לטיסה, הכול בהזמנה אחת.</p>
"""},
"en": {
"nav": "Family transportation",
"title": "Family Transportation in Israel | 6-7 Seat Vans & Minibuses | Tour VIP",
"desc": "Family transportation in Israel: airport, trips, holidays and family events. 6-7 seat vans with room for luggage and strollers, and minibuses for extended families. +972-54-283-1111.",
"h1": "Family transportation in Israel",
"lead": "The whole family in one vehicle, with room for the kids, the luggage and the stroller. Airport, holidays, day trips or family events.",
"body": """
<h2>Why a van instead of two taxis</h2>
<p>A family of five or more with luggage usually does not fit in one taxi. A 6 or 7 seat van keeps everyone together, with room for a stroller and suitcases. For extended families there is a 16-seat minibus.</p>
<h2>Travelling with children</h2>
<p>Tell us in your booking how many children are coming, their ages, and whether you are bringing your own car seats. That way we can match the vehicle and the space.</p>
<h2>A holiday in Israel</h2>
<p>You can book the airport pickup, the ride to your hotel, day trips during your stay and the ride back to your flight, all in one booking.</p>
"""}},
{
"slug": "19-passenger-minibus-israel", "icon": "bus",
"vehicles": ["mini16", "mini19", "mini22"],
"articles": ["choosing-vehicle-size", "event-transportation-checklist"],
"he": {
"nav": "מיניבוס 19 מקומות",
"title": "מיניבוס 19 מקומות עם נהג | הסעות קבוצות | Tour VIP",
"desc": "השכרת מיניבוס 19 מקומות עם נהג: איסוף קבוצות מנתב\"ג, אירועים, טיולים והסעות עובדים. גם 16 ו-22 מקומות. הזמנה בוואטסאפ 054-283-1111.",
"h1": "מיניבוס 19 מקומות עם נהג",
"lead": "הגודל הנוח ביותר לקבוצה: 19 נוסעים ברכב אחד, עם נהג, ממקום למקום בכל הארץ.",
"body": """
<h2>למה מיניבוס</h2>
<ul>
<li>כל הקבוצה מגיעה יחד, בלי לתאם כמה מוניות.</li>
<li>גמיש יותר מאוטובוס גדול: נכנס לרחובות צרים ולחניות של מלונות.</li>
<li>מתאים לאיסוף מנתב\"ג, לטיולים, לאירועים ולהסעות עובדים.</li>
</ul>
<h2>מזוודות</h2>
<p>קבוצה מלאה עם מזוודה גדולה לכל נוסע תופסת הרבה מקום. בהזמנה, כתבו כמה מזוודות יש, ונגיד לכם אם מספיק מיניבוס 19, או שעדיף 22 מקומות או רכב נוסף למטען.</p>
<h2>גדלים נוספים</h2>
<p>יש גם מיניבוס 16 ו-22 מקומות, ולקבוצות גדולות יותר אוטובוסים של 35, 50 ו-60 מקומות.</p>
"""},
"en": {
"nav": "19-passenger minibus",
"title": "19-Passenger Minibus with Driver in Israel | Group Transfers | Tour VIP",
"desc": "Hire a 19-passenger minibus with a driver in Israel: group airport pickups, events, day trips and staff shuttles. 16 and 22 seat minibuses too. Book on WhatsApp +972-54-283-1111.",
"h1": "19-passenger minibus with driver",
"lead": "The most convenient size for a group: 19 passengers in one vehicle, with a driver, anywhere in Israel.",
"body": """
<h2>Why a minibus</h2>
<ul>
<li>The whole group arrives together, with no juggling of several taxis.</li>
<li>More flexible than a full coach: fits narrow streets and hotel driveways.</li>
<li>Good for airport pickups, day trips, events and staff shuttles.</li>
</ul>
<h2>Luggage</h2>
<p>A full group with a large suitcase each takes a lot of space. Tell us how many suitcases you have, and we will say whether a 19-seater is enough, or a 22-seater or an extra luggage vehicle is better.</p>
<h2>Other sizes</h2>
<p>There are also 16 and 22 seat minibuses, and for bigger groups 35, 50 and 60 seat coaches.</p>
"""}},
{
"slug": "hasaot-iruvim", "icon": "event",
"vehicles": ["mini19", "mini22", "bus35", "bus50", "bus60"],
"articles": ["event-transportation-checklist", "choosing-vehicle-size"],
"he": {
"nav": "הסעות לאירועים",
"title": "הסעות לאירועים וחתונות | מיניבוסים ואוטובוסים | Tour VIP",
"desc": "הסעות אורחים לחתונות, בר מצוות, כנסים ואירועי חברה. מיניבוסים 19-22 מקומות ואוטובוסים 35, 50 ו-60 מקומות, הלוך וחזור. הזמנה בוואטסאפ 054-283-1111.",
"h1": "הסעות לאירועים",
"lead": "האורחים מגיעים יחד, בזמן, ובלי לחפש חניה, וחוזרים הביתה בלי לנהוג אחרי האירוע.",
"body": """
<h2>לאילו אירועים</h2>
<ul>
<li>חתונות, חינות ובר ובת מצוות.</li>
<li>כנסים, ימי גיבוש ואירועי חברה.</li>
<li>אירועים משפחתיים מחוץ לעיר.</li>
</ul>
<h2>איך מתכננים</h2>
<p>שלחו לנו את מספר האורחים, נקודות האיסוף, כתובת האולם, שעת ההגעה הרצויה ושעת החזרה. נציע שילוב רכבים, למשל אוטובוס אחד מאזור אחד ומיניבוס מאזור אחר, ונבנה לוח זמנים לאיסופים.</p>
<h2>החזרה בסוף הערב</h2>
<p>חשוב להחליט מראש אם החזרה בשעה אחת קבועה, או בשני סבבים, למשפחות עם ילדים ולמי שנשאר עד הסוף.</p>
"""},
"en": {
"nav": "Event transportation",
"title": "Event & Wedding Transportation in Israel | Minibuses & Coaches | Tour VIP",
"desc": "Guest transportation for weddings, bar/bat mitzvahs, conferences and company events in Israel. 19-22 seat minibuses and 35, 50 and 60 seat coaches, both ways. Book on WhatsApp +972-54-283-1111.",
"h1": "Event transportation",
"lead": "Your guests arrive together, on time and without hunting for parking, and get home without driving after the party.",
"body": """
<h2>Which events</h2>
<ul>
<li>Weddings, henna nights and bar/bat mitzvahs.</li>
<li>Conferences, team days and company events.</li>
<li>Family celebrations out of town.</li>
</ul>
<h2>How we plan it</h2>
<p>Send us the number of guests, pickup points, venue address, the arrival time you want and the return time. We suggest a mix of vehicles, for example a coach from one area and a minibus from another, and build a pickup schedule.</p>
<h2>The ride home</h2>
<p>Decide in advance whether everyone returns at one fixed time, or in two rounds: families with children earlier, and those who stay to the end later.</p>
"""}},
]
