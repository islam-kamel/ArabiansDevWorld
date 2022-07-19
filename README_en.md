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
