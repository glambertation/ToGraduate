# Restful

## Restful百度百科
REST（英文：Representational State Transfer，简称REST）描述了一个架构样式的网络系统，比如 web 应用程序。它首次出现在 2000 年 Roy Fielding 的博士论文中，他是 HTTP 规范的主要编写者之一。在目前主流的三种Web服务交互方案中，REST相比于SOAP（Simple Object Access protocol，简单对象访问协议）以及XML-RPC更加简单明了，无论是对URL的处理还是对Payload的编码，REST都倾向于用更加简单轻量的方法设计和实现。值得注意的是REST并没有一个明确的标准，而更像是一种设计的风格。

### 原则条件
REST 指的是一组架构约束条件和原则。满足这些约束条件和原则的应用程序或设计就是 RESTful。
Web 应用程序最重要的 REST 原则是，客户端和服务器之间的交互在请求之间是无状态的。从客户端到服务器的每个请求都必须包含理解请求所必需的信息。如果服务器在请求之间的任何时间点重启，客户端不会得到通知。此外，无状态请求可以由任何可用服务器回答，这十分适合云计算之类的环境。客户端可以缓存数据以改进性能。
在服务器端，应用程序状态和功能可以分为各种资源。资源是一个有趣的概念实体，它向客户端公开。资源的例子有：应用程序对象、数据库记录、算法等等。每个资源都使用 URI (Universal Resource Identifier) 得到一个唯一的地址。所有资源都共享统一的接口，以便在客户端和服务器之间传输状态。使用的是标准的 HTTP 方法，比如 GET、PUT、POST 和 DELETE。Hypermedia 是应用程序状态的引擎，资源表示通过超链接互联。
### 分层系统
另一个重要的 REST 原则是分层系统，这表示组件无法了解它与之交互的中间层以外的组件。通过将系统知识限制在单个层，可以限制整个系统的复杂性，促进了底层的独立性。
当 REST 架构的约束条件作为一个整体应用时，将生成一个可以扩展到大量客户端的应用程序。它还降低了客户端和服务器之间的交互延迟。统一界面简化了整个系统架构，改进了子系统之间交互的可见性。REST 简化了客户端和服务器的实现。

## Wiki百科

https://en.wikipedia.org/wiki/Representational_state_transfer

作者在写http规范的时候，所设定的一个模型，有一系列的原则，特性，约束条件。
That process honed my model down to a core set of principles, properties, and constraints that are now called REST.[7]
架构上的特性有：

1. 表现：组件上的交互 用户感知，网络效率
2. 规模：支持大量组件之间的交互
被约束的信息，都自我描述，交互之间无状态，标准的方法和格式（便于语义明确和交换信息），response可缓存的。

 REST enables intermediate processing by constraining messages to be self-descriptive: interaction is stateless between requests, standard methods and media types are used to indicate semantics and exchange information, and responses explicitly indicate cacheability.[2]
3. 接口统一
4. 组件的可替换性
5. 服务端组件的可视化交流
6. 可移植性：带着数据的代码迁移 Portability of components by moving program code with the data
7. 可靠性 抵御系统级别的错误：来自组件的错误，链接错误，数据错误

## 阮一峰的api restful理解

http://www.ruanyifeng.com/blog/2011/09/restful.html

越来越多的人开始意识到，网站即软件，而且是一种新型的软件。
这种"互联网软件"采用客户端/服务器模式，建立在分布式体系上，通过互联网通信，具有高延时（high latency）、高并发等特点

1.  资源：文本 图片 服务 都是资源
你可以用一个URI（统一资源定位符）指向它，每种资源对应一个特定的URI。要获取这个资源，访问它的URI就可以，因此URI就成了每一个资源的地址或独一无二的识别符。
所谓"上网"，就是与互联网上一系列的"资源"互动，调用它的URI。

2.  表现层： 资源的格式展现 比如html json 等
URI只代表资源的实体，不代表它的形式。严格地说，有些网址最后的".html"后缀名是不必要的，因为这个后缀名表示格式，属于"表现层"范畴，而URI应该只代表"资源"的位置。它的具体表现形式，应该在HTTP请求的头信息中用Accept和Content-Type字段指定，这两个字段才是对"表现层"的描述。

Accept:  ``` */* ```

Content-Type:  application/javascript

content-type:  text/html; charset=UTF-8


3.  状态转化
访问一个网站，就代表了客户端和服务器的一个互动过程。在这个过程中，势必涉及到数据和状态的变化。
互联网通信协议HTTP协议，是一个无状态协议。这意味着，所有的状态都保存在服务器端。因此，如果客户端想要操作服务器，必须通过某种手段，让服务器端发生"状态转化"（State Transfer）。而这种转化是建立在表现层之上的，所以就是"表现层状态转化"。
客户端用到的手段，只能是HTTP协议。具体来说，就是HTTP协议里面，四个表示操作方式的动词：GET、POST、PUT、DELETE。它们分别对应四种基本操作：GET用来获取资源，POST用来新建资源（也可以用于更新资源），PUT用来更新资源，DELETE用来删除资源。

## 上面的wiki和文章介绍了神马是restful
## 下面要介绍如何设计一个合理的restful

参考规范1 
https://codeplanet.io/principles-good-restful-api-design/

参考规范2 （没打开2333）
https://bourgeois.me/rest/

### https

SSL/TLS协议的基本思路是采用公钥加密法，也就是说，客户端先向服务器端索要公钥，然后用公钥加密信息，服务器收到密文后，用自己的私钥解密。

但是，这里有两个问题。

1. 如何保证公钥不被篡改？

    解决方法：将公钥放在数字证书中。只要证书是可信的，公钥就是可信的。


