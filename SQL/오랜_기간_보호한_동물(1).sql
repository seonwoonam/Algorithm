/**
    15 : 56 ~ 16 : 03
    ANIMAL_INS : 동물 보호소에 들어온 동물의 정보
    ANIMAL_OUTS : 동물 보호소에서 입양 보낸 동물의 정보
    
    아직 입양을 못 간 동물 중
    가장 오래 보호소에 있던 동물 
    3마리의 이름 과 보호 시작일 
    보호 시작일 순으로 결과 조회

    NOT EXISTS, NOT IN 같은걸로도 풀 수 있을듯
**/

SELECT 
    NAME, DATETIME
FROM ANIMAL_INS
WHERE ANIMAL_ID IN (
    SELECT
        ANIMAL_ID
    FROM ANIMAL_INS
    EXCEPT 
    SELECT
        ANIMAL_ID
    FROM ANIMAL_OUTS
)
ORDER BY DATETIME
LIMIT 3
