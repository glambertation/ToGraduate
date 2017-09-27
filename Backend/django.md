## Topic List
https://docs.djangoproject.com/en/1.11/topics/

## Cache

为了更快 为了省去计算 为了减少查询

A fundamental trade-off in dynamic websites is, well, they’re dynamic. Each time a user requests a page, the Web server makes all sorts of calculations – from database queries to template rendering to business logic – to create the page that your site’s visitor sees. This is a lot more expensive, from a processing-overhead perspective, than your standard read-a-file-off-the-filesystem server arrangement.

For most Web applications, this overhead isn’t a big deal. Most Web applications aren’t washingtonpost.com or slashdot.org; they’re simply small- to medium-sized sites with so-so traffic. But for medium- to high-traffic sites, it’s essential to cut as much overhead as possible.

That’s where caching comes in.

To cache something is to save the result of an expensive calculation so that you don’t have to perform the calculation next time. Here’s some pseudocode explaining how this would work for a dynamically generated Web page:

```
given a URL, try finding that page in the cache
if the page is in the cache:
    return the cached page
else:
    generate the page
    save the generated page in the cache (for next time)
    return the generated page

```
### Setting up the cache

The cache system requires a small amount of setup. Namely, you have to tell it where your cached data should live – whether in a database, on the filesystem or directly in memory. This is an important decision that affects your cache’s performance; yes, some cache types are faster than others.

* Memcached

    Memcached runs as a daemon and is allotted a specified amount of RAM. All it does is provide a fast interface for adding, retrieving and deleting data in the cache. All data is stored directly in memory, so there’s no overhead of database or filesystem usage.

* Database caching

    Django can store its cached data in your database. This works best if you’ve got a fast, well-indexed database server.

    1. Set BACKEND to django.core.cache.backends.db.DatabaseCache

    2. Set LOCATION to tablename, the name of the database table.

    ```
        CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
            'LOCATION': 'my_cache_table',
        }
    }

    ```

* Filesystem caching

    The file-based backend serializes and stores each cache value as a separate file. To use this backend set BACKEND to "django.core.cache.backends.filebased.FileBasedCache" and LOCATION to a suitable directory. 


* Local-memory caching
* Dummy caching (for development)

### The per-site cache

Once the cache is set up, the simplest way to use caching is to cache your entire site. You’ll need to add 'django.middleware.cache.UpdateCacheMiddleware' and 'django.middleware.cache.FetchFromCacheMiddleware' to your MIDDLEWARE setting, as in this example:

```
MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]

```

### The per-view cache

django.views.decorators.cache.cache_page()

A more granular way to use the caching framework is by caching the output of individual views. django.views.decorators.cache defines a cache_page decorator that will automatically cache the view’s response for you.

### Template fragment caching

### The low-level cache API






## ORM
Object-Relational Mapping or data mapping techniques.

* 关系型数据库
    * Django’s ORM 
        * Clearly, the power of relational databases lies in relating tables to each other. Django offers ways to define the three most common types of database relationships: many-to-one, many-to-many and one-to-one.


* 非关系型数据库
    * Django MongoDB Engine(这个也是别人对orm的理解后 扩展的mongodb engine)

        * git: https://github.com/django-nonrel/mongodb-engine

        * Documentation on http://django-mongodb-engine.readthedocs.org/

        * Use Django’s ORM (including Aggregations, Atomic Updates, Embedded Objects, Map/Reduce and GridFS), admin site, authentication, site, session and caching frameworks with MongoDB.

