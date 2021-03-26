#     #13.1 윤년
#
# import calendar
# print(calendar.isleap(1900))
# print(calendar.isleap(1996))
# print(calendar.isleap(1999))
# print(calendar.isleap(2000))
# print(calendar.isleap(2004))
# print(calendar.isleap(2002))
#
#     #13.2 datatime 모듈
#
# from datetime import date
# halloween = date(2019, 10, 31)
# print(halloween)
# print(halloween.day)
# print(halloween.month)
# print(halloween.year)
# print(halloween.isoformat())
#
# #today() 메서드를 사용하여 오늘 날짜를 출력
# now = date.today()
# print(now)
#
# #timedelta 객체를 사용하여 날짜에 시간 간격을 더해보자
# from datetime import timedelta
# one_day = timedelta(days=1)
# tomorrow = now + one_day
# print(tomorrow)
# print(now + 17*one_day)
# yesterday = now - one_day
# print(yesterday)
#
# #날짜의 범위는 date.min(year=1, month=1, day=1)부터 date.max(year=9999, month=12, day=31)까지다. 결과적으로 역사적 또는 천문학적인 날짜는 계산할 수 없다.
# #datetime모듈의 time객체는 하루의 시간을 나타내는 데 사용된다.
# from datetime import time
# noon = time(12, 0, 0)
# print(noon)
# print(noon.hour)
# print(noon.minute)
# print(noon.second)
# print(noon.microsecond)
#
# #인수는 가장 큰 시간 단위를(hour)부터 가장 작은 시간 단위(microsecond) 순으로 입력한다. 인수를 입력하지 않으면 time객체의 초기 인수는 0으로 간주된다. 그리고 컴퓨터는 마이크로초를 정확하게 계산할 수 없다.
#
# #datetime 객체는 날짜와 시간 모두를 포함한다. January 2, 2019, at 3:04 A.M, 5초, 6마이크로초와 같이 한 번에 생성된다.
# from datetime import datetime
# some_day = datetime(2019, 1, 2, 3, 4, 5, 6)
# print(some_day)
# #중간의 T는 날짜와 시간을 구분한다.
# print(some_day.isoformat())
#
# #datetime 객체에서 now() 메서드로 현재 날짜와 시간을 얻을 수 있다.
# from datetime import datetime
# now = datetime.now()
# print(now)
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)
# print(now.microsecond)
#
# #combine()으로 date 객체와 time 객체를 datetime 객체로 병합할 수 있다.
# from datetime import datetime, time, date
# noon = time(12)
# this_day = date.today()
# noon_today = datetime.combine(this_day, noon)
# print(noon_today)
# print(noon_today.date())
# print(noon_today.time())
#
#     #13.3 time 모듈
#
# #절대 시간을 나타내는 한 가지 방법은 어떤 시작점 이후 초를 세는 것이다. 유닉스 시간은 1970년 1월 1일 자정 이후 시간의 초를 사용한다. 이 값은 에폭epoch이라고 부르며, 에폭은 시스템간에 날짜와 시간을 교환하는 아주 간단한 방식이다.
# #time 모듈의 time() 함수는 현재 시간을 에폭 값으로 반환한다.
# import time
# now = time.time()
# print(now)
# #ctime() 함수를 사용하여 에폭 값을 문자열로 변환할 수 있다.
# print(time.ctime(now))
#
# #에폭 값은 자바스크립트와 같은 다른 시스템에서 날짜와 시간을 교환하기 위한 유용한 최소 공통분모다. 그리고 각각의 날짜와 시간 요소를 얻기 위해 time 모듈의 struct_time 객체를 사용할 수 있다. localtime() 메서드는 시간을 시스템의 표준 시간대로, gmtime() 메서드는 시간을 UTC로 제공한다.
# print(time.localtime(now))
# print(time.gmtime(now))
#
# #struct_time에서 tm_...대신, 네임드 튜플처럼 인덱스를 사용할 수 있다.
# import time
# now = time.localtime()
# print(now)
# print(now[0])
# print(list(now[x] for x in range(9)))
#
# #mktime() 메서드는 struct_time 객체를 에폭 초로 변환한다.
# #아래의 값은 위의 에폭값과 일치하지 않는다. struct_time객체는 시간을 초까지만 유지하기 때문이다.
# print(time.mktime(now))

