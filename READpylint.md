# Pylint raw report
## First run
```UNIX
************* Module app
app.py:25:0: C0303: Trailing whitespace (trailing-whitespace)
app.py:31:0: C0303: Trailing whitespace (trailing-whitespace)
app.py:97:0: C0303: Trailing whitespace (trailing-whitespace)
app.py:131:0: C0301: Line too long (108/100) (line-too-long)
app.py:223:20: C0303: Trailing whitespace (trailing-whitespace)
app.py:268:0: C0303: Trailing whitespace (trailing-whitespace)
app.py:280:0: C0303: Trailing whitespace (trailing-whitespace)
app.py:324:0: C0303: Trailing whitespace (trailing-whitespace)
app.py:329:0: C0303: Trailing whitespace (trailing-whitespace)
app.py:362:0: C0304: Final newline missing (missing-final-newline)
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:1:0: C0410: Multiple imports on one line (sqlite3, secrets, markupsafe) (multiple-imports)
app.py:2:0: E0401: Unable to import 'flask' (import-error)
app.py:3:0: C0410: Multiple imports on one line (config, items, users) (multiple-imports)
app.py:9:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:14:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:18:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:43:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:49:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:53:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:53:31: W0622: Redefining built-in 'input' (redefined-builtin)
app.py:59:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:63:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:67:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:71:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:78:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:89:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:99:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
app.py:89:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:109:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:116:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:125:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:134:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:140:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:169:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:193:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:208:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:217:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
app.py:208:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:226:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:238:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:250:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:273:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:284:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:308:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:318:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:339:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:348:0: C0116: Missing function or method docstring (missing-function-docstring)
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
items.py:23:0: C0301: Line too long (138/100) (line-too-long)
items.py:47:0: C0303: Trailing whitespace (trailing-whitespace)
items.py:79:37: C0303: Trailing whitespace (trailing-whitespace)
items.py:107:33: C0303: Trailing whitespace (trailing-whitespace)
items.py:114:0: C0301: Line too long (134/100) (line-too-long)
items.py:1:0: C0114: Missing module docstring (missing-module-docstring)
items.py:7:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:7:0: R0913: Too many arguments (8/5) (too-many-arguments)
items.py:19:8: R1704: Redefining argument with the local name 'title' (redefined-argument-from-local)
items.py:22:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:26:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:43:4: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
items.py:48:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:52:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:52:0: R0913: Too many arguments (7/5) (too-many-arguments)
items.py:65:8: R1704: Redefining argument with the local name 'title' (redefined-argument-from-local)
items.py:68:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:78:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:88:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:92:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:106:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:106:0: R0913: Too many arguments (6/5) (too-many-arguments)
items.py:113:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:119:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:124:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:128:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:132:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:2:0: C0411: standard import "import datetime" should be placed before "import db" (wrong-import-order)
************* Module users
users.py:5:0: C0301: Line too long (111/100) (line-too-long)
users.py:27:0: C0303: Trailing whitespace (trailing-whitespace)
users.py:1:0: C0114: Missing module docstring (missing-module-docstring)
users.py:2:0: E0401: Unable to import 'werkzeug.security' (import-error)
users.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:9:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:14:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:23:4: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
users.py:31:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:36:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:40:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:2:0: C0411: third party import "from werkzeug.security import generate_password_hash, check_password_hash" should be placed before "import db" (wrong-import-order)

-----------------------------------
Your code has been rated at 6.93/10
```

### Trailing whitespace
A large part of the report consisted of whitespace reports:
```UNIX
app.py:25:0: C0303: Trailing whitespace (trailing-whitespace)
app.py:31:0: C0303: Trailing whitespace (trailing-whitespace)
app.py:97:0: C0303: Trailing whitespace (trailing-whitespace)
```
These were present mainly to make the code more readable by implementing visible block separations where different subfunctions were present. These can be removed, provided one is adequately trusting of the code's users.

### Long lines
One of the lines reached close to the suggested line limit of 100.
```UNIX
app.py:131:0: C0301: Line too long (108/100) (line-too-long)
```
... in reference to this line:
```Python
    return render_template("review_data.html", item=item, classes=classes, comments=comments, images=images)
```
Not much can be done to remedy this since every applied variable is needed.

### Docstring
Docstring reports were very common in regards to functions and methods.
```UNIX
app.py:59:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:63:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:67:0: C0116: Missing function or method docstring (missing-function-docstring)
```
The idea is that these functions lacked docstring comments. This can be safely ignored since it is not being used regardless.

