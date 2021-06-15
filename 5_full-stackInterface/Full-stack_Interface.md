# Full-stack Interface

## Data Understanding - SQL

Client - Web Server - Application Servers - Databasem

"The goal of a model is to provide a simple low-dimensional summary of a dataset"

데이터 추상화



### MySQL & WorkBench 활용

#### 데이터베이스

구조화된 데이터의 모임. 여러 사람이 공유하고 사용할 목적으로 만들어진 정보의 집합으로, 테이블이라는 정보로 구조화되어 있음.

- 각 테이블은 특정 열의 조합으로 구성.

- 행(Observation): '가로축', row, 관측치, 개체(instance), 기록(record), 사례(example), 경우(case)
- 열(Feature): '세로축', 열(column), 특성, 속성(attribute), 변수(variable), field



#### 데이터베이스의 종류

**RDB**

- MySQL, MariaDB, Oracle 등.
- 관계형 데이터베이스는 행과 열로 구조화되어 있음. 구조화된 자료는 SQL을 통해 조회.

**NoSQL**

- MongoDB, Hbase, Casandara 등.
- 관계형 데이터베이스와 다르게 행, 열로 데이터가 구조화되지 않고 하나의 데이터를 하나의 문서로 표현. 즉, 행(Observation)이라는 개념보다 문서(Document)라는 개념으로 데이터를 바라봄.
- 분산 확장이 가능해 대용량 데이터 처리에 용이.



#### CRUD

create, read, update, delete



### SQL 문법

시작하기 전에 시스템 환경설정의 MySQL에서 서버가 실행중인지 확인.

자료 명령어 실행 후에는 항상 Response를 확인하여 자료의 정합성을 확인.

MySQL에서는 대소문자를 구분하지 않음(단, 따옴표'' 안의 문자열은 구분).

결과창에서 확인할 수 있는 cursor을 인지하고 있어야 함. 파이썬에서 연동할 때 사용.

종료시 강제종료하지 말고 File-Close Connection Tab을 이용해 종료할 것.



#### SELECT

- 칼럼 조회

  - `SELECT 호출하려는칼럼 또는 계산 FROM DB명.테이블명;`
  - `SELECT COUNT(상품 번호) FROM DB명.테이블명;`
  - `SELECT 칼럼1, 칼럼2 FROM DB명.테이블명;`

- 집계 함수

  - `SELECT 집계함수 FROM DB명.테이블명;`

    |   함수    |    의미     |
    | :-------: | :---------: |
    |  `AVG()`  |    평균     |
    | `COUNT()` | 개수 구하기 |
    |  `SUM()`  |    합계     |

    - 집계함수 COUNT() 내부에 CASE WHEN 구문을 사용하면 필요한 조건만 집계할 수 있음.

- *

  - 해당 테이블의 모든 칼럼을 조회.
  - `SELECT * FROM DB명.테이블명;`

- AS

  - 변수명 변경.
  - `SELECT 칼럼1 as 변경할칼럼명 FROM DB명.테이블명;`

- DISTINCT

  - 중복을 제외하고 데이터 조회.
  - `SELECT DISTINCT 칼럼 FROM DB명.테이블명;`



#### FROM

- `SELECT 호출하려는칼럼 또는 계산 FROM DB명.테이블명;`

- ```sql
  USE DB명;
  
  SELECT 호출하려는칼럼 또는 계산 
  FROM 테이블명;
  ```

  

#### WHERE

조건을 생성.

- `SELECT 칼럼 FROM DB명.테이블명 WHERE 칼럼 = '조건';`

- BETWEEN

  - 특정 칼럼의 값이 시작점~끝점인 데이터만 출력.

  - ``` sql
    SELECT *
    FROM DB명.테이블명
    WHERE 칼럼 BETWEEN 시작점 AND 끝점;
    ```

- 대소 관계 표현

  - ```sql
    SELECT *
    FROM DB명.테이블명
    WHERE 칼럼 '연산자' '조건';
    ```

    | 연산자 |   설명    |
    | :----: | :-------: |
    |   =    | 동일하다  |
    |   >    |   초과    |
    |   >=   |   이상    |
    |   <    |   미만    |
    |   <=   |   이하    |
    |   <>   | 같지 않다 |

- IN

  - 테이블에서 해당하는 칼럼값을 가진 데이터를 출력. ','는 '또는'을 의미.

  - ```sql
    SELECT 칼럼명
    FROM DB명.테이블명
    WHERE 칼럼명 IN (값1, 값2);
    ```

  - 숫자형은 그대로, 문자형은 ''를 사용하여 표현.

- NOT IN

  - 특정 값을 제외한 결과를 출력.

  - ```sql
    SELECT 칼럼명
    FROM DB명.테이블명
    WHERE 칼럼명 NOT IN (값1, 값2);
    ```

- IS NULL

  - 특정 값이 비어있는(NULL) 데이터를 출력.

  - NULL은 결측치(수집하지 못한 데이터)를 의미. 값이 0인 것과는 다름.

  - ```sql
    SELECT 칼럼명 또는 계산식
    FROM DB명.테이블명
    WHERE 칼럼명 IS NULL;
    ```

  - 특정 칼럼의 값이 NULL이 아닌 것만을 출력하고 싶다면 `IS NULL` 대신 `IS NOT NULL` 을 사용.

  - 주의) MySQL에서 데이터를 열람하면 각 테이블의 가장 마지막 행 다음에 모든 값이 `NULL` 인 행이 추가됨.

- LIKE '%TEXT%'

  - 특정 필드에 임의의 텍스트를 포함하는 경우를 출력.

  - ```sql
    SELECT *
    FROM DB명.테이블명
    WHERE 칼럼명 LIKE '%조건문자열%';
    ```

  - %는 문자를 의미하는데, 조건문자열 앞 뒤로 어떤 문자가 와도 상관없다는 뜻.



