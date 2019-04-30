#
# PySNMP MIB module AT-FLASH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AT-FLASH-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:13:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
DisplayStringUnsized, modules = mibBuilder.importSymbols("AT-SMI-MIB", "DisplayStringUnsized", "modules")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, IpAddress, MibIdentifier, Bits, Integer32, ObjectIdentity, Unsigned32, Counter32, Gauge32, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "IpAddress", "MibIdentifier", "Bits", "Integer32", "ObjectIdentity", "Unsigned32", "Counter32", "Gauge32", "TimeTicks", "Counter64")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
flash = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31))
flash.setRevisions(('2006-06-28 12:22',))
if mibBuilder.loadTexts: flash.setLastUpdated('200606281222Z')
if mibBuilder.loadTexts: flash.setOrganization('Allied Telesis, Inc')
flashGetFailure = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashGetFailure.setStatus('current')
flashOpenFailure = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashOpenFailure.setStatus('current')
flashReadFailure = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashReadFailure.setStatus('current')
flashCloseFailure = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashCloseFailure.setStatus('current')
flashCompleteFailure = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashCompleteFailure.setStatus('current')
flashWriteFailure = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashWriteFailure.setStatus('current')
flashCreateFailure = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashCreateFailure.setStatus('current')
flashPutFailure = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashPutFailure.setStatus('current')
flashDeleteFailure = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashDeleteFailure.setStatus('current')
flashCheckFailure = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashCheckFailure.setStatus('current')
flashEraseFailure = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashEraseFailure.setStatus('current')
flashCompactFailure = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashCompactFailure.setStatus('current')
flashVerifyFailure = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashVerifyFailure.setStatus('current')
flashTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 0))
flashFailureTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 31, 0, 1)).setObjects(("AT-FLASH-MIB", "flashGetFailure"), ("AT-FLASH-MIB", "flashOpenFailure"), ("AT-FLASH-MIB", "flashReadFailure"), ("AT-FLASH-MIB", "flashCloseFailure"), ("AT-FLASH-MIB", "flashCompleteFailure"), ("AT-FLASH-MIB", "flashWriteFailure"), ("AT-FLASH-MIB", "flashCreateFailure"), ("AT-FLASH-MIB", "flashPutFailure"), ("AT-FLASH-MIB", "flashDeleteFailure"), ("AT-FLASH-MIB", "flashCheckFailure"), ("AT-FLASH-MIB", "flashEraseFailure"), ("AT-FLASH-MIB", "flashCompactFailure"), ("AT-FLASH-MIB", "flashVerifyFailure"))
if mibBuilder.loadTexts: flashFailureTrap.setStatus('current')
mibBuilder.exportSymbols("AT-FLASH-MIB", flashCompactFailure=flashCompactFailure, flashCompleteFailure=flashCompleteFailure, flashCloseFailure=flashCloseFailure, flash=flash, flashWriteFailure=flashWriteFailure, flashCreateFailure=flashCreateFailure, flashReadFailure=flashReadFailure, flashOpenFailure=flashOpenFailure, flashGetFailure=flashGetFailure, flashDeleteFailure=flashDeleteFailure, flashPutFailure=flashPutFailure, flashCheckFailure=flashCheckFailure, flashVerifyFailure=flashVerifyFailure, flashFailureTrap=flashFailureTrap, flashEraseFailure=flashEraseFailure, PYSNMP_MODULE_ID=flash, flashTrap=flashTrap)