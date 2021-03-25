#     #12.1.1
# def unicode_test(value):
#     import unicodedata
#     name = unicodedata.name(value)
#     value2 = unicodedata.lookup(name)
#     print('value="%s", name="%s", value2="%s"' %(value, name, value2))
#
# unicode_test('A')
# unicode_test('$')
# unicode_test('\u00a2')
# unicode_test('\u20ac')
# unicode_test('\u2603')
#
# place = 'café'
# print(place)
#
# unicode_test("\u00e9")
#
# place2 = 'caf\u00e9'
# print(place2)
# place3 = 'caf\N{LATIN SMALL LETTER E WITH ACUTE}'
# print(place3)
#
# u_umlaut = "\N{LATIN SMALL LETTER U WITH DIAERESIS}"
# print(u_umlaut)
# drink = "Gew" + u_umlaut + 'rztraminer'
# print("Now I can finally have my", drink, 'in a ', place)
#
# print(len("$"))
# print(len('\U0001f47b'))
# print("$")
# print('\U0001f47b')
#
# print(chr(233))
# print(chr(0xe9))
# print(chr(0x1fc6))

#     #12.1.3 인코딩
# #유니코드 문자를 snowman에 할당
# snowman = '\u2603'
# print(snowman)
# print(len(snowman))
# #유니코드 문자를 바이트 시퀀스로 인코딩
# ds = snowman.encode('utf-8')
# #UTF-8은 가변 길이 인코딩이다. showman 유니코드 문자를 인코딩 하기 위해 3바이트를 사용한다.
# print(len(ds))
# print(ds)
# #알 수 없는 문자를 인코딩하지 않도록 한다.
# print(snowman.encode('ascii', 'ignore'))
# #알 수 없는 문자를 ? 로 대체한다.
# print(snowman.encode('ascii', 'replace'))
# #유니코드 이스케이프처럼 파이썬 유니코드 문자의 문자열을 만든다.
# print(snowman.encode('ascii', 'backslashreplace'))
# #HTML-safe 문자열 생성을 위해서 사용한다. 유니코드 이스케이프 시퀀스를 출력할 수 있는 문자열로 만든다.
# print(snowman.encode('ascii', 'xmlcharrefreplace'))

#     #12.1.4 디코딩
# #'cafe'의 유니코드 문자열을 생성
# place = 'caf\u00e9'
# print(place)
# print(type(place))
#
# #place 변수를 UTF-8 형식으로 아ㅣㄴ코딩하여 place_bytes 변수에 할당
# place_bytes = place.encode('utf-8')
# print(place_bytes)
# print(type(place_bytes))
#
# place2 = place_bytes.decode('utf-8')
# print(place2)
#
# # place3 = place_bytes.decode('ascii')
# #아스키 디코더는 예외를 던진다. 0xc3 바이트 값은 아스키 코드에 유효하지 않기 때문이다.
# #UTF-8은 123(16진수 80)과 255(16진수 FF) 사이에 있는 값의 8비트 문자를 인코딩 할 수 있지만, 아스키 코드는 그렇지 않다.
#
# place4 = place_bytes.decode('latin-1')
# print(place4)
# place5 = place_bytes.decode('windows-1252')
# print(place5)
# #위의 예제들의 교훈은 가능하면 UTF-8dmf tkdydgkfksms rjtdlek. UTF-8은 모든 유니코드 문자를 표현할 수 있고, 어디에서나 지원한다. 그리고 빠르게 디코딩과 인코딩을 수행한다.

