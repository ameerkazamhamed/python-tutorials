Counter loops in Python are done with the *for* loop syntax, which differs
significantly than the way it is done in most other programming languages
(including the JavaScript examples from 'Show Code' on code.org).

```javascript
for (var counter=0; counter < 5; counter++) {
  doSomething();
}
```

Becomes ...

```python
for counter in range(5):
    do_something()
```

Or for counter loops that increment by a set amount and begin at a given
number:

```javascript
for (var counter=10; counter < 25; counter+=5) {
  doSomething();
}
```

Becomes ...

```python
for counter in range(10,25,5):
    do_something()
```