#### GROUP BY

- 칼럼의 값들을 그룹화해 각 값들의 평균 값, 개수 등을 구할 때 사용.

- 일반적으로 집계 함수와 함께 사용.

- ```sql
  SELECT 칼럼명, 집계함수
  FROM DB명.테이블명
  GROUP
  BY 조건칼럼;
  ```



#### JOIN

여러 테이블로 나뉜 정보를 조합할 때 테이블 결합 함수 JOIN을 사용.

- LEFT JOIN(LEFT OUTER JOIN)

  - 특정 테이블 정보를 기준으로 타 테이블을 결합.

  - TABLE_A는 기준 테이블, TABLE_B는 결합대상 테이블일 때,

    ```sql
    SELECT *
    FROM TABLE_A
    LEFT JOIN TABLE_B
    ON TABLE_A.Column1 = TABLE_B.Column2;
    ```

  - ON에는 데이터를 결합할 키 값을 입력(TABLE_A.Column1와 TABLE_B.Column2를 매칭).

- INNER JOIN

  - 두 테이블에 공통으로 존재하는 정보만 출력(교집합 개념).

  - ```sql
    SELECT *
    FROM TABLE_A
    INNER JOIN TABLE_B
    ON TABLE_A.Column1 = TABLE_B.Column2;
    ```

- FULL JOIN

  - 두 테이블에 매칭되는 정보를 모두 출력(합집합 개념).

  - FULL JOIN의 결과는 매우 큰 데이터 세트가 될 수 있음.

  - ```sql
    SELECT *
    FROM TABLE_A
    FULL JOIN TABLE_B
    ON TABLE_A.Column1 = TABLE_B.Column2;
    ```

  

#### CASE WHEN

- 조건에 따른 값을 다르게 출력하고 싶은 경우에 사용.

- ```sql
  SELECT CASE WHEN 조건1 THEN 결과1
  WHEN 조건2 THEN 결과2
  ELSE 결과3 END
  FROM DB명.테이블명;
  ```

  - 조건1을 만족하는 경우 결과1을 출력, 조건2를 만족하는 경우 결과2 출력, 조건1과 조건2를 모두 만족하지 않는 경우 결과3을 출력.
  - `ELSE` 를 사용하지 않았을 때, 각 조건을 모두 만족하지 못하는 경우는 `NULL` 을 출력.

- `GROUP BY` 다음의 칼럼명은 숫자로 대체 가능.

  - `GROUP BY 1` 은 SELECT의 첫 번째 칼럼으로 그룹핑하겠다는 의미.

  

#### RANK, DENSE_RANK, ROW_NUMBER

- 데이터에 순위를 매기는 데 사용하는 함수. 동점의 처리 방법에 차이.
- `SELECT RANK() OVER(ORDER BY column) FROM ...`
  - 동점을 같은 등수로 계산하되, 데이터 세트를 고려해 다음 등수를 매김.
- `SELECT DENSE_RANK() OVER(ORDER BY column) FROM ...`
  - 동점을 같은 등수로 계산하되, 다음 등수는 동점 등수의 바로 다음 등수를 매김.

- `SELECT ROW_NUMBER() OVER(ORDER BY column) FROM ...`
  - 동점인 경우도 서로 다른 등수로 계산.
- 특정 칼럼 내에서 순위를 매기려면 parition 사용.
  - `SELECT RANK/DENSE_RANK/ROW_NUMBER() OVER(PARTITION BY 분류칼럼 ORDER BY 순위기준칼럼) FROM ...`



#### SUBQUERY

- 연산자 이후 () 안의 쿼리를 의미.
- IN, FROM, JOIN 등에서 사용.
- subquery의 실행 결과가 하나의 테이블로 사용.
- FROM, JOIN에 subquery를 사용하는 경우, (subquery) 뒤에 항상 문자열을 입력해야 함. 쿼리 내부에서 사용하는 해당 테이블의 명칭.



### Import CSV

- Schemas - 우클릭 - Create Schema - 스키마 이름 입력 후 Apply로 생성.

- Table - 우클릭 - Table Data Import Wizard - Browse를 통해 csv 파일 선택 - Create new table - Encoding 설정, 소스 컬럼의 데이터 타입 확인 및 설정하여 생성.

생성 후에는 새로고침하여 이용.



### Google BigQuery



### Python - pymysql 연동

pip install mysql-connector-python

pip install PyMySQL==1.0.0



```python
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='127.0.0.1',
        user='root',
        password='0000',
        db='TIP_Schema',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        # Read a single record
        #sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        sql = "select total_bill from TIP_Schema.tips where tip >= 7;"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
```

파이썬에서 sql을 실행시켜 커서가 위치한 부분의 값을 읽어오는 구문.



```python
import pymysql.cursors
import pandas as pd

# MySQL DB에서 데이터 받아와서 DataFrame에 저장
conn = pymysql.connect(host='127.0.0.1', user='root', 
                       password='0000', db='classicmodels',
                       charset='utf8', autocommit=True, 
                       cursorclass=pymysql.cursors.DictCursor)
try:
   with conn.cursor() as curs:
      sql = "select total_bill from TIP_Schema.tips where tip >= 7;"
      curs.execute(sql)
      rs = curs.fetchall()

      # DB에서 받아온 값을 DataFrame에 넣음
      df = pd.DataFrame(rs)
      print(df)
      # df.to_csv('query.csv')를 통해 받아온 데이터프레임을 csv로 저장할 수 있음.

finally:
   conn.close()
```

DataFrame의 형태로 표현.



### SQL vs NoSQL

최근에는 빅데이터에 적합한 NoSQL을 사용.



## Django



## Web_Crawling