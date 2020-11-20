# Main Server
API 메인 서버입니다.

## 회원가입
- URI : https:/tmp.prider.xyz/join
- METHOD : POST
- request
 
- 개인의 경우(type = 1)
  
    | key | explanation | type |
    |--- |--- |--- |
    | user_id | user id | string |
    | user_name | user name | string |
    | user_pw | user name | string |
    | phone | phone number | string |
    | birth | birthday | string |
    | gender | gender | string |
    | type | member type | string |
    
- 사업자의 경우 (type = 2)

    | key | explanation | type |
    |--- |--- |--- |
    | user_id | user id | string |
    | user_name | user name | string |
    | user_pw | user name | string |
    | phone | phone number | string |
    | birth | birthday | string |
    | gender | gender | string |
    | type | member type | string |
    | license | license number | string |
    
- example

    | key | explanation | type |
    |--- |--- |--- |
    | user_id | user id | string |
    | user_name | 소크라테스 | string |
    | user_pw | 1q2w3e | string |
    | phone | 01012341234 | string |
    | birth | 970101 | string |
    | gender | M/F | string |
    | type | 2 | string |
    | license | 1323412122 | string |

- response code
    - Header :
        Content-Type : application/json
    - ERROR RESPONSE
    
        |    key   | explanation |   type  |
        | -------- | ----------- |-------- |
        |code| 오류 코드     | integer | 
        |msg | 오류 내용  | string  |
        
        - code (오류 별 반환 내용 및 상태)
        
            | HTTP STATE | code | explanation |
            |----------- | ---------- | ----------- |
            | 401 |1| Duplicate ID exists |
    
    - SUCCESS RESPONSE
    
        | key | value | type |
        |--- |--- |--- |
        | code | 0 | int |
        | msg | Join success | string |


## 로그인
- URI : https:/tmp.prider.xyz/auth
- METHOD : POST
- request
 
    | key | explanation | type |
    |--- |--- |--- |
    | user_id | user id | string |
    | user_pw | user pw | string |

- example

    | key | value | type |
    |--- |--- |--- |
    | user_id | 5linesys | string |
    | user_pw | 1q2w3e | string |

- response code
    - Header :
        Content-Type : application/json
    - ERROR RESPONSE
    
        |    key   | explanation |   type  |
        | -------- | ----------- |-------- |
        |code| 오류 코드     | integer | 
        |msg | 오류 내용  | string  |
        
        - code (오류 별 반환 내용 및 상태)
        
            | HTTP STATE | code | explanation |
            |----------- | ---------- | ----------- |
            | 401 |1| No matching ID or PW exists |
    
    - SUCCESS RESPONSE
    
        | key | value | type |
        |--- |--- |--- |
        | code | 0 | int |
        | msg | login success | string |
        | user_name | user name | string |
        | type | user type | string |
        | access_token | token for access | string |
        | refresh_token | token for refresh | string |
        
## 재발급
- URI : https:/tmp.prider.xyz/refresh
- METHOD : GET
- request
    
    | key | explanation | type |
    |--- |--- |--- 

- example

    | key | value | type |
    |--- |--- |--- |

- response code
    - Header :
        - Content-Type : application/json
        - Authorization : Bearer \< Refresh token \>
    - ERROR RESPONSE
    
        |    key   | explanation |   type  |
        | -------- | ----------- |-------- |
        |code| 오류 코드     | integer | 
        |msg | 오류 내용  | string  |
        
        - code (오류 별 반환 내용 및 상태)
        
            | HTTP STATE | code | explanation |
            |----------- | ---------- | ----------- |
            | 401 |1| No matching ID or PW exists |
           - 토큰 문제 관련 메세지 오류 결과 확인 바람
    
    - SUCCESS RESPONSE
    
        | key | value | type |
        |--- |--- |--- |
        | access_token | token for access | string |
        | user_id | user id | string| 
        
## 사용자 정보 요청
- URI : https:/tmp.prider.xyz/get_info
- METHOD : GET
- request
 
    | key | explanation | type |
    |--- |--- |--- |

- example

    | key | value | type |
    |--- |--- |--- |

- response code
    - Header :
        - Content-Type : application/json
        - Authorization : Bearer \< Access token \>
    - ERROR RESPONSE
    
        |    key   | explanation |   type  |
        | -------- | ----------- |-------- |
        |code| 오류 코드     | integer | 
        |msg | 오류 내용  | string  |
        
        - code (오류 별 반환 내용 및 상태)
        
            | HTTP STATE | code | explanation |
            |----------- | ---------- | ----------- |
           - 토큰 문제 관련 메세지 오류 결과 확인 바람
    
    - SUCCESS RESPONSE
    
        | key | value | type |
        |--- |--- |--- |
        | user_id | user id | string |
        | user_name | user name | string |
        | gender | user gender | Char |
        | birth | birth day | string |
        | type | user type | string |
        | phone | phone number | string |
