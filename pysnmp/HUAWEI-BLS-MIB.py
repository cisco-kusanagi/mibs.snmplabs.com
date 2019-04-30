#
# PySNMP MIB module HUAWEI-BLS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-BLS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:31:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
mplsVpnVrfName, = mibBuilder.importSymbols("MPLS-VPN-MIB", "mplsVpnVrfName")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ObjectIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, Bits, Counter64, Integer32, Unsigned32, iso, Counter32, Gauge32, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "Bits", "Counter64", "Integer32", "Unsigned32", "iso", "Counter32", "Gauge32", "NotificationType", "ModuleIdentity")
DisplayString, TextualConvention, TruthValue, RowStatus, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue", "RowStatus", "DateAndTime")
hwBLS = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 8))
if mibBuilder.loadTexts: hwBLS.setLastUpdated('200304111150Z')
if mibBuilder.loadTexts: hwBLS.setOrganization('Huawei Technologies co.,Ltd.')
class BlsAddReason(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("reasonUnknow", 1), ("reasonManual", 2), ("reasonIPSweep", 3), ("reasonPortScan", 4))

hwBlsMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 8, 1))
hwBlsEnableFlag = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 8, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwBlsEnableFlag.setStatus('current')
hwBlsBlackListTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 8, 1, 2), )
if mibBuilder.loadTexts: hwBlsBlackListTable.setStatus('current')
hwBlsBlackListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 8, 1, 2, 1), ).setIndexNames((0, "MPLS-VPN-MIB", "mplsVpnVrfName"), (0, "HUAWEI-BLS-MIB", "hwBlsItemIPAddress"))
if mibBuilder.loadTexts: hwBlsBlackListEntry.setStatus('current')
hwBlsItemIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 8, 1, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwBlsItemIPAddress.setStatus('current')
hwBlsItemAge = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 8, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwBlsItemAge.setStatus('current')
hwBlsItemAddReason = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 8, 1, 2, 1, 3), BlsAddReason()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwBlsItemAddReason.setStatus('current')
hwBlsItemAddTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 8, 1, 2, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwBlsItemAddTime.setStatus('current')
hwBlsRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 8, 1, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwBlsRowStatus.setStatus('current')
hwBlsFilterTypeSet = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 8, 1, 3))
hwBlsFilterType = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 8, 1, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)).clone(15)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwBlsFilterType.setStatus('current')
hwBlsMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 8, 2))
hwBlsMibGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 8, 2, 1))
hwBlsEnableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 8, 2, 1, 1)).setObjects(("HUAWEI-BLS-MIB", "hwBlsEnableFlag"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwBlsEnableGroup = hwBlsEnableGroup.setStatus('current')
hwBlsBlackListTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 8, 2, 1, 2)).setObjects(("HUAWEI-BLS-MIB", "hwBlsItemIPAddress"), ("HUAWEI-BLS-MIB", "hwBlsItemAge"), ("HUAWEI-BLS-MIB", "hwBlsItemAddReason"), ("HUAWEI-BLS-MIB", "hwBlsItemAddTime"), ("HUAWEI-BLS-MIB", "hwBlsRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwBlsBlackListTableGroup = hwBlsBlackListTableGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-BLS-MIB", hwBlsItemAddReason=hwBlsItemAddReason, hwBlsBlackListTable=hwBlsBlackListTable, hwBlsMibGroup=hwBlsMibGroup, hwBlsFilterTypeSet=hwBlsFilterTypeSet, hwBlsItemAge=hwBlsItemAge, hwBLS=hwBLS, hwBlsFilterType=hwBlsFilterType, hwBlsMibObjects=hwBlsMibObjects, hwBlsRowStatus=hwBlsRowStatus, hwBlsEnableFlag=hwBlsEnableFlag, hwBlsBlackListTableGroup=hwBlsBlackListTableGroup, BlsAddReason=BlsAddReason, hwBlsEnableGroup=hwBlsEnableGroup, hwBlsMibConformance=hwBlsMibConformance, hwBlsItemAddTime=hwBlsItemAddTime, hwBlsItemIPAddress=hwBlsItemIPAddress, PYSNMP_MODULE_ID=hwBLS, hwBlsBlackListEntry=hwBlsBlackListEntry)
