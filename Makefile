include .env

up:
	docker compose up -d --build

down:
	docker compose down

start: up
	sleep 3
	docker compose exec db mysql -uroot -p$(DB_PASS) -e "CREATE DATABASE IF NOT EXISTS logs;"
	docker compose exec api alembic upgrade head
	docker compose exec -T db mysql -uroot -p$(DB_PASS) < dump.sql

migrate:
	docker compose exec api alembic upgrade head

migration:
	docker compose exec api alembic revision --autogenerate -m "$(name)"

seed:
	docker compose exec -T db mysql -uroot -p$(DB_PASS) < dump.sql
