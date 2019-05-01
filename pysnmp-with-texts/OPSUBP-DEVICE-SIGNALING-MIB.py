#
# PySNMP MIB module OPSUBP-DEVICE-SIGNALING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/OPSUBP-DEVICE-SIGNALING-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:35:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
nortel, = mibBuilder.importSymbols("NORTEL-MIB", "nortel")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, NotificationType, Bits, Counter32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, enterprises, IpAddress, Integer32, Unsigned32, TimeTicks, Gauge32, ModuleIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "Bits", "Counter32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "enterprises", "IpAddress", "Integer32", "Unsigned32", "TimeTicks", "Gauge32", "ModuleIdentity", "Counter64")
TextualConvention, DisplayString, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TimeStamp")
nnOPSNetIDGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 562, 42))
if mibBuilder.loadTexts: nnOPSNetIDGroup.setStatus('current')
if mibBuilder.loadTexts: nnOPSNetIDGroup.setDescription('The root naming arc for Nortel Networks.')
nnOPSMIBS = ObjectIdentity((1, 3, 6, 1, 4, 1, 562, 42, 5))
if mibBuilder.loadTexts: nnOPSMIBS.setStatus('current')
if mibBuilder.loadTexts: nnOPSMIBS.setDescription('The root naming arc for Nortel Networks.')
nnOPSQoSRootOID = ObjectIdentity((1, 3, 6, 1, 4, 1, 562, 42, 5, 1))
if mibBuilder.loadTexts: nnOPSQoSRootOID.setStatus('current')
if mibBuilder.loadTexts: nnOPSQoSRootOID.setDescription('The root naming arc for the ops ubp device signalling mib.')
nnOpsUbpDeviceSignalingMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3))
nnOpsUbpDeviceSignalingMIB.setRevisions(('2013-04-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: nnOpsUbpDeviceSignalingMIB.setRevisionsDescriptions(('Version 02: Corrected module compliance',))
if mibBuilder.loadTexts: nnOpsUbpDeviceSignalingMIB.setLastUpdated('201304120000Z')
if mibBuilder.loadTexts: nnOpsUbpDeviceSignalingMIB.setOrganization('Nortel Networks OPS group')
if mibBuilder.loadTexts: nnOpsUbpDeviceSignalingMIB.setContactInfo('Support ERC# 245 North America: (800) 4-NORTEL (800) 466-7835 EMEA: (33)(4) 92-966-968 Asia Pacific: 61-2-9927-8800 China: (800) 810-5000 ')
if mibBuilder.loadTexts: nnOpsUbpDeviceSignalingMIB.setDescription('UBP notifications MIB')
nnOpsUbpDeviceSignalingMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3, 1))
if mibBuilder.loadTexts: nnOpsUbpDeviceSignalingMIBObjects.setStatus('current')
if mibBuilder.loadTexts: nnOpsUbpDeviceSignalingMIBObjects.setDescription('OPS UBP device signaling MIB objects are all defined in this branch.')
ubpNotifyObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3, 1, 1))
if mibBuilder.loadTexts: ubpNotifyObjects.setStatus('current')
if mibBuilder.loadTexts: ubpNotifyObjects.setDescription('Group of objects related to notification information.')
ubpNotifyDeviceIdentifierType = MibScalar((1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("devicemgmtadd", 1), ("snmpengineid", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ubpNotifyDeviceIdentifierType.setStatus('current')
if mibBuilder.loadTexts: ubpNotifyDeviceIdentifierType.setDescription('This indicates the type of the device identifier that will be sent in the serverNotifyDeviceIdentifier attribute. This attribute is sent with the notification.')
ubpNotifyDeviceIdentifier = MibScalar((1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3, 1, 1, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ubpNotifyDeviceIdentifier.setStatus('current')
if mibBuilder.loadTexts: ubpNotifyDeviceIdentifier.setDescription('A string that can be used to uniquely identify the device which is acting as an EAP access point. This attribute is sent with the notification.')
ubpNotifyEAPAccessPortEntityIdentifier = MibScalar((1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3, 1, 1, 3), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ubpNotifyEAPAccessPortEntityIdentifier.setStatus('current')
if mibBuilder.loadTexts: ubpNotifyEAPAccessPortEntityIdentifier.setDescription('A string that can be used to identify the interface on the EAP access point on which the EAP session was started/ended. The format for this attribute is device specific. For Passport 8600 devices, it will take the form of ?<slot>/<port>? e.g. ?3/16?. This attribute is sent with the notification.')
ubpNotifyEAPUserIdentifier = MibScalar((1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3, 1, 1, 4), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ubpNotifyEAPUserIdentifier.setStatus('current')
if mibBuilder.loadTexts: ubpNotifyEAPUserIdentifier.setDescription('The name of the user initiating the EAP session e.g. ?Joe?. This attribute is sent with the notification.')
ubpNotifyEAPUserGroupIdentifier = MibScalar((1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3, 1, 1, 5), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ubpNotifyEAPUserGroupIdentifier.setStatus('current')
if mibBuilder.loadTexts: ubpNotifyEAPUserGroupIdentifier.setDescription('The groups the user initiating the EAP session is associated with. The value for this attribute is made available through vendor specific attributes in the RADIUS authentication message received by the EAP access point. This attribute may contain multiple group names following the format ?<groupname1>+<groupname2>? e.g. ?Engg+Admin?. This attribute is sent with the notification.')
ubpNotifyEAPUserRoles = MibScalar((1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3, 1, 1, 6), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ubpNotifyEAPUserRoles.setStatus('current')
if mibBuilder.loadTexts: ubpNotifyEAPUserRoles.setDescription('The name of the role combination. A role combination is a set of unordered roles; a role being an abstraction used to bind policies with actual interfaces on devices. Each role takes the form of a string. The value for this attribute is made available through vendor specific attributes in the RADIUS authentication message received by the EAP access point. This attribute may contain multiple roles, in the form ?<role1>+<role2>? e.g. ?Student+TeachingAssistant?. The invalid characters for a role are : ?+?, ? ? (space), null, lf, cr, bell, bs, HT (tab), VT, FF (form feed). The maximum length for a role is 31 characters. This attribute is sent with the notification.')
ubpNotifyEAPSignalSequenceNumber = MibScalar((1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3, 1, 1, 7), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ubpNotifyEAPSignalSequenceNumber.setStatus('current')
if mibBuilder.loadTexts: ubpNotifyEAPSignalSequenceNumber.setDescription('This is a unique sequence identifier for a EAP session start or end event. The EAP user session event signaling is done using SNMPv3 Inform messages. Each time the EAP access point does not get an acknowledgement for the Inform, it may retry sending the Inform message with the same EAP signal sequence number so that the Inform receiver can handle duplicate Informs. This attribute is sent with the notification.')
ubpNotifyEAPSessionStartSignalSequenceNumber = MibScalar((1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3, 1, 1, 8), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ubpNotifyEAPSessionStartSignalSequenceNumber.setStatus('current')
if mibBuilder.loadTexts: ubpNotifyEAPSessionStartSignalSequenceNumber.setDescription('This is the sequence identifier that was associated with the SNMP Inform message sent for a EAP session started event. It can be used to correlate the EAP session end event with the notification for the EAP session start event. This attribute is sent with the notification.')
ubpNotifyEAPSessionEndReason = MibScalar((1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("eapsessionEndUserlogoff", 1), ("eapsessionEndOther", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ubpNotifyEAPSessionEndReason.setStatus('current')
if mibBuilder.loadTexts: ubpNotifyEAPSessionEndReason.setDescription('The reason for the EAP user session end event. This is used for reporting purposes only. This attribute is sent with the notification.')
ubpNotifyEAPAccessPortEntityOpenFlag = MibScalar((1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("eapAccessPortFlagNotApplicable", 1), ("eapAccessPortOpenRequired", 2), ("eapAccessPortOpenNotRequired", 3)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ubpNotifyEAPAccessPortEntityOpenFlag.setStatus('current')
if mibBuilder.loadTexts: ubpNotifyEAPAccessPortEntityOpenFlag.setDescription('This is a flag indicating whether the receiver of the notification should perform an ?open? or ?activation? operation on the EAP access port entity after it has downloaded User based policies for the current EAP user session. This may be useful for reporting purposes. This attribute is sent with the notification.')
ubpDeviceSignalingMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3, 2))
ubpEAPSessionStart = NotificationType((1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3, 2, 1)).setObjects(("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyDeviceIdentifierType"), ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyDeviceIdentifier"), ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyEAPAccessPortEntityIdentifier"), ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyEAPUserIdentifier"), ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyEAPUserGroupIdentifier"), ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyEAPUserRoles"), ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyEAPSignalSequenceNumber"), ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyEAPAccessPortEntityOpenFlag"))
if mibBuilder.loadTexts: ubpEAPSessionStart.setStatus('current')
if mibBuilder.loadTexts: ubpEAPSessionStart.setDescription('This notification signifies that an EAP session was started on the host from which this notification has been sent.')
ubpEAPSessionEnd = NotificationType((1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3, 2, 2)).setObjects(("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyDeviceIdentifierType"), ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyDeviceIdentifier"), ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyEAPAccessPortEntityIdentifier"), ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyEAPUserIdentifier"), ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyEAPSessionEndReason"), ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyEAPSignalSequenceNumber"), ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyEAPSessionStartSignalSequenceNumber"))
if mibBuilder.loadTexts: ubpEAPSessionEnd.setStatus('current')
if mibBuilder.loadTexts: ubpEAPSessionEnd.setDescription('This notification signifies that an EAP session has ended on the host from which this notification has been sent.')
nnOpsUbpDeviceSignalingMIBConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3, 3))
if mibBuilder.loadTexts: nnOpsUbpDeviceSignalingMIBConformance.setStatus('current')
if mibBuilder.loadTexts: nnOpsUbpDeviceSignalingMIBConformance.setDescription('Policy Server MIB objects are all defined in this branch.')
nnOpsUbpDeviceSignalingMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3, 3, 1))
nnOpsUbpDeviceSignalingMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3, 3, 2))
nnOpsUbpDeviceSignalingMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3, 3, 1, 1)).setObjects(("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyObjectsGroup"), ("OPSUBP-DEVICE-SIGNALING-MIB", "serverNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nnOpsUbpDeviceSignalingMIBCompliance = nnOpsUbpDeviceSignalingMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: nnOpsUbpDeviceSignalingMIBCompliance.setDescription('Describes the requirements for conformance to the OPS Policy Server MIB')
ubpNotifyObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3, 3, 2, 1)).setObjects(("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyDeviceIdentifierType"), ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyDeviceIdentifier"), ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyEAPAccessPortEntityIdentifier"), ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyEAPUserIdentifier"), ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyEAPUserGroupIdentifier"), ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyEAPUserRoles"), ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyEAPSignalSequenceNumber"), ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyEAPSessionStartSignalSequenceNumber"), ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyEAPSessionEndReason"), ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpNotifyEAPAccessPortEntityOpenFlag"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ubpNotifyObjectsGroup = ubpNotifyObjectsGroup.setStatus('current')
if mibBuilder.loadTexts: ubpNotifyObjectsGroup.setDescription('Policy Server MIB objects used in notifications.')
serverNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 562, 42, 5, 1, 3, 3, 2, 2)).setObjects(("OPSUBP-DEVICE-SIGNALING-MIB", "ubpEAPSessionStart"), ("OPSUBP-DEVICE-SIGNALING-MIB", "ubpEAPSessionEnd"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    serverNotificationsGroup = serverNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: serverNotificationsGroup.setDescription('Notifications which are implemented by the agent on the EAP access point.')
mibBuilder.exportSymbols("OPSUBP-DEVICE-SIGNALING-MIB", ubpEAPSessionStart=ubpEAPSessionStart, serverNotificationsGroup=serverNotificationsGroup, nnOPSNetIDGroup=nnOPSNetIDGroup, nnOpsUbpDeviceSignalingMIBObjects=nnOpsUbpDeviceSignalingMIBObjects, ubpNotifyEAPSignalSequenceNumber=ubpNotifyEAPSignalSequenceNumber, nnOpsUbpDeviceSignalingMIBGroups=nnOpsUbpDeviceSignalingMIBGroups, ubpNotifyEAPUserIdentifier=ubpNotifyEAPUserIdentifier, nnOpsUbpDeviceSignalingMIBCompliance=nnOpsUbpDeviceSignalingMIBCompliance, ubpNotifyEAPSessionEndReason=ubpNotifyEAPSessionEndReason, nnOpsUbpDeviceSignalingMIBConformance=nnOpsUbpDeviceSignalingMIBConformance, nnOpsUbpDeviceSignalingMIB=nnOpsUbpDeviceSignalingMIB, nnOpsUbpDeviceSignalingMIBCompliances=nnOpsUbpDeviceSignalingMIBCompliances, ubpNotifyEAPAccessPortEntityOpenFlag=ubpNotifyEAPAccessPortEntityOpenFlag, ubpNotifyEAPAccessPortEntityIdentifier=ubpNotifyEAPAccessPortEntityIdentifier, ubpNotifyEAPUserRoles=ubpNotifyEAPUserRoles, ubpNotifyObjectsGroup=ubpNotifyObjectsGroup, ubpNotifyEAPUserGroupIdentifier=ubpNotifyEAPUserGroupIdentifier, ubpEAPSessionEnd=ubpEAPSessionEnd, ubpNotifyObjects=ubpNotifyObjects, ubpDeviceSignalingMIBNotifications=ubpDeviceSignalingMIBNotifications, ubpNotifyDeviceIdentifierType=ubpNotifyDeviceIdentifierType, ubpNotifyEAPSessionStartSignalSequenceNumber=ubpNotifyEAPSessionStartSignalSequenceNumber, nnOPSMIBS=nnOPSMIBS, PYSNMP_MODULE_ID=nnOpsUbpDeviceSignalingMIB, ubpNotifyDeviceIdentifier=ubpNotifyDeviceIdentifier, nnOPSQoSRootOID=nnOPSQoSRootOID)