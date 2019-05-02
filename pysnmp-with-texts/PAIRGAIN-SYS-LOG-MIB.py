#
# PySNMP MIB module PAIRGAIN-SYS-LOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PAIRGAIN-SYS-LOG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:36:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
pgainSysLog, = mibBuilder.importSymbols("PAIRGAIN-COMMON-HD-MIB", "pgainSysLog")
TimeSeconds, = mibBuilder.importSymbols("PAIRGAIN-DSLAM-CHASSIS-MIB", "TimeSeconds")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, ObjectIdentity, NotificationType, Bits, IpAddress, Unsigned32, iso, ModuleIdentity, MibIdentifier, TimeTicks, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "NotificationType", "Bits", "IpAddress", "Unsigned32", "iso", "ModuleIdentity", "MibIdentifier", "TimeTicks", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

class PgSysLogType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("unknown", 1), ("error", 2), ("alarm", 3), ("clralarm", 4), ("trap", 5), ("info", 6), ("bintrace", 7), ("txttrace", 8), ("debug", 9))

pgSystemLogTable = MibTable((1, 3, 6, 1, 4, 1, 927, 1, 10, 1), )
if mibBuilder.loadTexts: pgSystemLogTable.setStatus('mandatory')
if mibBuilder.loadTexts: pgSystemLogTable.setDescription('The system log table.')
pgSystemLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 927, 1, 10, 1, 1), ).setIndexNames((0, "PAIRGAIN-SYS-LOG-MIB", "pgSystemLogId"))
if mibBuilder.loadTexts: pgSystemLogEntry.setStatus('mandatory')
if mibBuilder.loadTexts: pgSystemLogEntry.setDescription('Entry in the system log table.')
pgSystemLogId = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 10, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSystemLogId.setStatus('mandatory')
if mibBuilder.loadTexts: pgSystemLogId.setDescription('The ID of the current log entry, with pgSystemLogId equals 1 represents the most current LOG, 2 represents the prior log entry, and etc. ')
pgSystemLogTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 10, 1, 1, 2), TimeSeconds()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSystemLogTimeStamp.setStatus('mandatory')
if mibBuilder.loadTexts: pgSystemLogTimeStamp.setDescription('The time stamp of the log entry . ')
pgSystemLogType = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 10, 1, 1, 3), PgSysLogType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSystemLogType.setStatus('mandatory')
if mibBuilder.loadTexts: pgSystemLogType.setDescription('The (PgSystemLogType) type of the log entry. ')
pgSystemLogSlotId = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 10, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSystemLogSlotId.setStatus('mandatory')
if mibBuilder.loadTexts: pgSystemLogSlotId.setDescription('The slot ID that the log message is orignated. ')
pgSystemLogDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 10, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSystemLogDescription.setStatus('mandatory')
if mibBuilder.loadTexts: pgSystemLogDescription.setDescription('The description of the log entry. ')
mibBuilder.exportSymbols("PAIRGAIN-SYS-LOG-MIB", pgSystemLogTable=pgSystemLogTable, pgSystemLogDescription=pgSystemLogDescription, PgSysLogType=PgSysLogType, pgSystemLogId=pgSystemLogId, pgSystemLogType=pgSystemLogType, pgSystemLogTimeStamp=pgSystemLogTimeStamp, pgSystemLogSlotId=pgSystemLogSlotId, DisplayString=DisplayString, pgSystemLogEntry=pgSystemLogEntry)
