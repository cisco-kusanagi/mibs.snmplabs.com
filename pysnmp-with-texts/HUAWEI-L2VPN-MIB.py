#
# PySNMP MIB module HUAWEI-L2VPN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-L2VPN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:45:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
sysUpTime, = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime")
Counter64, iso, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, ModuleIdentity, MibIdentifier, NotificationType, Bits, IpAddress, Integer32, TimeTicks, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "iso", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "ModuleIdentity", "MibIdentifier", "NotificationType", "Bits", "IpAddress", "Integer32", "TimeTicks", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hwL2VpnAttribute = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7))
if mibBuilder.loadTexts: hwL2VpnAttribute.setLastUpdated('200903030900Z')
if mibBuilder.loadTexts: hwL2VpnAttribute.setOrganization('Huawei Technologies Co., Ltd.')
if mibBuilder.loadTexts: hwL2VpnAttribute.setContactInfo('R&D BeiJing, Huawei Technologies co.,Ltd. Q2 Bld.,NO.156 BeiQing Rd., HuanBaoYuan Information Industry Base, Hai-Dian District Beijing P.R. China Zip:100094 Http://www.huawei.com E-mail:support@huawei.com')
if mibBuilder.loadTexts: hwL2VpnAttribute.setDescription('The HUAWEI-L2VPN-MIB contains objects to manage global Attributes of L2VPN.')
hwL2Vpn = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119))
hwL2VpnEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwL2VpnEnable.setStatus('current')
if mibBuilder.loadTexts: hwL2VpnEnable.setDescription('This object indicates whether enabled mpls L2vpn capability or not.')
hwL2VpnWorkingMode = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("pwe3", 1), ("martini", 2), ("unknown", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwL2VpnWorkingMode.setStatus('current')
if mibBuilder.loadTexts: hwL2VpnWorkingMode.setDescription('This object indicates the working mode of mpls L2vpn.')
hwL2VpnMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 3))
hwL2VpnMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 3, 1))
hwL2VpnMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 3, 1, 1)).setObjects(("HUAWEI-L2VPN-MIB", "hwL2VpnMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwL2VpnMIBCompliance = hwL2VpnMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: hwL2VpnMIBCompliance.setDescription('The compliance statement for systems supporting the HUAWEI-L2VPN-MIB.')
hwL2VpnMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 3, 2))
hwL2VpnMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 3, 2, 1)).setObjects(("HUAWEI-L2VPN-MIB", "hwL2VpnEnable"), ("HUAWEI-L2VPN-MIB", "hwL2VpnWorkingMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwL2VpnMIBGroup = hwL2VpnMIBGroup.setStatus('current')
if mibBuilder.loadTexts: hwL2VpnMIBGroup.setDescription("The L2VPN's attributes group.")
mibBuilder.exportSymbols("HUAWEI-L2VPN-MIB", hwL2VpnMIBGroup=hwL2VpnMIBGroup, hwL2VpnMIBConformance=hwL2VpnMIBConformance, hwL2VpnAttribute=hwL2VpnAttribute, hwL2VpnMIBGroups=hwL2VpnMIBGroups, PYSNMP_MODULE_ID=hwL2VpnAttribute, hwL2Vpn=hwL2Vpn, hwL2VpnMIBCompliances=hwL2VpnMIBCompliances, hwL2VpnWorkingMode=hwL2VpnWorkingMode, hwL2VpnEnable=hwL2VpnEnable, hwL2VpnMIBCompliance=hwL2VpnMIBCompliance)
