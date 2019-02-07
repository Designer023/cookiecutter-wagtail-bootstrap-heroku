#!/usr/bin/env bash
yarn run prod


if [ -n "$SKIP_RELEASE" ]; then
    echo "Skipping database migrate phase!";
else
    echo "Migrating existing database";
    python manage.py migrate --no-input
fi

python manage.py collectstatic --no-input -i admin

