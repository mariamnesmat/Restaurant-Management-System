CREATE DATABASE Restaurant1;
USE Restaurant1;
CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY,
    customer_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone_number VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    premium_status BOOLEAN DEFAULT FALSE,
    discounts DECIMAL(5,2) DEFAULT 0.00
);
select * from customer;
CREATE TABLE DeliveryArea (
    AreaCode INT PRIMARY KEY,
    area_name VARCHAR(255) NOT NULL
);
CREATE TABLE Restaurant (
    RestaurantID INT PRIMARY KEY,
    restaurant_name VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL,
    addressLine1 VARCHAR(100) NOT NULL,
    restaurant_category VARCHAR(255) NOT NULL,
    phone VARCHAR(50) NOT NULL,
    ContactInfo VARCHAR(255)
);

CREATE TABLE MenuItem (
    MenuItemID INT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    RestaurantID int, 
    Description VARCHAR(255),
    Price DECIMAL(10, 2) NOT NULL,
    Picture BLOB,
    Category VARCHAR(255),
    FOREIGN KEY (RestaurantID) REFERENCES Restaurant(RestaurantID)
);

CREATE TABLE DeliveryBoy (
    BoyID INT PRIMARY KEY,
    BoyName VARCHAR(255),
    BoyEmail VARCHAR(255) NOT NULL,
    BoyPhone VARCHAR(255) NOT NULL,
    DeliveryArea INT,
    BoyAvailable BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (DeliveryArea) REFERENCES DeliveryArea(AreaCode)
);
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,
    CustomerID INT,
    RestaurantID INT,
    DeliveryBoyID INT,
    delivery_area INT,
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Orderstatus ENUM('Placed', 'Confirmed', 'In Transit', 'Delivered', 'Canceled') DEFAULT 'Placed',
    total_amount DECIMAL(10, 2),
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
    FOREIGN KEY (RestaurantID) REFERENCES Restaurant(RestaurantID),
    FOREIGN KEY (DeliveryBoyID) REFERENCES DeliveryBoy(BoyID),
    FOREIGN KEY (delivery_area) REFERENCES DeliveryArea(AreaCode)
);

CREATE TABLE Payment (
    PaymentID INT PRIMARY KEY,
    OrderID INT,
    Amount DECIMAL(10, 2),
    PaymentDate TIMESTAMP,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);

CREATE TABLE Request (
    RequestID INT PRIMARY KEY,
    RequestName DATETIME,
    RequestDetails VARCHAR(255),
    RequestStatus BOOLEAN DEFAULT FALSE,
    CustomerID INT,
    DeliveryBoyID INT,
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
    FOREIGN KEY (DeliveryBoyID) REFERENCES DeliveryBoy(BoyID)
);

CREATE TABLE Report (
    ReportID INT PRIMARY KEY,
    ReportDate DATETIME,	
    DeliveryAreaCode INT,
    FOREIGN KEY (DeliveryAreaCode) REFERENCES DeliveryArea(AreaCode)
);

CREATE TABLE GeoLocation (
    LocationID INT PRIMARY KEY,
    LocationName VARCHAR(255),
    Latitude DECIMAL(10, 6),
    Longitude DECIMAL(10, 6)
);

CREATE TABLE CustomerRefund (
    RefundID INT PRIMARY KEY AUTO_INCREMENT,
    OrderID INT,
    RefundAmount DECIMAL(10, 2),
    RefundDate TIMESTAMP,
    Reason VARCHAR(255),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);

INSERT INTO Customer (CustomerID, customer_name, email, phone_number, address,premium_status,discounts)
VALUES 
  (100, 'Yasmeen', 'Y.Mostafa@gmail.com', '01034526700', '6th of October', true,0.1),
  (101, 'Jana', 'jana.smith@gmail.com', '01034528867', 'Faisal', false,0),
  (102, 'Maha', 'Maha@gmail.com', '01034526767', 'Nasr city', true,0.15),
  (103, 'Salma', 'michael.brown@gmail.com', '01035526767','Haram',false, 0),
  (104, 'Sophia', 'sophia.MO@gmail.com', '01554526767', 'Sharqya',true, 0.1),
  (105, 'Andrew', 'Andrew.anderson@gmail.com', '01134526767', 'Aswan',false, 0);
  
INSERT INTO Restaurant (RestaurantID, restaurant_name, city, addressLine1, restaurant_category, phone, ContactInfo)
VALUES 
  (5, 'Restaurant 5', 'Cairo', 'Cairo 5', 'Category 5', '0119633792', '9288972032'),
  (6, 'Restaurant 6', 'new cairo', 'new cairo 6', 'Category 6', '0119363442', '9288972099'),
  (7, 'Restaurant 7', 'giza', 'giza 6', 'Category 7', '0119637621', '9288972055'),
  (8, 'Restaurant 8', 'aswann', 'aswann 6', 'Category 8', '011963111', '92889720877'),
  (9, 'Restaurant 9', 'Sharqya', 'Sharqya 9', 'Category 9', '0119630000', '9288973232');
  