#     #12.15 HTML 엔티티
#
# import html
# print(html.unescape("&egrave;"))
# #숫자로 된 엔티티 10진수나 16진수에도 적용된다.
# print(html.unescape("&#233;"))
# print(html.unescape("&#xe9;"))
# #명명된 문자 엔티티 번역을 딕셔너리로 가져와서 직접 변활할 수 있다. 딕셔너리 키에서 처음 '&'문자를 삭제한다(마지막 ';'를 삭제할 수도 있지만 어느 쪽이든 동작한다.)
# from html.entities import html5
# print(html5["egrave"])
# print(html5["egrave;"])
# #단일 파이썬 유니코드 문자에서 HTML 엔티티 이름으로 변환해보자. 먼저 ord()를 사용하여 문자의 10진수 값을 얻는다.
# char = '\u00e9'
# dec_value = ord(char)
# print(html.entities.codepoint2name[dec_value])
# #문자가 2개 이상인 큐니코드 문자열의 경우 다음과 같이 2단계로 변환한다.
# place = 'caf\u00e9'
# byte_value = place.encode('ascii', 'xmlcharrefreplace')
# print(byte_value)
# print(byte_value.decode())
# #place.encode('ascii', 'xmlcharrefreplace') 표현식은 인코딩된 아스키 문자의 바이트 타입을 반환한다. byte_value를 HTML 호환 문자열로 변환하려면 byte_value.decode()로 디코딩한다.

#     #12.1.6 정규화
#
# #일부 유니코드 문자는 둘 이상의 유니코드 인코딩으로 표현된다. 모양은 같지만 내부 바이트 시퀀스가 다르기 때문에 동일하게 보지 않는다.
# eacute1 = 'é'                   #UTF-8
# eacute2 = '\u00e9'              #유니코드 코드 포인트
# eacute3 = '\N{LATIN SMALL LETTER E WITH ACUTE}' #유니코드 이름
# eacute4 = chr(233)             #10진수 바이트 값
# eacute5 = chr(0xe9)            #16진수 바이트 값
# print(eacute1,eacute2,eacute3,eacute4,eacute5)
# print(eacute1==eacute2==eacute3==eacute4==eacute5)
#
# import unicodedata
# print(unicodedata.name(eacute1))
# print(ord(eacute1))         #10진 정수
# print(0xe9)                 #유니코드 16진수 정수
#
# #그냥 e와 양음 악센트를 결합하여 é를 만들어보자
# eacute_combined1 = "e\u0301"
# eacute_combined2 = 'e\N{COMBINING ACUTE ACCENT}'
# eacute_combined3 = "e" + "\u0301"
# print(eacute_combined1, eacute_combined2, eacute_combined3)
# print(eacute_combined1 == eacute_combined2 == eacute_combined3)
# print(len(eacute_combined1))
# #동일하게 보이지만 서로 다르다.
# print(eacute1 == eacute_combined1)
# #uncodedata 모듈에서 normalize()함수를 사용하여 문제를 해결할 수 있다.
# import unicodedata
# eacute_nomalized = unicodedata.normalize('NFC', eacute_combined1)
# print(len(eacute_nomalized))
# print(eacute_nomalized == eacute1)
# print(unicodedata.name(eacute_nomalized))

#     #12.2 정규 표현식
#
# #정규 표현식(regular expression)으로 복잡한 문자열 패턴매칭이 가능하다. 정규 표현식은 임포트 할 수 있는 표준 모듈 re로 제공한다. 원하는 문자열 패턴을 정의하여 소스문자열과 일치하는지 비교한다.
# import re
# result = re.match('You', 'Young Frankenstein')
# print(result)
# # You는 패던이고, Young Frankenstein은 확ㅇ니하고자 하는 문자열 소스다. match()는 소스와 패턴의 일치 여부를 확인한다.
# #좀 더 복잡한 방법으로, 나중에 패턴 확인을 빠르게 하기 위해 패턴을 먼저 컴파일할 수 있다.
# youpattern = re.compile('You')
# result2 = youpattern.match('Young Frankenstein')
# print(result2)
# #match()는 소스 처음부터 시작하는 패턴만 매칭한다. search()는 소스 어디에서나 패던을 찾아 매칭한다. match()가 소스와 패턴을 비교하는 유일한 방법은 아니다. 사용할 수 있는 다른 메서드는 다음과 같다.
# #search()는 첫 번쨰 일치하는 항목을 반환한다.
# #findall()은 중첩에 상관없이 패턴에 일치하는 모든 문자열 리스트를 반환한다.
# #split()은 패턴에 맞게 소스를 쪼갠 후 문자열 조각의 리스트를 반환한다.
# #sub()는 대체 인수를 하나 더 받아서, 패턴에 일치하는 모든 소스 부분을 대체 인수로 변경한다.

