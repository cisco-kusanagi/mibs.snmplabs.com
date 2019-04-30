#
# PySNMP MIB module HUAWEI-BGP-ACCOUNTING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-BGP-ACCOUNTING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:31:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, ObjectIdentity, ModuleIdentity, Unsigned32, Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, Counter32, MibIdentifier, IpAddress, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "ModuleIdentity", "Unsigned32", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "Counter32", "MibIdentifier", "IpAddress", "iso", "Bits")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
hwBgpAcctMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 39))
if mibBuilder.loadTexts: hwBgpAcctMIB.setLastUpdated('200705100000Z')
if mibBuilder.loadTexts: hwBgpAcctMIB.setOrganization('Huawei Technologies co.,Ltd.')
class AddressType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("invalid", 0), ("source", 1), ("destination", 2))

class DirectionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("invalid", 0), ("inbound", 1), ("outbound", 2), ("inboundAndOutbound", 3))

hwBgpAcctMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 39, 1))
hwBgpAcctCfgTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 39, 1, 1), )
if mibBuilder.loadTexts: hwBgpAcctCfgTable.setStatus('current')
hwBgpAcctCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 39, 1, 1, 1), ).setIndexNames((0, "HUAWEI-BGP-ACCOUNTING-MIB", "hwbgpAcctCfgIfIndex"))
if mibBuilder.loadTexts: hwBgpAcctCfgEntry.setStatus('current')
hwbgpAcctCfgIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 39, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwbgpAcctCfgIfIndex.setStatus('current')
hwbgpAcctSrcOrDest = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 39, 1, 1, 1, 2), AddressType().clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwbgpAcctSrcOrDest.setStatus('current')
hwbgpAcctDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 39, 1, 1, 1, 3), DirectionType().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwbgpAcctDirection.setStatus('current')
hwbgpAcctCfgRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 39, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwbgpAcctCfgRowStatus.setStatus('current')
hwBgpAcctStatTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 39, 1, 2), )
if mibBuilder.loadTexts: hwBgpAcctStatTable.setStatus('current')
hwBgpAcctStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 39, 1, 2, 1), ).setIndexNames((0, "HUAWEI-BGP-ACCOUNTING-MIB", "hwbgpAcctStatIfIndex"), (0, "HUAWEI-BGP-ACCOUNTING-MIB", "hwbgpAcctTrafficIndex"))
if mibBuilder.loadTexts: hwBgpAcctStatEntry.setStatus('current')
hwbgpAcctStatIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 39, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwbgpAcctStatIfIndex.setStatus('current')
hwbgpAcctTrafficIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 39, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwbgpAcctTrafficIndex.setStatus('current')
hwbgpAcctInPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 39, 1, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwbgpAcctInPacketCount.setStatus('current')
hwbgpAcctInOctetCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 39, 1, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwbgpAcctInOctetCount.setStatus('current')
hwbgpAcctOutPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 39, 1, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwbgpAcctOutPacketCount.setStatus('current')
hwbgpAcctOutOctetCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 39, 1, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwbgpAcctOutOctetCount.setStatus('current')
hwBgpAcctConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 39, 2))
hwBgpAcctCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 39, 2, 1))
hwBgpAcctCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 39, 2, 1, 1)).setObjects(("HUAWEI-BGP-ACCOUNTING-MIB", "hwBgpAcctCfgGroup"), ("HUAWEI-BGP-ACCOUNTING-MIB", "hwBgpAcctStatGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwBgpAcctCompliance = hwBgpAcctCompliance.setStatus('current')
hwBgpAcctStatGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 39, 2, 2))
hwBgpAcctCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 39, 2, 2, 1)).setObjects(("HUAWEI-BGP-ACCOUNTING-MIB", "hwbgpAcctCfgIfIndex"), ("HUAWEI-BGP-ACCOUNTING-MIB", "hwbgpAcctSrcOrDest"), ("HUAWEI-BGP-ACCOUNTING-MIB", "hwbgpAcctDirection"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwBgpAcctCfgGroup = hwBgpAcctCfgGroup.setStatus('current')
hwBgpAcctStatGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 39, 2, 2, 2)).setObjects(("HUAWEI-BGP-ACCOUNTING-MIB", "hwbgpAcctStatIfIndex"), ("HUAWEI-BGP-ACCOUNTING-MIB", "hwbgpAcctTrafficIndex"), ("HUAWEI-BGP-ACCOUNTING-MIB", "hwbgpAcctInPacketCount"), ("HUAWEI-BGP-ACCOUNTING-MIB", "hwbgpAcctInOctetCount"), ("HUAWEI-BGP-ACCOUNTING-MIB", "hwbgpAcctOutPacketCount"), ("HUAWEI-BGP-ACCOUNTING-MIB", "hwbgpAcctOutOctetCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwBgpAcctStatGroup = hwBgpAcctStatGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-BGP-ACCOUNTING-MIB", hwbgpAcctInOctetCount=hwbgpAcctInOctetCount, hwbgpAcctOutPacketCount=hwbgpAcctOutPacketCount, hwBgpAcctConformance=hwBgpAcctConformance, hwBgpAcctCfgTable=hwBgpAcctCfgTable, hwbgpAcctInPacketCount=hwbgpAcctInPacketCount, hwbgpAcctOutOctetCount=hwbgpAcctOutOctetCount, hwBgpAcctCompliances=hwBgpAcctCompliances, hwbgpAcctDirection=hwbgpAcctDirection, hwBgpAcctMIB=hwBgpAcctMIB, hwBgpAcctCfgEntry=hwBgpAcctCfgEntry, hwBgpAcctStatEntry=hwBgpAcctStatEntry, DirectionType=DirectionType, hwBgpAcctCfgGroup=hwBgpAcctCfgGroup, hwbgpAcctStatIfIndex=hwbgpAcctStatIfIndex, hwBgpAcctStatGroups=hwBgpAcctStatGroups, PYSNMP_MODULE_ID=hwBgpAcctMIB, AddressType=AddressType, hwbgpAcctCfgIfIndex=hwbgpAcctCfgIfIndex, hwBgpAcctStatTable=hwBgpAcctStatTable, hwBgpAcctCompliance=hwBgpAcctCompliance, hwBgpAcctMIBObjects=hwBgpAcctMIBObjects, hwbgpAcctTrafficIndex=hwbgpAcctTrafficIndex, hwbgpAcctCfgRowStatus=hwbgpAcctCfgRowStatus, hwBgpAcctStatGroup=hwBgpAcctStatGroup, hwbgpAcctSrcOrDest=hwbgpAcctSrcOrDest)
