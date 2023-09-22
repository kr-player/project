import re  # 정규식 사용
from collections import Counter  # 빈도 계산
from wordcloud import WordCloud  # 워드 클라우드
from konlpy.tag import Okt  # 형태소 분석기

def text_normalization(text):
    # 공백 제거
    text = ' '.join(text.split())
    return text

def tokenize(text):
    okt = Okt()
    tokens = okt.nouns(text)  # 명사만 추출
    return tokens

def remove_stopwords(tokens):
    # 불용어 사전 로드
    stopwords = ['주무르도록', "피소"]  # 필요한 불용어 추가
    filtered_tokens = [word for word in tokens if word not in stopwords]
    return filtered_tokens

def count_word_frequency(tokens):
    word_counter = Counter(tokens)
    return word_counter

def generate_wordcloud(word_counter):
    wordcloud = WordCloud(font_path=':/Library/Fonts/AppleGothic', background_color='white').generate_from_frequencies(word_counter)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

text = "수업 시간 중 학생의 어깨를 안마했다가 피멍이 들었다는 이유로 아동학대로 신고당한 초등학교 교사가 무혐의 처분을 받았다.전주지검 남원지청은 아동학대 혐의로 조사를 받아온 A 교사에게 무혐의 처분을 내렸다고 22일 밝혔다.A 교사는 지난 4월 14일 스케이트보드 수업 중 B양의 어깨를 주물러 피멍이 들게 한 혐의를 받았다.당시 A 교사는 쉬는 시간에 학생들끼리 기차 대형을 만들어 앞 사람의 어깨를 주무르도록 하고는 본인도 대형에 끼었다.며칠 뒤 A 교사는 자신이 어깨를 주물렀던 B양의 어깨에 멍이 들었다며 학부모로부터 아동학대 혐의로 신고당했다.A 교사는 이후 경찰, 전북교육청 산하 전북교육인권센터, 남원시 아동학대 전담팀 등에 출석해 조사받았다.그 결과 전북교육인권센터와 남원교육지원청은 아동학대가 아니라고 판단했지만 남원시 아동학대 전담팀은 아동학대를 인정해 혼란을 야기했다.이 일로 전북 지역 교원단체들은 교권이 무너졌다며 아동학대 처벌법 개정을 촉구했고, 학부모는 전북교육인권센터의 재조사와 교원단체의 사과를 요구하는 등 갈등이 심화했다.이 사건을 조사한 검찰은 여러 참고인 조사를 거쳐 혐의없음 처분을 내렸다며 자세한 내용은 이야기하기 어렵다고 말했다.이 수업에 참여한 학생들, 보조 교사 등의 진술을 청취한 결과 당시 A 교사가 B양을 괴롭히고 체벌하는 분위기가 아니었다는 게 검찰의 조사 내용이다.이에 정재석 전북교사노동조합 위원장은 교원의 정당한 생활지도를 아동학대로 보지 않는다는 내용의 법안이 국회를 통과했지만, 여전히 교사들의 아동복지법 위반 혐의 피소를 막기에는 역부족이라며 교육은 보육과 엄연히 다르니 교원을 아동복지법 제17조 금지행위의 대상에서 배제해야 한다고 주장했다"
normalized_text = text_normalization(text)
tokens = tokenize(normalized_text)
filtered_tokens = remove_stopwords(tokens)
word_counter = count_word_frequency(filtered_tokens)
generate_wordcloud(word_counter)
