#
# PySNMP MIB module HUAWEI-BRAS-MVLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-BRAS-MVLAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:31:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
hwBRASMib, = mibBuilder.importSymbols("HUAWEI-MIB", "hwBRASMib")
VlanId, VlanIndex = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId", "VlanIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Counter64, Unsigned32, Bits, IpAddress, iso, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, ModuleIdentity, Integer32, NotificationType, MibIdentifier, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "Unsigned32", "Bits", "IpAddress", "iso", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "ModuleIdentity", "Integer32", "NotificationType", "MibIdentifier", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hwMVLAN = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 14))
if mibBuilder.loadTexts: hwMVLAN.setLastUpdated('200708271200Z')
if mibBuilder.loadTexts: hwMVLAN.setOrganization('Huawei Technologies Co., Ltd.')
hwhwMVLANMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 14, 1))
hwMulticastVlanTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 14, 1, 1), )
if mibBuilder.loadTexts: hwMulticastVlanTable.setStatus('current')
hwMulticastVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 14, 1, 1, 1), ).setIndexNames((0, "HUAWEI-BRAS-MVLAN-MIB", "hwMulticastVlanIfIndex"))
if mibBuilder.loadTexts: hwMulticastVlanEntry.setStatus('current')
hwMulticastVlanIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 14, 1, 1, 1, 1), VlanIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMulticastVlanIfIndex.setStatus('current')
hwMulticastInnerVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 14, 1, 1, 1, 2), VlanId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwMulticastInnerVlan.setStatus('current')
hwMulticastOuterVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 14, 1, 1, 1, 3), VlanId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwMulticastOuterVlan.setStatus('current')
hwMulticastOpType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 14, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("set", 0), ("undo", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwMulticastOpType.setStatus('current')
hwMVlanMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 14, 2))
hwMVlanMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 14, 2, 1))
hwMVlanMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 14, 2, 1, 1)).setObjects(("HUAWEI-BRAS-MVLAN-MIB", "hwMVlanGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwMVlanMIBCompliance = hwMVlanMIBCompliance.setStatus('current')
hwMVlanMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 14, 2, 2))
hwMVlanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 14, 2, 2, 1)).setObjects(("HUAWEI-BRAS-MVLAN-MIB", "hwMulticastVlanIfIndex"), ("HUAWEI-BRAS-MVLAN-MIB", "hwMulticastInnerVlan"), ("HUAWEI-BRAS-MVLAN-MIB", "hwMulticastOuterVlan"), ("HUAWEI-BRAS-MVLAN-MIB", "hwMulticastOpType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwMVlanGroup = hwMVlanGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-BRAS-MVLAN-MIB", hwMulticastVlanTable=hwMulticastVlanTable, PYSNMP_MODULE_ID=hwMVLAN, hwMVlanMIBGroups=hwMVlanMIBGroups, hwMVlanMIBConformance=hwMVlanMIBConformance, hwMulticastInnerVlan=hwMulticastInnerVlan, hwMVlanGroup=hwMVlanGroup, hwMulticastOpType=hwMulticastOpType, hwhwMVLANMibObjects=hwhwMVLANMibObjects, hwMVLAN=hwMVLAN, hwMulticastVlanIfIndex=hwMulticastVlanIfIndex, hwMVlanMIBCompliances=hwMVlanMIBCompliances, hwMulticastOuterVlan=hwMulticastOuterVlan, hwMVlanMIBCompliance=hwMVlanMIBCompliance, hwMulticastVlanEntry=hwMulticastVlanEntry)
