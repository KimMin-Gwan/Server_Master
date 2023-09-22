# #버린 코드 저장소
def fold:  #이러면 코드가 접히지
    dict_urgency_aac ={"AAC":[]}
    add_txt_dict_location(dict_aac, "카테고리/test_location.txt")
    add_txt_dict_category(dict_aac,"카테고리/test_category.txt")
    add_txt_dict_flow(dict_aac, "카테고리/test_flow.txt")   
    add_txt_dict_AAC(dict_aac, "카테고리/test_aac.txt")
    add_txt_dict_ai(dict_aac, "카테고리/category.txt")
    add_txt_dict_urgency(dict_urgency_aac, "카테고리/urgency.txt")
    add_txt_dict_urgency_aac(dict_urgency_aac, "카테고리/urgency_aac.txt")

    node_list=["주문:", "요청카페:", "계산요청:"]
    node_add_multi(dict_aac, id_finder(dict_aac,"카페"), id_finder_multi(dict_aac,node_list))
    node_add_single(dict_aac, id_finder(dict_aac,"주문"), id_finder(dict_aac,"종류"))
    node_list=["커피","티","스무디"]
    node_add_multi(dict_aac, id_finder(dict_aac,"종류"), id_finder_multi(dict_aac,node_list))
    node_list = ["에스프레소","아메리카노","카페라떼","카페모카","카라멜마끼야또","바닐라라떼"]
    node_add_multi(dict_aac, id_finder(dict_aac,"커피"), id_finder_multi(dict_aac,node_list))
    add_single_to_multi(dict_aac, node_list, id_finder(dict_aac,"HOTCOLD"))
    node_list = ["녹차","얼그레이티","히비스커스티","캐모마일티","패션후르츠티","밀크티"]
    node_add_multi(dict_aac, id_finder(dict_aac,"티"), id_finder_multi(dict_aac,node_list))
    add_single_to_multi(dict_aac, node_list, id_finder(dict_aac,"HOTCOLD"))
    node_list = ["수박스무디","망고스무디","딸기스무디","커피스무디","초콜릿스무디","민트스무디"]
    node_add_multi(dict_aac, id_finder(dict_aac,"스무디"), id_finder_multi(dict_aac,node_list))
    add_single_to_multi(dict_aac, node_list, id_finder(dict_aac,"잔"))
    node_list = ["따뜻하게","차갑게"]
    node_add_multi(dict_aac, id_finder(dict_aac,"HOTCOLD"), id_finder_multi(dict_aac,node_list))
    add_single_to_multi(dict_aac, node_list, id_finder(dict_aac,"잔"))
    node_list = ["포장","매장","텀블러"]
    node_add_multi(dict_aac, id_finder(dict_aac,"잔"), id_finder_multi(dict_aac,node_list))
    add_single_to_multi(dict_aac, node_list, id_finder(dict_aac,"결제방식"))
    node_list = ["카드","현금","기프티콘"]
    node_add_multi(dict_aac, id_finder(dict_aac,"결제방식"), id_finder_multi(dict_aac,node_list))

    node_list = ["빨대","물티슈","휴지","시럽","와이파이","화장실","흡연실","메뉴판"]
    node_add_multi(dict_aac, id_finder(dict_aac,"요청카페:"), id_finder_multi(dict_aac,node_list))
    list_where = node_list
    node_list = ["주세요","어디있어요","버려주세요","필요해요"]
    add_multi_to_multi(dict_aac, list_where, id_finder_multi(dict_aac,node_list))

    node_list = ["영수증","봉투","계산","가격","현금영수증"]
    node_add_multi(dict_aac, id_finder(dict_aac,"계산요청:"), id_finder_multi(dict_aac,node_list))
    list_where = node_list
    node_list = ["해주세요","주세요","필요해요","필요없어요","얼마에요"]
    add_multi_to_multi(dict_aac, list_where, id_finder_multi(dict_aac,node_list))

    node_list=["주문식당:", "추가요청:", "계산요청:"]
    node_add_multi(dict_aac, id_finder(dict_aac,"식당"), id_finder_multi(dict_aac,node_list))

    node_list=["수량", "인원", "맵기"]
    node_add_multi(dict_aac, id_finder(dict_aac,"주문식당:"), id_finder_multi(dict_aac,node_list))
    node_list=["1개" , "2개" , "3개", "4개"]
    node_add_multi(dict_aac, id_finder(dict_aac,"수량"), id_finder_multi(dict_aac,node_list))
    node_list=["1인분","2인분","3인분","4인분"]
    node_add_multi(dict_aac, id_finder(dict_aac,"인원"), id_finder_multi(dict_aac,node_list))
    node_list=["맵게" , "덜맵게" , "맵지않게"]
    node_add_multi(dict_aac, id_finder(dict_aac,"맵기"), id_finder_multi(dict_aac,node_list))

    node_list = ["휴지","물티슈","수저","젓가락","포크","나이프","소스","공기밥","반찬","메뉴판","물"]
    node_add_multi(dict_aac, id_finder(dict_aac,"추가요청:"), id_finder_multi(dict_aac,node_list))
    list_where = node_list
    node_list = ["주세요","더주세요","추가할게요"]
    add_multi_to_multi(dict_aac, list_where, id_finder_multi(dict_aac,node_list))

    node_list=["찾기마트:", "장소마트:", "계산요청:"]
    node_add_multi(dict_aac, id_finder(dict_aac,"마트"), id_finder_multi(dict_aac,node_list))

    node_list = ["가지","감자","강낭콩","계란","고구마","고추","호박","버섯","부추","우유","과자","젤리","음료수"]
    node_add_multi(dict_aac, id_finder(dict_aac,"찾기마트:"), id_finder_multi(dict_aac,node_list))
    list_where = node_list
    node_list = ["어디있어요","주세요","필요해요"]
    add_multi_to_multi(dict_aac, list_where, id_finder_multi(dict_aac,node_list))

    node_list = ["화장실","계산대","시식코너","행사장","바구니카트","푸드코트"]
    node_add_multi(dict_aac, id_finder(dict_aac,"장소마트:"), id_finder_multi(dict_aac,node_list))
    list_where = node_list
    node_list = ["어디에요","가고싶어요","필요해요","원해요"]
    add_multi_to_multi(dict_aac, list_where, id_finder_multi(dict_aac,node_list))

    node_list=["찾기편의점:", "계산요청:"]
    node_add_multi(dict_aac, id_finder(dict_aac,"편의점"), id_finder_multi(dict_aac,node_list))

    node_list = ["과자","라면","삼각김밥","빵","젤리","생필품","음료수","술","복권","담배"]
    node_add_multi(dict_aac, id_finder(dict_aac,"찾기편의점"), id_finder_multi(dict_aac,node_list))
    list_where = node_list
    node_list = ["어디있어요","주세요","필요해요"]
    add_multi_to_multi(dict_aac, list_where, id_finder_multi(dict_aac,node_list))

    node_list=["찾기문구점:", "계산요청:","요청문구점:"]
    node_add_multi(dict_aac, id_finder(dict_aac,"문구점"), id_finder_multi(dict_aac,node_list))

    node_list = ["가위","볼펜","연필",'샤프','지우개','테이프','도화지','물감','붓','딱풀','색종이','수첩','스케치북','실내화']
    node_add_multi(dict_aac, id_finder(dict_aac,"찾기문구점:"), id_finder_multi(dict_aac,node_list))
    list_where = node_list
    node_list = ["어디있어요","주세요","필요해요"]
    add_multi_to_multi(dict_aac, list_where, id_finder_multi(dict_aac,node_list))

    node_list = ['컬러인쇄','흑백인쇄','제본','코팅','스캔','선물포장','복사']
    node_add_multi(dict_aac, id_finder(dict_aac,"요청문구점:"), id_finder_multi(dict_aac,node_list))
    list_where = node_list
    node_list = ['고장났어요','필요해요','해주세요','교환해주세요','보내주세요','원해요']
    add_multi_to_multi(dict_aac, list_where, id_finder_multi(dict_aac,node_list))

    node_list=["찾기서점도서관:", "계산요청:","요청서점:"]
    node_add_multi(dict_aac, id_finder(dict_aac,"서점"), id_finder_multi(dict_aac,node_list))

    node_list = ['베스트셀러','국내소설','해외소설','만화책','도서검색대','문제집','수필','시집','신간도서','전공서적','잡지']
    node_add_multi(dict_aac, id_finder(dict_aac,"찾기서점도서관:"), id_finder_multi(dict_aac,node_list))
    list_where = node_list
    node_list = ['어디있어요','주세요','필요해요']
    add_multi_to_multi(dict_aac, list_where, id_finder_multi(dict_aac,node_list))

    node_list = ['환불해주세요','교환해주세요']
    node_add_multi(dict_aac, id_finder(dict_aac,"요청서점:"), id_finder_multi(dict_aac,node_list))

    node_list=["찾기서점도서관:", "장소도서관:","요청도서관:"]
    node_add_multi(dict_aac, id_finder(dict_aac,"도서관"), id_finder_multi(dict_aac,node_list))
    
    node_list = ['화장실','열람실','구내식당','정수기','컴퓨터실','장애인보조도구']
    node_add_multi(dict_aac, id_finder(dict_aac,"장소도서관:"), id_finder_multi(dict_aac,node_list))
    list_where = node_list
    node_list = ['어디에요','가고싶어요','필요해요','원해요']
    add_multi_to_multi(dict_aac, list_where, id_finder_multi(dict_aac,node_list))
    
    node_list = ['대여','반납']
    node_add_multi(dict_aac, id_finder(dict_aac,"요청도서관:"), id_finder_multi(dict_aac,node_list))
    list_where = node_list
    node_list = ['원해요','해주세요']
    add_multi_to_multi(dict_aac, list_where, id_finder_multi(dict_aac,node_list))

    node_list=["계산요청:","요청미용실:"]
    node_add_multi(dict_aac, id_finder(dict_aac,"미용실"), id_finder_multi(dict_aac,node_list))

    node_list = ['두피마사지','파마','커트','염색','앞머리','스포츠머리','짧게','짧지않게']
    node_add_multi(dict_aac, id_finder(dict_aac,"요청미용실:"), id_finder_multi(dict_aac,node_list))
    list_where = node_list
    node_list = ['깎아주세요','잘라주세요','원해요','해주세요','할래요']
    add_multi_to_multi(dict_aac, list_where, id_finder_multi(dict_aac,node_list))

    node_list=["계산요청:","티켓:","먹거리:","요청영화관:"]
    node_add_multi(dict_aac, id_finder(dict_aac,"영화관"), id_finder_multi(dict_aac,node_list))

    node_list = ['애니메이션','액션영화','코미디','스릴러','로맨스','조조영화','심야영화','가장빠른거']
    node_add_multi(dict_aac, id_finder(dict_aac,"티켓:"), id_finder_multi(dict_aac,node_list))
    list_where = node_list
    node_list = ['추천해주세요','예매해주세요','원해요',]
    add_multi_to_multi(dict_aac, list_where, id_finder_multi(dict_aac,node_list))

    node_list = ['팝콘','음료수','츄러스','핫도그','나쵸']
    node_add_multi(dict_aac, id_finder(dict_aac,"먹거리:"), id_finder_multi(dict_aac,node_list))
    list_where = node_list
    node_list = ['원해요','구매할게요','주세요']
    add_multi_to_multi(dict_aac, list_where, id_finder_multi(dict_aac,node_list))

    node_list = ['좌석변경','예매취소','장애인석']
    node_add_multi(dict_aac, id_finder(dict_aac,"요청영화관:"), id_finder_multi(dict_aac,node_list))
    list_where = node_list
    node_list = ['해주세요','원해요','가능해요']
    add_multi_to_multi(dict_aac, list_where, id_finder_multi(dict_aac,node_list))

    node_list = ['필요해요','필요없어요']
    node_add_multi(dict_aac, id_finder(dict_aac,"현금영수증발급문의"), id_finder_multi(dict_aac,node_list))

    node_list = ['필요해요','필요없어요']
    node_add_multi(dict_aac, id_finder(dict_aac,"현금영수증요청"), id_finder_multi(dict_aac,node_list))

    node_list=["응급 상황입니다", "심한 통증이 있습니다", "숨쉬기가 어렵습니다","피가 나고 있어요","기절할 것 같아요","곧 출산할 것 같아요","뼈가 부러진 것 같아요","배가 너무 아파요","머리가 너무 아파요"]
    node_add_multi(dict_urgency_aac, id_finder(dict_urgency_aac,"의료 상황"), id_finder_multi(dict_urgency_aac,node_list))

    node_list=['도와주세요','위험해요','불이야','도둑입니다','사고가 났어요','누군가 저를 따라옵니다','물이 넘쳐요','전기가 튀어요']
    node_add_multi(dict_urgency_aac, id_finder(dict_urgency_aac,"안전/위험 상황"), id_finder_multi(dict_urgency_aac,node_list))
    
    node_list=['길을 잃었어요','집으로 돌아가고 싶어요','경찰서로 가고 싶어요','병원으로 가고 싶어요','여기가 어디에요','버스 정류장은 어디에요','지하철 역은 어디에요','택시를 불러주세요']
    node_add_multi(dict_urgency_aac, id_finder(dict_urgency_aac,"위치/길 잃음"), id_finder_multi(dict_urgency_aac,node_list))

    node_list=['전화해주세요','119 불러주세요','112 불러주세요','가족에게 연락해주세요','물을 마시고 싶어요','화장실을 가고 싶어요','돈을 잃어버렸어요','성폭행을 당했어요']
    node_add_multi(dict_urgency_aac, id_finder(dict_urgency_aac,"기타 긴급 상황"), id_finder_multi(dict_urgency_aac,node_list))