#     #12.2.1 시작부터 일치하는 패턴 찾기: match()
#
# # Young Frankenstein 문자열은 You 단어로 시작하는가?
#
# import re
# source = 'Young Frankenstein'
# m = re.match('You', source)
# if m:
#     print(m.group())
# m = re.match('^You', source)
# if m:
#     print(m.group())
#
# #Frank로 찾아보자.
# import re
# source = 'Young Frankenstein'
# m = re.match('Frank', source)
# if m:
#     print(m.group())
# #match()가 아무것도 반환하지 않아서 실행되지 않았다.
# #match()는 패턴이 소스의 처음에 있는 경우에만 작동한다.
#
# #:= 연산자를 사용하여 위의 예제를 줄여보자.
# import re
# source = 'Young Frankenstein'
# if m := re.match('Frank', source):
#     print(m.group())
#
# #반면에 serach()는 패턴이 어떤 위치에 있더라도 동작한다.
#
# import re
# source = 'Young Frankenstein'
# m = re.search('Frank', source)
# if m:
#     print(m.group())
#
# import re
# source = 'Young Frankenstein'
# m = re.match('.*Frank', source)
# if m:
#     print(m.group())
# #.*Frank에서 . 은 한 문자를 의미한다. * 은 어떤 패턴이 0회 이상 올 수 있다는 것을 의미한다. 즉, .*는 0 회 이상의 문자가 올 수 있다는 것을 의미한다. Frank는 포함되어야 할 문구를 의미한다.
# #match()는 .*Frank와 일치하는 문자열 'Young Frank'를 반환한다.

    #12.2.2 첫 번째 일치하는 패턴 찾기: search()

# # .* 와일드카드 없이 'Young Frankenstein' 소스 문자열에서 'Frank' 패턴을 찾기 위해 serach()를 사용할 수 있다.
# import re
# source = 'Young Frankenstein'
# if m := re.search('Frank', source):
#     print(m.group())

#     #12.2.3 일치하는 모든 패턴 찾기: findall()
#
# #문자열의 n의 갯수
# import re
# source = 'Young Frankenstein'
# m = re.findall('n', source)
# print(m)
# print('Found', len(m), 'matches')
#
# #문자열에서 n의 문자
# import re
# source = 'Young Frankenstein'
# m = re.findall('n.', source)
# print(m)
#
# #마지막 n은 패턴에 포함되지 않는다. n이후에 오는 문자가 없기 떄문. ?를 추가하면 된다. .은 한 문자를 의미하고 ?는 0 또는 1회를 의미한다. 그러므로 ?은 하나의 문자가 0 또는 1회 올 수 있다는 뜻이다.
# import re
# source = 'Young Frankenstein'
# m = re.findall('n.?', source)
# print(m)

#     #12.2.4 패턴으로 나누기: split()
#
# import re
# source = 'Young Frankenstein'
# m = re.split('n', source)
# print(m)

#     #12.2.5 일치하는 패턴 대체하지: sub()
#
# #sub()메서드는 문자열 replace() 메서드와 비슷하지만, 리터럴 문자열이 아닌 패턴을 사용한다.
# import re
# source = 'Young Frankenstein'
# m = re.sub('n','?',source)
# print(m)

#     #12.2.6 패턴: 특수 문자
#
# import string
# printable = string.printable
# print(len(printable))
# print(printable[0:50])
# print(printable[50:])
# print(printable)
#
# import re
# #숫자
# print(re.findall('\d', printable))
# #숫자와 문자, 언더바
# print(re.findall('\w', printable))
# #공백 문자
# print(re.findall('\s', printable))