2. 公钥加密计算量太大，如何减少耗用的时间？

    解决方法：每一次对话（session），客户端和服务器端都生成一个"对话密钥"（session key），用它来加密信息。由于"对话密钥"是对称加密，所以运算速度非常快，而服务器公钥只用于加密"对话密钥"本身，这样就减少了加密运算的消耗时间。

Tips：

公钥私钥是非对称加密，对【对称秘钥】加密解密

然后【对称秘钥】对会话加密

http 4次握手

"握手阶段"涉及四次通信，需要注意的是，"握手阶段"的所有通信都是明文的。


## 如何设计restful

### 1. 应该尽量将API部署在专用域名之下。

https://api.example.com

如果确定API很简单，不会有进一步扩展，可以考虑放在主域名下。

https://example.org/api/

ig.

比如toutiao
wenda.toutiao.com

悟空
www.wukong.com

### 2.  version
应该将API的版本号放入URL。

https://api.example.com/v1/

另一种做法是，将版本号放在HTTP头信息中，但不如放入URL方便和直观。Github采用这种做法。

### 3.  路径

路径又称"终点"（endpoint），表示API的具体网址。

在RESTful架构中，每个网址代表一种资源（resource），所以网址中不能有动词，只能有名词，而且所用的名词往往与数据库的表格名对应。一般来说，数据库中的表都是同种记录的"集合"（collection），所以API中的名词也应该使用复数。

*   https://api.example.com/v1/zoos

*   https://api.example.com/v1/animals

*   https://api.example.com/v1/employees

资源用名词表示

url是资源的路径

### 4.  http动词

*   GET（SELECT）：从服务器取出资源（一项或多项）。

*   POST（CREATE）：在服务器新建一个资源。

*   PUT（UPDATE）：在服务器更新资源（客户端提供改变后的完整资源）。

*   PATCH（UPDATE）：在服务器更新资源（客户端提供改变的属性）。

*   DELETE（DELETE）：从服务器删除资源。


ig.

GET /zoos：列出所有动物园

*   POST /zoos：新建一个动物园

*   GET /zoos/ID：获取某个指定动物园的信息

*   PUT /zoos/ID：更新某个指定动物园的信息（提供该动物园的全部信息）

*   PATCH /zoos/ID：更新某个指定动物园的信息（提供该动物园的部分信息）

*   DELETE /zoos/ID：删除某个动物园

*   GET /zoos/ID/animals：列出某个指定动物园的所有动物

*   DELETE /zoos/ID/animals/ID：删除某个指定动物园的指定动物

### 5.  过滤

如果记录数量很多，服务器不可能都将它们返回给用户。API应该提供参数，过滤返回结果。

### 6.  状态码

*   200 OK - [GET]：服务器成功返回用户请求的数据，该操作是幂等的（Idempotent）。

*   201 CREATED - [POST/PUT/PATCH]：用户新建或修改数据成功。

*   202 Accepted - [*]：表示一个请求已经进入后台排队（异步任务）

*   204 NO CONTENT - [DELETE]：用户删除数据成功。

*   400 INVALID REQUEST - [POST/PUT/PATCH]：用户发出的请求有错误，服务器没有进行新建或修改数据的操作，该操作是幂等的。

*   401 Unauthorized - [*]：表示用户没有权限（令牌、用户名、密码错误）。

*   403 Forbidden - [*] 表示用户得到授权（与401错误相对），但是访问是被禁止的。

*   404 NOT FOUND - [*]：用户发出的请求针对的是不存在的记录，服务器没有进行操作，该操作是幂等的。

*   406 Not Acceptable - [GET]：用户请求的格式不可得（比如用户请求JSON格式，但是只有XML格式）。

*   410 Gone -[GET]：用户请求的资源被永久删除，且不会再得到的。

*   422 Unprocesable entity - [POST/PUT/PATCH] 当创建一个对象时，发生一个验证错误。

*   500 INTERNAL SERVER ERROR - [*]：服务器发生错误，用户将无法判断发出的请求是否成功。

Tips.

#### 密等的

在编程中.一个幂等操作的特点是其任意多次执行所产生的影响均与一次执行的影响相同。幂等函数，或幂等方法，是指可以使用相同参数重复执行，并能获得相同结果的函数。这些函数不会影响系统状态，也不用担心重复执行会对系统造成改变。
PUT是幂等方法，POST不是。所以PUT用于更新、POST用于新增比较合适。

#### XHR

XMLHttpRequest对象可以在不向服务器提交整个页面的情况下，实现局部更新网页。当页面全部加载完毕后，客户端通过该对象向服务器请求数据，服务器端接受数据并处理后，向客户端反馈数据。 XMLHttpRequest 对象提供了对 HTTP 协议的完全的访问，包括做出 POST 和 HEAD 请求以及普通的 GET 请求的能力。XMLHttpRequest 可以同步或异步返回 Web 服务器的响应，并且能以文本或者一个 DOM 文档形式返回内容。尽管名为 XMLHttpRequest，它并不限于和 XML 文档一起使用：它可以接收任何形式的文本文档。XMLHttpRequest 对象是名为 AJAX 的 Web 应用程序架构的一项关键功能。


### 7.  超链接

RESTful API最好做到Hypermedia，即返回结果中提供链接，连向其他API方法，使得用户不查文档，也知道下一步应该做什么。

参考github的设计:

https://api.github.com/

https://api.github.com/user

### 8.  其他

（1）API的身份认证应该使用OAuth 2.0框架。

（2）服务器返回的数据格式，应该尽量使用JSON，避免使用XML。


