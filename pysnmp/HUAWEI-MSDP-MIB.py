#
# PySNMP MIB module HUAWEI-MSDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-MSDP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:35:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
msdpPeerRemoteAddress, msdpPeerState, msdpPeerFsmEstablishedTransitions = mibBuilder.importSymbols("MSDP-MIB", "msdpPeerRemoteAddress", "msdpPeerState", "msdpPeerFsmEstablishedTransitions")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Gauge32, IpAddress, ObjectIdentity, Counter32, MibIdentifier, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ModuleIdentity, Unsigned32, NotificationType, Integer32, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "IpAddress", "ObjectIdentity", "Counter32", "MibIdentifier", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ModuleIdentity", "Unsigned32", "NotificationType", "Integer32", "TimeTicks", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hwMsdpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 218))
hwMsdpMIB.setRevisions(('2015-02-05 00:00', '2009-10-31 00:00',))
if mibBuilder.loadTexts: hwMsdpMIB.setLastUpdated('201502050000Z')
if mibBuilder.loadTexts: hwMsdpMIB.setOrganization('Huawei Technologies Co.,Ltd.')
hwMsdpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1))
hwMsdp = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1))
hwMsdpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 1))
hwMsdpTrapsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 2))
hwMsdpInstanceID = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 2, 1), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwMsdpInstanceID.setStatus('current')
hwMsdpInstanceName = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 2, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwMsdpInstanceName.setStatus('current')
hwMsdpNotificationReason = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 100))).clone(namedValues=NamedValues(("holdTimerExpired", 1), ("tcpNotEstablish", 2), ("sockerError", 3), ("receiveInvalidTLV", 4), ("receiveNotificationTLV", 5), ("userOperation", 6), ("peerUpAgain", 7), ("deletePeer", 8), ("alarmTimeout", 9), ("alarmClear", 100)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwMsdpNotificationReason.setStatus('current')
hwMsdpTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 3))
hwMsdpNeighborUnavailable = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 3, 1)).setObjects(("HUAWEI-MSDP-MIB", "hwMsdpInstanceID"), ("HUAWEI-MSDP-MIB", "hwMsdpInstanceName"), ("MSDP-MIB", "msdpPeerState"), ("HUAWEI-MSDP-MIB", "hwMsdpNotificationReason"))
if mibBuilder.loadTexts: hwMsdpNeighborUnavailable.setStatus('current')
hwMsdpNeighborUnvailableClear = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 3, 2)).setObjects(("HUAWEI-MSDP-MIB", "hwMsdpInstanceID"), ("HUAWEI-MSDP-MIB", "hwMsdpInstanceName"), ("MSDP-MIB", "msdpPeerState"), ("HUAWEI-MSDP-MIB", "hwMsdpNotificationReason"))
if mibBuilder.loadTexts: hwMsdpNeighborUnvailableClear.setStatus('current')
hwMsdpMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 4))
hwMsdpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 4, 1))
hwMsdpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 4, 1, 1)).setObjects()

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwMsdpMIBCompliance = hwMsdpMIBCompliance.setStatus('deprecated')
hwMsdpMIBFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 4, 1, 2)).setObjects(("HUAWEI-MSDP-MIB", "hwMsdpMIBPeerGroup"), ("HUAWEI-MSDP-MIB", "hwMsdpMIBNotificationGroup"), ("HUAWEI-MSDP-MIB", "hwMsdpMIBPeerGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwMsdpMIBFullCompliance = hwMsdpMIBFullCompliance.setStatus('current')
hwMsdpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 4, 2))
hwMsdpMIBPeerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 4, 2, 1)).setObjects(("HUAWEI-MSDP-MIB", "hwMsdpNotificationReason"), ("HUAWEI-MSDP-MIB", "hwMsdpInstanceName"), ("HUAWEI-MSDP-MIB", "hwMsdpInstanceID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwMsdpMIBPeerGroup = hwMsdpMIBPeerGroup.setStatus('current')
hwMsdpMIBNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 218, 1, 1, 4, 2, 2)).setObjects(("HUAWEI-MSDP-MIB", "hwMsdpNeighborUnavailable"), ("HUAWEI-MSDP-MIB", "hwMsdpNeighborUnvailableClear"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwMsdpMIBNotificationGroup = hwMsdpMIBNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-MSDP-MIB", hwMsdp=hwMsdp, hwMsdpObjects=hwMsdpObjects, hwMsdpNotificationReason=hwMsdpNotificationReason, hwMsdpMIBNotificationGroup=hwMsdpMIBNotificationGroup, hwMsdpNeighborUnvailableClear=hwMsdpNeighborUnvailableClear, hwMsdpMIBFullCompliance=hwMsdpMIBFullCompliance, hwMsdpMIBConformance=hwMsdpMIBConformance, hwMsdpMIBGroups=hwMsdpMIBGroups, hwMsdpMIBCompliances=hwMsdpMIBCompliances, hwMsdpInstanceName=hwMsdpInstanceName, hwMsdpNeighborUnavailable=hwMsdpNeighborUnavailable, hwMsdpMIBCompliance=hwMsdpMIBCompliance, hwMsdpTraps=hwMsdpTraps, hwMsdpMIBPeerGroup=hwMsdpMIBPeerGroup, PYSNMP_MODULE_ID=hwMsdpMIB, hwMsdpTrapsObjects=hwMsdpTrapsObjects, hwMsdpInstanceID=hwMsdpInstanceID, hwMsdpMIBObjects=hwMsdpMIBObjects, hwMsdpMIB=hwMsdpMIB)
