# my-vip-tours.com: Tour VIP

אתר סטטי בעברית ובאנגלית שמחליף את האתר ב-Base44. אין שרת אפליקציה ואין מסד נתונים. ‏nginx מגיש קובצי HTML מוכנים, וזה עושה את האתר מהיר מאוד: דף הבית שוקל כ-7KB דחוס.

## מה יש באתר

60 עמודים ו-56 הפניות. **כל כתובת מהאתר הישן נשארת באותה שפה שהייתה לה**, כפי שעולה מהייצוא של Base44 מ-16/11/2026:

- **עמודים בעברית**: `/` (דף הבית), ‏`/hasaot-menatbag`, ‏`/nahag-prati`, ‏`/hasaot-beisrael`, ‏`/hasaot-iruvim`, ‏`/hasaot-chasuna`, ‏`/hasaot-bar-mitzva`, ‏`/minibus-hashara`, ‏`/accessible-transportation`, ‏`/monit-*` (3 מסלולים), ‏`/siur-yerushalayim`, ‏`/tiyul-*` (3 טיולים), ‏`/rechavim-memugnay-yeri`, ‏`/rechavei-yukra`, ‏`/hasaot-meforsamim`, ‏`/hasaot-<עיר>` (8 ערים), ‏`/blog`.
- **עמודים באנגלית**: `/ben-gurion-airport-transfers`, ‏`/private-driver-israel`, ‏`/israel-private-tours`, ‏`/private-transportation-israel`, ‏`/israel-family-transportation`, ‏`/19-passenger-minibus-israel`, ‏`/israel-transportation-services`, ‏`/vip-transportation-israel`, ‏`/israel-vip-transportation-*` (4).
- **עמודים חדשים**: `/en` (דף הבית באנגלית), ‏`/fleet`, ‏`/en/fleet`, ‏`/siurim-pratiyim`, ‏`/en/accessible-transportation`, ‏`/en/event-transportation`, ‏`/en/blog`, ו-6 מאמרים בכל שפה.
- **עמוד שיש לו גרסה בשפה השנייה** מקושר אליה (hreflang), למשל `/nahag-prati` ↔ `/private-driver-israel`.
- **הבלוג הישן**: המאמר המלא "הסעה מנתב״ג לירושלים" נשאר בכתובת המקורית שלו. 52 המאמרים הקצרים והחוזרים מפנים (301) לעמוד הקרוב להם בנושא. גם `/Home`, ‏`/AdminPanel`, ‏`/ConfirmBooking` ו-`/ServiceAreas` מפנים. הרשימה המלאה נמצאת ב-`content/legacy.py`.

**טופס הזמנה** בתחתית כל עמוד. הטופס בודק את שדות החובה ופותח וואטסאפ ל-054-283-1111 עם הודעה מוכנה. בנוסף יש כפתורים צפים לוואטסאפ ולשיחה.

**קידום אורגני (SEO)**: לכל עמוד יש title ו-description ייחודיים, ‏canonical, ‏hreflang כשיש גרסה בשפה השנייה, ונתונים מובנים (LocalBusiness, ‏Service, ‏Article, ‏BreadcrumbList, ‏FAQPage). נוצרים גם `sitemap.xml` ו-`robots.txt`. לכל עמוד יש כתובת אחת בלבד: בלי `.html`, בלי `/` בסוף, ו-www מפנה לכתובת בלי www.

## עריכת תוכן

הכול בתיקייה `content/` (הסבר ב-[content/README.md](content/README.md)).

בדיקה מקומית:
```bash
python3 build.py --serve      # http://127.0.0.1:8080
python3 tests/check.py        # כל 44 הכתובות ו-53 המאמרים הישנים מכוסים, אין קישורים שבורים, SEO תקין
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
