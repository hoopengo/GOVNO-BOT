restart:
	docker compose up -d --build && docker logs govno-bot-bot-1 --follow
stop:
	docker compose down -v
alembic-revision: # make alembic-revision COMMENT="your comment"
	docker exec -it govno-bot-bot-1 bash -c "alembic revision --autogenerate -m ${COMMENT}"
relogs:
	docker logs govno-bot-bot-1 --follow
psql:
	docker exec -it --user postgres govno-bot-db-1 psql
