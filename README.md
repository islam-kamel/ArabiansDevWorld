# ArabiansDevWorld  👨‍💻👌
**Translation:**
[Readme EN](README_en.md)

> **"أرابيانس ديف وورلد"** هي أول واجهة برمجة تطبيقات REST في العالم العربي
> توفر للمطورين منصة يمكنهم استخدامها لتصميم وبناء عالم البرمجة الخاص بهم من المعرفة.
> ويهدف إلى أن يكون منصة معرفية مفتوحة المصدر يحركها المجتمع للمطورين والمستخدمين العرب
> لإنشاء ومشاركة والتواصل مع بعضهم البعض. نحن نؤمن بأن وجود مجتمع من المطورين العرب
> أمر ضروري لتطوير المحتوى التقني العربي من أجل تعزيز المواهب المحلية وإصلاح قضية التجزئة الوطنية.
> لحل هذه المشكلات ، نقوم بتطوير منصة REST API ومنتدى مفتوح المصدر لربط المطورين من جميع البلدان العربية ،
> وإبقائهم على اطلاع دائم بأحدث التطورات والأفكار. انضم إلى المجتمع اليوم!

سوف اقوم بناء هذا المشروع باستخدام مبادئ الخدمات  المصغرة `Microservices`

---

# تشغيل ArabiansDevWorld في بيئة التطور المحلية 👨‍💻 

- ### متطلبات التشغيل 🧾
    - [Docker 20.10.16](https://docs.docker.com/get-docker/)
    - إنشاء ملف `dotenv`

in `/ArabiansDevWorld/` create .env file

**Dotenv file ex.**

```dotenv
DB_HOST = "db"
DB_NAME = "test"
DB_USER = "postgres"
DB_PASSWORD = "password"
DB_PORT = "5432"

SECRET_KEY = "a*m@xq9jywl_#csypqx&ll#2vnlsvjjg&slhtzl^ycypc2*s68"
DEBUG = 1
API_KEY = "PLzKhF9aJEeX1KtkiLUmVyDgrCYnVvXFvZR0TB575j5t8nLVVnkTWe_Nb8K0ntEuktN0G-ga2751Ad-l2nYUqz56zHRttGO6L__QzCc8HjVnIDV1ltiAmbwgrjT1ia0OitmIBQ"
BASE_URL = "http://localhost/api/v1/"
FEED_URL = "/feed"
FEED_DOC_URL = "/feed/doc"
USER_URL = "api/v1/user/register"
TOKEN_URL = "api/v1/token"
REFRESH_TOKEN_URL = "api/v1/token/refresh"
LOGIN_URL = "http://localhost/api/v1/token"
ALLOWED_HOSTS = "*"
CORS_ALLOW_ALL_ORIGINS = 1
CORS_ALLOW_METHODS = DELETE,GET,OPTIONS,PATCH,POST,PUT
```

```shell
git clone https://github.com/islam-kamel/ArabiansDevWorld.git
```
```shell
cd ArabiansDevWorld
```
```shell
docker-compose build
```
```shell
docker-compose up
```
> لا تنسي انشاء قاعدة بيانات باسم test
---

## روابط الخاصة بالــ APIs 🔗
### user_api : URLs
```shell
POST:            api/v1/user/register     `Create New User`
[GET, PUT]:      api/v1/user/<username>   `Get User info and update user info` 
POST:            api/v1/token             `genration token`
POST:            api/v1/auth/token `Refresh token`
```
> You Have Send `client_id=<client_id>` and `client_secret=<client_secret>` and `grant_type=password` and `username=<user_name>` and `password=<password>` As Params In HTTP Request 

### feed_api : URLs
```shell
[GET, POST]:      api/v1/feed/                         `View All Posts And Create Post`
[GET, PUT ]:      api/v1/feed/<post_slug>-<post_id>    `Read Post and update post`
DELETE:           api/v1/feed/<post_slug>-<post_id>    `Delete Post`
```

### API UI
User Api `api/v1/user/doc`

Feed Api `api/v1/feed/doc`


## جرب 🧪
`localhost/api/v1/user/doc`

`localhost/api/v1/feed/doc`

---

## ساهم معنا 💖 
