# ArabiansDevWorld 👌

**Translation:**
[Readme EN](README_en.md)

هذا المشروع هو طموح لانشاء اكبر منصة لتجمع المطورين العرب
ومهندسي الحاسب الآلي من حول العالم
لنشر خبراتهم ومساعدة المقدمين علي دخول مجال البرمجة وهندسة الحاسوب
وتعزيز المحتوي العربي التقني علي الانترنت
---
"أرابيانس ديف وورلد" هي أول واجهة برمجة تطبيقات REST في العالم العربي
توفر للمطورين منصة يمكنهم استخدامها لتصميم وبناء عالم البرمجة الخاص بهم من المعرفة.
ويهدف إلى أن يكون منصة معرفية مفتوحة المصدر يحركها المجتمع للمطورين والمستخدمين العرب
لإنشاء ومشاركة والتواصل مع بعضهم البعض. نحن نؤمن بأن وجود مجتمع من المطورين العرب
أمر ضروري لتطوير المحتوى التقني العربي من أجل تعزيز المواهب المحلية وإصلاح قضية التجزئة الوطنية.
لحل هذه المشكلات ، نقوم بتطوير منصة REST API ومنتدى مفتوح المصدر لربط المطورين من جميع البلدان العربية ،
وإبقائهم على اطلاع دائم بأحدث التطورات والأفكار. انضم إلى المجتمع اليوم!

---
سوف اقوم بناء هذا المشروع باستخدام مبادئ  الخدمات المصغرة `Microservices`

---
سوف اقوم بعمل مشروع خاص بي العميل `Client`  وهو مسئول عن عرض البيانات من ال `APIs`

وبالطبع انشاء مشروع `APIs`

### user_read_api : URLs
```shell
GET:     users/list       `Admin only`
GET:     users/<username>
```
### user_write_api : URLs
```shell
POST:     users/list       `Admin only`
PUT:      users/<username>
POST:     token            `genration token`
POST:     token/refresh    `Refresh token`
```

### feed_read_api : URLs
```shell
GET:      feed/                         `View All Posts`
GET:      feed/<post_slug>-<post_id>    `Read Post`
```

### feed_write_api : URLs
```shell
POST:     feed/                         `View All Posts`
PUT:      feed/<post_slug>-<post_id>    `Update Post`
DELETE:   feed/<post_slug>-<post_id>    `Delete Post`
```
