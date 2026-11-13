"""Business details, fleet and interface strings (Hebrew + English)."""

SITE_URL = "https://my-vip-tours.com"
BRAND = "Tour VIP"
PHONE_DISPLAY = "054-283-1111"
PHONE_INTL = "+972542831111"
WHATSAPP = "972542831111"

LANGS = ("he", "en")
DEFAULT_LANG = "he"

# Fleet: seats are passenger seats (driver not included).
FLEET = [
    {"id": "taxi4", "seats": 4,
     "he": {"name": "מונית 4 מקומות", "desc": "לזוג, משפחה קטנה או נוסע עסקי. מתאימה לנסיעות לנתב\"ג ובין ערים."},
     "en": {"name": "4-seat taxi", "desc": "For a couple, a small family or a business traveler. Airport runs and city-to-city rides."}},
    {"id": "van6", "seats": 6,
     "he": {"name": "ואן 6 מקומות", "desc": "למשפחה עם מזוודות או לקבוצה קטנה. יותר מקום לרגליים ולמטען."},
     "en": {"name": "6-seat van", "desc": "For a family with luggage or a small group. More legroom and boot space."}},
    {"id": "van7", "seats": 7,
     "he": {"name": "ואן 7 מקומות", "desc": "למשפחות גדולות ולקבוצות של עד 7 נוסעים ברכב אחד."},
     "en": {"name": "7-seat van", "desc": "For larger families and groups of up to 7 passengers in one vehicle."}},
    {"id": "mini16", "seats": 16,
     "he": {"name": "מיניבוס 16 מקומות", "desc": "לקבוצות, צוותי עבודה וסיורים. כולם נוסעים יחד."},
     "en": {"name": "16-seat minibus", "desc": "For groups, work teams and tours. Everyone travels together."}},
    {"id": "mini19", "seats": 19,
     "he": {"name": "מיניבוס 19 מקומות", "desc": "הגודל הפופולרי לקבוצות: איסוף מנתב\"ג, אירועים וטיולים."},
     "en": {"name": "19-seat minibus", "desc": "The most popular group size: airport pickups, events and day trips."}},
    {"id": "mini22", "seats": 22,
     "he": {"name": "מיניבוס 22 מקומות", "desc": "לקבוצות גדולות יותר שעדיין רוצות רכב גמיש ונוח."},
     "en": {"name": "22-seat minibus", "desc": "For bigger groups that still want a flexible, comfortable vehicle."}},
    {"id": "bus35", "seats": 35,
     "he": {"name": "אוטובוס 35 מקומות", "desc": "לאירועים, כנסים וקבוצות תיירים."},
     "en": {"name": "35-seat coach", "desc": "For events, conferences and tour groups."}},
    {"id": "bus50", "seats": 50,
     "he": {"name": "אוטובוס 50 מקומות", "desc": "להסעות אורחים לחתונות ולאירועים גדולים, ולקבוצות מאורגנות."},
     "en": {"name": "50-seat coach", "desc": "For wedding guests, large events and organised groups."}},
    {"id": "bus60", "seats": 60,
     "he": {"name": "אוטובוס 60 מקומות", "desc": "הרכב הגדול בצי, לקבוצות הגדולות ביותר."},
     "en": {"name": "60-seat coach", "desc": "The largest vehicle in the fleet, for the biggest groups."}},
    {"id": "armored", "seats": None,
     "he": {"name": "רכבים ממוגנים", "desc": "לאורחים, משלחות ואנשי עסקים שצריכים רמת ביטחון גבוהה. מספר המקומות לפי הרכב, נא לשאול בהזמנה."},
     "en": {"name": "Armored vehicles", "desc": "For guests, delegations and executives who need a higher level of security. Seating depends on the vehicle; ask when booking."}},
]

