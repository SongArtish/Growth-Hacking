# Issues



## ipython에서 `db.create_all()` 명령어 입력 시 context 오류

> `db.create_all()`은 테이블을 생성함

```shell
from project import app, db
app.app_context().push()
db.create_all()
```