### Or else
The app marked an if-else branch within the code writing as unnecessary. This is strictly speaking true
```UNIX
app.py:94:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
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

### Return exceptions
... the Pylint program marked the login function with this:
```UNIX
app.py:87:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
```
This can also be ignored since every return here is doing something - redirecting or rendering. The idea is that, since methods available are `GET` and `POST`, there is a potential the function is called without it being any method. This is impossible - nothing else in the code calls to it directly and the only way HTML requests can be done is through the two methods. Safely ignore.

### Variable name
The program marked config's secret key as non-conforming to naming style. This can be true in larger projects, but I will elect to keep it in snake_case as it is better for this specific scenario where the file is a single line and it connects to the app.py as:
```Python
app.secret_key = config.secret_key
```

### Order of import / import issues
```UNIX
app.py:2:0: E0401: Unable to import 'flask' (import-error)
```
The program often fails to import flask, which is a problem we do not have, thus we can ignore it.
A more interesting note is that Pylint suggest third-party imports before first-party ones.
```UNIX
users.py:2:0: C0411: third party import "from werkzeug.security import generate_password_hash, check_password_hash" should be placed before "import db" (wrong-import-order)
```
This is true and it should be fixed.

### Empty list danger
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

### Function issues
Of particular note were alerts:
```UNIX
items.py:52:0: R0913: Too many arguments (7/5) (too-many-arguments)
items.py:106:0: R0913: Too many arguments (6/5) (too-many-arguments)
items.py:65:8: R1704: Redefining argument with the local name 'title' (redefined-argument-from-local)
```
Which are issues we do not need to worry about since it is necessary for us.

## Improved run
Note that I did multiple intermediate runs as code modifications necessarily change line numbers.
```UNIX
************* Module app
app.py:126:0: C0301: Line too long (108/100) (line-too-long)
app.py:216:20: C0303: Trailing whitespace (trailing-whitespace)
app.py:339:0: C0304: Final newline missing (missing-final-newline)
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:1:0: C0410: Multiple imports on one line (sqlite3, secrets, markupsafe) (multiple-imports)
app.py:2:0: E0401: Unable to import 'flask' (import-error)
app.py:3:0: C0410: Multiple imports on one line (config, items, users) (multiple-imports)
app.py:9:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:14:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:18:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:41:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:47:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:51:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:51:31: W0622: Redefining built-in 'input' (redefined-builtin)
app.py:57:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:61:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:65:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:69:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:76:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:87:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:94:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
app.py:87:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:104:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:111:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:120:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:129:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:135:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:164:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:186:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:201:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:210:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
app.py:201:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:219:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:231:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:243:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:263:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:273:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:293:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:301:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:319:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:327:0: C0116: Missing function or method docstring (missing-function-docstring)
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
items.py:23:0: C0301: Line too long (138/100) (line-too-long)
items.py:47:0: C0303: Trailing whitespace (trailing-whitespace)
items.py:79:37: C0303: Trailing whitespace (trailing-whitespace)
items.py:107:33: C0303: Trailing whitespace (trailing-whitespace)
items.py:114:0: C0301: Line too long (134/100) (line-too-long)
items.py:1:0: C0114: Missing module docstring (missing-module-docstring)
items.py:7:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:7:0: R0913: Too many arguments (8/5) (too-many-arguments)
items.py:19:8: R1704: Redefining argument with the local name 'title' (redefined-argument-from-local)
items.py:22:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:26:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:43:4: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
items.py:48:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:52:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:52:0: R0913: Too many arguments (7/5) (too-many-arguments)
items.py:65:8: R1704: Redefining argument with the local name 'title' (redefined-argument-from-local)
items.py:68:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:78:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:88:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:92:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:106:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:106:0: R0913: Too many arguments (6/5) (too-many-arguments)
items.py:113:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:119:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:124:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:128:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:132:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module users
users.py:5:0: C0301: Line too long (111/100) (line-too-long)
users.py:27:0: C0303: Trailing whitespace (trailing-whitespace)
users.py:1:0: C0114: Missing module docstring (missing-module-docstring)
users.py:1:0: E0401: Unable to import 'werkzeug.security' (import-error)
users.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:9:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:14:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:23:4: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
users.py:31:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:36:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:40:0: C0116: Missing function or method docstring (missing-function-docstring)

------------------------------------------------------------------
Your code has been rated at 7.17/10 (previous run: 7.12/10, +0.05)
```