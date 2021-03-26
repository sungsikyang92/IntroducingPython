    #13.1 윤년

import calendar
print(calendar.isleap(1900))
print(calendar.isleap(1996))
print(calendar.isleap(1999))
print(calendar.isleap(2000))
print(calendar.isleap(2004))
print(calendar.isleap(2002))

    #13.2 datatime 모듈

from datetime import date
halloween = date(2019, 10, 31)
print(halloween)
print(halloween.day)
print(halloween.month)
print(halloween.year)
print(halloween.isoformat())

#today() 메서드를 사용하여 오늘 날짜를 출력
now = date.today()
print(now)

#timedelta 객체를 사용하여 날짜에 시간 간격을 더해보자
from datetime import timedelta
one_day = timedelta(days=1)
tomorrow = now + one_day
print(tomorrow)
print(now + 17*one_day)
yesterday = now - one_day
print(yesterday)

#날짜의 범위는 date.min(year=1, month=1, day=1)부터 date.max(year=9999, month=12, day=31)까지다. 결과적으로 역사적 또는 천문학적인 날짜는 계산할 수 없다.
#datetime모듈의 time객체는 하루의 시간을 나타내는 데 사용된다.
from datetime import time
noon = time(12, 0, 0)
print(noon)
print(noon.hour)
print(noon.minute)
print(noon.second)
print(noon.microsecond)

#인수는 가장 큰 시간 단위를(hour)부터 가장 작은 시간 단위(microsecond) 순으로 입력한다. 인수를 입력하지 않으면 time객체의 초기 인수는 0으로 간주된다. 그리고 컴퓨터는 마이크로초를 정확하게 계산할 수 없다.

#datetime 객체는 날짜와 시간 모두를 포함한다. January 2, 2019, at 3:04 A.M, 5초, 6마이크로초와 같이 한 번에 생성된다.
from datetime import datetime
some_day = datetime(2019, 1, 2, 3, 4, 5, 6)
print(some_day)
#중간의 T는 날짜와 시간을 구분한다.
print(some_day.isoformat())

#datetime 객체에서 now() 메서드로 현재 날짜와 시간을 얻을 수 있다.
from datetime import datetime
now = datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

#combine()으로 date 객체와 time 객체를 datetime 객체로 병합할 수 있다.
from datetime import datetime, time, date
noon = time(12)
this_day = date.today()
noon_today = datetime.combine(this_day, noon)
print(noon_today)
print(noon_today.date())
print(noon_today.time())

    #13.3 time 모듈

#절대 시간을 나타내는 한 가지 방법은 어떤 시작점 이후 초를 세는 것이다. 유닉스 시간은 1970년 1월 1일 자정 이후 시간의 초를 사용한다. 이 값은 에폭epoch이라고 부르며, 에폭은 시스템간에 날짜와 시간을 교환하는 아주 간단한 방식이다.
#time 모듈의 time() 함수는 현재 시간을 에폭 값으로 반환한다.
import time
now = time.time()
print(now)
#ctime() 함수를 사용하여 에폭 값을 문자열로 변환할 수 있다.
print(time.ctime(now))

#에폭 값은 자바스크립트와 같은 다른 시스템에서 날짜와 시간을 교환하기 위한 유용한 최소 공통분모다. 그리고 각각의 날짜와 시간 요소를 얻기 위해 time 모듈의 struct_time 객체를 사용할 수 있다. localtime() 메서드는 시간을 시스템의 표준 시간대로, gmtime() 메서드는 시간을 UTC로 제공한다.
print(time.localtime(now))
print(time.gmtime(now))

#struct_time에서 tm_...대신, 네임드 튜플처럼 인덱스를 사용할 수 있다.
import time
now = time.localtime()
print(now)
print(now[0])
print(list(now[x] for x in range(9)))

#mktime() 메서드는 struct_time 객체를 에폭 초로 변환한다.
#아래의 값은 위의 에폭값과 일치하지 않는다. struct_time객체는 시간을 초까지만 유지하기 때문이다.
print(time.mktime(now))

    #13.4 날짜와 시간 읽고 쓰기

#isoformat()이 날짜와 시간을 쓰기 위한 유일한 방법은 아니다. time 모듈에서 본 ctime()함수로 쓸 수도 있다. 이 함수는 에폭 시간을 문자열로 변환한다.
import time
now = time.time()
print(time.ctime(now))

#또한 strftime()을 사용하여 날짜와 시간을 문자열로 변환할 수 있다. 이는 datetime, date, time객체에서 메서드로 제공되고, time 모듈에서 함수로 제공된다. strftime()은 아래의 표처럼 문자열의 출력 포맷을 지정할 수 있다.
