# clickhousePOC
created some unnecesary files for understanding sake.
# will be upadating info regarding files in some time\

STEPS TO BE FOLLOWED:

1. Install dockers
2. Installing clickhouse using dockers
3. config.xml,users.xml,client.xml,docker-compose.yml files imp
4. login to tabix (clickhouse GUI)
5. create table from 1. tabix 
                     2. terminal ($ docker-compose run --rm client --host ch) connect to server using this command
6. use (venv/IMP_SQL_cmds.sql) for useful SQL commands
7. use (benc_merge_trees_insert.sh) for setting table name and database name and batch size
8. use (inserter_config.py) for setting configurations
9. use (test.py) to insert rows in clickhouse db


Docker install -- (https://hub.docker.com/editions/community/docker-ce-desktop-mac)
after successfully installing docker-- open pycharam(preferable) and run the following commands in terminal
Download - [ch_configs(folder),client-config.xml,docker-compose.yaml into some folder]
IN (ch_configs/users.xml) line 90 change configurations create some other login credentials(can be used to login to tabix(gui clickhouse): dont use spl char for password. use number combinations.
ALSO do the same in (client-config.xml)
run the folowing commands after in the newly created directory/folder as mentioned above.
1. $ docker run -d --name some-clickhouse-server --ulimit nofile=262144:262144 yandex/clickhouse-server
2. $ docker run -it --rm --link some-clickhouse-server:clickhouse-server yandex/clickhouse-client --host clickhouse-server
you will now connect to database server..
you can try some basic sql commands : SELECT 1, SELECT 8-2, SELECT 9/2, SHOW DATABASES, SHOW TABLES FROM SYSTEM, SHOW TABLES FROM DEFAULT.
type 'q' to exit from server and get back to terminal.
To check number of dockers running use (docker ps)
Now to stop docker use command ($ docker stop $(docker ps -aq))
Now again to start docker (starts server service) use ($ docker-compose up -d ch)
now use this to connect from client ($ docker-compose run --rm client --host ch)
url for tabix -- http://ui.tabix.io/#!/login
Go to add new - give a name and in http://host:port --{pls do fill http://127.0.0.1:8123 type the same thing there again, its shows by defaukt as filled but it doesnt, we need to type} and username and password , login with edited credentials as in client-config.xml
---------------------------------------------------------------------------------------------------------------------------

Now create table using sql commands mentioned in (venv/IMP_SQL_cmds.sql) 
------follow steps from 6...

its taking lot of time to insert 1 milion rows:

Thanks. 






