#
# PySNMP MIB module CISCO-IF-EXTENSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IF-EXTENSION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:37:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
IfOperStatusReason, = mibBuilder.importSymbols("CISCO-TC", "IfOperStatusReason")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ifType, InterfaceIndexOrZero, ifAdminStatus, ifName, ifIndex, ifOperStatus = mibBuilder.importSymbols("IF-MIB", "ifType", "InterfaceIndexOrZero", "ifAdminStatus", "ifName", "ifIndex", "ifOperStatus")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Integer32, Counter64, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ObjectIdentity, Gauge32, IpAddress, Counter32, MibIdentifier, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "ObjectIdentity", "Gauge32", "IpAddress", "Counter32", "MibIdentifier", "iso", "Bits")
TimeStamp, TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "TruthValue", "DisplayString", "TextualConvention")
ciscoIfExtensionMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 276))
ciscoIfExtensionMIB.setRevisions(('2013-03-13 00:00', '2012-09-05 00:00', '2011-06-27 00:00', '2009-02-26 00:00', '2008-12-09 00:00', '2008-10-06 00:00', '2008-07-31 00:00', '2008-07-08 00:00', '2008-06-23 00:00', '2007-07-23 00:00', '2006-11-01 00:00', '2005-04-28 00:00', '2005-01-25 00:00', '2004-09-08 00:00', '2003-11-14 00:00', '2003-08-12 00:00', '2003-07-17 00:00', '2003-06-25 00:00', '2002-10-12 00:00', '2002-07-24 00:00',))
if mibBuilder.loadTexts: ciscoIfExtensionMIB.setLastUpdated('201303130000Z')
if mibBuilder.loadTexts: ciscoIfExtensionMIB.setOrganization('Cisco Systems, Inc.')
ciscoIfExtensionMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 276, 0))
ciscoIfExtensionMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 276, 1))
ciscoIfExtensionMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 276, 2))
ciscoIfExtensionStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1))
ciscoIfExtSystemConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 2))
ciscoIfExtDot1qCustomEtherType = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 3))
ciscoIfExtUtilization = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 4))
ciscoIfExtDot1dBaseMapping = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 5))
ciscoIfExtIfNameMapping = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 6))
class InterfaceIndexList(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class InterfaceOperModeList(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class InterfaceOperCauseList(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 128)

class InterfaceOwnershipList(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 8)

class IfIndexPersistenceState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("disable", 1), ("enable", 2), ("global", 3))

cieIfPacketStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 1), )
if mibBuilder.loadTexts: cieIfPacketStatsTable.setStatus('current')
cieIfPacketStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cieIfPacketStatsEntry.setStatus('current')
cieIfLastInTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 1, 1, 1), Gauge32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cieIfLastInTime.setStatus('current')
cieIfLastOutTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 1, 1, 2), Gauge32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cieIfLastOutTime.setStatus('current')
cieIfLastOutHangTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 1, 1, 3), Gauge32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cieIfLastOutHangTime.setStatus('current')
cieIfInRuntsErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieIfInRuntsErrs.setStatus('current')
cieIfInGiantsErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieIfInGiantsErrs.setStatus('current')
cieIfInFramingErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieIfInFramingErrs.setStatus('current')
cieIfInOverrunErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieIfInOverrunErrs.setStatus('current')
cieIfInIgnored = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieIfInIgnored.setStatus('current')
cieIfInAbortErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieIfInAbortErrs.setStatus('current')
cieIfInputQueueDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieIfInputQueueDrops.setStatus('current')
cieIfOutputQueueDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieIfOutputQueueDrops.setStatus('current')
cieIfPacketDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 1, 1, 12), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieIfPacketDiscontinuityTime.setStatus('current')
cieIfInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 2), )
if mibBuilder.loadTexts: cieIfInterfaceTable.setStatus('current')
cieIfInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cieIfInterfaceEntry.setStatus('current')
cieIfResetCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieIfResetCount.setStatus('current')
cieIfKeepAliveEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 2, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cieIfKeepAliveEnabled.setStatus('current')
cieIfStateChangeReason = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 2, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieIfStateChangeReason.setStatus('current')
cieIfCarrierTransitionCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieIfCarrierTransitionCount.setStatus('current')
cieIfInterfaceDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 2, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieIfInterfaceDiscontinuityTime.setStatus('current')
cieIfDhcpMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 2, 1, 6), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cieIfDhcpMode.setStatus('current')
cieIfMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(40, 2147483647)).clone(1500)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cieIfMtu.setStatus('current')
cieIfContextName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 2, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieIfContextName.setStatus('current')
cieIfOperStatusCause = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 2, 1, 9), IfOperStatusReason()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieIfOperStatusCause.setStatus('current')
cieIfOperStatusCauseDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 2, 1, 10), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieIfOperStatusCauseDescr.setStatus('current')
cieIfSpeedReceive = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 2, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieIfSpeedReceive.setStatus('current')
cieIfHighSpeedReceive = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 2, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieIfHighSpeedReceive.setStatus('current')
cieIfOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 2, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cieIfOwner.setStatus('current')
cieIfSharedConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("notApplicable", 1), ("ownerDedicated", 2), ("ownerShared", 3), ("sharedOnly", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieIfSharedConfig.setStatus('current')
cieIfSpeedGroupConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("notApplicable", 1), ("tenG", 2), ("oneTwoFourEightG", 3), ("twoFourEightSixteenG", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cieIfSpeedGroupConfig.setStatus('current')
cieIfTransceiverFrequencyConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notApplicable", 1), ("fibreChannel", 2), ("ethernet", 3))).clone('fibreChannel')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cieIfTransceiverFrequencyConfig.setStatus('current')
cieIfFillPatternConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 2, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("arbff8G", 1), ("idle8G", 2))).clone('arbff8G')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cieIfFillPatternConfig.setStatus('current')
cieIfIgnoreBitErrorsConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 2, 1, 18), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cieIfIgnoreBitErrorsConfig.setStatus('current')
cieIfIgnoreInterruptThresholdConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 2, 1, 19), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cieIfIgnoreInterruptThresholdConfig.setStatus('current')
cieIfStatusListTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 3), )
if mibBuilder.loadTexts: cieIfStatusListTable.setStatus('current')
cieIfStatusListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 3, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-IF-EXTENSION-MIB", "cieIfStatusListIndex"))
if mibBuilder.loadTexts: cieIfStatusListEntry.setStatus('current')
cieIfStatusListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 33554432)))
if mibBuilder.loadTexts: cieIfStatusListIndex.setStatus('current')
cieInterfacesIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 3, 1, 2), InterfaceIndexList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieInterfacesIndex.setStatus('current')
cieInterfacesOperMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 3, 1, 3), InterfaceOperModeList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieInterfacesOperMode.setStatus('current')
cieInterfacesOperCause = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 3, 1, 4), InterfaceOperCauseList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieInterfacesOperCause.setStatus('current')
cieInterfaceOwnershipBitmap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 3, 1, 5), InterfaceOwnershipList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieInterfaceOwnershipBitmap.setStatus('current')
cieIfVlStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 4), )
if mibBuilder.loadTexts: cieIfVlStatsTable.setStatus('current')
cieIfVlStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cieIfVlStatsEntry.setStatus('current')
cieIfNoDropVlInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 4, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieIfNoDropVlInPkts.setStatus('current')
cieIfNoDropVlInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 4, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieIfNoDropVlInOctets.setStatus('current')
cieIfNoDropVlOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 4, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieIfNoDropVlOutPkts.setStatus('current')
cieIfNoDropVlOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 4, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieIfNoDropVlOutOctets.setStatus('current')
cieIfDropVlInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 4, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieIfDropVlInPkts.setStatus('current')
cieIfDropVlInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 4, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieIfDropVlInOctets.setStatus('current')
cieIfDropVlOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 4, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieIfDropVlOutPkts.setStatus('current')
cieIfDropVlOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 4, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieIfDropVlOutOctets.setStatus('current')
cieSystemMtu = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 2, 1), Integer32().clone(1500)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cieSystemMtu.setStatus('current')
cieLinkUpDownEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 2, 2), Bits().clone(namedValues=NamedValues(("standard", 0), ("cisco", 1))).clone(namedValues=NamedValues(("standard", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cieLinkUpDownEnable.setStatus('deprecated')
cieStandardLinkUpDownVarbinds = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("standard", 1), ("additional", 2), ("other", 3))).clone('additional')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cieStandardLinkUpDownVarbinds.setStatus('deprecated')
cieIfIndexPersistence = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 2, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cieIfIndexPersistence.setStatus('deprecated')
cieIfIndexPersistenceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 2, 5), )
if mibBuilder.loadTexts: cieIfIndexPersistenceTable.setStatus('current')
cieIfIndexPersistenceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 2, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cieIfIndexPersistenceEntry.setStatus('current')
cieIfIndexPersistenceEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 2, 5, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cieIfIndexPersistenceEnabled.setStatus('deprecated')
cieIfIndexPersistenceControl = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 2, 5, 1, 2), IfIndexPersistenceState().clone('global')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cieIfIndexPersistenceControl.setStatus('current')
cieDelayedLinkUpDownNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 2, 6), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cieDelayedLinkUpDownNotifEnable.setStatus('current')
cieDelayedLinkUpDownNotifDelay = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 2, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 60)).clone(4)).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cieDelayedLinkUpDownNotifDelay.setStatus('current')
cieIfIndexGlobalPersistence = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 2, 8), IfIndexPersistenceState().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cieIfIndexGlobalPersistence.setStatus('current')
cieLinkUpDownConfig = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 2, 9), Bits().clone(namedValues=NamedValues(("standardLinkUp", 0), ("standardLinkDown", 1), ("additionalLinkUp", 2), ("additionalLinkDown", 3), ("ciscoLinkUp", 4), ("ciscoLinkDown", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cieLinkUpDownConfig.setStatus('current')
cieIfDot1qCustomEtherTypeTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 3, 1), )
if mibBuilder.loadTexts: cieIfDot1qCustomEtherTypeTable.setStatus('current')
cieIfDot1qCustomEtherTypeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cieIfDot1qCustomEtherTypeEntry.setStatus('current')
cieIfDot1qCustomAdminEtherType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cieIfDot1qCustomAdminEtherType.setStatus('current')
cieIfDot1qCustomOperEtherType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieIfDot1qCustomOperEtherType.setStatus('current')
cieIfUtilTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 4, 1), )
if mibBuilder.loadTexts: cieIfUtilTable.setStatus('current')
cieIfUtilEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 4, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cieIfUtilEntry.setStatus('current')
cieIfInPktRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 4, 1, 1, 1), Counter64()).setUnits('packets per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cieIfInPktRate.setStatus('current')
cieIfInOctetRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 4, 1, 1, 2), Counter64()).setUnits('octets per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cieIfInOctetRate.setStatus('current')
cieIfOutPktRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 4, 1, 1, 3), Counter64()).setUnits('packets per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cieIfOutPktRate.setStatus('current')
cieIfOutOctetRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 4, 1, 1, 4), Counter64()).setUnits('octets per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cieIfOutOctetRate.setStatus('current')
cieIfInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 4, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cieIfInterval.setStatus('current')
cieIfDot1dBaseMappingTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 5, 1), )
if mibBuilder.loadTexts: cieIfDot1dBaseMappingTable.setStatus('current')
cieIfDot1dBaseMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 5, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cieIfDot1dBaseMappingEntry.setStatus('current')
cieIfDot1dBaseMappingPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieIfDot1dBaseMappingPort.setStatus('current')
cieIfNameMappingTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 6, 1), )
if mibBuilder.loadTexts: cieIfNameMappingTable.setStatus('current')
cieIfNameMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 6, 1, 1), ).setIndexNames((0, "CISCO-IF-EXTENSION-MIB", "cieIfName"))
if mibBuilder.loadTexts: cieIfNameMappingEntry.setStatus('current')
cieIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 6, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 112)))
if mibBuilder.loadTexts: cieIfName.setStatus('current')
cieIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 6, 1, 1, 2), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieIfIndex.setStatus('current')
cieLinkDown = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 276, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifAdminStatus"), ("IF-MIB", "ifOperStatus"), ("IF-MIB", "ifName"), ("IF-MIB", "ifType"))
if mibBuilder.loadTexts: cieLinkDown.setStatus('current')
cieLinkUp = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 276, 0, 2)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifAdminStatus"), ("IF-MIB", "ifOperStatus"), ("IF-MIB", "ifName"), ("IF-MIB", "ifType"))
if mibBuilder.loadTexts: cieLinkUp.setStatus('current')
cieDelayedLinkUpDownNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 276, 0, 3)).setObjects(("IF-MIB", "ifAdminStatus"), ("IF-MIB", "ifOperStatus"), ("IF-MIB", "ifName"), ("IF-MIB", "ifType"), ("CISCO-IF-EXTENSION-MIB", "cieIfOperStatusCause"))
if mibBuilder.loadTexts: cieDelayedLinkUpDownNotif.setStatus('current')
ciscoIfExtensionMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 1))
ciscoIfExtensionMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2))
ciscoIfExtensionMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 1, 1)).setObjects(("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTablePacketGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTableIntfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtensionMIBCompliance = ciscoIfExtensionMIBCompliance.setStatus('deprecated')
ciscoIfExtensionMIBCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 1, 2)).setObjects(("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTablePacketGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTableIntfGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTableIntfGroup1"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionSystemGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtDot1qEtherTypeGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtensionMIBCompliance1 = ciscoIfExtensionMIBCompliance1.setStatus('deprecated')
ciscoIfExtensionMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 1, 3)).setObjects(("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTablePacketGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTableIntfGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTableIntfGroup1"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionSystemGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtDot1qEtherTypeGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtUtilizationGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtDot1dBaseMappingGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtensionMIBCompliance2 = ciscoIfExtensionMIBCompliance2.setStatus('deprecated')
ciscoIfExtensionMIBCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 1, 4)).setObjects(("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTablePacketGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTableIntfGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTableIntfGroup1"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionSystemGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtDot1qEtherTypeGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtUtilizationGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtDot1dBaseMappingGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtIfNameMappingGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtensionMIBCompliance3 = ciscoIfExtensionMIBCompliance3.setStatus('deprecated')
ciscoIfExtensionMIBCompliance4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 1, 5)).setObjects(("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTablePacketGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTableIntfGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTableIntfGroup2"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionSystemGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtDot1qEtherTypeGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtUtilizationGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtDot1dBaseMappingGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtIfNameMappingGroup"), ("CISCO-IF-EXTENSION-MIB", "cieIfStatusListGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtensionMIBCompliance4 = ciscoIfExtensionMIBCompliance4.setStatus('deprecated')
ciscoIfExtensionMIBCompliance5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 1, 6)).setObjects(("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTablePacketGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTableIntfGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTableIntfGroup2"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionSystemGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtDot1qEtherTypeGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtUtilizationGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtDot1dBaseMappingGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtIfNameMappingGroup"), ("CISCO-IF-EXTENSION-MIB", "cieIfStatusListGroup"), ("CISCO-IF-EXTENSION-MIB", "cieLinkUpDownNotifEnableGroup"), ("CISCO-IF-EXTENSION-MIB", "cieLinkUpDownNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtensionMIBCompliance5 = ciscoIfExtensionMIBCompliance5.setStatus('deprecated')
ciscoIfExtensionMIBCompliance6 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 1, 7)).setObjects(("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTablePacketGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTableIntfGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTableIntfGroup2"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionSystemGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtDot1qEtherTypeGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtUtilizationGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtDot1dBaseMappingGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtIfNameMappingGroup"), ("CISCO-IF-EXTENSION-MIB", "cieIfStatusListGroup"), ("CISCO-IF-EXTENSION-MIB", "cieLinkUpDownNotifEnableGroup"), ("CISCO-IF-EXTENSION-MIB", "cieLinkUpDownNotifGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionAsymmetricalSpeedGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtensionMIBCompliance6 = ciscoIfExtensionMIBCompliance6.setStatus('deprecated')
ciscoIfExtensionMIBCompliance7 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 1, 8)).setObjects(("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTablePacketGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTableIntfGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTableIntfGroup2"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionSystemGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtDot1qEtherTypeGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtUtilizationGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtDot1dBaseMappingGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtIfNameMappingGroup"), ("CISCO-IF-EXTENSION-MIB", "cieIfStatusListGroup"), ("CISCO-IF-EXTENSION-MIB", "cieLinkUpDownNotifEnableGroup"), ("CISCO-IF-EXTENSION-MIB", "cieLinkUpDownNotifGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionAsymmetricalSpeedGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtUtilIntervalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtensionMIBCompliance7 = ciscoIfExtensionMIBCompliance7.setStatus('deprecated')
ciscoIfExtensionMIBCompliance8 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 1, 9)).setObjects(("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTablePacketGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTableIntfGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTableIntfGroup2"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionSystemGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtDot1qEtherTypeGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtUtilizationGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtDot1dBaseMappingGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtIfNameMappingGroup"), ("CISCO-IF-EXTENSION-MIB", "cieIfStatusListGroup"), ("CISCO-IF-EXTENSION-MIB", "cieLinkUpDownNotifEnableGroup"), ("CISCO-IF-EXTENSION-MIB", "cieLinkUpDownNotifGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionAsymmetricalSpeedGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtUtilIntervalGroup"), ("CISCO-IF-EXTENSION-MIB", "cieIfIndexPersistenceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtensionMIBCompliance8 = ciscoIfExtensionMIBCompliance8.setStatus('deprecated')
ciscoIfExtensionMIBCompliance9 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 1, 10)).setObjects(("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTablePacketGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTableIntfGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTableIntfGroup2"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionSystemGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtDot1qEtherTypeGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtUtilizationGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtDot1dBaseMappingGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtIfNameMappingGroup"), ("CISCO-IF-EXTENSION-MIB", "cieIfStatusListGroup"), ("CISCO-IF-EXTENSION-MIB", "cieLinkUpDownNotifEnableGroup"), ("CISCO-IF-EXTENSION-MIB", "cieLinkUpDownNotifGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionAsymmetricalSpeedGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtUtilIntervalGroup"), ("CISCO-IF-EXTENSION-MIB", "cieDelayedLinkUpDownNotifNotifGroup"), ("CISCO-IF-EXTENSION-MIB", "cieDelayedLinkUpDownNotifNotifEnableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtensionMIBCompliance9 = ciscoIfExtensionMIBCompliance9.setStatus('deprecated')
ciscoIfExtensionMIBCompliance10 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 1, 11)).setObjects(("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTablePacketGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTableIntfGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTableIntfGroup2"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionSystemGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtDot1qEtherTypeGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtUtilizationGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtDot1dBaseMappingGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtIfNameMappingGroup"), ("CISCO-IF-EXTENSION-MIB", "cieIfStatusListGroup"), ("CISCO-IF-EXTENSION-MIB", "cieLinkUpDownNotifEnableGroup"), ("CISCO-IF-EXTENSION-MIB", "cieLinkUpDownNotifGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionAsymmetricalSpeedGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtUtilIntervalGroup"), ("CISCO-IF-EXTENSION-MIB", "cieDelayedLinkUpDownNotifNotifGroup"), ("CISCO-IF-EXTENSION-MIB", "cieDelayedLinkUpDownNotifNotifEnableGroup"), ("CISCO-IF-EXTENSION-MIB", "cieIfIndexPersistenceControlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtensionMIBCompliance10 = ciscoIfExtensionMIBCompliance10.setStatus('deprecated')
ciscoIfExtensionMIBCompliance11 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 1, 12)).setObjects(("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTablePacketGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTableIntfGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionSystemGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtDot1qEtherTypeGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtUtilizationGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtDot1dBaseMappingGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtIfNameMappingGroup"), ("CISCO-IF-EXTENSION-MIB", "cieIfStatusListGroup"), ("CISCO-IF-EXTENSION-MIB", "cieLinkUpDownNotifEnableGroup"), ("CISCO-IF-EXTENSION-MIB", "cieLinkUpDownNotifGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionAsymmetricalSpeedGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtUtilIntervalGroup"), ("CISCO-IF-EXTENSION-MIB", "cieDelayedLinkUpDownNotifNotifGroup"), ("CISCO-IF-EXTENSION-MIB", "cieDelayedLinkUpDownNotifNotifEnableGroup"), ("CISCO-IF-EXTENSION-MIB", "cieIfIndexPersistenceControlGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTableIntfGroup3"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtensionMIBCompliance11 = ciscoIfExtensionMIBCompliance11.setStatus('deprecated')
ciscoIfExtensionMIBCompliance12 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 1, 13)).setObjects(("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTablePacketGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTableIntfGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionSystemGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtDot1qEtherTypeGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtUtilizationGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtDot1dBaseMappingGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtIfNameMappingGroup"), ("CISCO-IF-EXTENSION-MIB", "cieLinkUpDownNotifEnableGroup"), ("CISCO-IF-EXTENSION-MIB", "cieLinkUpDownNotifGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionAsymmetricalSpeedGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtUtilIntervalGroup"), ("CISCO-IF-EXTENSION-MIB", "cieDelayedLinkUpDownNotifNotifGroup"), ("CISCO-IF-EXTENSION-MIB", "cieDelayedLinkUpDownNotifNotifEnableGroup"), ("CISCO-IF-EXTENSION-MIB", "cieIfIndexPersistenceControlGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTableIntfGroup3"), ("CISCO-IF-EXTENSION-MIB", "cieIfStatusListGroup"), ("CISCO-IF-EXTENSION-MIB", "cieIfStatusListGroupSup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtensionMIBCompliance12 = ciscoIfExtensionMIBCompliance12.setStatus('deprecated')
ciscoIfExtensionMIBCompliance13 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 1, 14)).setObjects(("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTablePacketGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTableIntfGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionSystemGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtDot1qEtherTypeGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtUtilizationGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtDot1dBaseMappingGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtIfNameMappingGroup"), ("CISCO-IF-EXTENSION-MIB", "cieLinkUpDownNotifEnableGroup"), ("CISCO-IF-EXTENSION-MIB", "cieLinkUpDownNotifGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionAsymmetricalSpeedGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtUtilIntervalGroup"), ("CISCO-IF-EXTENSION-MIB", "cieDelayedLinkUpDownNotifNotifGroup"), ("CISCO-IF-EXTENSION-MIB", "cieDelayedLinkUpDownNotifNotifEnableGroup"), ("CISCO-IF-EXTENSION-MIB", "cieIfIndexPersistenceControlGroup"), ("CISCO-IF-EXTENSION-MIB", "cieIfStatusListGroup"), ("CISCO-IF-EXTENSION-MIB", "cieIfStatusListGroupSup1"), ("CISCO-IF-EXTENSION-MIB", "cieIfVlStatsGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTableIntfGroup3"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTableIntfGroup3SupR01"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtensionMIBCompliance13 = ciscoIfExtensionMIBCompliance13.setStatus('deprecated')
ciscoIfExtensionMIBCompliance14 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 1, 15)).setObjects(("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTablePacketGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTableIntfGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionSystemGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtDot1qEtherTypeGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtUtilizationGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtDot1dBaseMappingGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtIfNameMappingGroup"), ("CISCO-IF-EXTENSION-MIB", "cieLinkUpDownNotifGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionAsymmetricalSpeedGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtUtilIntervalGroup"), ("CISCO-IF-EXTENSION-MIB", "cieDelayedLinkUpDownNotifNotifGroup"), ("CISCO-IF-EXTENSION-MIB", "cieDelayedLinkUpDownNotifNotifEnableGroup"), ("CISCO-IF-EXTENSION-MIB", "cieIfIndexPersistenceControlGroup"), ("CISCO-IF-EXTENSION-MIB", "cieIfStatusListGroup"), ("CISCO-IF-EXTENSION-MIB", "cieIfStatusListGroupSup1"), ("CISCO-IF-EXTENSION-MIB", "cieIfVlStatsGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTableIntfGroup3"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTableIntfGroup3SupR01"), ("CISCO-IF-EXTENSION-MIB", "cieLinkUpDownNotifConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtensionMIBCompliance14 = ciscoIfExtensionMIBCompliance14.setStatus('deprecated')
ciscoIfExtensionMIBCompliance15 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 1, 16)).setObjects(("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTablePacketGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTableIntfGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionSystemGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtDot1qEtherTypeGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtUtilizationGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtDot1dBaseMappingGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtIfNameMappingGroup"), ("CISCO-IF-EXTENSION-MIB", "cieLinkUpDownNotifGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionAsymmetricalSpeedGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtUtilIntervalGroup"), ("CISCO-IF-EXTENSION-MIB", "cieDelayedLinkUpDownNotifNotifGroup"), ("CISCO-IF-EXTENSION-MIB", "cieDelayedLinkUpDownNotifNotifEnableGroup"), ("CISCO-IF-EXTENSION-MIB", "cieIfIndexPersistenceControlGroup"), ("CISCO-IF-EXTENSION-MIB", "cieIfStatusListGroup"), ("CISCO-IF-EXTENSION-MIB", "cieIfStatusListGroupSup1"), ("CISCO-IF-EXTENSION-MIB", "cieIfVlStatsGroup"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTableIntfGroup3"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTableIntfGroup3SupR01"), ("CISCO-IF-EXTENSION-MIB", "ciscoIfExtensionTableIntfGroup3SupR02"), ("CISCO-IF-EXTENSION-MIB", "cieLinkUpDownNotifConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtensionMIBCompliance15 = ciscoIfExtensionMIBCompliance15.setStatus('current')
ciscoIfExtensionTablePacketGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 1)).setObjects(("CISCO-IF-EXTENSION-MIB", "cieIfLastInTime"), ("CISCO-IF-EXTENSION-MIB", "cieIfLastOutTime"), ("CISCO-IF-EXTENSION-MIB", "cieIfLastOutHangTime"), ("CISCO-IF-EXTENSION-MIB", "cieIfInRuntsErrs"), ("CISCO-IF-EXTENSION-MIB", "cieIfInGiantsErrs"), ("CISCO-IF-EXTENSION-MIB", "cieIfInFramingErrs"), ("CISCO-IF-EXTENSION-MIB", "cieIfInOverrunErrs"), ("CISCO-IF-EXTENSION-MIB", "cieIfInIgnored"), ("CISCO-IF-EXTENSION-MIB", "cieIfInAbortErrs"), ("CISCO-IF-EXTENSION-MIB", "cieIfInputQueueDrops"), ("CISCO-IF-EXTENSION-MIB", "cieIfOutputQueueDrops"), ("CISCO-IF-EXTENSION-MIB", "cieIfPacketDiscontinuityTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtensionTablePacketGroup = ciscoIfExtensionTablePacketGroup.setStatus('current')
ciscoIfExtensionTableIntfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 2)).setObjects(("CISCO-IF-EXTENSION-MIB", "cieIfResetCount"), ("CISCO-IF-EXTENSION-MIB", "cieIfKeepAliveEnabled"), ("CISCO-IF-EXTENSION-MIB", "cieIfStateChangeReason"), ("CISCO-IF-EXTENSION-MIB", "cieIfCarrierTransitionCount"), ("CISCO-IF-EXTENSION-MIB", "cieIfInterfaceDiscontinuityTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtensionTableIntfGroup = ciscoIfExtensionTableIntfGroup.setStatus('current')
ciscoIfExtensionTableIntfGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 3)).setObjects(("CISCO-IF-EXTENSION-MIB", "cieIfDhcpMode"), ("CISCO-IF-EXTENSION-MIB", "cieIfMtu"), ("CISCO-IF-EXTENSION-MIB", "cieIfContextName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtensionTableIntfGroup1 = ciscoIfExtensionTableIntfGroup1.setStatus('deprecated')
ciscoIfExtensionSystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 4)).setObjects(("CISCO-IF-EXTENSION-MIB", "cieSystemMtu"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtensionSystemGroup = ciscoIfExtensionSystemGroup.setStatus('current')
ciscoIfExtDot1qEtherTypeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 5)).setObjects(("CISCO-IF-EXTENSION-MIB", "cieIfDot1qCustomAdminEtherType"), ("CISCO-IF-EXTENSION-MIB", "cieIfDot1qCustomOperEtherType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtDot1qEtherTypeGroup = ciscoIfExtDot1qEtherTypeGroup.setStatus('current')
ciscoIfExtUtilizationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 6)).setObjects(("CISCO-IF-EXTENSION-MIB", "cieIfInPktRate"), ("CISCO-IF-EXTENSION-MIB", "cieIfInOctetRate"), ("CISCO-IF-EXTENSION-MIB", "cieIfOutPktRate"), ("CISCO-IF-EXTENSION-MIB", "cieIfOutOctetRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtUtilizationGroup = ciscoIfExtUtilizationGroup.setStatus('current')
ciscoIfExtDot1dBaseMappingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 7)).setObjects(("CISCO-IF-EXTENSION-MIB", "cieIfDot1dBaseMappingPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtDot1dBaseMappingGroup = ciscoIfExtDot1dBaseMappingGroup.setStatus('current')
ciscoIfExtIfNameMappingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 8)).setObjects(("CISCO-IF-EXTENSION-MIB", "cieIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtIfNameMappingGroup = ciscoIfExtIfNameMappingGroup.setStatus('current')
ciscoIfExtensionTableIntfGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 9)).setObjects(("CISCO-IF-EXTENSION-MIB", "cieIfDhcpMode"), ("CISCO-IF-EXTENSION-MIB", "cieIfMtu"), ("CISCO-IF-EXTENSION-MIB", "cieIfContextName"), ("CISCO-IF-EXTENSION-MIB", "cieIfOperStatusCause"), ("CISCO-IF-EXTENSION-MIB", "cieIfOperStatusCauseDescr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtensionTableIntfGroup2 = ciscoIfExtensionTableIntfGroup2.setStatus('deprecated')
cieIfStatusListGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 10)).setObjects(("CISCO-IF-EXTENSION-MIB", "cieInterfacesIndex"), ("CISCO-IF-EXTENSION-MIB", "cieInterfacesOperMode"), ("CISCO-IF-EXTENSION-MIB", "cieInterfacesOperCause"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cieIfStatusListGroup = cieIfStatusListGroup.setStatus('current')
cieLinkUpDownNotifEnableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 11)).setObjects(("CISCO-IF-EXTENSION-MIB", "cieLinkUpDownEnable"), ("CISCO-IF-EXTENSION-MIB", "cieStandardLinkUpDownVarbinds"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cieLinkUpDownNotifEnableGroup = cieLinkUpDownNotifEnableGroup.setStatus('deprecated')
cieLinkUpDownNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 12)).setObjects(("CISCO-IF-EXTENSION-MIB", "cieLinkDown"), ("CISCO-IF-EXTENSION-MIB", "cieLinkUp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cieLinkUpDownNotifGroup = cieLinkUpDownNotifGroup.setStatus('current')
ciscoIfExtensionAsymmetricalSpeedGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 13)).setObjects(("CISCO-IF-EXTENSION-MIB", "cieIfSpeedReceive"), ("CISCO-IF-EXTENSION-MIB", "cieIfHighSpeedReceive"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtensionAsymmetricalSpeedGroup = ciscoIfExtensionAsymmetricalSpeedGroup.setStatus('current')
ciscoIfExtUtilIntervalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 14)).setObjects(("CISCO-IF-EXTENSION-MIB", "cieIfInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtUtilIntervalGroup = ciscoIfExtUtilIntervalGroup.setStatus('current')
cieIfIndexPersistenceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 15)).setObjects(("CISCO-IF-EXTENSION-MIB", "cieIfIndexPersistence"), ("CISCO-IF-EXTENSION-MIB", "cieIfIndexPersistenceEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cieIfIndexPersistenceGroup = cieIfIndexPersistenceGroup.setStatus('deprecated')
cieDelayedLinkUpDownNotifNotifEnableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 16)).setObjects(("CISCO-IF-EXTENSION-MIB", "cieDelayedLinkUpDownNotifEnable"), ("CISCO-IF-EXTENSION-MIB", "cieDelayedLinkUpDownNotifDelay"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cieDelayedLinkUpDownNotifNotifEnableGroup = cieDelayedLinkUpDownNotifNotifEnableGroup.setStatus('current')
cieDelayedLinkUpDownNotifNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 17)).setObjects(("CISCO-IF-EXTENSION-MIB", "cieDelayedLinkUpDownNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cieDelayedLinkUpDownNotifNotifGroup = cieDelayedLinkUpDownNotifNotifGroup.setStatus('current')
cieIfIndexPersistenceControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 18)).setObjects(("CISCO-IF-EXTENSION-MIB", "cieIfIndexGlobalPersistence"), ("CISCO-IF-EXTENSION-MIB", "cieIfIndexPersistenceControl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cieIfIndexPersistenceControlGroup = cieIfIndexPersistenceControlGroup.setStatus('current')
ciscoIfExtensionTableIntfGroup3 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 19)).setObjects(("CISCO-IF-EXTENSION-MIB", "cieIfDhcpMode"), ("CISCO-IF-EXTENSION-MIB", "cieIfMtu"), ("CISCO-IF-EXTENSION-MIB", "cieIfContextName"), ("CISCO-IF-EXTENSION-MIB", "cieIfOperStatusCause"), ("CISCO-IF-EXTENSION-MIB", "cieIfOperStatusCauseDescr"), ("CISCO-IF-EXTENSION-MIB", "cieIfOwner"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtensionTableIntfGroup3 = ciscoIfExtensionTableIntfGroup3.setStatus('current')
cieIfStatusListGroupSup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 20)).setObjects(("CISCO-IF-EXTENSION-MIB", "cieInterfaceOwnershipBitmap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cieIfStatusListGroupSup1 = cieIfStatusListGroupSup1.setStatus('current')
cieIfVlStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 21)).setObjects(("CISCO-IF-EXTENSION-MIB", "cieIfNoDropVlInPkts"), ("CISCO-IF-EXTENSION-MIB", "cieIfNoDropVlInOctets"), ("CISCO-IF-EXTENSION-MIB", "cieIfNoDropVlOutPkts"), ("CISCO-IF-EXTENSION-MIB", "cieIfNoDropVlOutOctets"), ("CISCO-IF-EXTENSION-MIB", "cieIfDropVlInPkts"), ("CISCO-IF-EXTENSION-MIB", "cieIfDropVlInOctets"), ("CISCO-IF-EXTENSION-MIB", "cieIfDropVlOutPkts"), ("CISCO-IF-EXTENSION-MIB", "cieIfDropVlOutOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cieIfVlStatsGroup = cieIfVlStatsGroup.setStatus('current')
ciscoIfExtensionTableIntfGroup3SupR01 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 22)).setObjects(("CISCO-IF-EXTENSION-MIB", "cieIfSharedConfig"), ("CISCO-IF-EXTENSION-MIB", "cieIfSpeedGroupConfig"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtensionTableIntfGroup3SupR01 = ciscoIfExtensionTableIntfGroup3SupR01.setStatus('current')
cieLinkUpDownNotifConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 23)).setObjects(("CISCO-IF-EXTENSION-MIB", "cieLinkUpDownConfig"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cieLinkUpDownNotifConfigGroup = cieLinkUpDownNotifConfigGroup.setStatus('current')
ciscoIfExtensionTableIntfGroup3SupR02 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 24)).setObjects(("CISCO-IF-EXTENSION-MIB", "cieIfTransceiverFrequencyConfig"), ("CISCO-IF-EXTENSION-MIB", "cieIfFillPatternConfig"), ("CISCO-IF-EXTENSION-MIB", "cieIfIgnoreBitErrorsConfig"), ("CISCO-IF-EXTENSION-MIB", "cieIfIgnoreInterruptThresholdConfig"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtensionTableIntfGroup3SupR02 = ciscoIfExtensionTableIntfGroup3SupR02.setStatus('current')
mibBuilder.exportSymbols("CISCO-IF-EXTENSION-MIB", cieIfInFramingErrs=cieIfInFramingErrs, cieIfOutOctetRate=cieIfOutOctetRate, cieIfIndex=cieIfIndex, cieIfIndexPersistenceGroup=cieIfIndexPersistenceGroup, cieLinkUpDownNotifGroup=cieLinkUpDownNotifGroup, cieSystemMtu=cieSystemMtu, cieIfInterfaceEntry=cieIfInterfaceEntry, cieIfPacketStatsTable=cieIfPacketStatsTable, cieDelayedLinkUpDownNotif=cieDelayedLinkUpDownNotif, cieIfName=cieIfName, cieLinkUpDownConfig=cieLinkUpDownConfig, cieIfNoDropVlInPkts=cieIfNoDropVlInPkts, cieInterfacesOperCause=cieInterfacesOperCause, cieIfDropVlOutOctets=cieIfDropVlOutOctets, cieIfInterval=cieIfInterval, cieIfVlStatsEntry=cieIfVlStatsEntry, ciscoIfExtensionTableIntfGroup2=ciscoIfExtensionTableIntfGroup2, cieIfVlStatsGroup=cieIfVlStatsGroup, ciscoIfExtensionMIBCompliance12=ciscoIfExtensionMIBCompliance12, cieIfSpeedReceive=cieIfSpeedReceive, cieIfIndexPersistenceControlGroup=cieIfIndexPersistenceControlGroup, cieLinkUpDownNotifEnableGroup=cieLinkUpDownNotifEnableGroup, cieIfOutputQueueDrops=cieIfOutputQueueDrops, ciscoIfExtUtilization=ciscoIfExtUtilization, InterfaceOperCauseList=InterfaceOperCauseList, cieInterfacesIndex=cieInterfacesIndex, ciscoIfExtDot1qEtherTypeGroup=ciscoIfExtDot1qEtherTypeGroup, PYSNMP_MODULE_ID=ciscoIfExtensionMIB, cieInterfaceOwnershipBitmap=cieInterfaceOwnershipBitmap, ciscoIfExtensionMIBConformance=ciscoIfExtensionMIBConformance, ciscoIfExtensionMIBCompliance15=ciscoIfExtensionMIBCompliance15, ciscoIfExtensionSystemGroup=ciscoIfExtensionSystemGroup, cieDelayedLinkUpDownNotifNotifGroup=cieDelayedLinkUpDownNotifNotifGroup, cieIfDot1qCustomAdminEtherType=cieIfDot1qCustomAdminEtherType, cieIfStatusListIndex=cieIfStatusListIndex, cieDelayedLinkUpDownNotifDelay=cieDelayedLinkUpDownNotifDelay, cieIfStateChangeReason=cieIfStateChangeReason, cieIfIndexPersistenceEnabled=cieIfIndexPersistenceEnabled, cieIfIndexGlobalPersistence=cieIfIndexGlobalPersistence, cieIfMtu=cieIfMtu, cieIfDhcpMode=cieIfDhcpMode, cieIfIndexPersistenceTable=cieIfIndexPersistenceTable, ciscoIfExtensionStats=ciscoIfExtensionStats, cieIfContextName=cieIfContextName, cieStandardLinkUpDownVarbinds=cieStandardLinkUpDownVarbinds, cieIfDot1dBaseMappingPort=cieIfDot1dBaseMappingPort, cieIfNameMappingEntry=cieIfNameMappingEntry, cieIfInPktRate=cieIfInPktRate, cieIfIndexPersistence=cieIfIndexPersistence, cieIfOutPktRate=cieIfOutPktRate, cieIfSpeedGroupConfig=cieIfSpeedGroupConfig, cieIfLastOutHangTime=cieIfLastOutHangTime, ciscoIfExtensionMIBCompliance3=ciscoIfExtensionMIBCompliance3, ciscoIfExtUtilizationGroup=ciscoIfExtUtilizationGroup, cieIfOwner=cieIfOwner, ciscoIfExtensionMIBCompliance8=ciscoIfExtensionMIBCompliance8, ciscoIfExtensionMIBCompliance13=ciscoIfExtensionMIBCompliance13, ciscoIfExtensionMIBCompliance1=ciscoIfExtensionMIBCompliance1, cieLinkUp=cieLinkUp, cieIfNameMappingTable=cieIfNameMappingTable, ciscoIfExtensionMIBGroups=ciscoIfExtensionMIBGroups, cieIfInterfaceTable=cieIfInterfaceTable, cieIfUtilEntry=cieIfUtilEntry, cieDelayedLinkUpDownNotifNotifEnableGroup=cieDelayedLinkUpDownNotifNotifEnableGroup, ciscoIfExtensionMIBCompliance4=ciscoIfExtensionMIBCompliance4, cieIfInRuntsErrs=cieIfInRuntsErrs, cieIfInGiantsErrs=cieIfInGiantsErrs, ciscoIfExtensionMIBCompliance2=ciscoIfExtensionMIBCompliance2, cieIfDot1qCustomEtherTypeTable=cieIfDot1qCustomEtherTypeTable, cieIfDot1dBaseMappingTable=cieIfDot1dBaseMappingTable, cieIfInputQueueDrops=cieIfInputQueueDrops, cieIfNoDropVlOutPkts=cieIfNoDropVlOutPkts, IfIndexPersistenceState=IfIndexPersistenceState, cieLinkUpDownNotifConfigGroup=cieLinkUpDownNotifConfigGroup, ciscoIfExtensionTableIntfGroup=ciscoIfExtensionTableIntfGroup, cieIfHighSpeedReceive=cieIfHighSpeedReceive, cieIfInIgnored=cieIfInIgnored, InterfaceIndexList=InterfaceIndexList, cieIfStatusListTable=cieIfStatusListTable, ciscoIfExtensionMIBCompliance5=ciscoIfExtensionMIBCompliance5, cieIfDot1qCustomOperEtherType=cieIfDot1qCustomOperEtherType, cieIfDot1qCustomEtherTypeEntry=cieIfDot1qCustomEtherTypeEntry, cieIfDropVlInPkts=cieIfDropVlInPkts, cieIfKeepAliveEnabled=cieIfKeepAliveEnabled, InterfaceOwnershipList=InterfaceOwnershipList, cieIfDropVlInOctets=cieIfDropVlInOctets, cieIfPacketStatsEntry=cieIfPacketStatsEntry, cieIfTransceiverFrequencyConfig=cieIfTransceiverFrequencyConfig, cieLinkUpDownEnable=cieLinkUpDownEnable, cieIfNoDropVlOutOctets=cieIfNoDropVlOutOctets, ciscoIfExtensionTableIntfGroup3SupR01=ciscoIfExtensionTableIntfGroup3SupR01, ciscoIfExtensionMIBNotifications=ciscoIfExtensionMIBNotifications, ciscoIfExtensionMIBCompliance=ciscoIfExtensionMIBCompliance, ciscoIfExtensionMIBObjects=ciscoIfExtensionMIBObjects, ciscoIfExtSystemConfig=ciscoIfExtSystemConfig, cieIfOperStatusCause=cieIfOperStatusCause, ciscoIfExtDot1dBaseMapping=ciscoIfExtDot1dBaseMapping, cieIfCarrierTransitionCount=cieIfCarrierTransitionCount, cieIfVlStatsTable=cieIfVlStatsTable, cieIfDropVlOutPkts=cieIfDropVlOutPkts, ciscoIfExtensionTablePacketGroup=ciscoIfExtensionTablePacketGroup, ciscoIfExtDot1dBaseMappingGroup=ciscoIfExtDot1dBaseMappingGroup, InterfaceOperModeList=InterfaceOperModeList, cieIfNoDropVlInOctets=cieIfNoDropVlInOctets, ciscoIfExtensionTableIntfGroup3SupR02=ciscoIfExtensionTableIntfGroup3SupR02, cieIfIgnoreBitErrorsConfig=cieIfIgnoreBitErrorsConfig, cieIfStatusListGroupSup1=cieIfStatusListGroupSup1, ciscoIfExtensionMIBCompliances=ciscoIfExtensionMIBCompliances, cieIfLastInTime=cieIfLastInTime, cieIfIndexPersistenceControl=cieIfIndexPersistenceControl, cieIfInAbortErrs=cieIfInAbortErrs, cieIfOperStatusCauseDescr=cieIfOperStatusCauseDescr, ciscoIfExtensionMIBCompliance9=ciscoIfExtensionMIBCompliance9, cieDelayedLinkUpDownNotifEnable=cieDelayedLinkUpDownNotifEnable, cieIfStatusListEntry=cieIfStatusListEntry, cieInterfacesOperMode=cieInterfacesOperMode, cieIfDot1dBaseMappingEntry=cieIfDot1dBaseMappingEntry, ciscoIfExtDot1qCustomEtherType=ciscoIfExtDot1qCustomEtherType, ciscoIfExtensionTableIntfGroup3=ciscoIfExtensionTableIntfGroup3, cieIfResetCount=cieIfResetCount, ciscoIfExtIfNameMappingGroup=ciscoIfExtIfNameMappingGroup, ciscoIfExtUtilIntervalGroup=ciscoIfExtUtilIntervalGroup, ciscoIfExtensionMIB=ciscoIfExtensionMIB, cieIfSharedConfig=cieIfSharedConfig, ciscoIfExtensionMIBCompliance7=ciscoIfExtensionMIBCompliance7, cieIfLastOutTime=cieIfLastOutTime, ciscoIfExtensionAsymmetricalSpeedGroup=ciscoIfExtensionAsymmetricalSpeedGroup, ciscoIfExtIfNameMapping=ciscoIfExtIfNameMapping, cieLinkDown=cieLinkDown, cieIfIgnoreInterruptThresholdConfig=cieIfIgnoreInterruptThresholdConfig, ciscoIfExtensionTableIntfGroup1=ciscoIfExtensionTableIntfGroup1, cieIfStatusListGroup=cieIfStatusListGroup, ciscoIfExtensionMIBCompliance14=ciscoIfExtensionMIBCompliance14, cieIfUtilTable=cieIfUtilTable, cieIfInOverrunErrs=cieIfInOverrunErrs, ciscoIfExtensionMIBCompliance10=ciscoIfExtensionMIBCompliance10, cieIfInterfaceDiscontinuityTime=cieIfInterfaceDiscontinuityTime, cieIfInOctetRate=cieIfInOctetRate, cieIfIndexPersistenceEntry=cieIfIndexPersistenceEntry, ciscoIfExtensionMIBCompliance11=ciscoIfExtensionMIBCompliance11, cieIfPacketDiscontinuityTime=cieIfPacketDiscontinuityTime, cieIfFillPatternConfig=cieIfFillPatternConfig, ciscoIfExtensionMIBCompliance6=ciscoIfExtensionMIBCompliance6)