* cache
    * django-cache-machine
    
        * [django-cache-machine](https://github.com/django-cache-machine/django-cache-machine)
    
        * 可以参考看看 别人对django orm的理解，然后做出的这个东西..


## Middleware

处于 Handling HTTP requests 下面

Middleware is a framework of hooks into Django’s request/response processing. It’s a light, low-level “plugin” system for globally altering Django’s input or output.

Each middleware component is responsible for doing some specific function. For example, Django includes a middleware component, AuthenticationMiddleware, that associates users with requests using sessions.

内建middleware

* Cache middleware
* “Common” middleware
* Exception middleware
* GZip middleware
* Conditional GET middleware
* Locale middleware
* Message middleware
* Security middleware
* SSL Redirect
* Site middleware
* Authentication middleware
* CSRF protection middleware
* X-Frame-Options middleware

常用内建middleware
* [SecurityMiddleware](https://docs.djangoproject.com/en/1.11/ref/middleware/#django.middleware.security.SecurityMiddleware)
    * It should go near the top of the list if you’re going to turn on the SSL redirect as that avoids running through a bunch of other unnecessary middleware.
* [UpdateCacheMiddleware](https://docs.djangoproject.com/en/1.11/ref/middleware/#django.middleware.cache.UpdateCacheMiddleware)
    * It should go near the top of the list if you’re going to turn on the SSL redirect as that avoids running through a bunch of other unnecessary middleware.
    * Enable the site-wide cache. If these are enabled, each Django-powered page will be cached for as long as the CACHE_MIDDLEWARE_SECONDS setting defines. 
* GZipMiddleware
    * Before any middleware that may change or use the response body.
    * After UpdateCacheMiddleware: Modifies Vary headera.
    * [小心attack](https://docs.djangoproject.com/en/1.11/ref/middleware/#django.middleware.gzip.GZipMiddleware)
* ConditionalGetMiddleware
* SessionMiddleware
    * Enables session support.
* LocaleMiddleware
* CommonMiddleware
* CsrfViewMiddleware
* AuthenticationMiddleware
* MessageMiddleware
* FetchFromCacheMiddleware
* FlatpageFallbackMiddleware
* RedirectFallbackMiddleware

ps自己也可以写中间件

## Session
Django provides full support for anonymous sessions. The session framework lets you store and retrieve arbitrary data on a per-site-visitor basis. It stores data on the server side and abstracts the sending and receiving of cookies. Cookies contain a session ID – not the data itself (unless you’re using the cookie based backend).

ig.

This simplistic view sets a has_commented variable to True after a user posts a comment. It doesn’t let a user post a comment more than once:

```
def post_comment(request, new_comment):
    if request.session.get('has_commented', False):
        return HttpResponse("You've already commented.")
    c = comments.Comment(comment=new_comment)
    c.save()
    request.session['has_commented'] = True
    return HttpResponse('Thanks for your comment!')

```

```

def login(request):
    m = Member.objects.get(username=request.POST['username'])
    if m.password == request.POST['password']:
        request.session['member_id'] = m.id
        return HttpResponse("You're logged in.")
    else:
        return HttpResponse("Your username and password didn't match.")
```


```
def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")

```

The standard django.contrib.auth.logout() function actually does a bit more than this to prevent inadvertent data leakage. It calls the flush() method of request.session. We are using this example as a demonstration of how to work with session objects, not as a full logout() implementation.

## Glance
* model
* python manage.py migrate
* [Python API ](https://docs.djangoproject.com/en/1.11/topics/db/queries/) 基于database的查询
* admin
* url
* view 业务逻辑实现
* templates
* This is just the surface
    * A caching framework that integrates with memcached or other backends.
    * A syndication framework that makes creating RSS and Atom feeds as easy as writing a small Python class.

## Basic
Part 1: Requests and responses | 

Part 2: Models and the admin site | 

Part 3: Views and templates | 

Part 4: Forms and generic views | 

Part 5: Testing | 

Part 6: Static files | 

Part 7: Customizing the admin sitae

## Models

ig.

```
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)

```

The above Person model would create a database table like this:

```
CREATE TABLE myapp_person (
    "id" serial NOT NULL PRIMARY KEY,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL
);
```


## View

Django has the concept of “views” to encapsulate the logic responsible for processing a user’s request and for returning the response. 

## Template

The template layer provides a designer-friendly syntax for rendering the information to be presented to the user. Learn how this syntax can be used by designers and how it can be extended by programmers

## Forms

Django provides a rich framework to facilitate the creation of forms and the manipulation of form data.

## The development process

* setting
* application
* exception
* admin & manage.py
* testing
* deployment

## Admin

## Security

## Python compatibility

python 2 & 3 的区别：
https://docs.python.org/3/howto/pyporting.html#pyporting-howto

## Common Web application tools

* Authentication
* caching
* logging
* sending email
* Syndication feeds (RSS/Atom)
* Pagination
* message framework
* Serialization
* Sessions
* Sitemaps
* Static files management
* Data validation


