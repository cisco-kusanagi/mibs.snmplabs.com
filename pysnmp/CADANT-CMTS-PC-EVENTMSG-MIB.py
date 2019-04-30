#
# PySNMP MIB module CADANT-CMTS-PC-EVENTMSG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CADANT-CMTS-PC-EVENTMSG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:27:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
cadPCMibObjects, = mibBuilder.importSymbols("CADANT-CMTS-PACKETCABLE-MIB", "cadPCMibObjects")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, TimeTicks, ModuleIdentity, MibIdentifier, Counter64, IpAddress, Integer32, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ObjectIdentity, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "TimeTicks", "ModuleIdentity", "MibIdentifier", "Counter64", "IpAddress", "Integer32", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ObjectIdentity", "iso", "Bits")
TruthValue, DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "RowStatus", "TextualConvention")
cadEvMsgMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 5))
cadEvMsgMIB.setRevisions(('2007-10-24 00:00', '2005-05-23 00:00', '2003-02-05 00:00', '2002-12-27 00:00',))
if mibBuilder.loadTexts: cadEvMsgMIB.setLastUpdated('200710240000Z')
if mibBuilder.loadTexts: cadEvMsgMIB.setOrganization('Arris Interactive')
class TimeOfDay(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 5)

cadEvMsgMibBase = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 5, 1))
cadEvMsgElementType = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 5, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2)).clone(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadEvMsgElementType.setStatus('current')
cadEvMsgElementId = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 5, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000)).clone(100000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadEvMsgElementId.setStatus('current')
cadEvMsgMaxAge = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 5, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 30)).clone(1)).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadEvMsgMaxAge.setStatus('current')
cadEvMsgRetransTimer = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 5, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(10, 10000)).clone(1000)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadEvMsgRetransTimer.setStatus('current')
cadEvMsgMaxRetry = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 5, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 9))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadEvMsgMaxRetry.setStatus('current')
cadEvMsgMaxBatchSize = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 5, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(2, 10)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadEvMsgMaxBatchSize.setStatus('current')
cadEvMsgEnableFlag = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 5, 1, 7), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadEvMsgEnableFlag.setStatus('current')
cadEvMsgTransTimeTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 5, 2), )
if mibBuilder.loadTexts: cadEvMsgTransTimeTable.setStatus('current')
cadEvMsgTransTimeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 5, 2, 1), ).setIndexNames((0, "CADANT-CMTS-PC-EVENTMSG-MIB", "cadEvMsgTransTimeIdx"))
if mibBuilder.loadTexts: cadEvMsgTransTimeEntry.setStatus('current')
cadEvMsgTransTimeIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 5, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 24)))
if mibBuilder.loadTexts: cadEvMsgTransTimeIdx.setStatus('current')
cadEvMsgTransTOD = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 5, 2, 1, 2), TimeOfDay().clone('00:00')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadEvMsgTransTOD.setStatus('current')
cadEvMsgTransTimeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 5, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadEvMsgTransTimeStatus.setStatus('current')
mibBuilder.exportSymbols("CADANT-CMTS-PC-EVENTMSG-MIB", cadEvMsgMibBase=cadEvMsgMibBase, cadEvMsgMaxRetry=cadEvMsgMaxRetry, cadEvMsgElementId=cadEvMsgElementId, cadEvMsgRetransTimer=cadEvMsgRetransTimer, cadEvMsgTransTimeEntry=cadEvMsgTransTimeEntry, cadEvMsgElementType=cadEvMsgElementType, cadEvMsgTransTimeTable=cadEvMsgTransTimeTable, cadEvMsgMaxAge=cadEvMsgMaxAge, cadEvMsgEnableFlag=cadEvMsgEnableFlag, PYSNMP_MODULE_ID=cadEvMsgMIB, cadEvMsgMaxBatchSize=cadEvMsgMaxBatchSize, TimeOfDay=TimeOfDay, cadEvMsgTransTOD=cadEvMsgTransTOD, cadEvMsgMIB=cadEvMsgMIB, cadEvMsgTransTimeStatus=cadEvMsgTransTimeStatus, cadEvMsgTransTimeIdx=cadEvMsgTransTimeIdx)
