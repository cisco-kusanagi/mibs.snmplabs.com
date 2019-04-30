#
# PySNMP MIB module PAIRGAIN-SYS-LOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PAIRGAIN-SYS-LOG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:27:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
pgainSysLog, = mibBuilder.importSymbols("PAIRGAIN-COMMON-HD-MIB", "pgainSysLog")
TimeSeconds, = mibBuilder.importSymbols("PAIRGAIN-DSLAM-CHASSIS-MIB", "TimeSeconds")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Unsigned32, NotificationType, ObjectIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, MibIdentifier, iso, ModuleIdentity, Gauge32, Counter64, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Unsigned32", "NotificationType", "ObjectIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "MibIdentifier", "iso", "ModuleIdentity", "Gauge32", "Counter64", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

class PgSysLogType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("unknown", 1), ("error", 2), ("alarm", 3), ("clralarm", 4), ("trap", 5), ("info", 6), ("bintrace", 7), ("txttrace", 8), ("debug", 9))

pgSystemLogTable = MibTable((1, 3, 6, 1, 4, 1, 927, 1, 10, 1), )
if mibBuilder.loadTexts: pgSystemLogTable.setStatus('mandatory')
pgSystemLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 927, 1, 10, 1, 1), ).setIndexNames((0, "PAIRGAIN-SYS-LOG-MIB", "pgSystemLogId"))
if mibBuilder.loadTexts: pgSystemLogEntry.setStatus('mandatory')
pgSystemLogId = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 10, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSystemLogId.setStatus('mandatory')
pgSystemLogTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 10, 1, 1, 2), TimeSeconds()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSystemLogTimeStamp.setStatus('mandatory')
pgSystemLogType = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 10, 1, 1, 3), PgSysLogType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSystemLogType.setStatus('mandatory')
pgSystemLogSlotId = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 10, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSystemLogSlotId.setStatus('mandatory')
pgSystemLogDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 10, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSystemLogDescription.setStatus('mandatory')
mibBuilder.exportSymbols("PAIRGAIN-SYS-LOG-MIB", pgSystemLogTimeStamp=pgSystemLogTimeStamp, pgSystemLogType=pgSystemLogType, pgSystemLogTable=pgSystemLogTable, PgSysLogType=PgSysLogType, pgSystemLogSlotId=pgSystemLogSlotId, pgSystemLogId=pgSystemLogId, DisplayString=DisplayString, pgSystemLogEntry=pgSystemLogEntry, pgSystemLogDescription=pgSystemLogDescription)
