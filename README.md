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
    | password | user name | string |
    | phone | phone number | string |
    | birth | birthday | string |
    | gender | gender | string |
    | type | member type | string |
    
- 사업자의 경우 (type = 2)

    | key | explanation | type |
    |--- |--- |--- |
    | user_id | user id | string |
    | user_name | user name | string |
    | password | user name | string |
    | phone | phone number | string |
    | birth | birthday | string |
    | gender | gender | string |
    | type | member type | string |
    | license | license number | string |
    
- example

    | key | explanation | type |
    |--- |--- |--- |
    | user_id | user id | string |
    | user_name | user name | string |
    | password | user name | string |
    | phone | phone number | string |
    | birth | birthday | string |
    | gender | gender | string |
    | type | member type | string |
    | license | license number | string |

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
            | 400 |1| 파라미터 오류, 상세 내용은 msg 참고 |
    
    - SUCCESS RESPONSE
    
        | key | value | type |
        |--- |--- |--- |
        | code | 0 | int |
        | msg | Join success | string |


## GPS 데이터 저장
- URI : http://34.72.100.63:5000/save
- METHOD : POST
- request
 
    | key | explanation | type |
    |--- |--- |--- |
    | user_id | user id | string |
    | lat | Latitude | string |
    | lon | Longitude | string |
    | time | Current time | string |

- example

    | key | value | type |
    |--- |--- |--- |
    | user_id | 5linesys | string |
    | lat | 37.566676 | float |
    | lon | 126.978411 | float |
    | time | 13:12:19 | string |

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
            | 400 |1| 파라미터 오류, 상세 내용은 msg 참고 |
    
    - SUCCESS RESPONSE
    
        | key | value | type |
        |--- |--- |--- |
        | code | 0 | int |
        | msg | Storage completed | string |