#     #13.4 날짜와 시간 읽고 쓰기
#
# #isoformat()이 날짜와 시간을 쓰기 위한 유일한 방법은 아니다. time 모듈에서 본 ctime()함수로 쓸 수도 있다. 이 함수는 에폭 시간을 문자열로 변환한다.
# import time
# now = time.time()
# print(time.ctime(now))
#
# #또한 strftime()을 사용하여 날짜와 시간을 문자열로 변환할 수 있다. 이는 datetime, date, time객체에서 메서드로 제공되고, time 모듈에서 함수로 제공된다. strftime()은 아래의 표처럼 문자열의 출력 포맷을 지정할 수 있다.
#
# #숫자는 자릿수에 맞춰 왼족에 0이 채워진다.
# #다음은 time 모듈에서 제공하는 strftime() 함수다. 이것은 struct_time 객체를 문자열로 변환한다. 먼저 포맷 문자열 fmt를 정의하고, 이것을 다시 사용하자.
# import time
# fmt = "It's %A, %B, %d, %Y, local time %I:%M:%S%p"
# t = time.localtime()
# print(t)
# print(time.strftime(fmt, t))
#
# #이것을 다음과 같이 date 객체에 사용하면 날짜 부분만 작동한다. 그리고 시간은 기본값으로 자정으로 지정된다.
# from datetime import date
# some_day = date(2019, 7, 4)
# fmt = "It's %A, %B, %d, %Y, local time %I:%M:%S%p"
# print(some_day.strftime(fmt))
#
# #time 객체는 시간 부분만 변환한다.
# from datetime import time
# fmt = "It's %A, %B, %d, %Y, local time %I:%M:%S%p"
# some_time = time(10, 35)
# print(some_time.strftime(fmt))
#
# #time 객체에서 날짜를 사용할 수 없다.
# #문자열을 날짜나 시간으로 변환하기 위해 같은 포맷 문자열로 strptime()을 사용한다. 정규 표현식 패턴 매칭은 없다. 문자열의 비형식 부분(% 제외)이 정확히 일치해야 한다. 2019-01-29와 같이 년-월-일이 일치하는 포맷을 지정해보자. 날자 문자열에서 대시(-) 대신 공백을 사용하면 무슨 일이 일어날까?
# import time
# fmt = "%Y-%m-%d"
# # print(time.strptime("2019 01 29", fmt))
#
# #대시(-)를 붙이면 어떻게 될까?
# import time
# fmt = "%Y-%m-%d"
# print(time.strptime("2019-01-29", fmt))
#
# #혹은 날짜 문자열과 일치하도록 문자열 fmt을 수정할 수 있다.
# import time
# fmt = "%Y %m %d"
# print(time.strptime("2019 01 29", fmt))
#
# #문자열 포맷은 맞는데, 값 범위를 벗어나면 예외가 발생한다.
# # print(time.strptime("2019 13 29", fmt))
#
# #이름은 운영체제의 국제화 설정인 로케일locale에 따라 다르다. 다른 월, 일의 이름을 출력하려면 setlocale()을 사용하여 로케일을 바꿔야 한다. setlocale()의 첫 번째 인수는 날짜와 시간을 위한 locale.LC_TIME이고, 두 번재는 언어와 국가 약어가 결합된 문자열이다. 외국인 친구들을 핼러윈 파티에 초대해보자. 월, 일, 요ㅕ일을 한국어, 영어, 프랑스어, 독일어, 스페인어, 아이슬란드어로 출력한다.
#
# import locale
# from datetime import date
# halloween = date(2019, 10, 31)
# for lang_country in ['en_us', 'fr_fr', 'de_de', 'es_es', 'is_is']:
#     locale.setlocale(locale.LC_TIME, lang_country)
#     print(halloween.strftime('%A, %B, %d'))
#
# #lang_country에 대한 값은 어디서 찾을 수 있을까? 다음 예제를 실행하여 몇 백 개의 값을 모두 찾을 수 있다.
# import locale
# names = locale.locale_alias.keys()
#
# #이전 예제에서 사용했던 것처럼(두 글자 언어 코드, 언더바, 두 글자 국가 코드) setlocale()을 실행하기 위해 names로부터 로케일 이름을 얻어온다.
# good_names = [name for name in names if \
#               len(name) == 5 and name[2] == '_']
#
# #처음 5개가 의미하는 것은 무엇일까?
# print(good_names[:5])
#
# #모든 독일어 로케일을 원한다면 다음과 같이 실행한다.
# de = [name for name in good_names if name.startswith('de')]
# print(de)


