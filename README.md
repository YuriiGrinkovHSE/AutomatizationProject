# Quick start

### Запустить приложение и БД
```
docker compose up -d
```

### Отключить приложение
```
docker compose down

```

### Очистить кэш
```
docker compose down -v
docker rmi postgres:14.8-alpine3.18 automatization_project-python-app --force

```