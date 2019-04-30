#
# PySNMP MIB module HUAWEI-BGP-GR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-BGP-GR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:31:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
InetAddress, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ModuleIdentity, NotificationType, Integer32, Counter64, Gauge32, IpAddress, Counter32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, Bits, ObjectIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Integer32", "Counter64", "Gauge32", "IpAddress", "Counter32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "Bits", "ObjectIdentity", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hwBgpGRMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138))
if mibBuilder.loadTexts: hwBgpGRMIB.setLastUpdated('200611220000Z')
if mibBuilder.loadTexts: hwBgpGRMIB.setOrganization('Huawei Technologies co.,Ltd.')
class Status(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class AFIType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 25, 196))
    namedValues = NamedValues(("notspecified", 1), ("ipv4", 2), ("ipv6", 3), ("vpls", 25), ("l2vpn", 196))

class SAFIType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 65, 128))
    namedValues = NamedValues(("notspecified", 1), ("unicast", 2), ("multicast", 3), ("unicastandmulticast", 4), ("mpls", 5), ("vpls", 65), ("vpnv4", 128))

class GRRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("grnormal", 1), ("restarter", 2), ("helper", 3), ("grnegotiatefail", 4))

hwBgpGRMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 1))
hwBgpGRCapability = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 1, 1), Status()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwBgpGRCapability.setStatus('current')
hwBgpGRRestartTime = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwBgpGRRestartTime.setStatus('current')
hwBgpGRWaitForRibTime = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 3000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwBgpGRWaitForRibTime.setStatus('current')
hwBgpGRStatusInfoTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 1, 4), )
if mibBuilder.loadTexts: hwBgpGRStatusInfoTable.setStatus('current')
hwBgpGRStatusInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 1, 4, 1), ).setIndexNames((0, "HUAWEI-BGP-GR-MIB", "hwBgpGRStatAddressFamily"), (0, "HUAWEI-BGP-GR-MIB", "hwBgpGRStatSubAddressFamily"), (0, "HUAWEI-BGP-GR-MIB", "hwBgpGRStatInstanceID"), (0, "HUAWEI-BGP-GR-MIB", "hwBgpGRStatPeerAddress"))
if mibBuilder.loadTexts: hwBgpGRStatusInfoEntry.setStatus('current')
hwBgpGRStatAddressFamily = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 1, 4, 1, 1), AFIType())
if mibBuilder.loadTexts: hwBgpGRStatAddressFamily.setStatus('current')
hwBgpGRStatSubAddressFamily = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 1, 4, 1, 2), SAFIType())
if mibBuilder.loadTexts: hwBgpGRStatSubAddressFamily.setStatus('current')
hwBgpGRStatInstanceID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 1, 4, 1, 3), Unsigned32())
if mibBuilder.loadTexts: hwBgpGRStatInstanceID.setStatus('current')
hwBgpGRStatPeerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 1, 4, 1, 4), InetAddress())
if mibBuilder.loadTexts: hwBgpGRStatPeerAddress.setStatus('current')
hwBgpGRStatLocalGRRole = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 1, 4, 1, 5), GRRole()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwBgpGRStatLocalGRRole.setStatus('current')
hwBgpGRTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 2))
hwBgpGRRestarterEnterGR = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 2, 1)).setObjects(("HUAWEI-BGP-GR-MIB", "hwBgpGRStatLocalGRRole"))
if mibBuilder.loadTexts: hwBgpGRRestarterEnterGR.setStatus('current')
hwBgpGRRestarterExitGR = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 2, 2)).setObjects(("HUAWEI-BGP-GR-MIB", "hwBgpGRStatLocalGRRole"))
if mibBuilder.loadTexts: hwBgpGRRestarterExitGR.setStatus('current')
hwBgpGRHelperGRRestartTimeOut = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 2, 3)).setObjects(("HUAWEI-BGP-GR-MIB", "hwBgpGRStatLocalGRRole"))
if mibBuilder.loadTexts: hwBgpGRHelperGRRestartTimeOut.setStatus('current')
hwBgpGRHelperGRWaitForEndofRibTimeOut = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 2, 4)).setObjects(("HUAWEI-BGP-GR-MIB", "hwBgpGRStatLocalGRRole"))
if mibBuilder.loadTexts: hwBgpGRHelperGRWaitForEndofRibTimeOut.setStatus('current')
hwBgpGRMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 3))
hwBgpGRMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 3, 1))
hwBgpGRMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 3, 1, 1)).setObjects(("HUAWEI-BGP-GR-MIB", "hwBgpGRCfgGroup"), ("HUAWEI-BGP-GR-MIB", "hwBgpGRStatGroup"), ("HUAWEI-BGP-GR-MIB", "hwBgpGRTrapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwBgpGRMIBCompliance = hwBgpGRMIBCompliance.setStatus('current')
hwBgpGRMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 3, 2))
hwBgpGRCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 3, 2, 1)).setObjects(("HUAWEI-BGP-GR-MIB", "hwBgpGRRestartTime"), ("HUAWEI-BGP-GR-MIB", "hwBgpGRWaitForRibTime"), ("HUAWEI-BGP-GR-MIB", "hwBgpGRCapability"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwBgpGRCfgGroup = hwBgpGRCfgGroup.setStatus('current')
hwBgpGRStatGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 3, 2, 2)).setObjects(("HUAWEI-BGP-GR-MIB", "hwBgpGRStatLocalGRRole"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwBgpGRStatGroup = hwBgpGRStatGroup.setStatus('current')
hwBgpGRTrapGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 138, 3, 2, 3)).setObjects(("HUAWEI-BGP-GR-MIB", "hwBgpGRRestarterEnterGR"), ("HUAWEI-BGP-GR-MIB", "hwBgpGRRestarterExitGR"), ("HUAWEI-BGP-GR-MIB", "hwBgpGRHelperGRRestartTimeOut"), ("HUAWEI-BGP-GR-MIB", "hwBgpGRHelperGRWaitForEndofRibTimeOut"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwBgpGRTrapGroup = hwBgpGRTrapGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-BGP-GR-MIB", PYSNMP_MODULE_ID=hwBgpGRMIB, hwBgpGRHelperGRRestartTimeOut=hwBgpGRHelperGRRestartTimeOut, hwBgpGRTrap=hwBgpGRTrap, hwBgpGRRestarterExitGR=hwBgpGRRestarterExitGR, hwBgpGRHelperGRWaitForEndofRibTimeOut=hwBgpGRHelperGRWaitForEndofRibTimeOut, hwBgpGRStatusInfoTable=hwBgpGRStatusInfoTable, hwBgpGRMIBObjects=hwBgpGRMIBObjects, hwBgpGRMIBCompliance=hwBgpGRMIBCompliance, hwBgpGRCfgGroup=hwBgpGRCfgGroup, hwBgpGRStatAddressFamily=hwBgpGRStatAddressFamily, hwBgpGRMIBGroups=hwBgpGRMIBGroups, hwBgpGRStatSubAddressFamily=hwBgpGRStatSubAddressFamily, hwBgpGRStatGroup=hwBgpGRStatGroup, hwBgpGRStatPeerAddress=hwBgpGRStatPeerAddress, Status=Status, hwBgpGRStatLocalGRRole=hwBgpGRStatLocalGRRole, hwBgpGRTrapGroup=hwBgpGRTrapGroup, hwBgpGRStatusInfoEntry=hwBgpGRStatusInfoEntry, AFIType=AFIType, hwBgpGRMIBConformance=hwBgpGRMIBConformance, hwBgpGRMIBCompliances=hwBgpGRMIBCompliances, hwBgpGRCapability=hwBgpGRCapability, hwBgpGRMIB=hwBgpGRMIB, hwBgpGRRestartTime=hwBgpGRRestartTime, hwBgpGRWaitForRibTime=hwBgpGRWaitForRibTime, hwBgpGRRestarterEnterGR=hwBgpGRRestarterEnterGR, GRRole=GRRole, hwBgpGRStatInstanceID=hwBgpGRStatInstanceID, SAFIType=SAFIType)
