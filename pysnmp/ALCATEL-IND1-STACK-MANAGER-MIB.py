#
# PySNMP MIB module ALCATEL-IND1-STACK-MANAGER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALCATEL-IND1-STACK-MANAGER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:03:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
softentIND1StackMgr, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "softentIND1StackMgr")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, ModuleIdentity, MibIdentifier, ObjectIdentity, iso, TimeTicks, Bits, NotificationType, Counter64, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "iso", "TimeTicks", "Bits", "NotificationType", "Counter64", "Gauge32", "Counter32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
alcatelIND1StackMgrMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1))
alcatelIND1StackMgrMIB.setRevisions(('2009-02-06 00:00', '2007-04-03 00:00', '2005-07-15 00:00', '2004-07-01 00:00', '2004-04-23 00:00', '2004-04-08 00:00', '2004-04-04 00:00', '2004-03-22 00:00', '2004-03-08 00:00', '2001-08-27 00:00',))
if mibBuilder.loadTexts: alcatelIND1StackMgrMIB.setLastUpdated('200902060000Z')
if mibBuilder.loadTexts: alcatelIND1StackMgrMIB.setOrganization('Alcatel-Lucent')
alcatelIND1StackMgrMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1))
alcatelIND1StackMgrMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 2))
alcatelIND1StackMgrTrapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 3))
alaStackMgrTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 4))
class AlaStackMgrLinkNumber(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(27, 28, 51, 52, 31, 32, 25, 26, 29, 30, 1, 2))
    namedValues = NamedValues(("linkA27", 27), ("linkB28", 28), ("linkA51", 51), ("linkB52", 52), ("linkA31", 31), ("linkB32", 32), ("linkA25", 25), ("linkB26", 26), ("linkA29", 29), ("linkB30", 30), ("linkA", 1), ("linkB", 2))

class AlaStackMgrNINumber(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 1008)

class AlaStackMgrLinkStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class AlaStackMgrSlotRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("unassigned", 0), ("primary", 1), ("secondary", 2), ("idle", 3), ("standalone", 4), ("passthrough", 5))

class AlaStackMgrStackStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("loop", 1), ("noloop", 2))

class AlaStackMgrSlotState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("running", 1), ("duplicateSlot", 2), ("clearedSlot", 3), ("outOfSlots", 4), ("outOfTokens", 5), ("badMix", 6))

class AlaStackMgrCommandAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("notSignificant", 0), ("clearSlot", 1), ("clearSlotImmediately", 2), ("reloadAny", 3), ("reloadPassThru", 4))

class AlaStackMgrCommandStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("notSignificant", 0), ("clearSlotInProgress", 1), ("clearSlotFailed", 2), ("clearSlotSuccess", 3), ("setSlotInProgress", 4), ("setSlotFailed", 5), ("setSlotSuccess", 6))

class AlaStackMgrStackingMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("stackable", 1), ("standalone", 2))

alaStackMgrChassisTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1), )
if mibBuilder.loadTexts: alaStackMgrChassisTable.setStatus('current')
alaStackMgrChassisEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1), ).setIndexNames((0, "ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSlotNINumber"))
if mibBuilder.loadTexts: alaStackMgrChassisEntry.setStatus('current')
alaStackMgrSlotNINumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 1), AlaStackMgrNINumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrSlotNINumber.setStatus('current')
alaStackMgrSlotCMMNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 72))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrSlotCMMNumber.setStatus('current')
alaStackMgrChasRole = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 3), AlaStackMgrSlotRole()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrChasRole.setStatus('current')
alaStackMgrLocalLinkStateA = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 4), AlaStackMgrLinkStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrLocalLinkStateA.setStatus('current')
alaStackMgrRemoteNISlotA = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 5), AlaStackMgrNINumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrRemoteNISlotA.setStatus('current')
alaStackMgrRemoteLinkA = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 6), AlaStackMgrLinkNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrRemoteLinkA.setStatus('current')
alaStackMgrLocalLinkStateB = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 7), AlaStackMgrLinkStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrLocalLinkStateB.setStatus('current')
alaStackMgrRemoteNISlotB = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 8), AlaStackMgrNINumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrRemoteNISlotB.setStatus('current')
alaStackMgrRemoteLinkB = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 9), AlaStackMgrLinkNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrRemoteLinkB.setStatus('current')
alaStackMgrChasState = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 10), AlaStackMgrSlotState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrChasState.setStatus('current')
alaStackMgrSavedSlotNINumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 11), AlaStackMgrNINumber()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaStackMgrSavedSlotNINumber.setStatus('current')
alaStackMgrCommandAction = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 12), AlaStackMgrCommandAction()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaStackMgrCommandAction.setStatus('current')
alaStackMgrCommandStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 13), AlaStackMgrCommandStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrCommandStatus.setStatus('current')
alaStackMgrOperStackingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 14), AlaStackMgrStackingMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrOperStackingMode.setStatus('current')
alaStackMgrAdminStackingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 15), AlaStackMgrStackingMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaStackMgrAdminStackingMode.setStatus('current')
alaStackMgrStatsTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 2), )
if mibBuilder.loadTexts: alaStackMgrStatsTable.setStatus('current')
alaStackMgrStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 2, 1), ).setIndexNames((0, "ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSlotNINumber"), (0, "ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrStatLinkNumber"))
if mibBuilder.loadTexts: alaStackMgrStatsEntry.setStatus('current')
alaStackMgrStatLinkNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 2, 1, 1), AlaStackMgrLinkNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrStatLinkNumber.setStatus('current')
alaStackMgrStatPktsRx = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrStatPktsRx.setStatus('current')
alaStackMgrStatPktsTx = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrStatPktsTx.setStatus('current')
alaStackMgrStatErrorsRx = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrStatErrorsRx.setStatus('current')
alaStackMgrStatErrorsTx = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrStatErrorsTx.setStatus('current')
alaStackMgrStatDelayFromLastMsg = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrStatDelayFromLastMsg.setStatus('current')
alaStackMgrStackStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 3), AlaStackMgrStackStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrStackStatus.setStatus('current')
alaStackMgrTokensUsed = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrTokensUsed.setStatus('current')
alaStackMgrTokensAvailable = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrTokensAvailable.setStatus('current')
alaStackMgrStaticRouteTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 6), )
if mibBuilder.loadTexts: alaStackMgrStaticRouteTable.setStatus('current')
alaStackMgrStaticRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 6, 1), ).setIndexNames((0, "ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrStaticRouteSrcStartIf"), (0, "ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrStaticRouteSrcEndIf"), (0, "ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrStaticRouteDstStartIf"), (0, "ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrStaticRouteDstEndIf"))
if mibBuilder.loadTexts: alaStackMgrStaticRouteEntry.setStatus('current')
alaStackMgrStaticRouteSrcStartIf = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 6, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: alaStackMgrStaticRouteSrcStartIf.setStatus('current')
alaStackMgrStaticRouteSrcEndIf = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 6, 1, 2), InterfaceIndex())
if mibBuilder.loadTexts: alaStackMgrStaticRouteSrcEndIf.setStatus('current')
alaStackMgrStaticRouteDstStartIf = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 6, 1, 3), InterfaceIndex())
if mibBuilder.loadTexts: alaStackMgrStaticRouteDstStartIf.setStatus('current')
alaStackMgrStaticRouteDstEndIf = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 6, 1, 4), InterfaceIndex())
if mibBuilder.loadTexts: alaStackMgrStaticRouteDstEndIf.setStatus('current')
alaStackMgrStaticRoutePort = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 6, 1, 5), AlaStackMgrLinkNumber().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaStackMgrStaticRoutePort.setStatus('current')
alaStackMgrStaticRoutePortState = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 6, 1, 6), AlaStackMgrLinkStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrStaticRoutePortState.setStatus('current')
alaStackMgrStaticRouteStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 6, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2))).clone('on')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaStackMgrStaticRouteStatus.setStatus('current')
alaStackMgrStaticRouteRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 6, 1, 8), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaStackMgrStaticRouteRowStatus.setStatus('current')
alaStackMgrTrapLinkNumber = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 3, 1), AlaStackMgrLinkNumber()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alaStackMgrTrapLinkNumber.setStatus('current')
alaStackMgrPrimary = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 3, 2), AlaStackMgrNINumber()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alaStackMgrPrimary.setStatus('current')
alaStackMgrSecondary = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 3, 3), AlaStackMgrNINumber()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alaStackMgrSecondary.setStatus('current')
alaStackMgrDuplicateSlotTrap = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 4, 0, 1)).setObjects(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSlotNINumber"))
if mibBuilder.loadTexts: alaStackMgrDuplicateSlotTrap.setStatus('current')
alaStackMgrNeighborChangeTrap = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 4, 0, 2)).setObjects(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrStackStatus"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSlotNINumber"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrTrapLinkNumber"))
if mibBuilder.loadTexts: alaStackMgrNeighborChangeTrap.setStatus('current')
alaStackMgrRoleChangeTrap = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 4, 0, 3)).setObjects(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrPrimary"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSecondary"))
if mibBuilder.loadTexts: alaStackMgrRoleChangeTrap.setStatus('current')
alaStackMgrDuplicateRoleTrap = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 4, 0, 4)).setObjects(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSlotNINumber"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrChasRole"))
if mibBuilder.loadTexts: alaStackMgrDuplicateRoleTrap.setStatus('current')
alaStackMgrClearedSlotTrap = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 4, 0, 5)).setObjects(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSlotNINumber"))
if mibBuilder.loadTexts: alaStackMgrClearedSlotTrap.setStatus('current')
alaStackMgrOutOfSlotsTrap = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 4, 0, 6))
if mibBuilder.loadTexts: alaStackMgrOutOfSlotsTrap.setStatus('current')
alaStackMgrOutOfTokensTrap = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 4, 0, 7)).setObjects(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSlotNINumber"))
if mibBuilder.loadTexts: alaStackMgrOutOfTokensTrap.setStatus('current')
alaStackMgrOutOfPassThruSlotsTrap = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 4, 0, 8))
if mibBuilder.loadTexts: alaStackMgrOutOfPassThruSlotsTrap.setStatus('current')
alaStackMgrBadMixTrap = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 4, 0, 9)).setObjects(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSlotNINumber"))
if mibBuilder.loadTexts: alaStackMgrBadMixTrap.setStatus('current')
alcatelIND1StackMgrMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 2, 1))
alcatelIND1StackMgrMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 2, 2))
alaStackMgrCfgMgrGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSlotNINumber"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSlotCMMNumber"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrChasRole"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrLocalLinkStateA"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrRemoteNISlotA"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrRemoteLinkA"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrLocalLinkStateB"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrRemoteNISlotB"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrRemoteLinkB"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrChasState"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSavedSlotNINumber"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrCommandAction"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrCommandStatus"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrOperStackingMode"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrAdminStackingMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaStackMgrCfgMgrGroup = alaStackMgrCfgMgrGroup.setStatus('current')
alaStackMgrNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 2, 1, 2)).setObjects(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrDuplicateSlotTrap"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrNeighborChangeTrap"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrRoleChangeTrap"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrDuplicateRoleTrap"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrClearedSlotTrap"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrOutOfSlotsTrap"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrOutOfTokensTrap"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrOutOfPassThruSlotsTrap"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrBadMixTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaStackMgrNotificationGroup = alaStackMgrNotificationGroup.setStatus('current')
alcatelIND1StackMgrMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrCfgMgrGroup"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alcatelIND1StackMgrMIBCompliance = alcatelIND1StackMgrMIBCompliance.setStatus('current')
mibBuilder.exportSymbols("ALCATEL-IND1-STACK-MANAGER-MIB", alaStackMgrStaticRoutePortState=alaStackMgrStaticRoutePortState, AlaStackMgrCommandStatus=AlaStackMgrCommandStatus, alaStackMgrChassisEntry=alaStackMgrChassisEntry, alaStackMgrRemoteNISlotA=alaStackMgrRemoteNISlotA, alaStackMgrSecondary=alaStackMgrSecondary, AlaStackMgrSlotState=AlaStackMgrSlotState, alaStackMgrStatsTable=alaStackMgrStatsTable, alaStackMgrTokensUsed=alaStackMgrTokensUsed, alaStackMgrTokensAvailable=alaStackMgrTokensAvailable, alaStackMgrStatPktsTx=alaStackMgrStatPktsTx, alaStackMgrStaticRouteEntry=alaStackMgrStaticRouteEntry, alaStackMgrNotificationGroup=alaStackMgrNotificationGroup, alaStackMgrStaticRouteSrcStartIf=alaStackMgrStaticRouteSrcStartIf, alcatelIND1StackMgrMIBConformance=alcatelIND1StackMgrMIBConformance, AlaStackMgrCommandAction=AlaStackMgrCommandAction, alaStackMgrOutOfTokensTrap=alaStackMgrOutOfTokensTrap, alcatelIND1StackMgrMIBObjects=alcatelIND1StackMgrMIBObjects, alaStackMgrSavedSlotNINumber=alaStackMgrSavedSlotNINumber, alaStackMgrDuplicateSlotTrap=alaStackMgrDuplicateSlotTrap, AlaStackMgrLinkNumber=AlaStackMgrLinkNumber, AlaStackMgrStackingMode=AlaStackMgrStackingMode, alaStackMgrCommandStatus=alaStackMgrCommandStatus, alaStackMgrCommandAction=alaStackMgrCommandAction, alaStackMgrClearedSlotTrap=alaStackMgrClearedSlotTrap, alaStackMgrAdminStackingMode=alaStackMgrAdminStackingMode, alaStackMgrStaticRouteTable=alaStackMgrStaticRouteTable, alaStackMgrStaticRoutePort=alaStackMgrStaticRoutePort, alaStackMgrNeighborChangeTrap=alaStackMgrNeighborChangeTrap, alaStackMgrTrapLinkNumber=alaStackMgrTrapLinkNumber, alaStackMgrDuplicateRoleTrap=alaStackMgrDuplicateRoleTrap, AlaStackMgrNINumber=AlaStackMgrNINumber, alaStackMgrOperStackingMode=alaStackMgrOperStackingMode, AlaStackMgrLinkStatus=AlaStackMgrLinkStatus, alaStackMgrSlotNINumber=alaStackMgrSlotNINumber, alaStackMgrChasRole=alaStackMgrChasRole, alcatelIND1StackMgrMIB=alcatelIND1StackMgrMIB, alcatelIND1StackMgrMIBCompliances=alcatelIND1StackMgrMIBCompliances, alaStackMgrPrimary=alaStackMgrPrimary, alaStackMgrSlotCMMNumber=alaStackMgrSlotCMMNumber, alaStackMgrOutOfPassThruSlotsTrap=alaStackMgrOutOfPassThruSlotsTrap, alaStackMgrOutOfSlotsTrap=alaStackMgrOutOfSlotsTrap, alaStackMgrRemoteNISlotB=alaStackMgrRemoteNISlotB, alaStackMgrStackStatus=alaStackMgrStackStatus, alaStackMgrStatErrorsRx=alaStackMgrStatErrorsRx, alaStackMgrStaticRouteRowStatus=alaStackMgrStaticRouteRowStatus, alaStackMgrStatLinkNumber=alaStackMgrStatLinkNumber, alaStackMgrCfgMgrGroup=alaStackMgrCfgMgrGroup, alcatelIND1StackMgrMIBGroups=alcatelIND1StackMgrMIBGroups, alaStackMgrStaticRouteDstEndIf=alaStackMgrStaticRouteDstEndIf, alaStackMgrChasState=alaStackMgrChasState, alaStackMgrLocalLinkStateB=alaStackMgrLocalLinkStateB, alaStackMgrStatsEntry=alaStackMgrStatsEntry, alaStackMgrRoleChangeTrap=alaStackMgrRoleChangeTrap, alcatelIND1StackMgrTrapObjects=alcatelIND1StackMgrTrapObjects, alaStackMgrChassisTable=alaStackMgrChassisTable, alcatelIND1StackMgrMIBCompliance=alcatelIND1StackMgrMIBCompliance, alaStackMgrStaticRouteSrcEndIf=alaStackMgrStaticRouteSrcEndIf, alaStackMgrLocalLinkStateA=alaStackMgrLocalLinkStateA, alaStackMgrStatDelayFromLastMsg=alaStackMgrStatDelayFromLastMsg, AlaStackMgrStackStatus=AlaStackMgrStackStatus, PYSNMP_MODULE_ID=alcatelIND1StackMgrMIB, alaStackMgrStaticRouteDstStartIf=alaStackMgrStaticRouteDstStartIf, alaStackMgrRemoteLinkA=alaStackMgrRemoteLinkA, alaStackMgrStatPktsRx=alaStackMgrStatPktsRx, alaStackMgrBadMixTrap=alaStackMgrBadMixTrap, alaStackMgrStatErrorsTx=alaStackMgrStatErrorsTx, alaStackMgrStaticRouteStatus=alaStackMgrStaticRouteStatus, AlaStackMgrSlotRole=AlaStackMgrSlotRole, alaStackMgrTraps=alaStackMgrTraps, alaStackMgrRemoteLinkB=alaStackMgrRemoteLinkB)