INSERT INTO MenuItem (MenuItemID, Name, RestaurantID ,Description, Price,Picture,Category)
VALUES (1, 'SHITAKE MUSHROOOM', 5 ,'Delicious Mushroom beef burger.',120,'https://buffaloburger.com/_next/image?url=https%3A%2F%2Fbuffalonlineorderingprod.s3-accelerate.amazonaws.com%2Fmenu_items%2Fa76de047b66f2511962b600232c60769.png&w=640&q=75','Burgers'),
       (2, 'BACON MUSHROOM JACK', 6,'Delicious Mushroom and Bacon burger.',150 ,'https://buffaloburger.com/_next/image?url=https%3A%2F%2Fbuffalonlineorderingprod.s3-accelerate.amazonaws.com%2Fmenu_items%2Fd845c9309b0d95d8c5d945b6b2552491.png&w=640&q=75' ,'Burgers'),
       (3, 'OLD SCHOOL', 7 ,'Pure beef burger  topped with our Buffalo sauce and cheddar cheese.' ,115,'https://buffaloburger.com/_next/image?url=https%3A%2F%2Fbuffalonlineorderingprod.s3-accelerate.amazonaws.com%2Fmenu_items%2Fb4a9bce0163404b97f76e9cec638bb08.png&w=640&q=75' , 'Burgers' ),
       (4, 'TRIPLE', 8 ,'Three 100% British and Irish beef patties, onions, pickles, ketchup, mustard and cheese in a soft, toasted bun.',215, 'https://buffaloburger.com/_next/image?url=https%3A%2F%2Fbuffalonlineorderingprod.s3-accelerate.amazonaws.com%2Fmenu_items%2F05706e0e9313fa2972b1fe878f17b990.png&w=640&q=75','Burgers'),
       (5, 'BLUE CHEESE', 9, 'Crumbles of creamy French blue cheese top our famous burger patty with our signature mayonnaise sauce.',120,'https://buffaloburger.com/_next/image?url=https%3A%2F%2Fbuffalonlineorderingprod.s3-accelerate.amazonaws.com%2Fmenu_items%2Fb75ecb94aa633b1545de1318f9ca6d00.png&w=640&q=75', 'Burgers'),
       (6, 'DOUBLE DOUBLE ', 5 ,'2 Juicy beef patties with 2 layers of cheddar cheese and our creamy Buffalo sauce', 190 ,'https://buffaloburger.com/_next/image?url=https%3A%2F%2Fbuffalonlineorderingprod.s3-accelerate.amazonaws.com%2Fmenu_items%2Fff183e68e89cbe5674dfb3c8e7b1a26b.png&w=640&q=75','Burgers'),
       (7, 'THE RASTAFARI',6 ,'Crispy jalapeño bites, on a grilled burger patty with creamy Buffalo sauce.', 140,'https://buffaloburger.com/_next/image?url=https%3A%2F%2Fbuffalonlineorderingprod.s3-accelerate.amazonaws.com%2Fmenu_items%2F802131a7b4dd1d3a1ca23625a53082c3.png&w=640&q=75','Burgers'),
       (8, '16Pc Signature Chicken',7, '16 signature chicken pieces with patty and sauce', 340, 'https://cdn.sanity.io/images/czqk28jt/prod_plk_us/d6a82f9cc83d7dba106bb7691973dbf719e3bed4-2000x1333.png?w=750&q=40&fit=max&auto=format', 'Chicken'),
       (9,'2Pc Chicken Meal',8,'2 chicken pieces with patty and sauce ' ,50,'https://cdn.sanity.io/images/czqk28jt/prod_plk_us/47642b88e69bb5bbd75e285647c6df67aebe708c-2000x1333.png?w=750&q=40&fit=max&auto=format','Chicken'),
       (10,'3Pc Chicken Meal',9, '3 chicken pieces with patty and sauce' ,75,'https://cdn.sanity.io/images/czqk28jt/prod_plk_us/dbf3ed316da22492677b6bd2285db51b288dc466-2000x1333.png?w=750&q=40&fit=max&auto=format','Chicken'),
       (11,'4Pc Chicken Meal',5,'4 chicken pieces with patty and sauce' ,100,'https://cdn.sanity.io/images/czqk28jt/prod_plk_us/a412de33077dd22818675dbd6e095038f35e9e8c-2000x1333.png?w=750&q=40&fit=max&auto=format','Chicken'),
       (12,'8Pc Chicken Meal',6, '8 chicken pieces with patty and sauce' ,160,'https://cdn.sanity.io/images/czqk28jt/prod_plk_us/86e795d2820f6ec8d19894a79f293b145932e66f-2000x1333.png?w=750&q=40&fit=max&auto=format','Chicken'),
       (13,'12Pc Chicken Meal',7,'12 chicken pieces with patty and sauce' ,220,'https://cdn.sanity.io/images/czqk28jt/prod_plk_us/141e32d3e97fe639765882f1801f9bd87549f18d-2000x1333.png?w=750&q=40&fit=max&auto=format','Chicken'),
       (14,'16Pc Chicken Meal',8, '16 chicken pieces with patty and sauce' ,300,'https://cdn.sanity.io/images/czqk28jt/prod_plk_us/7488145e368122d31621d45c6759719155f66533-2000x1333.png?w=750&q=40&fit=max&auto=format','Chicken'),
       (15,'16Pc Signature Chicken',9,'16 signature chicken pieces with patty and sauce' ,340,'https://cdn.sanity.io/images/czqk28jt/prod_plk_us/d6a82f9cc83d7dba106bb7691973dbf719e3bed4-2000x1333.png?w=750&q=40&fit=max&auto=format','Chicken'),
       (16,'Cheese Lovers',5,'Mixed cheese pizza' ,185,'https://images.phi.content-cdn.io/cdn-cgi/image/height=170,width=180,quality=50/https://martjackamstorage.azureedge.net/am-resources/c3877a59-69f7-40fa-bb17-ae5b9ac37732/Images/ProductImages/Large/Cheese-Lovers-p1.png','Pizza'),
       (17,'Vegetarian',6,'Pizza topped with veggies' ,135,'https://images.phi.content-cdn.io/cdn-cgi/image/height=170,width=180,quality=50/https://martjackamstorage.azureedge.net/am-resources/c3877a59-69f7-40fa-bb17-ae5b9ac37732/Images/ProductImages/Large/CLASSIC-VEGETARIAN.png','Pizza'),
       (18,'Chicken BBQ',7,'Pizza topped with chicken and barbecue sauce' ,135,'https://images.phi.content-cdn.io/cdn-cgi/image/height=170,width=180,quality=50/https://martjackamstorage.azureedge.net/am-resources/c3877a59-69f7-40fa-bb17-ae5b9ac37732/Images/ProductImages/Large/CLASSIC--BBQ-CHICKEN.png','Pizza'),
       (19,'Pepperoni Supreme',8,'Pizza topped with pepperoni' ,150,'https://images.phi.content-cdn.io/cdn-cgi/image/height=170,width=180,quality=50/https://martjackamstorage.azureedge.net/am-resources/c3877a59-69f7-40fa-bb17-ae5b9ac37732/Images/ProductImages/Large/PEPPERONI%20Supreme.png','Pizza'),
       (20,'Meat Lover',9,'Pizza topped with meat' ,135,'https://images.phi.content-cdn.io/cdn-cgi/image/height=170,width=180,quality=50/https://martjackamstorage.azureedge.net/am-resources/c3877a59-69f7-40fa-bb17-ae5b9ac37732/Images/ProductImages/Large/MEAT-LOVERS.png','Pizza'),
       (21,'Spicy CHICKEN RANCH',5,'Pizza topped with spicy chicken and ranch sauce' ,185,'https://images.phi.content-cdn.io/cdn-cgi/image/height=170,width=180,quality=50/https://martjackamstorage.azureedge.net/am-resources/c3877a59-69f7-40fa-bb17-ae5b9ac37732/Images/ProductImages/Large/Spicy%20Chicken%20Ranch175x175.png','Pizza'),
       (22,'Margherita',6,'Pizza topped with margherita' ,125,'https://images.phi.content-cdn.io/cdn-cgi/image/height=170,width=180,quality=50/https://martjackamstorage.azureedge.net/am-resources/c3877a59-69f7-40fa-bb17-ae5b9ac37732/Images/ProductImages/Large/Margherita-p1.png','Pizza'),
       (23,'Super Supreme',7,'Pizza topped with Sausage, Pepperoni,Onions, Black Olives, Mushrooms, Mixed Peppers' ,160,'https://images.phi.content-cdn.io/cdn-cgi/image/height=170,width=180,quality=50/https://martjackamstorage.azureedge.net/am-resources/c3877a59-69f7-40fa-bb17-ae5b9ac37732/Images/ProductImages/Large/Super-Supreme-p1.png','Pizza');

