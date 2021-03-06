#
# PySNMP MIB module CISCO-UNITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-UNITY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:01:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Integer32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, iso, Gauge32, ModuleIdentity, TimeTicks, Unsigned32, NotificationType, Counter32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Integer32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "iso", "Gauge32", "ModuleIdentity", "TimeTicks", "Unsigned32", "NotificationType", "Counter32", "Counter64")
TruthValue, TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DateAndTime", "DisplayString")
ciscoUnityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 385))
ciscoUnityMIB.setRevisions(('2005-12-12 00:00', '2004-01-06 00:00',))
if mibBuilder.loadTexts: ciscoUnityMIB.setLastUpdated('200512120000Z')
if mibBuilder.loadTexts: ciscoUnityMIB.setOrganization('Cisco Systems, Inc.')
class CiscoUnityIndex(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class CiscoUnityServerStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("stopped", 1), ("starting", 2), ("running", 3), ("stopping", 4))

ciscoUnityMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 385, 0))
ciscoUnityMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 385, 1))
ciscoUnityMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 385, 2))
ciscoUnityGeneralInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 1))
ciscoUnityGlobalInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2))
ciscoUnityNotificationsInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 3))
ciscoUnityTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 1, 1), )
if mibBuilder.loadTexts: ciscoUnityTable.setStatus('current')
ciscoUnityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-UNITY-MIB", "ciscoUnityIndex"))
if mibBuilder.loadTexts: ciscoUnityEntry.setStatus('current')
ciscoUnityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 1, 1, 1, 1), CiscoUnityIndex())
if mibBuilder.loadTexts: ciscoUnityIndex.setStatus('current')
ciscoUnityName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 1, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoUnityName.setStatus('current')
ciscoUnityVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 1, 1, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoUnityVersion.setStatus('current')
ciscoUnityPortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 1, 2), )
if mibBuilder.loadTexts: ciscoUnityPortTable.setStatus('current')
ciscoUnityPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-UNITY-MIB", "ciscoUnityPortIndex"))
if mibBuilder.loadTexts: ciscoUnityPortEntry.setStatus('current')
ciscoUnityPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 1, 2, 1, 1), CiscoUnityIndex())
if mibBuilder.loadTexts: ciscoUnityPortIndex.setStatus('current')
ciscoUnityPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 1, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoUnityPortNumber.setStatus('current')
ciscoUnityPortIntegration = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 1, 2, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoUnityPortIntegration.setStatus('current')
ciscoUnityPortExtension = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 1, 2, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoUnityPortExtension.setStatus('current')
ciscoUnityPortEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 1, 2, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoUnityPortEnabled.setStatus('current')
ciscoUnityPortAnswerCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 1, 2, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoUnityPortAnswerCalls.setStatus('current')
ciscoUnityPortMessageNotif = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 1, 2, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoUnityPortMessageNotif.setStatus('current')
ciscoUnityPortDialoutMWI = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 1, 2, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoUnityPortDialoutMWI.setStatus('current')
ciscoUnityPortAMISDelivery = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 1, 2, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoUnityPortAMISDelivery.setStatus('current')
ciscoUnityPortTRAPConnection = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 1, 2, 1, 10), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoUnityPortTRAPConnection.setStatus('current')
ciscoUnityPortActivity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 1, 2, 1, 11), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoUnityPortActivity.setStatus('current')
ciscoUnityPortObjectId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 1, 2, 1, 12), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 38))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoUnityPortObjectId.setStatus('current')
ciscoUnityServerState = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 1), CiscoUnityServerStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoUnityServerState.setStatus('current')
ciscoUnityPorts = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoUnityPorts.setStatus('current')
ciscoUnityPortsActive = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoUnityPortsActive.setStatus('current')
ciscoUnityPortsInbound = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoUnityPortsInbound.setStatus('current')
ciscoUnityPortsInboundActive = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoUnityPortsInboundActive.setStatus('current')
ciscoUnityPortsOutbound = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoUnityPortsOutbound.setStatus('current')
ciscoUnityPortsOutboundActive = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoUnityPortsOutboundActive.setStatus('current')
ciscoUnityLicLanguagesMax = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoUnityLicLanguagesMax.setStatus('current')
ciscoUnityLicTTSSessionsMax = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoUnityLicTTSSessionsMax.setStatus('current')
ciscoUnityLicSubscribersMax = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoUnityLicSubscribersMax.setStatus('current')
ciscoUnityLicUMSubscribersMax = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoUnityLicUMSubscribersMax.setStatus('current')
ciscoUnityLicVMISubscribersMax = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 12), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoUnityLicVMISubscribersMax.setStatus('current')
ciscoUnityLicVoicePortsMax = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoUnityLicVoicePortsMax.setStatus('current')
ciscoUnityLicBridgeSessionsMax = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 14), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoUnityLicBridgeSessionsMax.setStatus('current')
ciscoUnityLicAMISIsLicensed = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 15), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoUnityLicAMISIsLicensed.setStatus('current')
ciscoUnityLicMaxMsgRecLenIsLic = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 16), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoUnityLicMaxMsgRecLenIsLic.setStatus('current')
ciscoUnityLicPoolingIsEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 17), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoUnityLicPoolingIsEnabled.setStatus('current')
ciscoUnityLicVPIMIsLicensed = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 18), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoUnityLicVPIMIsLicensed.setStatus('current')
ciscoUnityLicPrimaryServerIsLic = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 19), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoUnityLicPrimaryServerIsLic.setStatus('current')
ciscoUnityLicSecondServerIsLic = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 20), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoUnityLicSecondServerIsLic.setStatus('current')
ciscoUnityLicUtilSecondServer = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 21), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoUnityLicUtilSecondServer.setStatus('current')
ciscoUnityLicUtilSubs = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 22), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoUnityLicUtilSubs.setStatus('current')
ciscoUnityLicUtilVMISubs = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 2, 23), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoUnityLicUtilVMISubs.setStatus('current')
ciscoUnityEventType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("error", 1), ("warning", 2), ("informational", 3)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ciscoUnityEventType.setStatus('current')
ciscoUnityEventSource = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 3, 2), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ciscoUnityEventSource.setStatus('current')
ciscoUnityEventCategory = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 3, 3), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ciscoUnityEventCategory.setStatus('current')
ciscoUnityEventId = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 3, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ciscoUnityEventId.setStatus('current')
ciscoUnityEventDate = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 3, 5), DateAndTime()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ciscoUnityEventDate.setStatus('current')
ciscoUnityEventUser = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 3, 6), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ciscoUnityEventUser.setStatus('current')
ciscoUnityEventComputer = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 3, 7), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ciscoUnityEventComputer.setStatus('current')
ciscoUnityEventDescription = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 3, 8), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ciscoUnityEventDescription.setStatus('current')
ciscoUnityEventEMSNotes = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 385, 1, 3, 9), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ciscoUnityEventEMSNotes.setStatus('current')
ciscoUnityMonitoredEvent = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 385, 0, 1)).setObjects(("CISCO-UNITY-MIB", "ciscoUnityEventType"), ("CISCO-UNITY-MIB", "ciscoUnityEventSource"), ("CISCO-UNITY-MIB", "ciscoUnityEventCategory"), ("CISCO-UNITY-MIB", "ciscoUnityEventId"), ("CISCO-UNITY-MIB", "ciscoUnityEventDate"), ("CISCO-UNITY-MIB", "ciscoUnityEventUser"), ("CISCO-UNITY-MIB", "ciscoUnityEventComputer"), ("CISCO-UNITY-MIB", "ciscoUnityEventDescription"), ("CISCO-UNITY-MIB", "ciscoUnityEventEMSNotes"))
if mibBuilder.loadTexts: ciscoUnityMonitoredEvent.setStatus('current')
ciscoUnityMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 385, 2, 1))
ciscoUnityMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 385, 2, 2))
ciscoUnityMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 385, 2, 1, 1)).setObjects(("CISCO-UNITY-MIB", "ciscoUnityInfoGroup"), ("CISCO-UNITY-MIB", "ciscoUnityNotificationsInfoGroup"), ("CISCO-UNITY-MIB", "ciscoUnityNotificationsGroup"), ("CISCO-UNITY-MIB", "ciscoUnityPortInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUnityMIBCompliance = ciscoUnityMIBCompliance.setStatus('deprecated')
ciscoUnityMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 385, 2, 1, 2)).setObjects(("CISCO-UNITY-MIB", "ciscoUnityInfoGroup"), ("CISCO-UNITY-MIB", "ciscoUnityNotificationsInfoGroup"), ("CISCO-UNITY-MIB", "ciscoUnityNotificationsGroup"), ("CISCO-UNITY-MIB", "ciscoUnityLicInfoGroup"), ("CISCO-UNITY-MIB", "ciscoUnityPortInfoGroup"), ("CISCO-UNITY-MIB", "ciscoUnityPortInfoGroup2"), ("CISCO-UNITY-MIB", "ciscoUnityPortInfoGroup3"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUnityMIBComplianceRev1 = ciscoUnityMIBComplianceRev1.setStatus('current')
ciscoUnityInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 385, 2, 2, 1)).setObjects(("CISCO-UNITY-MIB", "ciscoUnityName"), ("CISCO-UNITY-MIB", "ciscoUnityVersion"), ("CISCO-UNITY-MIB", "ciscoUnityServerState"), ("CISCO-UNITY-MIB", "ciscoUnityPorts"), ("CISCO-UNITY-MIB", "ciscoUnityPortsActive"), ("CISCO-UNITY-MIB", "ciscoUnityPortsInbound"), ("CISCO-UNITY-MIB", "ciscoUnityPortsInboundActive"), ("CISCO-UNITY-MIB", "ciscoUnityPortsOutbound"), ("CISCO-UNITY-MIB", "ciscoUnityPortsOutboundActive"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUnityInfoGroup = ciscoUnityInfoGroup.setStatus('current')
ciscoUnityPortInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 385, 2, 2, 2)).setObjects(("CISCO-UNITY-MIB", "ciscoUnityPortNumber"), ("CISCO-UNITY-MIB", "ciscoUnityPortIntegration"), ("CISCO-UNITY-MIB", "ciscoUnityPortExtension"), ("CISCO-UNITY-MIB", "ciscoUnityPortEnabled"), ("CISCO-UNITY-MIB", "ciscoUnityPortAnswerCalls"), ("CISCO-UNITY-MIB", "ciscoUnityPortMessageNotif"), ("CISCO-UNITY-MIB", "ciscoUnityPortDialoutMWI"), ("CISCO-UNITY-MIB", "ciscoUnityPortAMISDelivery"), ("CISCO-UNITY-MIB", "ciscoUnityPortTRAPConnection"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUnityPortInfoGroup = ciscoUnityPortInfoGroup.setStatus('current')
ciscoUnityNotificationsInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 385, 2, 2, 3)).setObjects(("CISCO-UNITY-MIB", "ciscoUnityEventType"), ("CISCO-UNITY-MIB", "ciscoUnityEventSource"), ("CISCO-UNITY-MIB", "ciscoUnityEventCategory"), ("CISCO-UNITY-MIB", "ciscoUnityEventId"), ("CISCO-UNITY-MIB", "ciscoUnityEventDate"), ("CISCO-UNITY-MIB", "ciscoUnityEventUser"), ("CISCO-UNITY-MIB", "ciscoUnityEventComputer"), ("CISCO-UNITY-MIB", "ciscoUnityEventDescription"), ("CISCO-UNITY-MIB", "ciscoUnityEventEMSNotes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUnityNotificationsInfoGroup = ciscoUnityNotificationsInfoGroup.setStatus('current')
ciscoUnityNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 385, 2, 2, 4)).setObjects(("CISCO-UNITY-MIB", "ciscoUnityMonitoredEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUnityNotificationsGroup = ciscoUnityNotificationsGroup.setStatus('current')
ciscoUnityLicInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 385, 2, 2, 5)).setObjects(("CISCO-UNITY-MIB", "ciscoUnityLicLanguagesMax"), ("CISCO-UNITY-MIB", "ciscoUnityLicTTSSessionsMax"), ("CISCO-UNITY-MIB", "ciscoUnityLicSubscribersMax"), ("CISCO-UNITY-MIB", "ciscoUnityLicUMSubscribersMax"), ("CISCO-UNITY-MIB", "ciscoUnityLicVMISubscribersMax"), ("CISCO-UNITY-MIB", "ciscoUnityLicVoicePortsMax"), ("CISCO-UNITY-MIB", "ciscoUnityLicBridgeSessionsMax"), ("CISCO-UNITY-MIB", "ciscoUnityLicAMISIsLicensed"), ("CISCO-UNITY-MIB", "ciscoUnityLicMaxMsgRecLenIsLic"), ("CISCO-UNITY-MIB", "ciscoUnityLicPoolingIsEnabled"), ("CISCO-UNITY-MIB", "ciscoUnityLicVPIMIsLicensed"), ("CISCO-UNITY-MIB", "ciscoUnityLicPrimaryServerIsLic"), ("CISCO-UNITY-MIB", "ciscoUnityLicSecondServerIsLic"), ("CISCO-UNITY-MIB", "ciscoUnityLicUtilSecondServer"), ("CISCO-UNITY-MIB", "ciscoUnityLicUtilSubs"), ("CISCO-UNITY-MIB", "ciscoUnityLicUtilVMISubs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUnityLicInfoGroup = ciscoUnityLicInfoGroup.setStatus('current')
ciscoUnityPortInfoGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 385, 2, 2, 6)).setObjects(("CISCO-UNITY-MIB", "ciscoUnityPortActivity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUnityPortInfoGroup2 = ciscoUnityPortInfoGroup2.setStatus('current')
ciscoUnityPortInfoGroup3 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 385, 2, 2, 7)).setObjects(("CISCO-UNITY-MIB", "ciscoUnityPortObjectId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUnityPortInfoGroup3 = ciscoUnityPortInfoGroup3.setStatus('current')
mibBuilder.exportSymbols("CISCO-UNITY-MIB", ciscoUnityMIBObjects=ciscoUnityMIBObjects, ciscoUnityTable=ciscoUnityTable, ciscoUnityServerState=ciscoUnityServerState, ciscoUnityPortNumber=ciscoUnityPortNumber, ciscoUnityPortsInbound=ciscoUnityPortsInbound, ciscoUnityPortsOutbound=ciscoUnityPortsOutbound, ciscoUnityLicBridgeSessionsMax=ciscoUnityLicBridgeSessionsMax, ciscoUnityLicAMISIsLicensed=ciscoUnityLicAMISIsLicensed, ciscoUnityPortInfoGroup3=ciscoUnityPortInfoGroup3, ciscoUnityLicVoicePortsMax=ciscoUnityLicVoicePortsMax, ciscoUnityPortsOutboundActive=ciscoUnityPortsOutboundActive, ciscoUnityLicTTSSessionsMax=ciscoUnityLicTTSSessionsMax, ciscoUnityEventEMSNotes=ciscoUnityEventEMSNotes, ciscoUnityEventUser=ciscoUnityEventUser, ciscoUnityLicSecondServerIsLic=ciscoUnityLicSecondServerIsLic, ciscoUnityLicPoolingIsEnabled=ciscoUnityLicPoolingIsEnabled, ciscoUnityPortInfoGroup=ciscoUnityPortInfoGroup, ciscoUnityEventType=ciscoUnityEventType, ciscoUnityEntry=ciscoUnityEntry, ciscoUnityLicSubscribersMax=ciscoUnityLicSubscribersMax, ciscoUnityPortAMISDelivery=ciscoUnityPortAMISDelivery, ciscoUnityMIBCompliances=ciscoUnityMIBCompliances, ciscoUnityLicLanguagesMax=ciscoUnityLicLanguagesMax, ciscoUnityPortActivity=ciscoUnityPortActivity, ciscoUnityMIBConform=ciscoUnityMIBConform, ciscoUnityNotificationsInfo=ciscoUnityNotificationsInfo, PYSNMP_MODULE_ID=ciscoUnityMIB, ciscoUnityPortEnabled=ciscoUnityPortEnabled, ciscoUnityPortAnswerCalls=ciscoUnityPortAnswerCalls, ciscoUnityIndex=ciscoUnityIndex, ciscoUnityLicPrimaryServerIsLic=ciscoUnityLicPrimaryServerIsLic, ciscoUnityLicUtilSubs=ciscoUnityLicUtilSubs, ciscoUnityPortsActive=ciscoUnityPortsActive, ciscoUnityPortTRAPConnection=ciscoUnityPortTRAPConnection, ciscoUnityMIBCompliance=ciscoUnityMIBCompliance, ciscoUnityMonitoredEvent=ciscoUnityMonitoredEvent, ciscoUnityLicMaxMsgRecLenIsLic=ciscoUnityLicMaxMsgRecLenIsLic, ciscoUnityEventCategory=ciscoUnityEventCategory, ciscoUnityPortEntry=ciscoUnityPortEntry, ciscoUnityLicInfoGroup=ciscoUnityLicInfoGroup, ciscoUnityNotificationsGroup=ciscoUnityNotificationsGroup, ciscoUnityEventSource=ciscoUnityEventSource, ciscoUnityInfoGroup=ciscoUnityInfoGroup, ciscoUnityPortObjectId=ciscoUnityPortObjectId, ciscoUnityPortTable=ciscoUnityPortTable, ciscoUnityPortIntegration=ciscoUnityPortIntegration, ciscoUnityPortExtension=ciscoUnityPortExtension, ciscoUnityMIBComplianceRev1=ciscoUnityMIBComplianceRev1, ciscoUnityLicUtilSecondServer=ciscoUnityLicUtilSecondServer, ciscoUnityName=ciscoUnityName, ciscoUnityLicUMSubscribersMax=ciscoUnityLicUMSubscribersMax, ciscoUnityMIBGroups=ciscoUnityMIBGroups, ciscoUnityPorts=ciscoUnityPorts, CiscoUnityServerStatus=CiscoUnityServerStatus, ciscoUnityGeneralInfo=ciscoUnityGeneralInfo, ciscoUnityPortIndex=ciscoUnityPortIndex, ciscoUnityMIB=ciscoUnityMIB, ciscoUnityGlobalInfo=ciscoUnityGlobalInfo, ciscoUnityLicUtilVMISubs=ciscoUnityLicUtilVMISubs, ciscoUnityLicVMISubscribersMax=ciscoUnityLicVMISubscribersMax, ciscoUnityEventDate=ciscoUnityEventDate, ciscoUnityVersion=ciscoUnityVersion, ciscoUnityPortsInboundActive=ciscoUnityPortsInboundActive, ciscoUnityEventId=ciscoUnityEventId, ciscoUnityMIBNotifs=ciscoUnityMIBNotifs, ciscoUnityPortMessageNotif=ciscoUnityPortMessageNotif, ciscoUnityEventComputer=ciscoUnityEventComputer, ciscoUnityLicVPIMIsLicensed=ciscoUnityLicVPIMIsLicensed, ciscoUnityEventDescription=ciscoUnityEventDescription, CiscoUnityIndex=CiscoUnityIndex, ciscoUnityPortInfoGroup2=ciscoUnityPortInfoGroup2, ciscoUnityPortDialoutMWI=ciscoUnityPortDialoutMWI, ciscoUnityNotificationsInfoGroup=ciscoUnityNotificationsInfoGroup)
