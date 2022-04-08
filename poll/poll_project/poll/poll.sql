CREATE TABLE "Poll" (
  "id" serial NOT NULL PRIMARY KEY,
  "question" varchar(250) NOT NULL,
  "option_one" varchar(30) NOT NULL,
  "option_two" varchar(30) NOT NULL,
  "option_three" varchar(30) NOT NULL,
  "option_one_count" integer DEFAULT 0,
  "option_two_count" integer DEFAULT 0,
  "option_three_count" integer DEFAULT 0
);