#     #12.2.7 패턴: 지정자
#
# source = '''I wish I may, I wish I might
# Have a dish of fish tonight.'''
# import re
# #wish를 모두 찾는다.
# print(re.findall('wish', source))
# #wish 또는 fish를 모두 찾는다.
# print(re.findall('wish|fish', source))
# #wish로 시작하는 것을 찾는다.
# print(re.findall('^wish', source))
# #I wish로 시작하는 것을 찾는다.
# print(re.findall('^I wish', source))
# #fish로 끝나는 것을 찾는다.
# print(re.findall('fish$', source))
# #fish tonight.으로 끝나는 것을 찾는다.
# print(re.findall('fish tonight.$', source))
# print(re.findall('fish tonight\.$', source))
# # w 또는 f 다음에 ish가 오는 것을 찾는다.
# print(re.findall('[wf]ish', source))
# #w,s,h가 하나 이상인 것을 찾는다.
# print(re.findall('[wsh]+', source))
# #ght 다음에 알파벳 문자가 아닌 것을 찾는다.
# print(re.findall('ght\W', source))
# #wish 이전에 나오는 I를 찾는다.
# print(re.findall('I (?=wish)', source))
# #I 다음에 나오는 wish를 찾는다.
# print(re.findall('(?<=I) wish', source))
# #fish로 시작하는 단어를 찾는다. 작동하지 않음! 정규 표현식의 패턴을 입력하기 전에 항상 문자 r(raw string)을 입력한다.
# print(re.findall('\bfish', source))
# #작동한다!
# print(re.findall(r'\bfish', source))

#     #12.2.8 패턴: 매칭 결과 지정하지
#
# #match() 또는 search()를 사용할 때 모든 매칭은 m.group()과 같이 객체 m으로부터 결과를 반환한다. 패턴을 괄호로 둘러싸면 매칭은 그 괄호만의 그룹으로 저장된다. 그리고 다음과 같이 m.group()를 사용하여 그룹의 튜플을 출력한다.
# source = '''I wish I may, I wish I might
# Have a dish of fish tonight.'''
#
# import re
# m = re.search(r'(. dish\b).*(\bfish)', source)
# print(m.group())
# print(m.groups())
#
# #만약 (?P<name>expr)패턴을 사용한다면, 표현식(expr)이 매칭되고, 그룹 이름(name)의 매칭이 저장된다.
# m = re.search(r'(?P<DISH>. dish\b).*(?P<FISH>\bfish)', source)
# print(m.group())
# print(m.groups())
# print(m.group('DISH'))
# print(m.group('FISH'))

