from gb_groupwork.phonebook.controllers import controller_cli


DB_PATH = '../../gb_groupwork/phonebook/DATA/'
DB_SQL_NAME = 'sqlite'
DB_CSV_NAME = 'CSV'

ExpoptDB_CSV_NAME = 'CSVto'
ExpoptDB_CSVtoSqlite_NAME = 'CSVtoSqlite'

ExpoptDB_SqlitetoTxt_NAME = 'SqlitetoTxt'
ExpoptDB_SqlitetoCSV_NAME = 'SqlitetoCSV'

DB_CSV_PATH_FULL = DB_PATH + DB_CSV_NAME + '.csv'
DB_SQL_PATH_FULL = DB_PATH + DB_SQL_NAME + '.sqlite'

ExportDB_CSV_PATH_FULL = DB_PATH + ExpoptDB_CSV_NAME + '.txt'
ExpoptDB_CSVtoSqlite_PATH_FULL = DB_PATH + ExpoptDB_CSVtoSqlite_NAME + '.sqlite'

ExportDB_SqlitetoTxt_PATH_FULL = DB_PATH + ExpoptDB_SqlitetoTxt_NAME + '.txt'
ExpoptDB_SqlitetoCSV_PATH_FULL = DB_PATH + ExpoptDB_SqlitetoCSV_NAME + '.csv'


def init():
    cli = controller_cli.CLI_PhoneBook()
    cli.init()

