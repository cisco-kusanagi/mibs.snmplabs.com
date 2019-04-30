#
# PySNMP MIB module CISCO-ERR-DISABLE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ERR-DISABLE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:40:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
VlanIndexOrZero, = mibBuilder.importSymbols("CISCO-PRIVATE-VLAN-MIB", "VlanIndexOrZero")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
TimeIntervalSec, = mibBuilder.importSymbols("CISCO-TC", "TimeIntervalSec")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Gauge32, ObjectIdentity, Bits, Counter64, iso, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32, ModuleIdentity, NotificationType, TimeTicks, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "Bits", "Counter64", "iso", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32", "ModuleIdentity", "NotificationType", "TimeTicks", "Counter32")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoErrDisableMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 548))
ciscoErrDisableMIB.setRevisions(('2016-06-02 00:00', '2013-04-23 00:00', '2010-10-19 00:00', '2009-03-23 00:00', '2008-04-07 00:00', '2006-05-31 00:00',))
if mibBuilder.loadTexts: ciscoErrDisableMIB.setLastUpdated('201606020000Z')
if mibBuilder.loadTexts: ciscoErrDisableMIB.setOrganization('Cisco Systems, Inc.')
ciscoErrDisableMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 548, 0))
ciscoErrDisableMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 548, 1))
ciscoErrDisableMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 548, 2))
cErrDisableGlobalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 1))
cErrDisableFeatureObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 2))
cErrDisableIfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 3))
class CErrDisableFeatureID(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61))
    namedValues = NamedValues(("udld", 1), ("bpduGuard", 2), ("channelMisconfig", 3), ("pagpFlap", 4), ("dtpFlap", 5), ("linkFlap", 6), ("l2ptGuard", 7), ("dot1xSecurityViolation", 8), ("portSecurityViolation", 9), ("gbicInvalid", 10), ("dhcpRateLimit", 11), ("unicastFlood", 12), ("vmps", 13), ("stormControl", 14), ("inlinePower", 15), ("arpInspection", 16), ("portLoopback", 17), ("packetBuffer", 18), ("macLimit", 19), ("linkMonitorFailure", 20), ("oamRemoteFailure", 21), ("dot1adIncompEtype", 22), ("dot1adIncompTunnel", 23), ("sfpConfigMismatch", 24), ("communityLimit", 25), ("invalidPolicy", 26), ("lsGroup", 27), ("ekey", 28), ("portModeFailure", 29), ("pppoeIaRateLimit", 30), ("oamRemoteCriticalEvent", 31), ("oamRemoteDyingGasp", 32), ("oamRemoteLinkFault", 33), ("mvrp", 34), ("tranceiverIncomp", 35), ("other", 36), ("portReinitLimitReached", 37), ("adminRxBBCreditPerfBufIncomp", 38), ("ficonNotEnabled", 39), ("adminModeIncomp", 40), ("adminSpeedIncomp", 41), ("adminRxBBCreditIncomp", 42), ("adminRxBufSizeIncomp", 43), ("eppFailure", 44), ("osmEPortUp", 45), ("osmNonEPortUp", 46), ("udldUniDir", 47), ("udldTxRxLoop", 48), ("udldNeighbourMismatch", 49), ("udldEmptyEcho", 50), ("udldAggrasiveModeLinkFailed", 51), ("excessivePortInterrupts", 52), ("channelErrDisabled", 53), ("hwProgFailed", 54), ("internalHandshakeFailed", 55), ("stpInconsistencyOnVpcPeerLink", 56), ("stpPortStateFailure", 57), ("ipConflict", 58), ("multipleMSapIdsRcvd", 59), ("oneHundredPdusWithoutAck", 60), ("ipQosCompatCheckFailure", 61))

cErrDisableRecoveryInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 1, 1), TimeIntervalSec()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cErrDisableRecoveryInterval.setStatus('current')
cErrDisableNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cErrDisableNotifEnable.setStatus('current')
cErrDisableNotifRate = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 1, 3), Unsigned32()).setUnits('Notification/Minute').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cErrDisableNotifRate.setStatus('current')
cErrDisableFeatureTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 2, 1), )
if mibBuilder.loadTexts: cErrDisableFeatureTable.setStatus('current')
cErrDisableFeatureEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-ERR-DISABLE-MIB", "cErrDisableFeatureIndex"))
if mibBuilder.loadTexts: cErrDisableFeatureEntry.setStatus('current')
cErrDisableFeatureIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 2, 1, 1, 1), CErrDisableFeatureID())
if mibBuilder.loadTexts: cErrDisableFeatureIndex.setStatus('current')
cErrDisableFeatureConfigurable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 2, 1, 1, 2), Bits().clone(namedValues=NamedValues(("detectionEnable", 0), ("recoveryEnable", 1), ("recoveryInterval", 2), ("detectShutdownVlan", 3), ("flapControl", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cErrDisableFeatureConfigurable.setStatus('current')
cErrDisableFeatureDetectEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 2, 1, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cErrDisableFeatureDetectEnable.setStatus('current')
cErrDisableFeatureRecoveryEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 2, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cErrDisableFeatureRecoveryEnable.setStatus('current')
cErrDisableFeatureRecoveryInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 2, 1, 1, 5), TimeIntervalSec()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cErrDisableFeatureRecoveryInterval.setStatus('current')
cErrDisableFeatureDetectShutdownVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 2, 1, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cErrDisableFeatureDetectShutdownVlan.setStatus('current')
cErrDisableFeatureMaxFlapCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 2, 1, 1, 7), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cErrDisableFeatureMaxFlapCount.setStatus('current')
cErrDisableFeatureFlapTimePeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 2, 1, 1, 8), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cErrDisableFeatureFlapTimePeriod.setStatus('current')
cErrDisableIfStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 3, 1), )
if mibBuilder.loadTexts: cErrDisableIfStatusTable.setStatus('current')
cErrDisableIfStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-ERR-DISABLE-MIB", "cErrDisableIfStatusVlanIndex"))
if mibBuilder.loadTexts: cErrDisableIfStatusEntry.setStatus('current')
cErrDisableIfStatusVlanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 3, 1, 1, 1), VlanIndexOrZero())
if mibBuilder.loadTexts: cErrDisableIfStatusVlanIndex.setStatus('current')
cErrDisableIfStatusCause = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 3, 1, 1, 2), CErrDisableFeatureID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cErrDisableIfStatusCause.setStatus('current')
cErrDisableIfStatusTimeToRecover = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 3, 1, 1, 3), TimeIntervalSec()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cErrDisableIfStatusTimeToRecover.setStatus('current')
cErrDisableNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 548, 0, 1))
cErrDisableInterfaceEvent = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 548, 0, 1, 1)).setObjects(("CISCO-ERR-DISABLE-MIB", "cErrDisableIfStatusCause"))
if mibBuilder.loadTexts: cErrDisableInterfaceEvent.setStatus('deprecated')
cErrDisableInterfaceEventRev1 = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 548, 0, 2)).setObjects(("CISCO-ERR-DISABLE-MIB", "cErrDisableIfStatusCause"))
if mibBuilder.loadTexts: cErrDisableInterfaceEventRev1.setStatus('current')
ciscoErrDisableMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 548, 2, 1))
ciscoErrDisableMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 548, 2, 2))
ciscoErrDisableMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 548, 2, 1, 1)).setObjects(("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableGlobalCfgGroup"), ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableFeatureCfgGroup"), ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableIfStatusGroup"), ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableNotifCfgGroup"), ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoErrDisableMIBCompliance = ciscoErrDisableMIBCompliance.setStatus('deprecated')
ciscoErrDisableMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 548, 2, 1, 2)).setObjects(("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableGlobalCfgGroup"), ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableFeatureCfgGroup"), ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableIfStatusGroup"), ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableNotifCfgGroup"), ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableNotifGroupRev1"), ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableShutdownVlanGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoErrDisableMIBComplianceRev1 = ciscoErrDisableMIBComplianceRev1.setStatus('deprecated')
ciscoErrDisableMIBComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 548, 2, 1, 3)).setObjects(("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableGlobalCfgGroup"), ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableFeatureCfgGroup"), ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableIfStatusGroup"), ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableNotifCfgGroup"), ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableNotifGroupRev1"), ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableShutdownVlanGroup"), ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableFeatureFlapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoErrDisableMIBComplianceRev2 = ciscoErrDisableMIBComplianceRev2.setStatus('current')
ciscoErrDisableGlobalCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 548, 2, 2, 1)).setObjects(("CISCO-ERR-DISABLE-MIB", "cErrDisableRecoveryInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoErrDisableGlobalCfgGroup = ciscoErrDisableGlobalCfgGroup.setStatus('current')
ciscoErrDisableFeatureCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 548, 2, 2, 2)).setObjects(("CISCO-ERR-DISABLE-MIB", "cErrDisableFeatureConfigurable"), ("CISCO-ERR-DISABLE-MIB", "cErrDisableFeatureDetectEnable"), ("CISCO-ERR-DISABLE-MIB", "cErrDisableFeatureRecoveryEnable"), ("CISCO-ERR-DISABLE-MIB", "cErrDisableFeatureRecoveryInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoErrDisableFeatureCfgGroup = ciscoErrDisableFeatureCfgGroup.setStatus('current')
ciscoErrDisableIfStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 548, 2, 2, 3)).setObjects(("CISCO-ERR-DISABLE-MIB", "cErrDisableIfStatusCause"), ("CISCO-ERR-DISABLE-MIB", "cErrDisableIfStatusTimeToRecover"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoErrDisableIfStatusGroup = ciscoErrDisableIfStatusGroup.setStatus('current')
ciscoErrDisableNotifCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 548, 2, 2, 4)).setObjects(("CISCO-ERR-DISABLE-MIB", "cErrDisableNotifEnable"), ("CISCO-ERR-DISABLE-MIB", "cErrDisableNotifRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoErrDisableNotifCfgGroup = ciscoErrDisableNotifCfgGroup.setStatus('current')
ciscoErrDisableNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 548, 2, 2, 5)).setObjects(("CISCO-ERR-DISABLE-MIB", "cErrDisableInterfaceEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoErrDisableNotifGroup = ciscoErrDisableNotifGroup.setStatus('deprecated')
ciscoErrDisableNotifGroupRev1 = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 548, 2, 2, 6)).setObjects(("CISCO-ERR-DISABLE-MIB", "cErrDisableInterfaceEventRev1"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoErrDisableNotifGroupRev1 = ciscoErrDisableNotifGroupRev1.setStatus('current')
ciscoErrDisableShutdownVlanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 548, 2, 2, 7)).setObjects(("CISCO-ERR-DISABLE-MIB", "cErrDisableFeatureDetectShutdownVlan"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoErrDisableShutdownVlanGroup = ciscoErrDisableShutdownVlanGroup.setStatus('current')
ciscoErrDisableFeatureFlapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 548, 2, 2, 8)).setObjects(("CISCO-ERR-DISABLE-MIB", "cErrDisableFeatureMaxFlapCount"), ("CISCO-ERR-DISABLE-MIB", "cErrDisableFeatureFlapTimePeriod"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoErrDisableFeatureFlapGroup = ciscoErrDisableFeatureFlapGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ERR-DISABLE-MIB", cErrDisableFeatureConfigurable=cErrDisableFeatureConfigurable, cErrDisableRecoveryInterval=cErrDisableRecoveryInterval, ciscoErrDisableMIBCompliance=ciscoErrDisableMIBCompliance, ciscoErrDisableMIBComplianceRev1=ciscoErrDisableMIBComplianceRev1, ciscoErrDisableMIBConform=ciscoErrDisableMIBConform, cErrDisableIfStatusEntry=cErrDisableIfStatusEntry, cErrDisableGlobalObjects=cErrDisableGlobalObjects, ciscoErrDisableFeatureCfgGroup=ciscoErrDisableFeatureCfgGroup, ciscoErrDisableNotifCfgGroup=ciscoErrDisableNotifCfgGroup, ciscoErrDisableMIBGroups=ciscoErrDisableMIBGroups, cErrDisableFeatureMaxFlapCount=cErrDisableFeatureMaxFlapCount, cErrDisableNotifEnable=cErrDisableNotifEnable, cErrDisableInterfaceEventRev1=cErrDisableInterfaceEventRev1, cErrDisableIfStatusTable=cErrDisableIfStatusTable, cErrDisableFeatureTable=cErrDisableFeatureTable, cErrDisableFeatureObjects=cErrDisableFeatureObjects, cErrDisableFeatureRecoveryEnable=cErrDisableFeatureRecoveryEnable, ciscoErrDisableMIBNotifs=ciscoErrDisableMIBNotifs, ciscoErrDisableNotifGroup=ciscoErrDisableNotifGroup, cErrDisableIfStatusVlanIndex=cErrDisableIfStatusVlanIndex, ciscoErrDisableMIBComplianceRev2=ciscoErrDisableMIBComplianceRev2, ciscoErrDisableFeatureFlapGroup=ciscoErrDisableFeatureFlapGroup, cErrDisableFeatureIndex=cErrDisableFeatureIndex, cErrDisableInterfaceEvent=cErrDisableInterfaceEvent, cErrDisableFeatureDetectEnable=cErrDisableFeatureDetectEnable, cErrDisableIfStatusTimeToRecover=cErrDisableIfStatusTimeToRecover, cErrDisableNotifRate=cErrDisableNotifRate, cErrDisableFeatureEntry=cErrDisableFeatureEntry, ciscoErrDisableMIBObjects=ciscoErrDisableMIBObjects, cErrDisableIfStatusCause=cErrDisableIfStatusCause, PYSNMP_MODULE_ID=ciscoErrDisableMIB, ciscoErrDisableShutdownVlanGroup=ciscoErrDisableShutdownVlanGroup, ciscoErrDisableMIB=ciscoErrDisableMIB, cErrDisableIfObjects=cErrDisableIfObjects, cErrDisableNotificationsPrefix=cErrDisableNotificationsPrefix, ciscoErrDisableMIBCompliances=ciscoErrDisableMIBCompliances, ciscoErrDisableIfStatusGroup=ciscoErrDisableIfStatusGroup, ciscoErrDisableGlobalCfgGroup=ciscoErrDisableGlobalCfgGroup, CErrDisableFeatureID=CErrDisableFeatureID, cErrDisableFeatureDetectShutdownVlan=cErrDisableFeatureDetectShutdownVlan, ciscoErrDisableNotifGroupRev1=ciscoErrDisableNotifGroupRev1, cErrDisableFeatureFlapTimePeriod=cErrDisableFeatureFlapTimePeriod, cErrDisableFeatureRecoveryInterval=cErrDisableFeatureRecoveryInterval)
