PettanWeb
=========
Author: Jim Chen (jabbany)

PettanWeb : Minimalisic Python CGI Web Engine implemented in Functions. 
平坦Web : 一个极简主义的Python网络架构，全部由散装函数实现！

Using
--------
Clone the repo into your project, and then `import pettanweb`!

Provides
--------

- Basic header handling 基础的头部信息处理
  
  Sending any HTTP header (to be processed by the CGI Server)
  Handles repeated sends of header
  
- Basic router 基础的路由

  Router entries are implemented as tuples. We support end wildcard and specific
  entry. E.g.: `("page","thispage")`, or `("pages", "*")`.
  
  Router falls through to `()` if it cannot find a matching route. If `()` does not
  exist router will give a very crude 404 message.
  
- Basic Cookie handling 基础的Cookie处理

  Router handles reading cookies through python's Cookie module. Write your own
  cookies using header handling.

Does Not Provide
------
- Templater Bindings, nope.
- Sessions, nope, DIY.
- Static routing /w 304 not modified support, nope, DIY.

PettanWeb is small, and flat. It's not necessarily fast.
平坦Web，小，平，不快。她不会帮你做很多。但是平啊！是稀有价值！！

Contributing
------
Suggestions, bug-reports and code are all very welcome. 

Note: Code should be flat, and optionally importable. Pettan is flat and simple, 
you should keep it that way.

License
------
Read the [other](LICENSE) file.
