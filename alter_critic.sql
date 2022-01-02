BEGIN;

CREATE TABLE "db_usertype" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL);

CREATE TABLE "new__db_criticism" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(100) NOT NULL, "text" varchar(5000) NOT NULL, "score" integer NOT NULL, "image" varch
ar(100) NOT NULL, "created_at" datetime NOT NULL, "game_id" integer NOT NULL REFERENCES "db_game" ("id") DEFERRABLE INITIALLY DEFERRED, "critic_id" integer NOT NULL REFERENCES "db_user
" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "new__db_criticism" ("id", "title", "text", "score", "image", "created_at", "game_id", "critic_id") SELECT "id", "title", "text", "score", "image", "created_at", "game_id",
 "critic_id" FROM "db_criticism";
DROP TABLE "db_criticism";
ALTER TABLE "new__db_criticism" RENAME TO "db_criticism";

DROP TABLE "db_critic";

COMMIT;