INSERT INTO DeliveryArea (AreaCode, area_name)
VALUES 
  (11, 'Downtown Area'),
  (22, 'October Area'),
  (33, 'Haram Area'),
  (44, 'Fesail Area'),
  (55, 'Naser District'),
  (66, 'Zayed Area');

  
INSERT INTO DeliveryBoy (BoyID, BoyName, BoyEmail, BoyPhone, DeliveryArea, BoyAvailable)
VALUES 
(1, 'Yousef', 'yousef@gmail.com', '01134526760', 11, true),
(2, 'Ahmed', 'ahmed@gmail.com', '011345267640', 33, false),
(3, 'Aly', 'aly@gmail.com', '01134526710', 44, true),
(4, 'Maged', 'maged@gmail.com', '01094526767', 55,false),
(5, 'Monzer', 'monzer@gmail.com', '01134500767', 66,true);


INSERT INTO Orders (OrderID, CustomerID, RestaurantID, DeliveryBoyID, delivery_area, OrderDate, Orderstatus, total_amount)
VALUES 
  (60, 100, 9, 1, 11, '2023-05-02', 'Placed', 250),
  (61, 101, 8, 2, 22, '2023-05-03', 'Confirmed',730),
  (62, 102, 7, 3, 33, '2023-05-03', 'Delivered',1500),
  (63, 103, 6, 4, 44, '2023-05-05', 'Placed',85),
  (64, 104, 5, 5, 55, '2023-05-07', 'In Transit',126);