#     #12.3 이진 데이터
#
# #이진 데이터를 다루기 위해서는 엔디언endian(컴퓨터 프로세서가 데이터를 바이트로 나누는 방법)과 정수에 대한 사인 비트sigh bit 같은 개념을 알아야 한다. 또한 데이터를 추출하거나 변경하는 바이너리 파일형식과 네트워크 패킷을 배워야 할 수 도 있다.
#
#     #12.3.1 바이트와 바이트 배열
# #바이트byte는 바이트의 튜플처럼 불변immutable한다.
# #바이트 배열bytearray은 바이트의 리스트처럼 가변mutable이다.
#
# #먼저 리스트의 변수를 blist, 바이트 변수를 the_bytes. 바이트 배열 변수를 the_byte_array라고 하자.
# blist = [1, 2, 3, 255]
# the_bytes = bytes(blist)
# print(the_bytes)
# the_byte_array = bytearray(blist)
# print(the_byte_array)
#
# ##바이트 값은 b로 시작하고, 그다음 인용 부호가 따라온다. 인용 부호 안에는 \x02 또는 아스키 문자와 같은 16진수 시퀀스가 온다. 파이썬은 16진수 시퀀스나 아스키 문자를 작은 정수로 변환하지만, 아스키문자처럼 유효한 아스키 인코딩의 바이트 배열을 보여준다.
# print(b'\x61')
# print(b'\x01abc\xff')
#
# #다음 예제는 바이트 변수가 불변하다는 것을 보여준다.
# blist = [1, 2, 3, 255]
# the_bytes = bytes(blist)
# the_bytes[1] = 127
#
# #바이트 배열 변수는 변경 가능하다.
# blist = [1, 2, 3, 255]
# the_byte_array = bytearray(blist)
# print(the_byte_array)
# the_byte_array[1] = 127
# print(the_byte_array)
#
# #다음 예제의 각 줄은 0에서 255까지, 256개의 결과를 생성한다.
# the_bytes = bytes(range(0, 256))
# the_byte_array = bytearray(range(0, 256))
#
# #바이트 혹은 바이트 배열 데이터를 출력할 때, 파이썬은 출력할 수 없는 바이트에 대해서는 \xxx를 사용하고, 출력할 수 있는 바이트에 대해서는 아스키 코드 값을 사용한다(\x0a 대신 \n을 사용하는 것처럼, 일부 아스키 코드 값은 일반적인 이스케이프 문자를 사용한다).
# #다음은 the_bytes의 출력 결과다.
# print(the_bytes)
# #이것은 문자가 아닌 바이트(작은 정수)이기 때문에 혼란스러워 보인다.

#     #12.3.2 이진 데이터 변환하기: struct
#
# #파이썬 표준 라이브러리는 데이터를 처리하는 struct 모듈이 있다. struct를 사용하면 이진 데이터를 파이썬 데이터 구조로 바꾸거나 파이썬 데이터 구조를 이진 데이터로 바꿀 수 잇다.
#
# #PNG 데이터에서 이미지의 가로와 세로의 길이를 추출하는 프로그램을 작성해보자.
# #파일을 내려받은 후, 파일값을 바이트로 출력하기 위한 코드를 작성한다. 그리고 첫 30바이트의 값을 data라는 바이트 변수에 할당했다(PNG 형식 사양은 가로와 세로의 길이가 첫 24바이트 내에 저장되므로 여기서 이 데이터만 활용한다).
#
# import struct
# valid_png_header = b'\x89PNG\r\n\x1a\n'
# data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR' + \
#     b'\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'
# if data[:8] == valid_png_header:
#     width, height = struct.unpack('>LL', data[16:24])
#     print('Valid PNG, width', width, 'height', height)
# else:
#     print('Not a valid PNG')
#
# #다음은 코드에 대한 설명이다.
# ## data는 PNG 파일의 첫 30바이트를 포함한다. 페이지에 맞추기 위해 두 개의 바이트 문자열을 +로 결합하고, 라인을 유지하는 문자(\)를 사용했다.
# ## valid_png_header는 유효한 PNG 파일의 시작을 표시하는 8바이트의 시퀀스를 포함한다.
# ## width는 16~19바이트에서 추출되었고, height는 20~23바이트에서 추출됐다.
#
# #unpack()에서 >LL은 입력한 바이트 시퀀스를 해석하고, 파이썬의 데이터 형식으로 만들어주는 형식 문자열format string이다. 그 의미를 살펴보자.
# ##>는 정수가 빅 엔디언big_endian형식으로 저장되었다는 것을 의미한다.
# ##각각의 L은 4바이트의 부호 없는 long 정수unsigned long integer를 지정한다.
# #각 4바이트 값을 직접 볼 수 있다.
# print(data[16:20])
# # print(data[20:24]0x9a)
#
# #빅 엔디언 정수는 왼쪽에 최상위 바이트가 저장된다. 가로와 세로의 각 길이는 255 이하이므로 각 시퀀스의 마지막 바이트와 일치한다. 이러한 16진수 값이 예상한 10진수 값과 맞는지 확인 할 수 있다.
# print(0x9a)
# print(0x8d)
#
# #또한 struct 모듈의 pack() 함수로 파이썬 데이터를 바이트로 변환할 수 있다.
# import struct
# print(struct.pack('>L', 154))
# print(struct.pack('>L', 141))
#
# #타입 지정자는 엔디언 문자를 따른다. 어떤 지정자는 수count를 가리키는 숫자가 선행될 수 있다. 예를 들어 5B는 BBBBB와 같다. 그러므로 >LL 대신 수를 선행하여 >2L로 지정할 수 있다.
# print(struct.unpack('>2L', data[16:24]))
#
# #원하는 바이트를 바로 얻기 위해 슬라이스 data[16:24]를 사용했다. 또한 다음과 같이 x 지정자를 사용하여 필요 없는 부분을 건너뛸 수 있다.
# print(struct.unpack('>16x2L6x', data))
#
# #다음은 위 예제에 대한 설명이다.
# ##빅 엔디언 정수 형식 사용(>)
# ##16바이트를 건너뜀(16x)
# ##두 개의 부호 없는 long 정수unsigned long integer의 8 바이트를 읽음(2L)
# ##마지막 6바이트를 건너뜀 (6x)

