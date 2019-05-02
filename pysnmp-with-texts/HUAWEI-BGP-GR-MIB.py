#
# PySNMP MIB module HUAWEI-BGP-GR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-BGP-GR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:43:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
InetAddress, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
iso, Counter64, ObjectIdentity, Counter32, IpAddress, Gauge32, NotificationType, Bits, TimeTicks, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "ObjectIdentity", "Counter32", "IpAddress", "Gauge32", "NotificationType", "Bits", "TimeTicks", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ModuleIdentity", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hwBgpGRMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138))
if mibBuilder.loadTexts: hwBgpGRMIB.setLastUpdated('200611220000Z')
if mibBuilder.loadTexts: hwBgpGRMIB.setOrganization('Huawei Technologies co.,Ltd.')
if mibBuilder.loadTexts: hwBgpGRMIB.setContactInfo(' R&D BeiJing, Huawei Technologies co.,Ltd. Huawei Bld.,NO.3 Xinxi Rd., Shang-Di Information Industry Base, Hai-Dian District Beijing P.R. China Zip:100085 Http://www.huawei.com E-mail:support@huawei.com ')
if mibBuilder.loadTexts: hwBgpGRMIB.setDescription('The HUAWEI-BGP-GR-MIB contains objects to Manage configuration and Monitor running state for BGP Graceful Restart feature.')
class Status(TextualConvention, Integer32):
    description = "This type is used to show status of GR,for example 'enable' means capability of GR have enabled, 'disable' means capability of GR have disabled"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class AFIType(TextualConvention, Integer32):
    description = 'This type is used to show Address Family'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 25, 196))
    namedValues = NamedValues(("notspecified", 1), ("ipv4", 2), ("ipv6", 3), ("vpls", 25), ("l2vpn", 196))

class SAFIType(TextualConvention, Integer32):
    description = 'This type is used to show Sub Address Family'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 65, 128))
    namedValues = NamedValues(("notspecified", 1), ("unicast", 2), ("multicast", 3), ("unicastandmulticast", 4), ("mpls", 5), ("vpls", 65), ("vpnv4", 128))

class GRRole(TextualConvention, Integer32):
    description = "This type is used to show Role of router in the process of GR, 'restarter' means the router pay Restarter role in the process of GR,'helper'means the router pay Helper role in the process of GR,if each peer have conferred with each others on GR,we call the kind of state is 'grnormal',if negotiation is unsuccessful,the kind of state is 'grnegotiatefail'."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("grnormal", 1), ("restarter", 2), ("helper", 3), ("grnegotiatefail", 4))

hwBgpGRMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 1))
hwBgpGRCapability = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 1, 1), Status()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwBgpGRCapability.setStatus('current')
if mibBuilder.loadTexts: hwBgpGRCapability.setDescription("We can see status of GR by this node,the value 'enable' denotes that capability of GR have be actived, 'disable' denotes that capability of GR have be disabled.")
hwBgpGRRestartTime = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwBgpGRRestartTime.setStatus('current')
if mibBuilder.loadTexts: hwBgpGRRestartTime.setDescription('The Value of BGP GR restart timer(second)')
hwBgpGRWaitForRibTime = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 3000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwBgpGRWaitForRibTime.setStatus('current')
if mibBuilder.loadTexts: hwBgpGRWaitForRibTime.setDescription('The value of BGP GR wait-for-EndofRib timer(second)')
hwBgpGRStatusInfoTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 1, 4), )
if mibBuilder.loadTexts: hwBgpGRStatusInfoTable.setStatus('current')
if mibBuilder.loadTexts: hwBgpGRStatusInfoTable.setDescription('This table show state of local router for a special peer.')
hwBgpGRStatusInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 1, 4, 1), ).setIndexNames((0, "HUAWEI-BGP-GR-MIB", "hwBgpGRStatAddressFamily"), (0, "HUAWEI-BGP-GR-MIB", "hwBgpGRStatSubAddressFamily"), (0, "HUAWEI-BGP-GR-MIB", "hwBgpGRStatInstanceID"), (0, "HUAWEI-BGP-GR-MIB", "hwBgpGRStatPeerAddress"))
if mibBuilder.loadTexts: hwBgpGRStatusInfoEntry.setStatus('current')
if mibBuilder.loadTexts: hwBgpGRStatusInfoEntry.setDescription('State of local router for a special peer in this entry')
hwBgpGRStatAddressFamily = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 1, 4, 1, 1), AFIType())
if mibBuilder.loadTexts: hwBgpGRStatAddressFamily.setStatus('current')
if mibBuilder.loadTexts: hwBgpGRStatAddressFamily.setDescription('Address family of BGP( notspecified(1), ipv4(2), ipv6(3), vpls(25), l2vpn(196))')
hwBgpGRStatSubAddressFamily = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 1, 4, 1, 2), SAFIType())
if mibBuilder.loadTexts: hwBgpGRStatSubAddressFamily.setStatus('current')
if mibBuilder.loadTexts: hwBgpGRStatSubAddressFamily.setDescription('Sub address family of BGP( notspecified(1), unicast(2), multicast(3), unicastandmulticast(4), mpls(5), vpls(65), vpnv4(128))')
hwBgpGRStatInstanceID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 1, 4, 1, 3), Unsigned32())
if mibBuilder.loadTexts: hwBgpGRStatInstanceID.setStatus('current')
if mibBuilder.loadTexts: hwBgpGRStatInstanceID.setDescription('The instance index of linking peer')
hwBgpGRStatPeerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 1, 4, 1, 4), InetAddress())
if mibBuilder.loadTexts: hwBgpGRStatPeerAddress.setStatus('current')
if mibBuilder.loadTexts: hwBgpGRStatPeerAddress.setDescription('Ipv4 address family of peer,note:there is only one kind of IP Address at a special address family,for example,there is ipv4 address at public unicast,and there will not be ipv6 address.')
hwBgpGRStatLocalGRRole = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 1, 4, 1, 5), GRRole()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwBgpGRStatLocalGRRole.setStatus('current')
if mibBuilder.loadTexts: hwBgpGRStatLocalGRRole.setDescription("Role of router in the process of GR,'restarter' means the router pay Restarter role in the process of GR,'helper' means the router pay Helper role in the process of GR,if each peer have confered with each others on GR,we call the kind of state is 'grnormal',if negotiation is unsuccessful,the kind of state is 'grnegotiatefail'")
hwBgpGRTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 2))
hwBgpGRRestarterEnterGR = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 2, 1)).setObjects(("HUAWEI-BGP-GR-MIB", "hwBgpGRStatLocalGRRole"))
if mibBuilder.loadTexts: hwBgpGRRestarterEnterGR.setStatus('current')
if mibBuilder.loadTexts: hwBgpGRRestarterEnterGR.setDescription('We will report alarm when the local Router enters the GR state.')
hwBgpGRRestarterExitGR = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 2, 2)).setObjects(("HUAWEI-BGP-GR-MIB", "hwBgpGRStatLocalGRRole"))
if mibBuilder.loadTexts: hwBgpGRRestarterExitGR.setStatus('current')
if mibBuilder.loadTexts: hwBgpGRRestarterExitGR.setDescription('We will recover the hwRestarterEnterGR alarm when the local Router exit the GR state.')
hwBgpGRHelperGRRestartTimeOut = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 2, 3)).setObjects(("HUAWEI-BGP-GR-MIB", "hwBgpGRStatLocalGRRole"))
if mibBuilder.loadTexts: hwBgpGRHelperGRRestartTimeOut.setStatus('current')
if mibBuilder.loadTexts: hwBgpGRHelperGRRestartTimeOut.setDescription('The Restart Timer of Helper is overtime for special reason in process of GR.')
hwBgpGRHelperGRWaitForEndofRibTimeOut = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 2, 4)).setObjects(("HUAWEI-BGP-GR-MIB", "hwBgpGRStatLocalGRRole"))
if mibBuilder.loadTexts: hwBgpGRHelperGRWaitForEndofRibTimeOut.setStatus('current')
if mibBuilder.loadTexts: hwBgpGRHelperGRWaitForEndofRibTimeOut.setDescription('The WaitForEndofRib Timer of Helper is overtime for special reason in process of GR.')
hwBgpGRMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 3))
hwBgpGRMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 3, 1))
hwBgpGRMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 3, 1, 1)).setObjects(("HUAWEI-BGP-GR-MIB", "hwBgpGRCfgGroup"), ("HUAWEI-BGP-GR-MIB", "hwBgpGRStatGroup"), ("HUAWEI-BGP-GR-MIB", "hwBgpGRTrapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwBgpGRMIBCompliance = hwBgpGRMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: hwBgpGRMIBCompliance.setDescription('The compliance statement for Border GateWay Protocol Graceful Restart MIB.')
hwBgpGRMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 3, 2))
hwBgpGRCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 3, 2, 1)).setObjects(("HUAWEI-BGP-GR-MIB", "hwBgpGRRestartTime"), ("HUAWEI-BGP-GR-MIB", "hwBgpGRWaitForRibTime"), ("HUAWEI-BGP-GR-MIB", "hwBgpGRCapability"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwBgpGRCfgGroup = hwBgpGRCfgGroup.setStatus('current')
if mibBuilder.loadTexts: hwBgpGRCfgGroup.setDescription('Required objects to provide hwBgpGRMIB objects configuration information. hwBgpGRCfgGroup is optional.')
hwBgpGRStatGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 3, 2, 2)).setObjects(("HUAWEI-BGP-GR-MIB", "hwBgpGRStatLocalGRRole"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwBgpGRStatGroup = hwBgpGRStatGroup.setStatus('current')
if mibBuilder.loadTexts: hwBgpGRStatGroup.setDescription('Required objects to provide hwBgpGRMIB objects configuration information. hwBgpGRStatGroup is optional.')
hwBgpGRTrapGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 3, 2, 3)).setObjects(("HUAWEI-BGP-GR-MIB", "hwBgpGRRestarterEnterGR"), ("HUAWEI-BGP-GR-MIB", "hwBgpGRRestarterExitGR"), ("HUAWEI-BGP-GR-MIB", "hwBgpGRHelperGRRestartTimeOut"), ("HUAWEI-BGP-GR-MIB", "hwBgpGRHelperGRWaitForEndofRibTimeOut"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwBgpGRTrapGroup = hwBgpGRTrapGroup.setStatus('current')
if mibBuilder.loadTexts: hwBgpGRTrapGroup.setDescription('Objects required for BGP GR Trap.')
mibBuilder.exportSymbols("HUAWEI-BGP-GR-MIB", hwBgpGRStatPeerAddress=hwBgpGRStatPeerAddress, hwBgpGRRestarterEnterGR=hwBgpGRRestarterEnterGR, hwBgpGRCapability=hwBgpGRCapability, hwBgpGRTrap=hwBgpGRTrap, hwBgpGRRestarterExitGR=hwBgpGRRestarterExitGR, hwBgpGRMIB=hwBgpGRMIB, PYSNMP_MODULE_ID=hwBgpGRMIB, hwBgpGRWaitForRibTime=hwBgpGRWaitForRibTime, hwBgpGRStatSubAddressFamily=hwBgpGRStatSubAddressFamily, hwBgpGRStatAddressFamily=hwBgpGRStatAddressFamily, hwBgpGRHelperGRRestartTimeOut=hwBgpGRHelperGRRestartTimeOut, hwBgpGRStatLocalGRRole=hwBgpGRStatLocalGRRole, hwBgpGRMIBConformance=hwBgpGRMIBConformance, Status=Status, hwBgpGRCfgGroup=hwBgpGRCfgGroup, AFIType=AFIType, hwBgpGRHelperGRWaitForEndofRibTimeOut=hwBgpGRHelperGRWaitForEndofRibTimeOut, GRRole=GRRole, hwBgpGRTrapGroup=hwBgpGRTrapGroup, hwBgpGRStatInstanceID=hwBgpGRStatInstanceID, hwBgpGRMIBCompliance=hwBgpGRMIBCompliance, hwBgpGRRestartTime=hwBgpGRRestartTime, hwBgpGRMIBCompliances=hwBgpGRMIBCompliances, hwBgpGRMIBGroups=hwBgpGRMIBGroups, hwBgpGRMIBObjects=hwBgpGRMIBObjects, hwBgpGRStatusInfoEntry=hwBgpGRStatusInfoEntry, hwBgpGRStatusInfoTable=hwBgpGRStatusInfoTable, hwBgpGRStatGroup=hwBgpGRStatGroup, SAFIType=SAFIType)
