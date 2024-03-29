CREATE TYPE "status" AS ENUM (
  'approved',
  'disapproved',
  'under_consideration'
);

CREATE TABLE if not exists "users" (
  "user_telegram_id" bigint UNIQUE PRIMARY KEY NOT NULL,
  "telegram_nickname" text NOT NULL,
  "is_admin" boolean DEFAULT FALSE,
  "registration_date" timestamp NOT NULL
);

CREATE TABLE if not exists "jokes" (
  "joke_id" SERIAL UNIQUE PRIMARY KEY,
  "publication_status" status DEFAULT 'under_consideration',
  "joke_text" text NOT NULL,
  "author_telegram_id" bigint NOT NULL,
  "creation_date" timestamp NOT NULL
);
ALTER TABLE "jokes" ADD FOREIGN KEY ("author_telegram_id") REFERENCES "users" ("user_telegram_id");
