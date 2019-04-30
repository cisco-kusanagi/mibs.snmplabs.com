#
# PySNMP MIB module FASTPATH-QOS-AUTOVOIP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FASTPATH-QOS-AUTOVOIP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:58:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
fastPathQOS, = mibBuilder.importSymbols("FASTPATH-QOS-MIB", "fastPathQOS")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, IpAddress, ObjectIdentity, MibIdentifier, Unsigned32, NotificationType, Integer32, Gauge32, iso, Counter64, TimeTicks, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "IpAddress", "ObjectIdentity", "MibIdentifier", "Unsigned32", "NotificationType", "Integer32", "Gauge32", "iso", "Counter64", "TimeTicks", "ModuleIdentity")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
fastPathQOSAUTOVOIP = ModuleIdentity((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 4))
fastPathQOSAUTOVOIP.setRevisions(('2007-11-23 00:00', '2007-11-23 00:00',))
if mibBuilder.loadTexts: fastPathQOSAUTOVOIP.setLastUpdated('200711230000Z')
if mibBuilder.loadTexts: fastPathQOSAUTOVOIP.setOrganization('Broadcom Corporation')
class PercentByFives(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(5, 5), ValueRangeConstraint(10, 10), ValueRangeConstraint(15, 15), ValueRangeConstraint(20, 20), ValueRangeConstraint(25, 25), ValueRangeConstraint(30, 30), ValueRangeConstraint(35, 35), ValueRangeConstraint(40, 40), ValueRangeConstraint(45, 45), ValueRangeConstraint(50, 50), ValueRangeConstraint(55, 55), ValueRangeConstraint(60, 60), ValueRangeConstraint(65, 65), ValueRangeConstraint(70, 70), ValueRangeConstraint(75, 75), ValueRangeConstraint(80, 80), ValueRangeConstraint(85, 85), ValueRangeConstraint(90, 90), ValueRangeConstraint(95, 95), ValueRangeConstraint(100, 100), )
class Sixteenths(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 16)

agentAutoVoIPCfgGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 4, 1))
agentAutoVoIPTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 4, 1, 1), )
if mibBuilder.loadTexts: agentAutoVoIPTable.setStatus('current')
agentAutoVoIPEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 4, 1, 1, 1), ).setIndexNames((0, "FASTPATH-QOS-AUTOVOIP-MIB", "agentAutoVoIPIntfIndex"))
if mibBuilder.loadTexts: agentAutoVoIPEntry.setStatus('current')
agentAutoVoIPIntfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 4, 1, 1, 1, 1), InterfaceIndexOrZero())
if mibBuilder.loadTexts: agentAutoVoIPIntfIndex.setStatus('current')
agentAutoVoIPMode = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 4, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentAutoVoIPMode.setStatus('current')
agentAutoVoIPCosQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 4, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentAutoVoIPCosQueue.setStatus('current')
mibBuilder.exportSymbols("FASTPATH-QOS-AUTOVOIP-MIB", fastPathQOSAUTOVOIP=fastPathQOSAUTOVOIP, agentAutoVoIPEntry=agentAutoVoIPEntry, Sixteenths=Sixteenths, agentAutoVoIPIntfIndex=agentAutoVoIPIntfIndex, agentAutoVoIPMode=agentAutoVoIPMode, PercentByFives=PercentByFives, PYSNMP_MODULE_ID=fastPathQOSAUTOVOIP, agentAutoVoIPCosQueue=agentAutoVoIPCosQueue, agentAutoVoIPTable=agentAutoVoIPTable, agentAutoVoIPCfgGroup=agentAutoVoIPCfgGroup)
