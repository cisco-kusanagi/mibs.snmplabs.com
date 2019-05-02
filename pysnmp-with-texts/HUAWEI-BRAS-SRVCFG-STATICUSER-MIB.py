#
# PySNMP MIB module HUAWEI-BRAS-SRVCFG-STATICUSER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-BRAS-SRVCFG-STATICUSER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:43:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
hwBRASMib, = mibBuilder.importSymbols("HUAWEI-MIB", "hwBRASMib")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
mplsVpnVrfName, = mibBuilder.importSymbols("MPLS-VPN-MIB", "mplsVpnVrfName")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Bits, Unsigned32, ModuleIdentity, IpAddress, iso, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, Counter64, Counter32, MibIdentifier, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Unsigned32", "ModuleIdentity", "IpAddress", "iso", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "Counter64", "Counter32", "MibIdentifier", "ObjectIdentity")
DisplayString, RowStatus, TextualConvention, TruthValue, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TruthValue", "MacAddress")
hwBRASSrvcfgStaticUser = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5))
hwBRASSrvcfgStaticUser.setRevisions(('2013-06-26 16:08', '2009-08-09 18:50',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hwBRASSrvcfgStaticUser.setRevisionsDescriptions((' V2.01, Inital version. ', ' V2.00, Inital version. ',))
if mibBuilder.loadTexts: hwBRASSrvcfgStaticUser.setLastUpdated('201306261608Z')
if mibBuilder.loadTexts: hwBRASSrvcfgStaticUser.setOrganization('Huawei Technologies Co.,Ltd.')
if mibBuilder.loadTexts: hwBRASSrvcfgStaticUser.setContactInfo("Huawei Industrial Base Bantian, Longgang Shenzhen 518129 People's Republic of China Website: http://www.huawei.com Email: support@huawei.com ")
if mibBuilder.loadTexts: hwBRASSrvcfgStaticUser.setDescription('The MIB contains objects of module SRVCFG.')
hwSrvcfgStaticUserMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1))
hwStaticUserTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 1), )
if mibBuilder.loadTexts: hwStaticUserTable.setStatus('current')
if mibBuilder.loadTexts: hwStaticUserTable.setDescription('The table of static user.')
hwStaticUserEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 1, 1), ).setIndexNames((0, "MPLS-VPN-MIB", "mplsVpnVrfName"), (0, "HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserStartIpAddr"))
if mibBuilder.loadTexts: hwStaticUserEntry.setStatus('current')
if mibBuilder.loadTexts: hwStaticUserEntry.setDescription('Description.')
hwStaticUserStartIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwStaticUserStartIpAddr.setStatus('current')
if mibBuilder.loadTexts: hwStaticUserStartIpAddr.setDescription('The start ip address of static user.')
hwStaticUserEndIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 1, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwStaticUserEndIpAddr.setStatus('current')
if mibBuilder.loadTexts: hwStaticUserEndIpAddr.setDescription('The end ip address of static user.')
hwStaticUserIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 1, 1, 3), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwStaticUserIfIndex.setStatus('current')
if mibBuilder.loadTexts: hwStaticUserIfIndex.setDescription('The interface of static user logining.')
hwStaticUserVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwStaticUserVlan.setStatus('current')
if mibBuilder.loadTexts: hwStaticUserVlan.setDescription('The vlan of static user.')
hwStaticUserVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwStaticUserVpi.setStatus('current')
if mibBuilder.loadTexts: hwStaticUserVpi.setDescription('The vpi of static user.')
hwStaticUserVci = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65534))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwStaticUserVci.setStatus('current')
if mibBuilder.loadTexts: hwStaticUserVci.setDescription('The vci of static user.')
hwStaticUserMac = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 1, 1, 7), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwStaticUserMac.setStatus('current')
if mibBuilder.loadTexts: hwStaticUserMac.setDescription('The MAC address of static user.')
hwStaticUserDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 200))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwStaticUserDomain.setStatus('current')
if mibBuilder.loadTexts: hwStaticUserDomain.setDescription('The domain of static user belong to.')
hwStaticUserDetect = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 1, 1, 9), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwStaticUserDetect.setStatus('current')
if mibBuilder.loadTexts: hwStaticUserDetect.setDescription('Whether or not detect static user.')
hwStaticUserRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 1, 1, 10), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwStaticUserRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwStaticUserRowStatus.setDescription('The status of row.')
hwStaticUserStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("ready", 0), ("detecting", 1), ("deleting", 2), ("online", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwStaticUserStatus.setStatus('current')
if mibBuilder.loadTexts: hwStaticUserStatus.setDescription('The status of static user.')
hwStaticUserQinQVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwStaticUserQinQVlan.setStatus('current')
if mibBuilder.loadTexts: hwStaticUserQinQVlan.setDescription('The QinQ vlan of static user.')
hwStaticUserDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 1, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwStaticUserDescription.setStatus('current')
if mibBuilder.loadTexts: hwStaticUserDescription.setDescription('The description of static user.')
hwStaticUserGatewayIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 1, 1, 14), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwStaticUserGatewayIpAddr.setStatus('current')
if mibBuilder.loadTexts: hwStaticUserGatewayIpAddr.setDescription('The gateway ip address of static user.')
hwStaticUserVrfName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 1, 1, 15), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwStaticUserVrfName.setStatus('current')
if mibBuilder.loadTexts: hwStaticUserVrfName.setDescription('The vrfname of static user.')
hwStaticUserV2Table = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 2), )
if mibBuilder.loadTexts: hwStaticUserV2Table.setStatus('current')
if mibBuilder.loadTexts: hwStaticUserV2Table.setDescription('The table of static user.(V2)')
hwStaticUserV2Entry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 2, 1), ).setIndexNames((0, "HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserVrfNameV2"), (0, "HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserStartIpAddrV2"))
if mibBuilder.loadTexts: hwStaticUserV2Entry.setStatus('current')
if mibBuilder.loadTexts: hwStaticUserV2Entry.setDescription('Description.(V2)')
hwStaticUserStartIpAddrV2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwStaticUserStartIpAddrV2.setStatus('current')
if mibBuilder.loadTexts: hwStaticUserStartIpAddrV2.setDescription('The start ip address of static user.(V2)')
hwStaticUserEndIpAddrV2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 2, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwStaticUserEndIpAddrV2.setStatus('current')
if mibBuilder.loadTexts: hwStaticUserEndIpAddrV2.setDescription('The end ip address of static user.(V2)')
hwStaticUserIfIndexV2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 2, 1, 3), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwStaticUserIfIndexV2.setStatus('current')
if mibBuilder.loadTexts: hwStaticUserIfIndexV2.setDescription('The interface of static user logining.(V2)')
hwStaticUserVlanV2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwStaticUserVlanV2.setStatus('current')
if mibBuilder.loadTexts: hwStaticUserVlanV2.setDescription('The vlan of static user.(V2)')
hwStaticUserVpiV2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwStaticUserVpiV2.setStatus('current')
if mibBuilder.loadTexts: hwStaticUserVpiV2.setDescription('The vpi of static user.(V2)')
hwStaticUserVciV2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65534))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwStaticUserVciV2.setStatus('current')
if mibBuilder.loadTexts: hwStaticUserVciV2.setDescription('The vci of static user.(V2)')
hwStaticUserMacV2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 2, 1, 7), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwStaticUserMacV2.setStatus('current')
if mibBuilder.loadTexts: hwStaticUserMacV2.setDescription('The MAC address of static user.(V2)')
hwStaticUserDomainV2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 2, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwStaticUserDomainV2.setStatus('current')
if mibBuilder.loadTexts: hwStaticUserDomainV2.setDescription('The domain of static user belong to.(V2)')
hwStaticUserDetectV2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 2, 1, 9), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwStaticUserDetectV2.setStatus('current')
if mibBuilder.loadTexts: hwStaticUserDetectV2.setDescription('Whether or not detect static user.(V2)')
hwStaticUserRowStatusV2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 2, 1, 10), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwStaticUserRowStatusV2.setStatus('current')
if mibBuilder.loadTexts: hwStaticUserRowStatusV2.setDescription('The status of row.(V2)')
hwStaticUserStatusV2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("ready", 0), ("detecting", 1), ("deleting", 2), ("online", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwStaticUserStatusV2.setStatus('current')
if mibBuilder.loadTexts: hwStaticUserStatusV2.setDescription('The status of static user.(V2)')
hwStaticUserQinQVlanV2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 2, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwStaticUserQinQVlanV2.setStatus('current')
if mibBuilder.loadTexts: hwStaticUserQinQVlanV2.setDescription('The QinQ vlan of static user.(V2)')
hwStaticUserVrfNameV2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 2, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwStaticUserVrfNameV2.setStatus('current')
if mibBuilder.loadTexts: hwStaticUserVrfNameV2.setDescription('The vpn instance of static user.(V2)')
hwStaticUserPassowrd = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 3), OctetString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 16), ValueSizeConstraint(32, 32), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwStaticUserPassowrd.setStatus('current')
if mibBuilder.loadTexts: hwStaticUserPassowrd.setDescription('Description.')
hwStaticUserUserNameFormatInclude = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("default", 1), ("ipaddress", 2), ("macaddress", 3), ("sysname", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwStaticUserUserNameFormatInclude.setStatus('current')
if mibBuilder.loadTexts: hwStaticUserUserNameFormatInclude.setDescription('Description.')
hwStaticUserConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 2))
hwStaticUserCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 2, 1))
hwStaticUserCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 2, 1, 1)).setObjects(("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserTableGroup"), ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserTableV2Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwStaticUserCompliance = hwStaticUserCompliance.setStatus('current')
if mibBuilder.loadTexts: hwStaticUserCompliance.setDescription('The compliance statement for systems supporting the this module.')
hwStaticUserObjectGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 2, 1, 2))
hwStaticUserTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 2, 1, 2, 1)).setObjects(("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserStartIpAddr"), ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserEndIpAddr"), ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserIfIndex"), ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserVlan"), ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserVpi"), ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserVci"), ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserMac"), ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserDomain"), ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserDetect"), ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserRowStatus"), ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserStatus"), ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserQinQVlan"), ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserDescription"), ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserGatewayIpAddr"), ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserVrfName"), ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserPassowrd"), ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserUserNameFormatInclude"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwStaticUserTableGroup = hwStaticUserTableGroup.setStatus('current')
if mibBuilder.loadTexts: hwStaticUserTableGroup.setDescription('Static user configuraion table.')
hwStaticUserTableV2Group = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 2, 1, 2, 2)).setObjects(("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserStartIpAddrV2"), ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserEndIpAddrV2"), ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserIfIndexV2"), ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserVlanV2"), ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserVpiV2"), ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserVciV2"), ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserMacV2"), ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserDomainV2"), ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserDetectV2"), ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserRowStatusV2"), ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserStatusV2"), ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserQinQVlanV2"), ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserVrfNameV2"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwStaticUserTableV2Group = hwStaticUserTableV2Group.setStatus('current')
if mibBuilder.loadTexts: hwStaticUserTableV2Group.setDescription('Static user configuraion table.(V2)')
mibBuilder.exportSymbols("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", hwSrvcfgStaticUserMibObjects=hwSrvcfgStaticUserMibObjects, hwStaticUserTableV2Group=hwStaticUserTableV2Group, hwStaticUserGatewayIpAddr=hwStaticUserGatewayIpAddr, hwStaticUserUserNameFormatInclude=hwStaticUserUserNameFormatInclude, hwStaticUserDomainV2=hwStaticUserDomainV2, hwStaticUserIfIndex=hwStaticUserIfIndex, hwStaticUserMacV2=hwStaticUserMacV2, hwStaticUserCompliances=hwStaticUserCompliances, hwStaticUserCompliance=hwStaticUserCompliance, hwStaticUserDetect=hwStaticUserDetect, hwStaticUserVrfNameV2=hwStaticUserVrfNameV2, hwStaticUserObjectGroups=hwStaticUserObjectGroups, hwStaticUserEndIpAddrV2=hwStaticUserEndIpAddrV2, hwBRASSrvcfgStaticUser=hwBRASSrvcfgStaticUser, hwStaticUserVpi=hwStaticUserVpi, hwStaticUserStatusV2=hwStaticUserStatusV2, hwStaticUserStartIpAddr=hwStaticUserStartIpAddr, hwStaticUserDomain=hwStaticUserDomain, hwStaticUserV2Table=hwStaticUserV2Table, hwStaticUserVci=hwStaticUserVci, hwStaticUserStartIpAddrV2=hwStaticUserStartIpAddrV2, hwStaticUserVrfName=hwStaticUserVrfName, hwStaticUserTable=hwStaticUserTable, hwStaticUserVlanV2=hwStaticUserVlanV2, hwStaticUserRowStatus=hwStaticUserRowStatus, hwStaticUserConformance=hwStaticUserConformance, hwStaticUserEntry=hwStaticUserEntry, hwStaticUserQinQVlan=hwStaticUserQinQVlan, hwStaticUserStatus=hwStaticUserStatus, PYSNMP_MODULE_ID=hwBRASSrvcfgStaticUser, hwStaticUserRowStatusV2=hwStaticUserRowStatusV2, hwStaticUserPassowrd=hwStaticUserPassowrd, hwStaticUserDetectV2=hwStaticUserDetectV2, hwStaticUserEndIpAddr=hwStaticUserEndIpAddr, hwStaticUserVlan=hwStaticUserVlan, hwStaticUserMac=hwStaticUserMac, hwStaticUserQinQVlanV2=hwStaticUserQinQVlanV2, hwStaticUserTableGroup=hwStaticUserTableGroup, hwStaticUserVciV2=hwStaticUserVciV2, hwStaticUserIfIndexV2=hwStaticUserIfIndexV2, hwStaticUserDescription=hwStaticUserDescription, hwStaticUserVpiV2=hwStaticUserVpiV2, hwStaticUserV2Entry=hwStaticUserV2Entry)
