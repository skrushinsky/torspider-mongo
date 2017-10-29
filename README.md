# torspider-mongo

This is "official" plugin to [Torspider crawler](/skrushinsky/torspider), that
saves each report to MongoDB.

## Configuration

* **db**: MongoDB connections string, including database name, by default:<br>
  `mongodb://localhost:27017/torspider`



## Report format

Both success and error reports are saved in **reports** collection.

#### Example of success report

```
{
    "_id" : ObjectId("59f257578ed173c4e710e5d7"),
    "url" : "http://crawlers.info/",
    "ts" : ISODate("2017-10-28T18:02:53.181Z"),
    "page" : {
        "title" : "Crawlers.Info",
        "text" : "Page text here",
        "meta" : {
            "yandex-verification" : "UID here"
        },
        "language" : "ru",
        "links" : {
            "inner" : [
                "http://crawlers.info/tag/skrinshot.html",
                "http://crawlers.info/proxies.html",
                "http://crawlers.info/category/retsepty.html",
                ...
            ],
            "outer" : [
                "http://www.celeryproject.org",
                "http://pypi.python.org/pypi/pip",
                "http://www.facebook.com/crawlersinfo",
                ...
            ]
        },
        "headers" : {
            "Content-Encoding" : "gzip",
            "Content-Length" : 10243,
            "Content-Type" : "text/html",
            "Date" : ISODate("2017-10-28T18:02:53.000Z"),
            "Last-Modified" : ISODate("2017-09-03T17:12:04.000Z"),
            "Server" : "lighttpd/1.4.35"
        }
    }
}
```

#### Example of failure report

```
{
    "_id" : ObjectId("59f257648ed173c4e710e627"),
    "url" : "http://crawlers.info/feeds/all.atom.xml",
    "ts" : ISODate("2017-10-26T21:47:06.241Z"),
    "error" : "Illegal  Content-Type: application/xml"
}
```
