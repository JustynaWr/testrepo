import cx_Oracle

try:
    con = cx_Oracle.connect('system/Quokka2019@XE')
    print(con.version)

    cur = con.cursor()
    cur.execute('select * from employee')
    for line in cur:
        print(line)

except:
    print('Unable to connect to database')

statement = """
    CREATE TABLE python_modules (
    module_name VARCHAR2(50) NOT NULL,
    file_path VARCHAR2(300) NOT NULL )
    """
#calling stored procedure
cur.callproc('delobject', ["python_modules", "TABLE"])
cur.execute(statement)

#insert statement
statement = 'insert into python_modules(module_name, file_path) values (:1, :2)'
cur.execute(statement, ('module_name', 'I like horses'))
con.commit()

cur.close()
con.close()