#     #12.3.3 기타 이진 데이터 도구
#
# #다음 예제는 construct를 이용하여 data 바이트 문자열로부터 PNG의 크기를 추출하는 방법이다.
# from construct import Struct, Magic, UBInt32, Const, String
# # https://github.com/construct에 있는 코드를 적용했음
# fmt = Struct('png',
#              Magic(b'\x89PNG\r\n\x1a\n'),
#              UBInt32('length'),
#              Const(String('type', 4), b'IHDR'),
#              UBInt32('width'),
#              UBInt32('height'))
# data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR' + \
#     b'\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'
# result = fmt.parse(data)
# print(result)
# print(result.width, result.height)

#     #12.3.4 바이트/문자열 변환하기:binascii()
#
# #표준 binascii 모듈은 이진 데이터와 다양한 문자열 표현(16진수, 64진수, uuencoded 등)을 서로 변환할 수 있는 함수를 제공한다. 다음 예제는 아스키 코드 혼합과 바이트 변수를 보여주기 위해 사용했던 \x xx 이스케이프 대신 16진수 시퀀스인 8바이트의 PNG 헤더를 출력한다.
# import binascii
# valid_png_header = b'x89PNG\r\n\x1a\n'
# print(binascii.hexlify(valid_png_header))
# #그 반대도 가능하다.
# print(binascii.unhexlify(b'89504e470d0a1a0a'))

    #12.3.5 비트 연산자

#연산자        설명      예제      10진수 결과     2진수 결과
#&          And         x&y         1           0b0001
#|          Or          x|y         5           0b0101
#^          XOR         x^y         4           0b0100
#~          NOT         ~x          -6          정수 크기에 따라 이진 표현이 다름
#<<         왼쪽 시프트      x<<1        10          0b1010
#>>         오른쪽 시프트     x>>1        2           0b0010

#이러한 연산자는 8장의 셋set 연산자처럼 동작한다. & 연산자는 두 인수의 비트가 모두 1일 때 1을 반환한다. | 연산자는 둘 중 하나의 비트라도 1일 때 1을 반환한다. ^연산자는 두 인수의 비트가 서로 다를 때 1을 반환한다. ~ 연산자는 1은 0으로, 0은 1로 비트를 반전시킨다. 이것은 또한 부호를 반전시킨다. 모든 현대 컴퓨터에 사용되는 2의 보수 연산에서 최상위 비트는 부호(1 = 음수)를 나타내기 때문이다. <<와 >> 연산자는 왼쪽 또는 오른쪽으로 비트를 이동시킨다. 한번의 왼쪽 비트 시프트는 2를 곱한 것과 같고, 오른쪽 비트 시프트는 2로 나눈 것과 같다.

    #12.4 보석비유
