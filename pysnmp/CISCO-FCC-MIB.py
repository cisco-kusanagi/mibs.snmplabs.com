#
# PySNMP MIB module CISCO-FCC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-FCC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:41:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
FcAddressId, VsanIndex = mibBuilder.importSymbols("CISCO-ST-TC", "FcAddressId", "VsanIndex")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, IpAddress, MibIdentifier, iso, Counter32, Integer32, Gauge32, Bits, ObjectIdentity, TimeTicks, ModuleIdentity, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "IpAddress", "MibIdentifier", "iso", "Counter32", "Integer32", "Gauge32", "Bits", "ObjectIdentity", "TimeTicks", "ModuleIdentity", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention, TimeStamp, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TimeStamp", "TruthValue")
ciscoFCCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 365))
ciscoFCCMIB.setRevisions(('2004-07-08 00:00', '2004-02-25 00:00', '2003-08-06 00:00', '2003-05-26 00:00',))
if mibBuilder.loadTexts: ciscoFCCMIB.setLastUpdated('200407080000Z')
if mibBuilder.loadTexts: ciscoFCCMIB.setOrganization('Cisco Systems, Inc.')
ciscoFCCMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 365, 0))
ciscoFCCMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 365, 1))
ciscoFCCMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 365, 2))
cFCCConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 1))
cFCCPortEntries = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 2))
cFCCNotifObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 3))
class CiscoFCCCongestionState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("noCongestion", 1), ("congested", 2), ("severelyCongested", 3))

cFCCEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cFCCEnable.setStatus('current')
cFCCPacketPriority = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cFCCPacketPriority.setStatus('current')
cFCCNotificationEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cFCCNotificationEnable.setStatus('current')
cFCCPortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 2, 1), )
if mibBuilder.loadTexts: cFCCPortTable.setStatus('current')
cFCCPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cFCCPortEntry.setStatus('current')
cFCCEdgeQuenchPktsRecd = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 2, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cFCCEdgeQuenchPktsRecd.setStatus('current')
cFCCEdgeQuenchPktsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cFCCEdgeQuenchPktsSent.setStatus('current')
cFCCPathQuenchPktsRecd = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cFCCPathQuenchPktsRecd.setStatus('current')
cFCCPathQuenchPktsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cFCCPathQuenchPktsSent.setStatus('current')
cFCCCurrentCongestionState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 2, 1, 1, 5), CiscoFCCCongestionState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cFCCCurrentCongestionState.setStatus('current')
cFCCLastCongestedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 2, 1, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cFCCLastCongestedTime.setStatus('current')
cFCCLastCongestionStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 2, 1, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cFCCLastCongestionStartTime.setStatus('current')
cFCCIsRateLimitingApplied = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 2, 1, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cFCCIsRateLimitingApplied.setStatus('current')
cFCCCongestionSourceID = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 3, 1), FcAddressId()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cFCCCongestionSourceID.setStatus('current')
cFCCCongestionDestinationID = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 3, 2), FcAddressId()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cFCCCongestionDestinationID.setStatus('current')
cFCCCongestionNotifyVSANIndex = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 3, 3), VsanIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cFCCCongestionNotifyVSANIndex.setStatus('current')
cFCCCongestionState = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 365, 1, 3, 4), CiscoFCCCongestionState()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cFCCCongestionState.setStatus('current')
ciscoFCCCongestionStateChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 365, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("CISCO-FCC-MIB", "cFCCCongestionState"))
if mibBuilder.loadTexts: ciscoFCCCongestionStateChange.setStatus('current')
ciscoFCCCongestionRateLimitStart = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 365, 0, 2)).setObjects(("IF-MIB", "ifIndex"), ("CISCO-FCC-MIB", "cFCCCongestionSourceID"), ("CISCO-FCC-MIB", "cFCCCongestionDestinationID"), ("CISCO-FCC-MIB", "cFCCCongestionNotifyVSANIndex"))
if mibBuilder.loadTexts: ciscoFCCCongestionRateLimitStart.setStatus('current')
ciscoFCCCongestionRateLimitEnd = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 365, 0, 3)).setObjects(("IF-MIB", "ifIndex"), ("CISCO-FCC-MIB", "cFCCCongestionSourceID"), ("CISCO-FCC-MIB", "cFCCCongestionDestinationID"), ("CISCO-FCC-MIB", "cFCCCongestionNotifyVSANIndex"))
if mibBuilder.loadTexts: ciscoFCCCongestionRateLimitEnd.setStatus('current')
ciscoFCCMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 365, 2, 1))
ciscoFCCMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 365, 2, 2))
ciscoFCCMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 365, 2, 1, 1)).setObjects(("CISCO-FCC-MIB", "cFCCConfigurationGroup"), ("CISCO-FCC-MIB", "cFCCPortEntriesGroup"), ("CISCO-FCC-MIB", "cFCCNotificationObjectsGroup"), ("CISCO-FCC-MIB", "cFCCNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFCCMIBCompliance = ciscoFCCMIBCompliance.setStatus('deprecated')
ciscoFCCMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 365, 2, 1, 2)).setObjects(("CISCO-FCC-MIB", "cFCCConfigurationGroup"), ("CISCO-FCC-MIB", "cFCCPortEntriesGroupRev1"), ("CISCO-FCC-MIB", "cFCCNotificationObjectsGroup"), ("CISCO-FCC-MIB", "cFCCNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFCCMIBComplianceRev1 = ciscoFCCMIBComplianceRev1.setStatus('current')
cFCCConfigurationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 365, 2, 2, 1)).setObjects(("CISCO-FCC-MIB", "cFCCEnable"), ("CISCO-FCC-MIB", "cFCCPacketPriority"), ("CISCO-FCC-MIB", "cFCCNotificationEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cFCCConfigurationGroup = cFCCConfigurationGroup.setStatus('current')
cFCCPortEntriesGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 365, 2, 2, 2)).setObjects(("CISCO-FCC-MIB", "cFCCEdgeQuenchPktsRecd"), ("CISCO-FCC-MIB", "cFCCEdgeQuenchPktsSent"), ("CISCO-FCC-MIB", "cFCCPathQuenchPktsRecd"), ("CISCO-FCC-MIB", "cFCCPathQuenchPktsSent"), ("CISCO-FCC-MIB", "cFCCCurrentCongestionState"), ("CISCO-FCC-MIB", "cFCCLastCongestedTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cFCCPortEntriesGroup = cFCCPortEntriesGroup.setStatus('deprecated')
cFCCNotificationObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 365, 2, 2, 3)).setObjects(("CISCO-FCC-MIB", "cFCCCongestionDestinationID"), ("CISCO-FCC-MIB", "cFCCCongestionSourceID"), ("CISCO-FCC-MIB", "cFCCCongestionNotifyVSANIndex"), ("CISCO-FCC-MIB", "cFCCCongestionState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cFCCNotificationObjectsGroup = cFCCNotificationObjectsGroup.setStatus('current')
cFCCNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 365, 2, 2, 4)).setObjects(("CISCO-FCC-MIB", "ciscoFCCCongestionStateChange"), ("CISCO-FCC-MIB", "ciscoFCCCongestionRateLimitStart"), ("CISCO-FCC-MIB", "ciscoFCCCongestionRateLimitEnd"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cFCCNotificationGroup = cFCCNotificationGroup.setStatus('current')
cFCCPortEntriesGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 365, 2, 2, 5)).setObjects(("CISCO-FCC-MIB", "cFCCEdgeQuenchPktsRecd"), ("CISCO-FCC-MIB", "cFCCEdgeQuenchPktsSent"), ("CISCO-FCC-MIB", "cFCCPathQuenchPktsRecd"), ("CISCO-FCC-MIB", "cFCCPathQuenchPktsSent"), ("CISCO-FCC-MIB", "cFCCCurrentCongestionState"), ("CISCO-FCC-MIB", "cFCCLastCongestedTime"), ("CISCO-FCC-MIB", "cFCCLastCongestionStartTime"), ("CISCO-FCC-MIB", "cFCCIsRateLimitingApplied"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cFCCPortEntriesGroupRev1 = cFCCPortEntriesGroupRev1.setStatus('current')
mibBuilder.exportSymbols("CISCO-FCC-MIB", cFCCLastCongestionStartTime=cFCCLastCongestionStartTime, cFCCCongestionDestinationID=cFCCCongestionDestinationID, cFCCEdgeQuenchPktsRecd=cFCCEdgeQuenchPktsRecd, cFCCLastCongestedTime=cFCCLastCongestedTime, cFCCPortEntries=cFCCPortEntries, cFCCCurrentCongestionState=cFCCCurrentCongestionState, cFCCConfigurationGroup=cFCCConfigurationGroup, cFCCPacketPriority=cFCCPacketPriority, cFCCPortTable=cFCCPortTable, cFCCPathQuenchPktsRecd=cFCCPathQuenchPktsRecd, ciscoFCCMIBNotifs=ciscoFCCMIBNotifs, ciscoFCCCongestionRateLimitStart=ciscoFCCCongestionRateLimitStart, PYSNMP_MODULE_ID=ciscoFCCMIB, ciscoFCCCongestionStateChange=ciscoFCCCongestionStateChange, cFCCNotifObjects=cFCCNotifObjects, cFCCNotificationEnable=cFCCNotificationEnable, cFCCIsRateLimitingApplied=cFCCIsRateLimitingApplied, cFCCCongestionState=cFCCCongestionState, ciscoFCCMIBCompliances=ciscoFCCMIBCompliances, cFCCNotificationObjectsGroup=cFCCNotificationObjectsGroup, ciscoFCCMIBConformance=ciscoFCCMIBConformance, cFCCEnable=cFCCEnable, cFCCCongestionNotifyVSANIndex=cFCCCongestionNotifyVSANIndex, ciscoFCCCongestionRateLimitEnd=ciscoFCCCongestionRateLimitEnd, ciscoFCCMIBCompliance=ciscoFCCMIBCompliance, cFCCPortEntriesGroup=cFCCPortEntriesGroup, ciscoFCCMIBObjects=ciscoFCCMIBObjects, CiscoFCCCongestionState=CiscoFCCCongestionState, ciscoFCCMIBComplianceRev1=ciscoFCCMIBComplianceRev1, cFCCPortEntry=cFCCPortEntry, ciscoFCCMIB=ciscoFCCMIB, cFCCEdgeQuenchPktsSent=cFCCEdgeQuenchPktsSent, cFCCCongestionSourceID=cFCCCongestionSourceID, cFCCNotificationGroup=cFCCNotificationGroup, cFCCConfig=cFCCConfig, ciscoFCCMIBGroups=ciscoFCCMIBGroups, cFCCPortEntriesGroupRev1=cFCCPortEntriesGroupRev1, cFCCPathQuenchPktsSent=cFCCPathQuenchPktsSent)
