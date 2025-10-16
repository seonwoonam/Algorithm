/**
    16:56 ~ 
    ANIMAL_INS : 들어온 동물의 정보
    ANIMAL_OUTS : 입양 보낸 동물의 정보
    
    보호소에 들어올 당시에는 중성화 되지 않았지만, 보호소를 나갈 당시에는 중성화된 Spayed, Neutered
    동물의 아이디와 생물 종, 이름을 조회하는 아이디 순으로 조회하는 SQL
**/
SELECT 
    TEMP.ANIMAL_ID AS ANIMAL_ID, TEMP.ANIMAL_TYPE AS ANIMAL_TYPE, TEMP.NAME AS NAME
FROM (SELECT
    *
FROM ANIMAL_INS 
WHERE (NOT SEX_UPON_INTAKE LIKE "%Spayed%") AND (NOT SEX_UPON_INTAKE LIKE "%Neutered%")) AS TEMP    
JOIN (
    SELECT
        *
    FROM ANIMAL_OUTS 
    WHERE (SEX_UPON_OUTCOME LIKE "%Spayed%") OR (SEX_UPON_OUTCOME LIKE "%Neutered%")
) AS TEMP2 ON TEMP.ANIMAL_ID = TEMP2.ANIMAL_ID
ORDER BY ANIMAL_ID, ANIMAL_TYPE, NAME

