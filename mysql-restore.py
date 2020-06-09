#!/usr/bin/env python

import os
import logging
import mysql.connector
from mysql.connector import Error
from multiprocessing import Pool
from datetime import datetime
from customLogger import Log


dbUser="root"
dbPass="R0º7"
dbHost="localhost"
dbName="mydb"

params=" -u'{}' -h'{}' -p'{}' {} -A --force --show-warnings --max-allowed-packet=1G --net-buffer-length=1M --quick ".format(dbUser, dbPass, dbHost, dbName)


def restoreTable(fileName):
    if not fileName:
        return False

    logName="/mysql/restore/logs/"+fileName.replace("sql","log")
    logErr="/mysql/restore/logs/"+fileName.replace("sql","err")
    filePath="/mysql/backup/mysqldump/tables/"

    appLog.info("Iniciado o restore do arquivo " + fileName)

    bashCmd="mysql {} < {}{} 1>> {} 2>> {}".format(params, filePath, fileName, logName, logErr)
    os.system(bashCmd)
    # print(bashCmd)
    appLog.info("Restore do arquivo " + fileName + " finalizado")


if __name__ == '__main__':

    print('Script iniciado')

    logDir="/mysql/restore/logs"
    appLog = Log(filename="teste")
    appLog.info("## SCRIPT DE RESTORE INICIADO ##")

    listOfFiles = os.listdir("/mysql/backup/mysqldump/table/")

    # Define quantas threads serao abertas restaurando backup
    poolSize=3
    p = Pool(poolSize)
    p.map(restoreTable, listOfFiles)

    appLog.info("## SCRIPT DE RESTORE FINALIZADO ##")

    print('Script finalizado')
