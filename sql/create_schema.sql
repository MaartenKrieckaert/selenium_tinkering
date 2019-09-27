DROP SCHEMA IF EXISTS {schema}_{version} CASCADE;
CREATE SCHEMA {schema}_{version} AUTHORIZATION {dbadmin};
GRANT USAGE ON SCHEMA {schema}_{version} TO {dbuser};
GRANT SELECT ON ALL TABLES IN SCHEMA {schema}_{version} TO {dbuser};