INSERT INTO Payment (PaymentID, OrderID, Amount, PaymentDate)
values 
(200, 60, 500, '2023-05-02'),
(201, 61, 1000, '2023-05-03'),
(202, 62, 700, '2023-05-03'),
(203, 63, 750, '2023-05-05'),
(204, 64, 400, '2023-05-07'),
(205, 62, 500, '2023-02-05');


INSERT INTO Orders (OrderID, CustomerID, RestaurantID, DeliveryBoyID, delivery_area, OrderDate, Orderstatus, total_amount)
VALUES (66, 100, 9, 1, 11, '2023-05-02', 'Placed', 250);



ALTER TABLE Request MODIFY RequestName VARCHAR(255);
INSERT INTO Request (RequestID, RequestName, RequestDetails, RequestStatus)
VALUES (1, 'Delivery Boy Allocation', 'Order Number 63', FALSE);

UPDATE DeliveryBoy
SET BoyAvailable = FALSE
WHERE BoyID = 1;

SELECT * FROM Orders;

SELECT customer_name, email, phone_number, address FROM Customer;

SELECT * FROM Customer WHERE discounts = 0;
select * from Customer;
SELECT * FROM DeliveryBoy;

SELECT Name, Description, Price FROM MenuItem;

SELECT DISTINCT Address FROM Customer;

SELECT * FROM Customer WHERE discounts = 0.1;
SET SQL_SAFE_UPDATES = 0;
UPDATE MenuItem
SET Price = 200
WHERE Name = 'pizza';

UPDATE MenuItem SET Price = 170
WHERE MenuItemID = 11;

SELECT DeliveryBoy.BoyName, DeliveryArea.area_name
FROM DeliveryBoy
INNER JOIN DeliveryArea ON DeliveryBoy.DeliveryArea = DeliveryArea.AreaCode;

INSERT INTO Restaurant (RestaurantID, restaurant_name, city, addressLine1, restaurant_category, phone, ContactInfo)
VALUES (2, 'Oat Restaurant', 'zayed', 'nile university street', 'Healthy Food', '9999999', 'esraa@nu.edu.eg');

INSERT INTO Payment (PaymentID, OrderID, Amount, PaymentDate)
VALUES (206, 60, 50, '2024-01-02');

-- Report: Available delivery boys per area
SELECT DeliveryArea.area_name, COUNT(DeliveryBoy.BoyID) AS AvailableDeliveryBoys
FROM DeliveryArea
LEFT JOIN DeliveryBoy ON DeliveryArea.AreaCode = DeliveryBoy.DeliveryArea AND DeliveryBoy.BoyAvailable = TRUE
GROUP BY DeliveryArea.area_name;

select * from deliveryboy;

DELETE FROM Customer
WHERE CustomerID = 105;


SELECT * FROM Payment WHERE OrderID IN (SELECT OrderID FROM Orders WHERE DeliveryBoyID = 1);
DELETE FROM Payment WHERE OrderID IN (SELECT OrderID FROM Orders WHERE DeliveryBoyID = 1);
DELETE FROM DeliveryBoy WHERE BoyID = 1;

SELECT * FROM MenuItem WHERE RestaurantID = 6;
DELETE FROM MenuItem WHERE RestaurantID = 6;
SELECT * FROM Orders WHERE RestaurantID = 6;
DELETE Payment FROM Payment
JOIN Orders ON Payment.OrderID = Orders.OrderID
WHERE Orders.RestaurantID = 6;
DELETE FROM Orders WHERE RestaurantID = 6;
DELETE FROM Restaurant WHERE RestaurantID = 6;

DELETE FROM DeliveryArea WHERE AreaCode = 66;
