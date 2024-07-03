echo "Waiting for postgres..."

while ! nc -z web-db 5423; do
    sleep 0.1
done

echo "PostgreSQL started"

exec "$@"