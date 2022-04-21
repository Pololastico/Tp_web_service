CREATE TABLE IF NOT EXISTS app_user (
    id serial primary key, 
    firstname varchar(100) not null,
    lastname varchar(100) not null,
    age int not null,
    email varchar(100),
    job varchar(100)
);

CREATE TABLE IF NOT EXISTS applications (
   id serial PRIMARY KEY,
   appname VARCHAR(100) NOT NULL,
   username VARCHAR(100) UNIQUE NOT NULL,
   lastconnection DATE,
   userid serial NOT NULL,
    CONSTRAINT fk_user
      FOREIGN KEY(userid)
	  REFERENCES app_user(id)
);

































