class Config : 
    # 이 부분은 시드 값으로 외부 유출 XX
    JWT_SECRET_KEY = 'vforvendeta12061121'

    # True는 토큰 유지 시간제한을 원할 때, False 시간제한 없음
    JWT_ACCESS_TOKEN_EXPIRES = False
    PROPAGATE_EXEPTIONS = True


    # AWS IM_02
    ACCESS_KEY = 'AKIA53RDC2H4IBE5U7MF'
    SECRET_ACCESS_KEY = '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'


    # S3 버킷 이름과, 기본 URL 주소 셋팅
    S3_BUCKET = 'im-02-image-test'
    S3_LOCATION = 'https://im-02-image-test.s3.amazonaws.com/'