-- Enable the dblink extension if it's not already enabled
DO
$$
BEGIN
   IF NOT EXISTS (SELECT 1 FROM pg_extension WHERE extname = 'dblink') THEN
       CREATE EXTENSION dblink;
   END IF;
END
$$;

-- Create the shopping database only if it does not already exist
DO
$$
BEGIN
   IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'shopping') THEN
       PERFORM dblink_exec('dbname=postgres', 'CREATE DATABASE shopping');
   END IF;
END
$$;

-- Create the shopping_test database only if it does not already exist
DO
$$
BEGIN
   IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'shopping_test') THEN
       PERFORM dblink_exec('dbname=postgres', 'CREATE DATABASE shopping_test');
   END IF;
END
$$;