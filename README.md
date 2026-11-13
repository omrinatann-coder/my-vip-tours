# my-vip-tours.com: Tour VIP

אתר סטטי בעברית ובאנגלית שמחליף את האתר ב-Base44. אין שרת אפליקציה ואין מסד נתונים. ‏nginx מגיש קובצי HTML מוכנים, וזה עושה את האתר מהיר מאוד: דף הבית שוקל כ-7KB דחוס.

## מה יש באתר

| עברית (הכתובות המקוריות) | אנגלית |
|---|---|
| `/` | `/en` |
| `/ben-gurion-airport-transfers` | `/en/ben-gurion-airport-transfers` |
| `/private-driver-israel` | `/en/private-driver-israel` |
| `/israel-private-tours` (כולל רשימת הסיורים) | `/en/israel-private-tours` |
| `/private-transportation-israel` | `/en/private-transportation-israel` |
| `/accessible-transportation` | `/en/accessible-transportation` |
| `/israel-family-transportation` | `/en/israel-family-transportation` |
| `/19-passenger-minibus-israel` | `/en/19-passenger-minibus-israel` |
| `/hasaot-iruvim` | `/en/hasaot-iruvim` |
| `/fleet`: הצי | `/en/fleet` |
| `/articles` + 6 מאמרים | `/en/articles` |
| `/faq` (נוצר כשיש שאלות ב-`content/faq.json`) | `/en/faq` |

**טופס הזמנה** בתחתית כל עמוד. הטופס בודק את שדות החובה ופותח וואטסאפ ל-054-283-1111 עם הודעה מוכנה. הפרטים לא נשמרים בשום מקום אחר.
בנוסף, יש בכל עמוד כפתורים צפים לוואטסאפ ולשיחה.

**קידום אורגני (SEO)**: לכל עמוד יש title ו-description ייחודיים, ‏canonical, ‏hreflang לעברית ולאנגלית, תגי Open Graph ונתונים מובנים (LocalBusiness, ‏Service, ‏Article, ‏BreadcrumbList, ‏FAQPage, ודירוג ממוצע כשיש ביקורות). נוצרים גם `sitemap.xml` עם חלופות שפה ו-`robots.txt`, ולכל עמוד יש כתובת אחת בלבד: בלי `.html` ובלי `/` בסוף, ו-www מפנה לכתובת בלי www.

## עריכת תוכן

הכול בתיקייה `content/` (הסבר מפורט ב-[content/README.md](content/README.md)):

- `reviews.json`, ‏`tours.json`, ‏`faq.json`: **להשלים מהאתר הישן**. הקבצים ריקים כרגע, וכל עוד קובץ ריק, האזור שלו לא מוצג באתר.
- `services.py`: טקסטים של עמודי השירות. `articles.py`: מאמרים. `business.py`: טלפון, הצי וטקסטים של הממשק.

בדיקה מקומית:
```bash
python3 build.py --serve      # http://127.0.0.1:8080
python3 tests/check.py        # כל הכתובות הישנות קיימות, אין קישורים שבורים, ותגי SEO תקינים
```
אין תלויות: מספיק Python 3.9 ומעלה.

## העלאה לשרת (34.46.194.89, לצד TaxiApp)

האתר רץ כאתר nginx נפרד (`/etc/nginx/sites-available/my-vip-tours`) ולא נוגע ב-TaxiApp.

### 1. התקנה. אפשר לעשות את זה לפני שמשנים DNS, ו-Base44 ממשיך לעבוד.
```bash
sudo bash -c "git clone <repo-url> /opt/my-vip-tours && bash /opt/my-vip-tours/deploy/install.sh <repo-url>"
# בדיקה על השרת, לפני שה-DNS מצביע אליו:
curl -sI -H 'Host: my-vip-tours.com' http://127.0.0.1/ben-gurion-airport-transfers
```
אפשר לבדוק גם מהמחשב שלכם. מוסיפים לקובץ hosts את השורה `34.46.194.89 my-vip-tours.com` וגולשים ל-http://my-vip-tours.com. אחרי הבדיקה מוחקים את השורה.

### 2. מעבר DNS ב-IONOS
1. **יום לפני**: ב-IONOS, ‏Domains & SSL → my-vip-tours.com → DNS, מורידים את ה-TTL של רשומות ה-A (ושל ה-CNAME של www, אם יש) לערך הנמוך ביותר.
2. **ביום המעבר**: רשומת A של `@` → `34.46.194.89`. עבור `www`, רשומת A ל-`34.46.194.89` (במקום ה-CNAME של Base44, אם יש כזה).
   לא לגעת ברשומות MX או TXT. הן שייכות למייל ולאימותים.
3. ברגע שהשינוי מתפשט (בודקים עם `getent hosts my-vip-tours.com` על השרת):
   ```bash
   sudo bash /opt/my-vip-tours/deploy/https.sh <email>
   ```
   הסקריפט בודק שה-DNS באמת מצביע לשרת, מוציא תעודת HTTPS ומפעיל הפניה מ-http ל-https.
4. **לא לבטל את Base44** עד שהאתר החדש עולה ב-https ונבדק. אם משהו משתבש, מחזירים את רשומות ה-DNS לערכים הקודמים, והאתר הישן חוזר.

### 3. אחרי המעבר
- Google Search Console: מאמתים את הדומיין, שולחים את `https://my-vip-tours.com/sitemap.xml`, ובודקים את הכיסוי במשך כשבועיים.
- אם לאתר הישן היו כתובות נוספות שמופיעות בגוגל (למשל עמודי מאמרים), מוסיפים להן הפניית 301 בקובץ ה-nginx.

### עדכון האתר
```bash
sudo bash /opt/my-vip-tours/deploy/update.sh
```
הסקריפט מושך מ-git, בונה, ומריץ את `tests/check.py`. אם הבדיקה נכשלת, האתר החי לא משתנה. אם היא עוברת, הוא עובר לגרסה החדשה בבת אחת. נשמרות 5 גרסאות אחרונות לחזרה לאחור:
`sudo ln -sfn /var/www/my-vip-tours/releases/<גרסה> /var/www/my-vip-tours/current`
