-- 1st question

SELECT 
    account_id, cust_id, avail_balance
FROM
    account
WHERE
    status = 'active'
        AND avail_balance > 2500;
        
-- 2nd question

SELECT 
    *
FROM
    account
WHERE
    open_date BETWEEN '2000-01-01' AND '2000-12-31';
    
-- 3rd question

SELECT 
    account_id, avail_balance, pending_balance
FROM
    account
WHERE
    avail_balance != pending_balance;
    
-- 4th question

SELECT 
    account_id, product_cd
FROM
    account
WHERE
    account_id IN (1 , 10, 23, 27);
    
-- 5th question

SELECT 
    account_id, avail_balance
FROM
    account
WHERE
    avail_balance BETWEEN 101 AND 199;