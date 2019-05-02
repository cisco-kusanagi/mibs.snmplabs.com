#
# PySNMP MIB module HUAWEI-MSDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-MSDP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:47:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
msdpPeerRemoteAddress, msdpPeerState, msdpPeerFsmEstablishedTransitions = mibBuilder.importSymbols("MSDP-MIB", "msdpPeerRemoteAddress", "msdpPeerState", "msdpPeerFsmEstablishedTransitions")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, TimeTicks, ObjectIdentity, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, Counter32, MibIdentifier, Integer32, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "Counter32", "MibIdentifier", "Integer32", "Counter64", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hwMsdpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 218))
hwMsdpMIB.setRevisions(('2015-02-05 00:00', '2009-10-31 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hwMsdpMIB.setRevisionsDescriptions(('Delete hwPimTuningParametersGroup from hwMsdpMIBFullCompliance.', 'The initial revision of this Mib module.',))
if mibBuilder.loadTexts: hwMsdpMIB.setLastUpdated('201502050000Z')
if mibBuilder.loadTexts: hwMsdpMIB.setOrganization('Huawei Technologies Co.,Ltd.')
if mibBuilder.loadTexts: hwMsdpMIB.setContactInfo("Huawei Industrial Base Bantian, Longgang Shenzhen 518129 People's Republic of China Website: http://www.huawei.com Email: support@huawei.com ")
if mibBuilder.loadTexts: hwMsdpMIB.setDescription('The MIB module for management of PIM routers. Huawei Technologies co.,Ltd . Supplementary information may be available at: http://www.huawei.com')
hwMsdpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1))
hwMsdp = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1))
hwMsdpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 1))
hwMsdpTrapsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 2))
hwMsdpInstanceID = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 2, 1), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwMsdpInstanceID.setStatus('current')
if mibBuilder.loadTexts: hwMsdpInstanceID.setDescription('The instance ID of the trap.')
hwMsdpInstanceName = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 2, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwMsdpInstanceName.setStatus('current')
if mibBuilder.loadTexts: hwMsdpInstanceName.setDescription('The instance name of the trap.')
hwMsdpNotificationReason = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 100))).clone(namedValues=NamedValues(("holdTimerExpired", 1), ("tcpNotEstablish", 2), ("sockerError", 3), ("receiveInvalidTLV", 4), ("receiveNotificationTLV", 5), ("userOperation", 6), ("peerUpAgain", 7), ("deletePeer", 8), ("alarmTimeout", 9), ("alarmClear", 100)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwMsdpNotificationReason.setStatus('current')
if mibBuilder.loadTexts: hwMsdpNotificationReason.setDescription('The reason for trap sending. 1.HoldTime expired 2.TCP not establish 3.Socket error 4.Receive invalid TLV 5.Receive notification TLV 6.User operation 7.Peer Up again 8.Delete peer 9.Alarm timeout 100.Alarm Clear')
hwMsdpTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 3))
hwMsdpNeighborUnavailable = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 3, 1)).setObjects(("HUAWEI-MSDP-MIB", "hwMsdpInstanceID"), ("HUAWEI-MSDP-MIB", "hwMsdpInstanceName"), ("MSDP-MIB", "msdpPeerState"), ("HUAWEI-MSDP-MIB", "hwMsdpNotificationReason"))
if mibBuilder.loadTexts: hwMsdpNeighborUnavailable.setStatus('current')
if mibBuilder.loadTexts: hwMsdpNeighborUnavailable.setDescription('A hwMsdpNeighborUnavailable notification signifies that the MSDP peer is unavailable.')
hwMsdpNeighborUnvailableClear = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 3, 2)).setObjects(("HUAWEI-MSDP-MIB", "hwMsdpInstanceID"), ("HUAWEI-MSDP-MIB", "hwMsdpInstanceName"), ("MSDP-MIB", "msdpPeerState"), ("HUAWEI-MSDP-MIB", "hwMsdpNotificationReason"))
if mibBuilder.loadTexts: hwMsdpNeighborUnvailableClear.setStatus('current')
if mibBuilder.loadTexts: hwMsdpNeighborUnvailableClear.setDescription('A hwMsdpNeighborUnvailableClear notification signifies that the MSDP peer is available.')
hwMsdpMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 4))
hwMsdpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 4, 1))
hwMsdpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 4, 1, 1)).setObjects()

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwMsdpMIBCompliance = hwMsdpMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: hwMsdpMIBCompliance.setDescription('Description.')
hwMsdpMIBFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 4, 1, 2)).setObjects(("HUAWEI-MSDP-MIB", "hwMsdpMIBPeerGroup"), ("HUAWEI-MSDP-MIB", "hwMsdpMIBNotificationGroup"), ("HUAWEI-MSDP-MIB", "hwMsdpMIBPeerGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwMsdpMIBFullCompliance = hwMsdpMIBFullCompliance.setStatus('current')
if mibBuilder.loadTexts: hwMsdpMIBFullCompliance.setDescription('The compliance statement for HUAWEI-MSDP MIB.')
hwMsdpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 4, 2))
hwMsdpMIBPeerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 4, 2, 1)).setObjects(("HUAWEI-MSDP-MIB", "hwMsdpNotificationReason"), ("HUAWEI-MSDP-MIB", "hwMsdpInstanceName"), ("HUAWEI-MSDP-MIB", "hwMsdpInstanceID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwMsdpMIBPeerGroup = hwMsdpMIBPeerGroup.setStatus('current')
if mibBuilder.loadTexts: hwMsdpMIBPeerGroup.setDescription('Description.')
hwMsdpMIBNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 4, 2, 2)).setObjects(("HUAWEI-MSDP-MIB", "hwMsdpNeighborUnavailable"), ("HUAWEI-MSDP-MIB", "hwMsdpNeighborUnvailableClear"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwMsdpMIBNotificationGroup = hwMsdpMIBNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: hwMsdpMIBNotificationGroup.setDescription('Description.')
mibBuilder.exportSymbols("HUAWEI-MSDP-MIB", hwMsdpObjects=hwMsdpObjects, hwMsdpInstanceID=hwMsdpInstanceID, hwMsdpTraps=hwMsdpTraps, hwMsdpNeighborUnavailable=hwMsdpNeighborUnavailable, hwMsdpMIBNotificationGroup=hwMsdpMIBNotificationGroup, hwMsdpMIBCompliances=hwMsdpMIBCompliances, hwMsdpNeighborUnvailableClear=hwMsdpNeighborUnvailableClear, hwMsdpMIBGroups=hwMsdpMIBGroups, hwMsdpMIB=hwMsdpMIB, hwMsdpMIBObjects=hwMsdpMIBObjects, hwMsdpInstanceName=hwMsdpInstanceName, hwMsdp=hwMsdp, hwMsdpMIBCompliance=hwMsdpMIBCompliance, hwMsdpTrapsObjects=hwMsdpTrapsObjects, PYSNMP_MODULE_ID=hwMsdpMIB, hwMsdpMIBConformance=hwMsdpMIBConformance, hwMsdpMIBFullCompliance=hwMsdpMIBFullCompliance, hwMsdpNotificationReason=hwMsdpNotificationReason, hwMsdpMIBPeerGroup=hwMsdpMIBPeerGroup)
