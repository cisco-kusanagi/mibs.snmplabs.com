#
# PySNMP MIB module ALPHA-NOTIFICATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALPHA-NOTIFICATION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:20:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
alarmModelDescription, alarmActiveModelPointer, alarmActiveResourceId = mibBuilder.importSymbols("ALARM-MIB", "alarmModelDescription", "alarmActiveModelPointer", "alarmActiveResourceId")
componentListStaticName, controllerInfoName, componentListReference, alpha = mibBuilder.importSymbols("ALPHA-RESOURCE-MIB", "componentListStaticName", "controllerInfoName", "componentListReference", "alpha")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
TimeTicks, iso, ModuleIdentity, ObjectIdentity, Gauge32, Unsigned32, IpAddress, Counter64, NotificationType, MibIdentifier, Counter32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "ModuleIdentity", "ObjectIdentity", "Gauge32", "Unsigned32", "IpAddress", "Counter64", "NotificationType", "MibIdentifier", "Counter32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
alphaAlarmNotifications = ModuleIdentity((1, 3, 6, 1, 4, 1, 7309, 100))
alphaAlarmNotifications.setRevisions(('2015-07-28 00:00', '2015-07-23 00:00', '2015-06-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: alphaAlarmNotifications.setRevisionsDescriptions((' Updated to follow MIB structure conformance rules. Tested with SimpleWeb: http://www.simpleweb.org Passed highest level of compliance. (level 6) ', 'Fixed MIB syntax warnings.', 'General revision.',))
if mibBuilder.loadTexts: alphaAlarmNotifications.setLastUpdated('201507280000Z')
if mibBuilder.loadTexts: alphaAlarmNotifications.setOrganization('Alpha Technologies Ltd.')
if mibBuilder.loadTexts: alphaAlarmNotifications.setContactInfo('Alpha Technologies Ltd. 7700 Riverfront Gate Burnaby, BC V5J 5M4 Canada Tel: 1-604-436-5900 Fax: 1-604-436-1233')
if mibBuilder.loadTexts: alphaAlarmNotifications.setDescription('This MIB defines the notification block(s) available in system controllers.')
alphaAlarmNotificationsExtension = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 101))
alphaAlarmActiveState = NotificationType((1, 3, 6, 1, 4, 1, 7309, 100, 1)).setObjects(("ALARM-MIB", "alarmActiveModelPointer"), ("ALARM-MIB", "alarmActiveResourceId"), ("ALPHA-NOTIFICATION-MIB", "alarmPriority"), ("ALARM-MIB", "alarmModelDescription"), ("ALPHA-RESOURCE-MIB", "componentListStaticName"), ("ALPHA-RESOURCE-MIB", "componentListReference"), ("ALPHA-NOTIFICATION-MIB", "alarmSeverity"), ("ALPHA-RESOURCE-MIB", "controllerInfoName"), ("ALPHA-NOTIFICATION-MIB", "alarmCustomDescription"))
if mibBuilder.loadTexts: alphaAlarmActiveState.setStatus('current')
if mibBuilder.loadTexts: alphaAlarmActiveState.setDescription(' SNMPv2 notification varbinds start with SysUptime and Notification Oid as the first two in the list by default. The first varbind in this definition would be the third varbind in the raw output of the notification. An instance of the alarm indicated by alarmActiveModelPointer has been raised against the entity indicated by alarmActiveResourceId. The state of the alarm is indicated by the alarmModelState. The description of the alarm along with its source is indicated by the alarmModelDescription and componentListStaticName respectively. componentListSnmpId provides the Id set to the source of the alarm. The agent must throttle the generation of consecutive alarmActiveState traps so that there is at least a two-second gap between traps of this type against the same alarmActiveModelPointer and alarmActiveResourceId. When traps are throttled, they are queued for sending at a future time. A management application should periodically check the value of alarmActiveLastChanged to detect any missed alarmActiveState notification-events, e.g., due to throttling or transmission loss. ')
alphaAlarmClearState = NotificationType((1, 3, 6, 1, 4, 1, 7309, 100, 2)).setObjects(("ALARM-MIB", "alarmActiveModelPointer"), ("ALARM-MIB", "alarmActiveResourceId"), ("ALPHA-NOTIFICATION-MIB", "alarmPriority"), ("ALARM-MIB", "alarmModelDescription"), ("ALPHA-RESOURCE-MIB", "componentListStaticName"), ("ALPHA-RESOURCE-MIB", "componentListReference"), ("ALPHA-NOTIFICATION-MIB", "alarmSeverity"), ("ALPHA-RESOURCE-MIB", "controllerInfoName"), ("ALPHA-NOTIFICATION-MIB", "alarmCustomDescription"))
if mibBuilder.loadTexts: alphaAlarmClearState.setStatus('current')
if mibBuilder.loadTexts: alphaAlarmClearState.setDescription(' SNMPv2 notification varbinds start with SysUptime and Notification Oid as the first two in the list by default. The first varbind in this definition would be the third varbind in the raw output of the notification. An instance of the alarm indicated by alarmActiveModelPointer has been cleared against the entity indicated by alarmActiveResourceId. The state of the alarm is indicated by the alarmModelState. The description of the alarm along with its source is indicated by the alarmModelDescription and componentListStaticName respectively. componentListSnmpId provides the Id set to the source of the alarm. The agent must throttle the generation of consecutive alarmActiveClear traps so that there is at least a two-second gap between traps of this type against the same alarmActiveModelPointer and alarmActiveResourceId. When traps are throttled, they are queued for sending at a future time. A management application should periodically check the value of alarmActiveLastChanged to detect any missed alarmClearState notification-events, e.g., due to throttling or transmission loss. ')
alarmSeverity = MibScalar((1, 3, 6, 1, 4, 1, 7309, 101, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmSeverity.setStatus('current')
if mibBuilder.loadTexts: alarmSeverity.setDescription(' User defined value used for filtering purposes. ')
alarmCustomDescription = MibScalar((1, 3, 6, 1, 4, 1, 7309, 101, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmCustomDescription.setStatus('current')
if mibBuilder.loadTexts: alarmCustomDescription.setDescription(' User defined value used for filtering purposes. ')
alarmPriority = MibScalar((1, 3, 6, 1, 4, 1, 7309, 101, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmPriority.setStatus('current')
if mibBuilder.loadTexts: alarmPriority.setDescription(' User defined value used for filtering purposes. ')
alphaAlarmNotificationConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 100, 102))
alphaAlarmNotificationCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 100, 102, 1))
alphaAlarmNotificationCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7309, 100, 102, 1, 1)).setObjects(("ALPHA-NOTIFICATION-MIB", "alphaParameterGroup"), ("ALPHA-NOTIFICATION-MIB", "alphaNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alphaAlarmNotificationCompliance = alphaAlarmNotificationCompliance.setStatus('current')
if mibBuilder.loadTexts: alphaAlarmNotificationCompliance.setDescription('The compliance statement for systems supporting the alpha MIB.')
alphaAlarmNotificationGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 100, 102, 1, 2))
alphaParameterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7309, 100, 102, 1, 2, 1)).setObjects(("ALPHA-NOTIFICATION-MIB", "alarmSeverity"), ("ALPHA-NOTIFICATION-MIB", "alarmCustomDescription"), ("ALPHA-NOTIFICATION-MIB", "alarmPriority"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alphaParameterGroup = alphaParameterGroup.setStatus('current')
if mibBuilder.loadTexts: alphaParameterGroup.setDescription('Active alpha list group.')
alphaNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 7309, 100, 102, 1, 2, 2)).setObjects(("ALPHA-NOTIFICATION-MIB", "alphaAlarmActiveState"), ("ALPHA-NOTIFICATION-MIB", "alphaAlarmClearState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alphaNotificationsGroup = alphaNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: alphaNotificationsGroup.setDescription('The collection of notifications that can be used to model alarms for faults lacking pre-existing notification definitions.')
mibBuilder.exportSymbols("ALPHA-NOTIFICATION-MIB", alphaParameterGroup=alphaParameterGroup, alphaAlarmNotifications=alphaAlarmNotifications, alarmCustomDescription=alarmCustomDescription, alphaAlarmNotificationCompliance=alphaAlarmNotificationCompliance, alphaAlarmNotificationCompliances=alphaAlarmNotificationCompliances, alarmPriority=alarmPriority, alphaAlarmNotificationConformance=alphaAlarmNotificationConformance, alphaAlarmNotificationGroups=alphaAlarmNotificationGroups, alphaNotificationsGroup=alphaNotificationsGroup, alarmSeverity=alarmSeverity, alphaAlarmClearState=alphaAlarmClearState, PYSNMP_MODULE_ID=alphaAlarmNotifications, alphaAlarmActiveState=alphaAlarmActiveState, alphaAlarmNotificationsExtension=alphaAlarmNotificationsExtension)
