# Pylint raw report
```UNIX
************* Module app
app.py:22:0: C0301: Line too long (131/100) (line-too-long)
app.py:148:0: C0301: Line too long (142/100) (line-too-long)
app.py:238:20: C0303: Trailing whitespace (trailing-whitespace)
app.py:373:0: C0304: Final newline missing (missing-final-newline)
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:1:0: C0410: Multiple imports on one line (sqlite3, secrets, markupsafe, math, time) (multiple-imports)
app.py:2:0: E0401: Unable to import 'flask' (import-error)
app.py:3:0: C0410: Multiple imports on one line (config, items, users) (multiple-imports)
app.py:10:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:25:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:29:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:52:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:58:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:62:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:62:31: W0622: Redefining built-in 'input' (redefined-builtin)
app.py:68:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:72:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:76:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:80:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:87:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:98:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:105:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
app.py:98:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:115:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:122:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:132:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:151:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:157:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:186:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:208:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:223:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:232:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
app.py:223:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:241:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:253:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:265:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:285:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:295:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:315:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:323:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:341:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:349:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:362:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:366:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:1:0: C0411: standard import "import sqlite3, secrets, markupsafe, math, time" should be placed before "import sqlite3, secrets, markupsafe, math, time" (wrong-import-order)
app.py:1:0: C0411: standard import "import sqlite3, secrets, markupsafe, math, time" should be placed before "import sqlite3, secrets, markupsafe, math, time" (wrong-import-order)
************* Module config
config.py:2:0: C0304: Final newline missing (missing-final-newline)
config.py:1:0: C0114: Missing module docstring (missing-module-docstring)
config.py:1:0: C0103: Constant name "secret_key" doesn't conform to UPPER_CASE naming style (invalid-name)
************* Module db
db.py:18:27: C0303: Trailing whitespace (trailing-whitespace)
db.py:19:0: C0303: Trailing whitespace (trailing-whitespace)
db.py:24:0: C0304: Final newline missing (missing-final-newline)
db.py:1:0: C0114: Missing module docstring (missing-module-docstring)
db.py:2:0: E0401: Unable to import 'flask' (import-error)
db.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:10:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:10:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:20:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:20:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
************* Module items
items.py:9:112: C0303: Trailing whitespace (trailing-whitespace)
items.py:9:0: C0301: Line too long (112/100) (line-too-long)
items.py:23:101: C0303: Trailing whitespace (trailing-whitespace)
items.py:23:0: C0301: Line too long (101/100) (line-too-long)
items.py:51:0: C0303: Trailing whitespace (trailing-whitespace)
items.py:83:56: C0303: Trailing whitespace (trailing-whitespace)
items.py:116:33: C0303: Trailing whitespace (trailing-whitespace)
items.py:123:71: C0303: Trailing whitespace (trailing-whitespace)
items.py:1:0: C0114: Missing module docstring (missing-module-docstring)
items.py:7:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:7:0: R0913: Too many arguments (8/5) (too-many-arguments)
items.py:19:8: R1704: Redefining argument with the local name 'title' (redefined-argument-from-local)
items.py:22:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:30:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:47:4: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
items.py:52:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:56:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:56:0: R0913: Too many arguments (7/5) (too-many-arguments)
items.py:69:8: R1704: Redefining argument with the local name 'title' (redefined-argument-from-local)
items.py:72:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:82:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:91:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:97:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:101:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:115:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:115:0: R0913: Too many arguments (6/5) (too-many-arguments)
items.py:122:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:132:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:139:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:144:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:148:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:152:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module seed
seed.py:22:0: C0301: Line too long (123/100) (line-too-long)
seed.py:23:0: C0301: Line too long (115/100) (line-too-long)
seed.py:1:0: C0114: Missing module docstring (missing-module-docstring)
seed.py:1:0: C0410: Multiple imports on one line (random, datetime) (multiple-imports)
seed.py:10:0: C0103: Constant name "user_count" doesn't conform to UPPER_CASE naming style (invalid-name)
seed.py:11:0: C0103: Constant name "thread_count" doesn't conform to UPPER_CASE naming style (invalid-name)
seed.py:12:0: C0103: Constant name "message_count" doesn't conform to UPPER_CASE naming style (invalid-name)
************* Module users
users.py:5:0: C0301: Line too long (111/100) (line-too-long)
users.py:28:0: C0303: Trailing whitespace (trailing-whitespace)
users.py:1:0: C0114: Missing module docstring (missing-module-docstring)
users.py:1:0: E0401: Unable to import 'werkzeug.security' (import-error)
users.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:9:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:14:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:24:4: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
users.py:32:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:37:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:41:0: C0116: Missing function or method docstring (missing-function-docstring)

------------------------------------------------------------------
Your code has been rated at 7.18/10 (previous run: 7.17/10, +0.01)
```
# DETAILS
## Trailing whitespace
A large part of the report consisted of whitespace reports:
```UNIX
db.py:18:27: C0303: Trailing whitespace (trailing-whitespace)
db.py:19:0: C0303: Trailing whitespace (trailing-whitespace)
```
These were present mainly to make the code more readable by implementing visible block separations where different subfunctions were present. These can be removed, provided one is adequately trusting of the code's users.

