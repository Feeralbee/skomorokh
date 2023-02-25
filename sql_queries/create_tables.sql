CREATE TYPE "status" AS ENUM (
  'approved',
  'not_approved',
  'under_consideration'
);

CREATE TABLE if not exists "users" (
  "id" int UNIQUE PRIMARY KEY NOT NULL,
  "nickname" text NOT NULL,
  "created_at" timestamp NOT NULL
);

CREATE TABLE if not exists "jokes" (
  "id" SERIAL UNIQUE PRIMARY KEY,
  "status" status NOT NULL DEFAULT 'under_consideration',
  "joke" text UNIQUE NOT NULL,
  "author_id" int NOT NULL,
  "created_at" timestamp NOT NULL
);
ALTER TABLE "jokes" ADD FOREIGN KEY (author_id) REFERENCES "users" ("id");