UI = {
    "he": {
        "lang_name": "עברית", "other_lang": "English",
        "home": "דף הבית", "services": "שירותים", "fleet": "הצי שלנו", "tours": "סיורים",
        "articles": "מאמרים", "faq": "שאלות נפוצות", "reviews": "ביקורות", "book": "הזמנה",
        "call": "התקשרו", "whatsapp": "וואטסאפ", "menu": "תפריט",
        "tagline": "הסעות פרטיות, נהג צמוד וסיורים בכל הארץ",
        "book_title": "הזמנת נסיעה", "book_lead": "ממלאים את הפרטים, וההזמנה נפתחת בוואטסאפ מוכנה לשליחה. נחזור אליכם עם אישור ומחיר.",
        "f_name": "שם מלא", "f_phone": "טלפון", "f_service": "סוג שירות", "f_vehicle": "רכב",
        "f_vehicle_any": "תמליצו לי", "f_date": "תאריך", "f_time": "שעה", "f_from": "מאיפה",
        "f_to": "לאן", "f_pax": "מספר נוסעים", "f_bags": "מזוודות", "f_flight": "מספר טיסה (אם יש)",
        "f_return": "גם נסיעה חזרה", "f_notes": "הערות (כיסא תינוק, כיסא גלגלים, עצירות בדרך...)",
        "f_submit": "שליחה בוואטסאפ", "f_required": "שדה חובה",
        "noscript": "הטופס צריך JavaScript. אפשר לכתוב לנו ישירות בוואטסאפ:",
        "wa_intro": "שלום, אני רוצה להזמין נסיעה:",
        "seats": "מקומות", "seats_ask": "לפי הרכב",
        "suitable": "רכבים מתאימים", "read_more": "להמשך קריאה", "related": "עוד באתר",
        "all_services": "כל השירותים", "updated": "עודכן",
        "reviews_title": "מה הלקוחות אומרים", "tours_title": "הסיורים שלנו", "faq_title": "שאלות נפוצות",
        "duration": "משך", "price": "מחיר",
        "contact": "יצירת קשר", "available": "זמינים בטלפון ובוואטסאפ",
        "not_found": "העמוד לא נמצא", "not_found_text": "ייתכן שהקישור השתנה. אפשר לחזור לדף הבית או להזמין נסיעה.",
        "skip": "דילוג לתוכן",
        "rights": "כל הזכויות שמורות",
    },
    "en": {
        "lang_name": "English", "other_lang": "עברית",
        "home": "Home", "services": "Services", "fleet": "Our fleet", "tours": "Tours",
        "articles": "Articles", "faq": "FAQ", "reviews": "Reviews", "book": "Book",
        "call": "Call", "whatsapp": "WhatsApp", "menu": "Menu",
        "tagline": "Private transfers, private drivers and tours across Israel",
        "book_title": "Book a ride", "book_lead": "Fill in the details and your booking opens in WhatsApp, ready to send. We will reply with confirmation and a price.",
        "f_name": "Full name", "f_phone": "Phone", "f_service": "Service", "f_vehicle": "Vehicle",
        "f_vehicle_any": "Recommend one", "f_date": "Date", "f_time": "Time", "f_from": "From",
        "f_to": "To", "f_pax": "Passengers", "f_bags": "Suitcases", "f_flight": "Flight number (if any)",
        "f_return": "Return trip too", "f_notes": "Notes (baby seat, wheelchair, stops on the way...)",
        "f_submit": "Send on WhatsApp", "f_required": "Required",
        "noscript": "The form needs JavaScript. You can message us on WhatsApp directly:",
        "wa_intro": "Hello, I would like to book a ride:",
        "seats": "seats", "seats_ask": "varies",
        "suitable": "Suitable vehicles", "read_more": "Read more", "related": "More on the site",
        "all_services": "All services", "updated": "Updated",
        "reviews_title": "What our customers say", "tours_title": "Our tours", "faq_title": "Frequently asked questions",
        "duration": "Duration", "price": "Price",
        "contact": "Contact", "available": "Available by phone and WhatsApp",
        "not_found": "Page not found", "not_found_text": "The link may have changed. Go back to the home page or book a ride.",
        "skip": "Skip to content",
        "rights": "All rights reserved",
    },
}