## Long lines
One of the lines reached close to the suggested line limit of 100.
```UNIX
app.py:22:0: C0301: Line too long (131/100) (line-too-long)
app.py:148:0: C0301: Line too long (142/100) (line-too-long)
```
... in reference to these line:
```Python
    return render_template("index.html", message = "Welcome to film review site!", page=page, page_count=page_count, items=reviews)

    #...
    
    return render_template("review_data.html", item=item, classes=classes, comments=comments, images=images, page=page, page_count=page_count)
```
Not much can be done to remedy this since every applied variable is needed.

## Docstring
Docstring reports were very common in regards to functions and methods.
```UNIX
app.py:10:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:25:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:29:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:52:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:58:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:62:0: C0116: Missing function or method docstring (missing-function-docstring)
```
The idea is that these functions lacked docstring comments. This can be safely ignored since it is not being used regardless.

## Or else
The app marked an if-else branch within the code writing as unnecessary. This is strictly speaking true
```UNIX
app.py:105:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
```
Referring to this snippet of code ...
```Python
        if user_id:
            session["user_id"] = user_id
            session["username"] = username
            session["csrf_token"] = secrets.token_hex(16)
            return redirect("/")
        else:
            flash("Error: Double-check your username or password.")
            return redirect("/login")

```
... which can be rewritten as this ...
```Python
        if user_id:
            session["user_id"] = user_id
            session["username"] = username
            session["csrf_token"] = secrets.token_hex(16)
            return redirect("/")
        flash("Error: Double-check your username or password.")
        return redirect("/login")

```
Though it is more useful to developers if it was branched for clarity, cutting it down is fine too. I will elect to leave it as is. Similarly ...

## Return exceptions
... the Pylint program marked the login function with this:
```UNIX
app.py:98:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
```
This can also be ignored since every return here is doing something - redirecting or rendering. The idea is that, since methods available are `GET` and `POST`, there is a potential the function is called without it being any method. This is impossible - nothing else in the code calls to it directly and the only way HTML requests can be done is through the two methods. Safely ignore.

## Variable name
The program marked config's secret key as non-conforming to naming style. This can be true in larger projects, but I will elect to keep it in snake_case as it is better for this specific scenario where the file is a single line and it connects to the app.py as:
```Python
app.secret_key = config.secret_key
```

## Order of import / import issues
```UNIX
app.py:2:0: E0401: Unable to import 'flask' (import-error)
```
The program often fails to import flask, which is a problem we do not have, thus we can ignore it.
A more interesting note is that Pylint suggest standard and third-party imports before first-party ones.
```UNIX
app.py:1:0: C0411: standard import "import sqlite3, secrets, markupsafe, math, time" should be placed before "import sqlite3, secrets, markupsafe, math, time" (wrong-import-order)
```
Given this is a one-liner, it is scarcely important to switch it.

## Empty list danger
The report does mention dangerous list values
```UNIX
db.py:10:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:20:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
```
Referring to the execute and query functions of db.py:
```Python
def execute(sql, params=[]):
    con = get_connection()
    result = con.execute(sql, params)
    con.commit()
    g.last_insert_id = result.lastrowid
    con.close()
    
def query(sql, params=[]):
    con = get_connection()
    result = con.execute(sql, params).fetchall()
    con.close()
    return result
```
The concern is that the functions that modify the list object itself will affect all other functions due to the way references and objects work. Example: 
```Python
def f(value, lister=[]):
    lister.append(value)
    return lister

print(f(1))
print(f(2))
```
... In this scenario, a call like an empty dictionary is dangerous because it can output:
```UNIX
[1]
[1, 2]
```
Instead of
```UNIX
[1]
[2]
```
This is no concern here since we are not modifying this empty list at all.

## Function issues
Of particular note were alerts:
```UNIX
items.py:56:0: R0913: Too many arguments (7/5) (too-many-arguments)
items.py:115:0: R0913: Too many arguments (6/5) (too-many-arguments)
items.py:69:8: R1704: Redefining argument with the local name 'title' (redefined-argument-from-local)
```
Which are issues we do not need to worry about since all arguments are necessary for us. Redefining title though is a little dangerous and thus the variable was swapped to a different name - "classy".

