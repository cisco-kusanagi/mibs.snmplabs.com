#
# PySNMP MIB module NETI-DTM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETI-DTM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:09:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
netiExperimentalGeneric, FaultStatus = mibBuilder.importSymbols("NETI-COMMON-MIB", "netiExperimentalGeneric", "FaultStatus")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, Counter32, ModuleIdentity, MibIdentifier, Counter64, Integer32, TimeTicks, IpAddress, Unsigned32, NotificationType, Gauge32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "Counter32", "ModuleIdentity", "MibIdentifier", "Counter64", "Integer32", "TimeTicks", "IpAddress", "Unsigned32", "NotificationType", "Gauge32", "ObjectIdentity")
DateAndTime, MacAddress, DisplayString, RowPointer, TruthValue, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "MacAddress", "DisplayString", "RowPointer", "TruthValue", "TextualConvention", "RowStatus")
netiDTMMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4))
netiDTMMIB.setRevisions(('2013-11-12 08:00', '2013-09-10 13:00', '2010-09-01 14:00', '2010-03-03 09:00', '2009-06-25 14:00', '2008-02-06 17:00', '2006-08-22 10:00', '2006-05-16 13:00', '2004-09-29 00:00', '2003-02-28 00:00',))
if mibBuilder.loadTexts: netiDTMMIB.setLastUpdated('201311120800Z')
if mibBuilder.loadTexts: netiDTMMIB.setOrganization('Net Insight AB')
netiDTMMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1))
dtmAddrGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 1))
dtmIfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2))
dtmLinkStateGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 3))
dtmRouteGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 4))
dtmHistoryGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 5))
dtmNodeGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 6))
dtmSyncGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 7))
class DtmAddress(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x.'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class DtmSourceRoute(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x.1x.1x.1x.1x.1x.1x.1x 1x:1x'

dtmAddrTable = MibTable((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 1, 1), )
if mibBuilder.loadTexts: dtmAddrTable.setStatus('current')
dtmAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 1, 1, 1), ).setIndexNames((0, "NETI-DTM-MIB", "dtmAddrEntryIndex"))
if mibBuilder.loadTexts: dtmAddrEntry.setStatus('current')
dtmAddrEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtmAddrEntryIndex.setStatus('current')
dtmAddrEntryAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 1, 1, 1, 2), DtmAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dtmAddrEntryAddr.setStatus('current')
dtmAddrEntryIsAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 1, 1, 1, 3), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dtmAddrEntryIsAlias.setStatus('current')
dtmAddrEntryAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unspecified", 1), ("loopback", 2), ("local", 3), ("multicast", 4), ("global", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtmAddrEntryAddrType.setStatus('current')
dtmAddrEntryRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dtmAddrEntryRowStatus.setStatus('current')
dtmHostsTable = MibTable((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 1, 2), )
if mibBuilder.loadTexts: dtmHostsTable.setStatus('current')
dtmHostsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 1, 2, 1), ).setIndexNames((0, "NETI-DTM-MIB", "dtmHostsEntryIndex"))
if mibBuilder.loadTexts: dtmHostsEntry.setStatus('current')
dtmHostsEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: dtmHostsEntryIndex.setStatus('current')
dtmHostsEntryAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 1, 2, 1, 2), DtmAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dtmHostsEntryAddr.setStatus('current')
dtmHostsEntryName = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 1, 2, 1, 3), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dtmHostsEntryName.setStatus('current')
dtmHostsEntryRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dtmHostsEntryRowStatus.setStatus('current')
dtmIfTable = MibTable((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1), )
if mibBuilder.loadTexts: dtmIfTable.setStatus('current')
dtmIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1), ).setIndexNames((0, "NETI-DTM-MIB", "dtmIfIndex"))
if mibBuilder.loadTexts: dtmIfEntry.setStatus('current')
dtmIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtmIfIndex.setStatus('current')
dtmIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 2), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dtmIfName.setStatus('current')
dtmIfMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtmIfMacAddress.setStatus('current')
dtmIfTxCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtmIfTxCapacity.setStatus('current')
dtmIfTxCapacityCtrl = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 5), Gauge32().clone(5)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dtmIfTxCapacityCtrl.setStatus('current')
dtmIfTxCapacityStart = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 6), Gauge32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtmIfTxCapacityStart.setStatus('deprecated')
dtmIfTxCapacityOwned = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtmIfTxCapacityOwned.setStatus('deprecated')
dtmIfTxCapacityBorrowed = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtmIfTxCapacityBorrowed.setStatus('deprecated')
dtmIfTxCapacityMaxLend = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 9), Gauge32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dtmIfTxCapacityMaxLend.setStatus('deprecated')
dtmIfTxCapacityLent = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtmIfTxCapacityLent.setStatus('deprecated')
dtmIfTxCapacityUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtmIfTxCapacityUsed.setStatus('current')
dtmIfRxCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtmIfRxCapacity.setStatus('current')
dtmIfRxCapacityUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtmIfRxCapacityUsed.setStatus('current')
dtmIfIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtmIfIfIndex.setStatus('deprecated')
dtmIfAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2))).clone('down')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dtmIfAdminStatus.setStatus('current')
dtmIfOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("absent", 3), ("lowerLayerDown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtmIfOperStatus.setStatus('current')
dtmIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 17), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dtmIfRowStatus.setStatus('current')
dtmIfAbsent = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 18), FaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtmIfAbsent.setStatus('deprecated')
dtmIfLOS = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 19), FaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtmIfLOS.setStatus('current')
dtmIfReducedCtrlCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 20), FaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtmIfReducedCtrlCapacity.setStatus('current')
dtmIfTxCapacityOwnedFirstSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 21), Gauge32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dtmIfTxCapacityOwnedFirstSlot.setStatus('deprecated')
dtmIfTxCapacityOwnedLastSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 22), Gauge32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dtmIfTxCapacityOwnedLastSlot.setStatus('current')
dtmIfRouteMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 23), Unsigned32().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dtmIfRouteMetric.setStatus('current')
dtmIfLinkClass = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normal", 1), ("persistent", 2), ("nailed", 3))).clone('normal')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dtmIfLinkClass.setStatus('current')
dtmIfPurpose = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 25), SnmpAdminString().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dtmIfPurpose.setStatus('current')
dtmIfSyncEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 2, 1, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('enabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dtmIfSyncEnabled.setStatus('current')
dtmLinkStateTableLastChangedTime = MibScalar((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 3, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtmLinkStateTableLastChangedTime.setStatus('current')
dtmLinkStateNrOfLinks = MibScalar((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 3, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtmLinkStateNrOfLinks.setStatus('current')
dtmLinkStateTable = MibTable((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 3, 3), )
if mibBuilder.loadTexts: dtmLinkStateTable.setStatus('current')
dtmLinkStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 3, 3, 1), ).setIndexNames((0, "NETI-DTM-MIB", "dtmLinkStateIndex"))
if mibBuilder.loadTexts: dtmLinkStateEntry.setStatus('current')
dtmLinkStateIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 3, 3, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtmLinkStateIndex.setStatus('current')
dtmLinkStateType = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 3, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("looped", 2), ("open", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtmLinkStateType.setStatus('current')
dtmLinkStateLocalIf = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 3, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtmLinkStateLocalIf.setStatus('current')
dtmLinkStateNrOfIfs = MibScalar((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 3, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtmLinkStateNrOfIfs.setStatus('current')
dtmLinkStateIfTable = MibTable((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 3, 5), )
if mibBuilder.loadTexts: dtmLinkStateIfTable.setStatus('current')
dtmLinkStateIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 3, 5, 1), ).setIndexNames((0, "NETI-DTM-MIB", "dtmLinkStateIndex"), (0, "NETI-DTM-MIB", "dtmLinkStateIfIndex"))
if mibBuilder.loadTexts: dtmLinkStateIfEntry.setStatus('current')
dtmLinkStateIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 3, 5, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtmLinkStateIfIndex.setStatus('current')
dtmLinkStateIfMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 3, 5, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtmLinkStateIfMacAddress.setStatus('current')
dtmLinkStateIfNodeMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 3, 5, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtmLinkStateIfNodeMacAddress.setStatus('current')
dtmLinkStateIfNodeAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 3, 5, 1, 4), DtmAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtmLinkStateIfNodeAddress.setStatus('current')
dtmLinkStateLocalSubIf = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 3, 5, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtmLinkStateLocalSubIf.setStatus('current')
dtmLinkStateIfNodeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 3, 5, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("notApplicable", 0), ("up", 1), ("recover", 2), ("limited", 3), ("noControl", 4), ("downKeep", 5), ("pending", 6), ("loopback", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtmLinkStateIfNodeStatus.setStatus('current')
dtmDrpNodeRouteMetric = MibScalar((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 4, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dtmDrpNodeRouteMetric.setStatus('current')
dtmDrpNodeType = MibScalar((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 4, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("switch", 1), ("endNode", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dtmDrpNodeType.setStatus('current')
dtmDrpAreaNumber = MibScalar((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 4, 4), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dtmDrpAreaNumber.setStatus('current')
dtmDrpDetectAreaNumber = MibScalar((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 4, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dtmDrpDetectAreaNumber.setStatus('current')
dtmDrpDetectDefaultGateway = MibScalar((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 4, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dtmDrpDetectDefaultGateway.setStatus('current')
dtmNodeStatus = MibScalar((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 6, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("recover", 2), ("limited", 3), ("noControl", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dtmNodeStatus.setStatus('current')
dtmNodeRestartOnError = MibScalar((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 6, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dtmNodeRestartOnError.setStatus('current')
dtmNodeId = MibScalar((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 6, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtmNodeId.setStatus('current')
dtmSyncNodeId = MibScalar((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 7, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtmSyncNodeId.setStatus('current')
dtmCurrentTimingSourceName = MibScalar((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 7, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtmCurrentTimingSourceName.setStatus('current')
dtmCurrentTimingSourcePeerId = MibScalar((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 7, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtmCurrentTimingSourcePeerId.setStatus('current')
dtmTimeScaleStatus = MibScalar((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 7, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("notSupported", 1), ("uninitiated", 2), ("reassigned", 3), ("compensated", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtmTimeScaleStatus.setStatus('current')
dtmTimeSourceCalibrationReference = MibScalar((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 7, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dtmTimeSourceCalibrationReference.setStatus('current')
dtmTimeSourceTable = MibTable((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 7, 6), )
if mibBuilder.loadTexts: dtmTimeSourceTable.setStatus('current')
dtmTimeSourceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 7, 6, 1), ).setIndexNames((0, "NETI-DTM-MIB", "dtmTimeSourceIndex"))
if mibBuilder.loadTexts: dtmTimeSourceEntry.setStatus('current')
dtmTimeSourceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 7, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: dtmTimeSourceIndex.setStatus('current')
dtmTimeSourceName = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 7, 6, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtmTimeSourceName.setStatus('current')
dtmTimeSourceAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 7, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dtmTimeSourceAdminStatus.setStatus('current')
dtmTimeSourceOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 7, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("absent", 3), ("lowerLayerDown", 4), ("dormant", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtmTimeSourceOperStatus.setStatus('current')
dtmTimeSourceType = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 7, 6, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("dsyp", 1), ("sqc", 2), ("ssm", 3), ("internal", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtmTimeSourceType.setStatus('current')
dtmTimeSourceRef = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 7, 6, 1, 6), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtmTimeSourceRef.setStatus('current')
dtmTimeSourceRoundTripTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 7, 6, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtmTimeSourceRoundTripTime.setStatus('current')
dtmTimeSourceTimeError = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 7, 6, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtmTimeSourceTimeError.setStatus('current')
dtmTimeSourceCalibrationTimeError = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 7, 6, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dtmTimeSourceCalibrationTimeError.setStatus('current')
dtmTimeSourceCalibrationRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 6, 2, 4, 1, 7, 6, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-499999, 499999))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dtmTimeSourceCalibrationRatio.setStatus('current')
mibBuilder.exportSymbols("NETI-DTM-MIB", dtmRouteGroup=dtmRouteGroup, dtmLinkStateIfMacAddress=dtmLinkStateIfMacAddress, dtmHostsEntryName=dtmHostsEntryName, dtmLinkStateIndex=dtmLinkStateIndex, dtmLinkStateNrOfLinks=dtmLinkStateNrOfLinks, dtmTimeSourceAdminStatus=dtmTimeSourceAdminStatus, dtmTimeSourceTable=dtmTimeSourceTable, dtmIfIndex=dtmIfIndex, dtmIfTxCapacityLent=dtmIfTxCapacityLent, dtmIfTxCapacity=dtmIfTxCapacity, dtmIfAdminStatus=dtmIfAdminStatus, dtmAddrEntry=dtmAddrEntry, dtmLinkStateTable=dtmLinkStateTable, dtmCurrentTimingSourcePeerId=dtmCurrentTimingSourcePeerId, dtmIfRxCapacity=dtmIfRxCapacity, dtmIfRouteMetric=dtmIfRouteMetric, dtmIfLinkClass=dtmIfLinkClass, dtmLinkStateIfNodeAddress=dtmLinkStateIfNodeAddress, dtmLinkStateIfNodeStatus=dtmLinkStateIfNodeStatus, dtmLinkStateLocalIf=dtmLinkStateLocalIf, dtmDrpAreaNumber=dtmDrpAreaNumber, dtmIfPurpose=dtmIfPurpose, dtmTimeSourceIndex=dtmTimeSourceIndex, dtmAddrEntryRowStatus=dtmAddrEntryRowStatus, dtmHostsTable=dtmHostsTable, dtmIfMacAddress=dtmIfMacAddress, dtmAddrTable=dtmAddrTable, dtmIfRowStatus=dtmIfRowStatus, dtmIfTable=dtmIfTable, dtmAddrEntryAddr=dtmAddrEntryAddr, dtmIfIfIndex=dtmIfIfIndex, dtmDrpNodeType=dtmDrpNodeType, dtmIfTxCapacityMaxLend=dtmIfTxCapacityMaxLend, dtmLinkStateIfIndex=dtmLinkStateIfIndex, dtmSyncGroup=dtmSyncGroup, dtmLinkStateIfTable=dtmLinkStateIfTable, dtmTimeSourceCalibrationReference=dtmTimeSourceCalibrationReference, dtmIfTxCapacityOwnedLastSlot=dtmIfTxCapacityOwnedLastSlot, dtmLinkStateLocalSubIf=dtmLinkStateLocalSubIf, dtmIfGroup=dtmIfGroup, dtmIfEntry=dtmIfEntry, dtmIfTxCapacityCtrl=dtmIfTxCapacityCtrl, dtmAddrEntryIndex=dtmAddrEntryIndex, dtmTimeSourceTimeError=dtmTimeSourceTimeError, dtmTimeSourceRoundTripTime=dtmTimeSourceRoundTripTime, dtmIfTxCapacityStart=dtmIfTxCapacityStart, dtmIfRxCapacityUsed=dtmIfRxCapacityUsed, dtmLinkStateIfEntry=dtmLinkStateIfEntry, dtmCurrentTimingSourceName=dtmCurrentTimingSourceName, dtmTimeSourceEntry=dtmTimeSourceEntry, dtmNodeRestartOnError=dtmNodeRestartOnError, dtmIfName=dtmIfName, dtmTimeSourceName=dtmTimeSourceName, dtmTimeScaleStatus=dtmTimeScaleStatus, dtmNodeId=dtmNodeId, DtmSourceRoute=DtmSourceRoute, dtmHostsEntry=dtmHostsEntry, dtmAddrGroup=dtmAddrGroup, dtmIfTxCapacityUsed=dtmIfTxCapacityUsed, dtmSyncNodeId=dtmSyncNodeId, dtmIfSyncEnabled=dtmIfSyncEnabled, dtmHistoryGroup=dtmHistoryGroup, dtmLinkStateType=dtmLinkStateType, dtmLinkStateIfNodeMacAddress=dtmLinkStateIfNodeMacAddress, dtmDrpDetectAreaNumber=dtmDrpDetectAreaNumber, dtmHostsEntryAddr=dtmHostsEntryAddr, dtmDrpNodeRouteMetric=dtmDrpNodeRouteMetric, dtmTimeSourceOperStatus=dtmTimeSourceOperStatus, dtmIfTxCapacityOwned=dtmIfTxCapacityOwned, dtmTimeSourceCalibrationTimeError=dtmTimeSourceCalibrationTimeError, dtmTimeSourceCalibrationRatio=dtmTimeSourceCalibrationRatio, dtmHostsEntryRowStatus=dtmHostsEntryRowStatus, dtmIfReducedCtrlCapacity=dtmIfReducedCtrlCapacity, dtmDrpDetectDefaultGateway=dtmDrpDetectDefaultGateway, dtmLinkStateEntry=dtmLinkStateEntry, dtmIfTxCapacityOwnedFirstSlot=dtmIfTxCapacityOwnedFirstSlot, dtmIfAbsent=dtmIfAbsent, dtmAddrEntryAddrType=dtmAddrEntryAddrType, dtmIfLOS=dtmIfLOS, dtmNodeGroup=dtmNodeGroup, dtmLinkStateTableLastChangedTime=dtmLinkStateTableLastChangedTime, DtmAddress=DtmAddress, netiDTMMIBObjects=netiDTMMIBObjects, dtmLinkStateNrOfIfs=dtmLinkStateNrOfIfs, dtmHostsEntryIndex=dtmHostsEntryIndex, dtmTimeSourceRef=dtmTimeSourceRef, dtmTimeSourceType=dtmTimeSourceType, dtmNodeStatus=dtmNodeStatus, dtmAddrEntryIsAlias=dtmAddrEntryIsAlias, dtmIfTxCapacityBorrowed=dtmIfTxCapacityBorrowed, netiDTMMIB=netiDTMMIB, dtmIfOperStatus=dtmIfOperStatus, PYSNMP_MODULE_ID=netiDTMMIB, dtmLinkStateGroup=dtmLinkStateGroup)
