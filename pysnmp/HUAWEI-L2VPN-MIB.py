#
# PySNMP MIB module HUAWEI-L2VPN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-L2VPN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:33:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
sysUpTime, = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, iso, NotificationType, Bits, IpAddress, Counter64, ModuleIdentity, Gauge32, TimeTicks, MibIdentifier, Integer32, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "iso", "NotificationType", "Bits", "IpAddress", "Counter64", "ModuleIdentity", "Gauge32", "TimeTicks", "MibIdentifier", "Integer32", "Counter32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hwL2VpnAttribute = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7))
if mibBuilder.loadTexts: hwL2VpnAttribute.setLastUpdated('200903030900Z')
if mibBuilder.loadTexts: hwL2VpnAttribute.setOrganization('Huawei Technologies Co., Ltd.')
hwL2Vpn = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119))
hwL2VpnEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwL2VpnEnable.setStatus('current')
hwL2VpnWorkingMode = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("pwe3", 1), ("martini", 2), ("unknown", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwL2VpnWorkingMode.setStatus('current')
hwL2VpnMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 3))
hwL2VpnMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 3, 1))
hwL2VpnMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 3, 1, 1)).setObjects(("HUAWEI-L2VPN-MIB", "hwL2VpnMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwL2VpnMIBCompliance = hwL2VpnMIBCompliance.setStatus('current')
hwL2VpnMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 3, 2))
hwL2VpnMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 3, 2, 1)).setObjects(("HUAWEI-L2VPN-MIB", "hwL2VpnEnable"), ("HUAWEI-L2VPN-MIB", "hwL2VpnWorkingMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwL2VpnMIBGroup = hwL2VpnMIBGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-L2VPN-MIB", hwL2VpnEnable=hwL2VpnEnable, hwL2VpnMIBCompliances=hwL2VpnMIBCompliances, hwL2VpnWorkingMode=hwL2VpnWorkingMode, hwL2VpnMIBGroups=hwL2VpnMIBGroups, hwL2Vpn=hwL2Vpn, hwL2VpnAttribute=hwL2VpnAttribute, hwL2VpnMIBConformance=hwL2VpnMIBConformance, hwL2VpnMIBCompliance=hwL2VpnMIBCompliance, PYSNMP_MODULE_ID=hwL2VpnAttribute, hwL2VpnMIBGroup=hwL2VpnMIBGroup)
