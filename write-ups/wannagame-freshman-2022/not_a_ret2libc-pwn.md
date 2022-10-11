# not\_a\_ret2libc (Pwn)

Bài này đưa sẵn source code, libc

<figure><img src="../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

{% code title="not_ret2libc.c" lineNumbers="true" %}
```c
#include <stdio.h>

int main()
{
    char buf;
    write(1,"give me something please: ",0x1b);
    gets(&buf);
return 0;
}
```
{% endcode %}

Nhìn đề bà

