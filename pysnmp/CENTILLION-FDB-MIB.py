#
# PySNMP MIB module CENTILLION-FDB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CENTILLION-FDB-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:30:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
StatusIndicator, CardId, BitField, PortId, sysConfig = mibBuilder.importSymbols("CENTILLION-ROOT-MIB", "StatusIndicator", "CardId", "BitField", "PortId", "sysConfig")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Integer32, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, ModuleIdentity, IpAddress, Counter64, ObjectIdentity, Bits, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "ModuleIdentity", "IpAddress", "Counter64", "ObjectIdentity", "Bits", "MibIdentifier", "Counter32")
PhysAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "DisplayString", "TextualConvention")
class FdbTypeId(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("token-ring", 2), ("ethernet", 3), ("route-descriptor", 4))

class VlanId(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4095)

fdbGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22))
fdbRemoteAgingTimer = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 1000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fdbRemoteAgingTimer.setStatus('mandatory')
fdbTableFlush = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fdbTableFlush.setStatus('mandatory')
fdbTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 3), )
if mibBuilder.loadTexts: fdbTable.setStatus('deprecated')
fdbEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 3, 1), ).setIndexNames((0, "CENTILLION-FDB-MIB", "fdbType"), (0, "CENTILLION-FDB-MIB", "fdbAddress"), (0, "CENTILLION-FDB-MIB", "fdbCard"), (0, "CENTILLION-FDB-MIB", "fdbPort"))
if mibBuilder.loadTexts: fdbEntry.setStatus('deprecated')
fdbType = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 3, 1, 1), FdbTypeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdbType.setStatus('deprecated')
fdbAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 3, 1, 2), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdbAddress.setStatus('deprecated')
fdbCard = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 3, 1, 3), CardId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdbCard.setStatus('deprecated')
fdbPort = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 3, 1, 4), PortId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdbPort.setStatus('deprecated')
fdbIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdbIfIndex.setStatus('deprecated')
fdbStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 3, 1, 6), StatusIndicator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fdbStatus.setStatus('deprecated')
fdbLocal = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 3, 1, 7), BitField()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fdbLocal.setStatus('deprecated')
fdbStatic = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 3, 1, 8), BitField()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdbStatic.setStatus('deprecated')
fdbDuplicate = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 3, 1, 9), BitField()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdbDuplicate.setStatus('deprecated')
fdbRIFPath = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 3, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 28))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fdbRIFPath.setStatus('deprecated')
fdbSSTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 4), )
if mibBuilder.loadTexts: fdbSSTable.setStatus('mandatory')
fdbSSEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 4, 1), ).setIndexNames((0, "CENTILLION-FDB-MIB", "fdbSSIndex"))
if mibBuilder.loadTexts: fdbSSEntry.setStatus('mandatory')
fdbSSIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdbSSIndex.setStatus('mandatory')
fdbSSType = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 4, 1, 2), FdbTypeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdbSSType.setStatus('mandatory')
fdbSSAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 4, 1, 3), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdbSSAddress.setStatus('mandatory')
fdbSSCard = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 4, 1, 4), CardId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdbSSCard.setStatus('mandatory')
fdbSSPort = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 4, 1, 5), PortId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdbSSPort.setStatus('mandatory')
fdbSSVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 4, 1, 6), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdbSSVlanId.setStatus('mandatory')
cnfdbTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 5), )
if mibBuilder.loadTexts: cnfdbTable.setStatus('mandatory')
cnfdbEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 5, 1), ).setIndexNames((0, "CENTILLION-FDB-MIB", "cnfdbType"), (0, "CENTILLION-FDB-MIB", "cnfdbAddress"), (0, "CENTILLION-FDB-MIB", "cnfdbCard"), (0, "CENTILLION-FDB-MIB", "cnfdbPort"), (0, "CENTILLION-FDB-MIB", "cnfdbVlanId"))
if mibBuilder.loadTexts: cnfdbEntry.setStatus('mandatory')
cnfdbType = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 5, 1, 1), FdbTypeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnfdbType.setStatus('mandatory')
cnfdbAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 5, 1, 2), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnfdbAddress.setStatus('mandatory')
cnfdbCard = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 5, 1, 3), CardId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnfdbCard.setStatus('mandatory')
cnfdbPort = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 5, 1, 4), PortId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnfdbPort.setStatus('mandatory')
cnfdbVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 5, 1, 5), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnfdbVlanId.setStatus('mandatory')
cnfdbIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 5, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnfdbIfIndex.setStatus('mandatory')
cnfdbStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 5, 1, 7), StatusIndicator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnfdbStatus.setStatus('mandatory')
cnfdbLocal = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 5, 1, 8), BitField()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnfdbLocal.setStatus('mandatory')
cnfdbStatic = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 5, 1, 9), BitField()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnfdbStatic.setStatus('mandatory')
cnfdbDuplicate = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 5, 1, 10), BitField()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnfdbDuplicate.setStatus('mandatory')
cnfdbRIFPath = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 22, 5, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 28))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnfdbRIFPath.setStatus('mandatory')
mibBuilder.exportSymbols("CENTILLION-FDB-MIB", fdbSSVlanId=fdbSSVlanId, cnfdbTable=cnfdbTable, cnfdbRIFPath=cnfdbRIFPath, fdbStatus=fdbStatus, fdbStatic=fdbStatic, fdbSSType=fdbSSType, fdbType=fdbType, fdbEntry=fdbEntry, fdbDuplicate=fdbDuplicate, fdbSSCard=fdbSSCard, fdbSSIndex=fdbSSIndex, cnfdbIfIndex=cnfdbIfIndex, fdbCard=fdbCard, fdbTableFlush=fdbTableFlush, fdbRemoteAgingTimer=fdbRemoteAgingTimer, cnfdbEntry=cnfdbEntry, fdbSSPort=fdbSSPort, FdbTypeId=FdbTypeId, fdbAddress=fdbAddress, cnfdbLocal=cnfdbLocal, fdbSSEntry=fdbSSEntry, fdbSSAddress=fdbSSAddress, fdbGroup=fdbGroup, cnfdbStatic=cnfdbStatic, cnfdbVlanId=cnfdbVlanId, cnfdbStatus=cnfdbStatus, cnfdbType=cnfdbType, fdbLocal=fdbLocal, VlanId=VlanId, cnfdbCard=cnfdbCard, cnfdbDuplicate=cnfdbDuplicate, cnfdbPort=cnfdbPort, fdbPort=fdbPort, fdbRIFPath=fdbRIFPath, fdbIfIndex=fdbIfIndex, cnfdbAddress=cnfdbAddress, fdbSSTable=fdbSSTable, fdbTable=fdbTable)