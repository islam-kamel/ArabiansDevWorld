# ArabiansDevWorld
```
This project is an ambition to create the largest platform
for the gathering of Arab developers 🧑‍💻
and computer engineers from around the world
to disseminate their expertise
and help providers enter the field of programming
and computer engineering to enhance
the technical Arab content on the Internet ❤️
```

I will build this project using the `Microservices` principles

---
I will do my own client project `Client` which is responsible for displaying data from the 'APIs'

Of course, the `APIs` project was established.

### user_api : URLs
```shell
POST:     users/list        `Admin only`
GET:      users/<username>  `Get User info` 
PUT:      users/<username>  `Update User info`
POST:     token             `genration token`
POST:     token/refresh     `Refresh token`
```

### feed_api : URLs
```shell
GET:      feed/                         `View All Posts`
GET:      feed/<post_slug>-<post_id>    `Read Post`
POST:     feed/                         `View All Posts`
PUT:      feed/<post_slug>-<post_id>    `Update Post`
DELETE:   feed/<post_slug>-<post_id>    `Delete Post`
```
