#
# PySNMP MIB module RBN-SFP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBN-SFP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:53:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
IANAItuEventType, IANAItuProbableCause = mibBuilder.importSymbols("IANA-ITU-ALARM-TC-MIB", "IANAItuEventType", "IANAItuProbableCause")
ItuPerceivedSeverity, = mibBuilder.importSymbols("ITU-ALARM-TC-MIB", "ItuPerceivedSeverity")
RbnAlarmServiceAffecting, RbnAlarmId = mibBuilder.importSymbols("RBN-ALARM-TC", "RbnAlarmServiceAffecting", "RbnAlarmId")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
RbnSlot, RbnPort = mibBuilder.importSymbols("RBN-TC", "RbnSlot", "RbnPort")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
NotificationType, Bits, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Integer32, MibIdentifier, ModuleIdentity, Counter64, Gauge32, Unsigned32, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Integer32", "MibIdentifier", "ModuleIdentity", "Counter64", "Gauge32", "Unsigned32", "TimeTicks", "iso")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
rbnSfpMonMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 49))
rbnSfpMonMIB.setRevisions(('2008-08-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rbnSfpMonMIB.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: rbnSfpMonMIB.setLastUpdated('200808200000Z')
if mibBuilder.loadTexts: rbnSfpMonMIB.setOrganization('RedBack Networks, Inc.')
if mibBuilder.loadTexts: rbnSfpMonMIB.setContactInfo(' RedBack Networks, Inc. Postal: 300 Holger Way San Jose, CA 95134 USA Phone: +1 408 750 5000 Fax: +1 408 750 5599 E-mail: mib-info@redback.com')
if mibBuilder.loadTexts: rbnSfpMonMIB.setDescription('The MIB used to manage the SFP (Small Form Factor Pluggable) on RedBack Networks devices.')
rbnSfpMonMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 49, 0))
rbnSfpMonMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 49, 1))
rbnSfpMonMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 49, 2))
rbnSfpAlarmActiveTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 49, 1, 1), )
if mibBuilder.loadTexts: rbnSfpAlarmActiveTable.setStatus('current')
if mibBuilder.loadTexts: rbnSfpAlarmActiveTable.setDescription('This table contains the SFP alarms currently active on the SFP.')
rbnSfpAlarmActiveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 49, 1, 1, 1), ).setIndexNames((0, "RBN-SFP-MIB", "rbnSfpActiveAlarmIndex"))
if mibBuilder.loadTexts: rbnSfpAlarmActiveEntry.setStatus('current')
if mibBuilder.loadTexts: rbnSfpAlarmActiveEntry.setDescription('Entries appear in this table when alarms are raised. They are removed when the alarms are cleared.')
rbnSfpActiveAlarmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 49, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: rbnSfpActiveAlarmIndex.setStatus('current')
if mibBuilder.loadTexts: rbnSfpActiveAlarmIndex.setDescription('A monotonically increasing integer index. It wraps back to 1 after it reaches its maximum value.')
rbnSfpAlarmCardSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 49, 1, 1, 1, 2), RbnSlot()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnSfpAlarmCardSlot.setStatus('current')
if mibBuilder.loadTexts: rbnSfpAlarmCardSlot.setDescription('The chassis slot number in which the card is present where the SFP plugged in.')
rbnSfpAlarmPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 49, 1, 1, 1, 3), RbnPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnSfpAlarmPort.setStatus('current')
if mibBuilder.loadTexts: rbnSfpAlarmPort.setDescription('The port number where the SFP plugged in.')
rbnSfpAlarmId = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 49, 1, 1, 1, 4), RbnAlarmId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnSfpAlarmId.setStatus('current')
if mibBuilder.loadTexts: rbnSfpAlarmId.setDescription('An identifier for the alarm.')
rbnSfpAlarmSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 49, 1, 1, 1, 5), ItuPerceivedSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnSfpAlarmSeverity.setStatus('current')
if mibBuilder.loadTexts: rbnSfpAlarmSeverity.setDescription('The perceived severity of the alarm.')
rbnSfpAlarmType = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 49, 1, 1, 1, 6), IANAItuEventType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnSfpAlarmType.setStatus('current')
if mibBuilder.loadTexts: rbnSfpAlarmType.setDescription('The type of the alarm.')
rbnSfpAlarmDateAndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 49, 1, 1, 1, 7), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnSfpAlarmDateAndTime.setStatus('current')
if mibBuilder.loadTexts: rbnSfpAlarmDateAndTime.setDescription('The local date and time when the alarm was raised')
rbnSfpAlarmDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 49, 1, 1, 1, 8), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnSfpAlarmDescription.setStatus('current')
if mibBuilder.loadTexts: rbnSfpAlarmDescription.setDescription('A text string which conveys additional information about the alarm.')
rbnSfpAlarmProbableCause = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 49, 1, 1, 1, 9), IANAItuProbableCause()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnSfpAlarmProbableCause.setStatus('current')
if mibBuilder.loadTexts: rbnSfpAlarmProbableCause.setDescription('The probable cause for this alarm.')
rbnSfpAlarmServiceAffecting = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 49, 1, 1, 1, 10), RbnAlarmServiceAffecting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnSfpAlarmServiceAffecting.setStatus('current')
if mibBuilder.loadTexts: rbnSfpAlarmServiceAffecting.setDescription('Indicates whether the alarm is perceived to be service impacting.')
rbnSfpAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 49, 0, 1)).setObjects(("RBN-SFP-MIB", "rbnSfpAlarmCardSlot"), ("RBN-SFP-MIB", "rbnSfpAlarmPort"), ("RBN-SFP-MIB", "rbnSfpAlarmId"), ("RBN-SFP-MIB", "rbnSfpAlarmSeverity"), ("RBN-SFP-MIB", "rbnSfpAlarmType"), ("RBN-SFP-MIB", "rbnSfpAlarmDateAndTime"), ("RBN-SFP-MIB", "rbnSfpAlarmDescription"), ("RBN-SFP-MIB", "rbnSfpAlarmProbableCause"))
if mibBuilder.loadTexts: rbnSfpAlarm.setStatus('current')
if mibBuilder.loadTexts: rbnSfpAlarm.setDescription('An rbnSfpAlarm notification signifies that an alarm has been raised or cleared on a SFP')
rbnSfpMonMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 49, 2, 1))
rbnSfpMonMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 49, 2, 2))
rbnSfpMonMIBObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 49, 2, 1, 1)).setObjects(("RBN-SFP-MIB", "rbnSfpAlarmCardSlot"), ("RBN-SFP-MIB", "rbnSfpAlarmPort"), ("RBN-SFP-MIB", "rbnSfpAlarmId"), ("RBN-SFP-MIB", "rbnSfpAlarmType"), ("RBN-SFP-MIB", "rbnSfpAlarmDateAndTime"), ("RBN-SFP-MIB", "rbnSfpAlarmDescription"), ("RBN-SFP-MIB", "rbnSfpAlarmProbableCause"), ("RBN-SFP-MIB", "rbnSfpAlarmSeverity"), ("RBN-SFP-MIB", "rbnSfpAlarmServiceAffecting"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnSfpMonMIBObjectGroup = rbnSfpMonMIBObjectGroup.setStatus('current')
if mibBuilder.loadTexts: rbnSfpMonMIBObjectGroup.setDescription('A collection of objects providing active SFP Alarm information')
rbnSfpMonMIBNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2352, 2, 49, 2, 1, 2)).setObjects(("RBN-SFP-MIB", "rbnSfpAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnSfpMonMIBNotificationGroup = rbnSfpMonMIBNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: rbnSfpMonMIBNotificationGroup.setDescription('A collection of notifications providing SFP fault condition')
rbnSfpMonMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 49, 2, 2, 1)).setObjects(("RBN-SFP-MIB", "rbnSfpMonMIBObjectGroup"), ("RBN-SFP-MIB", "rbnSfpMonMIBNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnSfpMonMIBCompliance = rbnSfpMonMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: rbnSfpMonMIBCompliance.setDescription('The compliance statement for the Sfp active alarm MIB')
mibBuilder.exportSymbols("RBN-SFP-MIB", rbnSfpAlarmDateAndTime=rbnSfpAlarmDateAndTime, rbnSfpAlarmActiveEntry=rbnSfpAlarmActiveEntry, rbnSfpMonMIBGroups=rbnSfpMonMIBGroups, rbnSfpAlarmServiceAffecting=rbnSfpAlarmServiceAffecting, rbnSfpMonMIBCompliances=rbnSfpMonMIBCompliances, rbnSfpMonMIBConformance=rbnSfpMonMIBConformance, rbnSfpAlarmActiveTable=rbnSfpAlarmActiveTable, rbnSfpMonMIBNotificationGroup=rbnSfpMonMIBNotificationGroup, rbnSfpMonMIBObjectGroup=rbnSfpMonMIBObjectGroup, rbnSfpAlarmCardSlot=rbnSfpAlarmCardSlot, rbnSfpMonMIBCompliance=rbnSfpMonMIBCompliance, rbnSfpMonMIBNotifications=rbnSfpMonMIBNotifications, rbnSfpMonMIBObjects=rbnSfpMonMIBObjects, rbnSfpAlarm=rbnSfpAlarm, rbnSfpAlarmDescription=rbnSfpAlarmDescription, rbnSfpAlarmId=rbnSfpAlarmId, rbnSfpAlarmPort=rbnSfpAlarmPort, rbnSfpAlarmProbableCause=rbnSfpAlarmProbableCause, rbnSfpMonMIB=rbnSfpMonMIB, PYSNMP_MODULE_ID=rbnSfpMonMIB, rbnSfpAlarmSeverity=rbnSfpAlarmSeverity, rbnSfpAlarmType=rbnSfpAlarmType, rbnSfpActiveAlarmIndex=rbnSfpActiveAlarmIndex)
