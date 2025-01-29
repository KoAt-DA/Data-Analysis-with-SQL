                                        -- BASE REPORTS

-- Calculate the total revenue for the webshop:
-- This query calculates the total revenue of the webshop by
-- summing the sales of all products, taking both quantity and price into account.
-- The sum is obtained by joining the "OrderDetails" and "Products" tables.
SELECT 
    SUM(OD."Quantity" * P."Price") AS "Total_revenue"
FROM "OrderDetails" OD
JOIN "Products" P ON OD."Product_ID" = P."Product_ID";

---------------------------------------------------------------------------------------------------

-- Top 5 most popular products:
-- This query identifies the top 5 most popular products in terms of total quantity sold.
-- It calculates the total quantity for each product and sorts the result in descending order,
-- showing only the top 5 most purchased products.
SELECT
    P."Product_name", 
    SUM(OD."Quantity") AS "Total_quantity"
FROM "Products" P
JOIN "OrderDetails" OD ON P."Product_ID" = OD."Product_ID"
GROUP BY P."Product_name"
ORDER BY "Total_quantity" DESC
LIMIT 5;

---------------------------------------------------------------------------------------------------

-- Monthly total income:
-- This query calculates the total revenue for each month by summing the sales for all products.
-- The revenue is calculated by multiplying the quantity and price of each product,
-- and grouping the results by month. It then orders the results by month in ascending order.
SELECT 
    DATE_TRUNC('month', O."Order_Date") AS "Month", 
    SUM(OD."Quantity" * P."Price") AS "Total_Revenue"
FROM "OrderDetails" OD
JOIN "Orders" O ON OD."Order_ID" = O."Order_ID"
JOIN "Products" P ON OD."Product_ID" = P."Product_ID"
GROUP BY "Month"
ORDER BY "Month";

---------------------------------------------------------------------------------------------------

                                        -- CUSTOMER ANALYSIS


-- Top 5 highest spending customers:
-- This query identifies the top 5 customers who have spent the most in total.
-- It calculates the total spending for each customer by multiplying the quantity of 
-- purchased products by their price, then summing the total amount per customer.
-- The results are sorted in descending order to highlight the highest spenders
SELECT
    C."Name",
    SUM(OD."Quantity" * P."Price") AS "Total_spending"
FROM "OrderDetails" OD 
JOIN "Orders" O On O."Order_ID" = OD."Order_ID"
JOIN "Products" P ON OD."Product_ID" = P."Product_ID"
JOIN "Customers" C ON O."Customer_ID" = C."Customer_ID"
GROUP BY C."Name"
ORDER BY "Total spending" DESC
LIMIT 5;

---------------------------------------------------------------------------------------------------

-- High-value customers analysis:
-- This query identifies the most valuable customers based on their total spending, 
-- number of unique products purchased, and average order amount.
-- A subquery is used to calculate detailed spending metrics for each customer.
-- The results are then filtered to include only customers who:
--    - Have spent at least 5000 in total
--    - Have an average order amount of at least 1000
--    - Have placed at least 3 separate orders
-- The final results are ordered by their total spending in descending order.
SELECT
    C."Name",
    sub."Total_order_amount",
    sub."Unique_ordered_products",
    sub."Average_order_amount"
FROM(
    SELECT
        O."Customer_ID",
        SUM(OD."Quantity" * P."Price") AS "Total_order_amount",
        COUNT(DISTINCT OD."Product_ID") AS "Unique_ordered_products",
        COUNT(DISTINCT OD."Order_ID") AS "Total_orders",
        ((SUM(OD."Quantity" * P."Price")) / (COUNT(DISTINCT OD."Order_ID"))) AS "Average_order_amount"
    FROM "OrderDetails" OD
    JOIN "Orders" O ON O."Order_ID" = OD."Order_ID"
    JOIN "Products" P ON P."Product_ID" = OD."Product_ID"
    GROUP BY O."Customer_ID"
    HAVING SUM(OD."Quantity" * P."Price") >= 5000 AND ((SUM(OD."Quantity" * P."Price")) / (COUNT(DISTINCT OD."Order_ID"))) >= 1000 AND COUNT(DISTINCT OD."Order_ID") >= 3
    )sub
JOIN "Customers" C On C."Customer_ID" = sub."Customer_ID"
ORDER BY sub."Total_order_amount" DESC;

---------------------------------------------------------------------------------------------------

-- Customer demographics and high-spending countries:
-- This query identifies countries with significant total spending (at least 10,000 in revenue)
-- and calculates the average customer age for each of these countries.
-- The results help understand the age distribution of customers in high-spending regions.
SELECT 
    C."Country",
    AVG(C."Age") AS "Average_age",
    sub."Total_amount"
FROM(
    SELECT
    C."Country",
    SUM(OD."Quantity" * P."Price") AS "Total_amount"
    FROM "OrderDetails" OD 
    JOIN "Products" P ON OD."Product_ID" = P."Product_ID"
    JOIN "Orders" O ON OD."Order_ID" = O."Order_ID"
    JOIN "Customers" C ON C."Customer_ID" = O."Customer_ID"
    GROUP BY C."Country"
    HAVING SUM(OD."Quantity" * P."Price") >= 10000
)sub
JOIN "Customers" C ON C."Country" = sub."Country"
GROUP BY C."Country",sub."Total_amount"
ORDER BY sub."Total_amount" DESC;