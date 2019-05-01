#
# PySNMP MIB module ARC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ARC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:24:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ResourceId, = mibBuilder.importSymbols("ALARM-MIB", "ResourceId")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
IpAddress, Counter64, MibIdentifier, ObjectIdentity, iso, Counter32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, mib_2, ModuleIdentity, Unsigned32, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter64", "MibIdentifier", "ObjectIdentity", "iso", "Counter32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "mib-2", "ModuleIdentity", "Unsigned32", "Gauge32", "Integer32")
DisplayString, StorageType, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "StorageType", "TextualConvention", "RowStatus")
arcMibModule = ModuleIdentity((1, 3, 6, 1, 2, 1, 117))
arcMibModule.setRevisions(('2004-09-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: arcMibModule.setRevisionsDescriptions(('Initial version, published as RFC 3878.',))
if mibBuilder.loadTexts: arcMibModule.setLastUpdated('200409090000Z')
if mibBuilder.loadTexts: arcMibModule.setOrganization('IETF Distributed Management Working Group')
if mibBuilder.loadTexts: arcMibModule.setContactInfo('WG EMail: disman@ietf.org Subscribe: disman-request@ietf.org http://www.ietf.org/html.charters/disman-charter.html Chair: Randy Presuhn E-mail: randy_presuhn@mindspring.com Editor: Hing-Kam Lam Lucent Technologies, 4C-616 101 Crawfords Corner Road Holmdel, NJ 07733 USA Tel: +1 732 949 8338 E-mail: hklam@lucent.com')
if mibBuilder.loadTexts: arcMibModule.setDescription('The MIB module describes the objects for controlling a resource in reporting alarm conditions that it detects. Copyright (C) The Internet Society (2004). This version of this MIB module is part of RFC 3878; see the RFC itself for full legal notices.')
class IANAItuProbableCauseOrZero(TextualConvention, Integer32):
    reference = 'IANA-ITU-ALARM-TC MIB module as maintained at the IANA web site. The initial module was also published in RFC 3877.'
    description = 'This TC can take any value of IANAItuProbableCause or 0. IANAItuProbableCause is defined in the IANA-ITU-ALARM-TC module, which is maintained at the IANA web site and published in the Alarm MIB document (see RFC 3877).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

arcTimeIntervals = MibIdentifier((1, 3, 6, 1, 2, 1, 117, 1))
arcObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 117, 2))
arcTITimeInterval = MibScalar((1, 3, 6, 1, 2, 1, 117, 1, 1), Unsigned32()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: arcTITimeInterval.setStatus('current')
if mibBuilder.loadTexts: arcTITimeInterval.setDescription('This variable indicates the time interval used for the nalmTI state, in units of second. It is a pre-defined length of time in which the resource will stay in the nalmTI state before transition into the alm state. Instances of this object SHOULD persist across agent restarts.')
arcCDTimeInterval = MibScalar((1, 3, 6, 1, 2, 1, 117, 1, 2), Unsigned32()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: arcCDTimeInterval.setStatus('current')
if mibBuilder.loadTexts: arcCDTimeInterval.setDescription('This variable indicates the time interval used for the nalmQICD state, in units of second. It is a pre-defined length of time in which the resource will stay in the nalmQICD state before transition into the alm state after it is problem-free. Instances of this object SHOULD persist across agent restarts.')
arcTable = MibTable((1, 3, 6, 1, 2, 1, 117, 2, 1), )
if mibBuilder.loadTexts: arcTable.setReference("ITU Recommendation M.3100 Amendment 3, 'Generic Network Information Model', January 2001.")
if mibBuilder.loadTexts: arcTable.setStatus('current')
if mibBuilder.loadTexts: arcTable.setDescription("A table of Alarm Reporting Control (ARC) settings on the system. Alarm Reporting Control is a feature that provides an automatic in-service provisioning capability. Alarm reporting is turned off on a per-resource basis for a selective set of potential alarm conditions to allow sufficient time for customer testing and other maintenance activities in an 'alarm free' state. Once a resource is ready for service, alarm reporting is automatically or manually turned on. Functional description and requirements of Alarm Reporting Control are defined in ITU-T Recommendation M.3100 Amendment 3 [M.3100 Amd3].")
arcEntry = MibTableRow((1, 3, 6, 1, 2, 1, 117, 2, 1, 1), ).setIndexNames((0, "ARC-MIB", "arcIndex"), (0, "ARC-MIB", "arcAlarmType"), (0, "ARC-MIB", "arcNotificationId"))
if mibBuilder.loadTexts: arcEntry.setStatus('current')
if mibBuilder.loadTexts: arcEntry.setDescription('A conceptual row that contains information about an ARC setting of a resource in the system. Implementation need to be aware that if the total size of arcIndex and arcNotificationId exceeds 114 sub-IDs, then OIDs of column instances in this table will have more than 128 sub-IDs and cannot be access using SNMPv1, SNMPv2c, or snmpv3.')
arcIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 117, 2, 1, 1, 1), ResourceId())
if mibBuilder.loadTexts: arcIndex.setStatus('current')
if mibBuilder.loadTexts: arcIndex.setDescription("This object uniquely identifies a resource, which is under the arcState's control for the associated arcAlarmType. For example, if the resource is an interface, this object will point to an instance of interface, e.g., ifIndex.1.")
arcAlarmType = MibTableColumn((1, 3, 6, 1, 2, 1, 117, 2, 1, 1, 2), IANAItuProbableCauseOrZero())
if mibBuilder.loadTexts: arcAlarmType.setStatus('current')
if mibBuilder.loadTexts: arcAlarmType.setDescription('This object identifies the alarm condition type controlled by the arcState. It specifies the value 0 or a value of IANAItuProbableCause that is applicable to the resource. IANAItuProbableCause is defined in the IANA-ITU-ALARM-TC module in the Alarm MIB document. The value of zero (0) implies any probable causes that are applicable to the resource. Usually, the applicable probable causes of a resource are specified in the resource-specific mib.')
arcNotificationId = MibTableColumn((1, 3, 6, 1, 2, 1, 117, 2, 1, 1, 3), ObjectIdentifier())
if mibBuilder.loadTexts: arcNotificationId.setStatus('current')
if mibBuilder.loadTexts: arcNotificationId.setDescription('This object identifies the type of notification to be suppressed. The notification type identified should be the one normally used by the resource for reporting its alarms. When the value of 0.0 is specified for this object, it implies all applicable notification types.')
arcState = MibTableColumn((1, 3, 6, 1, 2, 1, 117, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("nalm", 1), ("nalmQI", 2), ("nalmTI", 3), ("nalmQICD", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: arcState.setStatus('current')
if mibBuilder.loadTexts: arcState.setDescription("Defined in M.3100 Amendment 3 [M.3100 Amd3], there are five ARC states: alm, nalm, nalmQI, nalmQICD, and nalmTI. alm: Alarm reporting is turned on (i.e., is allowed). nalm: Alarm reporting is turned off (i.e., not allowed). nalmQI: nalm - Qualified Inhibit. Alarm reporting is turned off until the managed entity is qualified problem-free for an optional persistence interval. Problem-free means that the condition corresponding to the specified alarm type is cleared. nalmQICD: nalmQI - Count down. This is a substate of nalmQI and performs the persistence timing countdown function after the managed entity is qualified problem-free. nalmTI: nalm - Timed Inhibit. Alarm reporting is turned off for a specified time interval. alm may transition to nalm, nalmQI or nalmTI by management request. nalm may transition to alm, nalmQI or nalmTI by management request. nalmQI may transition to nalm or alm by management request. nalmQI may transition to alm automatically if qualified problem-free (if nalmQICD is not supported) or if the CD timer expired (if nalmQICD is supported) nalmTI may transition to alm or nalm by management request. nalmTI may transition to alm automatically if the TI timer expired. Further details of ARC state transitions are defined in Figure 3 of M.3100 Amd3 [M.3100 Amd3]. According to the requirements in M.3100 Amd3, a resource supporting the ARC feature shall support the alm state and at least one of the nalm, nalmTI, and nalmQI states. The nalmQICD state is an optional substate of nalmQI. The arcState object controls the alarm reporting state of a resource. Note that the state alm (alarm reporting is allowed) is not listed in the enumeration of the value of this object. However, this state is implicitly supported by the mib. Once a resource enters the normal reporting mode (i.e., in the alm state) for the specified alarm type, the corresponding row will be automatically deleted from the arc table. Also the manual setting of arcState to alm can be achieved through setting the RowStatus object to 'destroy'. The nalamQICD state is a transitional state from nalmQI to alm. It is optional depending on the resource type and the implementation of the resource. If it is supported, before the state transitions from nalmQI to alm, a count down period is activated for a duration set by the object arcNalmCDTimeInterval. When the time is up, the arcState transitions to alm.")
arcNalmTimeRemaining = MibTableColumn((1, 3, 6, 1, 2, 1, 117, 2, 1, 1, 5), Unsigned32()).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: arcNalmTimeRemaining.setStatus('current')
if mibBuilder.loadTexts: arcNalmTimeRemaining.setDescription('This variable indicates the time remaining in the nalmTI state or the nalmQICD state, in units of second. At the moment the resource enters the nalmTI state, this variable will have the initial value equal to the value of arcNalmTITimeInterval and then starts decrementing as time goes by. Similarly at the moment the resource enters the nalmQICD state, this variable will have the initial value equal to the value of arcNalmCDTimeInterval and then starts decrementing as time goes by. This variable is read-create and thus will allow the manager to write (extend or shorten), as needed, the remaining time when the resource is in the nalmTI or nalmQICD state. If this variable is supported and the resource is currently not in the nalmTI nor nalmQICD state, the value of this variable shall equal to zero.')
arcRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 117, 2, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: arcRowStatus.setStatus('current')
if mibBuilder.loadTexts: arcRowStatus.setDescription('This columnar object is used for creating and deleting a conceptual row of the arcTable. It is used to create and delete an arc setting. Setting RowStatus to createAndGo or createAndWait implies creating a new ARC setting for the specified resource and alarm type. Setting RowStatus to destroy implies removing the ARC setting and thus has the effect of resuming normal reporting behaviour of the resource for the alarm type. Only the objects arcState, arcNalmTimeRemaining, and arcRowStatus can be updated when a row is active. All the objects, except arcNalmTimeRemaining, must be set before the row can be activated.')
arcStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 117, 2, 1, 1, 7), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: arcStorageType.setStatus('current')
if mibBuilder.loadTexts: arcStorageType.setDescription("The storage type for this conceptual row. Conceptual rows having the value 'permanent' must allow write-access at a minimum to arcState. Note that arcState must allow change by management request. Therefore, no row can be created with 'readOnly'. If a set operation tries to set the value to 'readOnly', then an 'inconsistentValue' error must be returned.")
arcConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 117, 3))
arcCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 117, 3, 1))
arcCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 117, 3, 1, 1)).setObjects(("ARC-MIB", "arcSettingGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    arcCompliance = arcCompliance.setStatus('current')
if mibBuilder.loadTexts: arcCompliance.setDescription('The compliance statement for systems supporting the ARC MIB module.')
arcGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 117, 3, 2))
arcSettingGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 117, 3, 2, 1)).setObjects(("ARC-MIB", "arcState"), ("ARC-MIB", "arcRowStatus"), ("ARC-MIB", "arcStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    arcSettingGroup = arcSettingGroup.setStatus('current')
if mibBuilder.loadTexts: arcSettingGroup.setDescription('A collection of objects applicable to basic ARC setting.')
arcTIGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 117, 3, 2, 2)).setObjects(("ARC-MIB", "arcTITimeInterval"), ("ARC-MIB", "arcNalmTimeRemaining"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    arcTIGroup = arcTIGroup.setStatus('current')
if mibBuilder.loadTexts: arcTIGroup.setDescription('A collection of objects applicable to ARC setting that support the Time Inhibit (TI) function.')
arcQICDGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 117, 3, 2, 3)).setObjects(("ARC-MIB", "arcCDTimeInterval"), ("ARC-MIB", "arcNalmTimeRemaining"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    arcQICDGroup = arcQICDGroup.setStatus('current')
if mibBuilder.loadTexts: arcQICDGroup.setDescription('A collection of objects applicable to ARC setting that support the Quality Inhibit (QI) Count Down (CD) function.')
mibBuilder.exportSymbols("ARC-MIB", arcStorageType=arcStorageType, arcIndex=arcIndex, arcEntry=arcEntry, PYSNMP_MODULE_ID=arcMibModule, arcCDTimeInterval=arcCDTimeInterval, arcRowStatus=arcRowStatus, arcMibModule=arcMibModule, arcTIGroup=arcTIGroup, arcObjects=arcObjects, arcCompliances=arcCompliances, arcAlarmType=arcAlarmType, arcConformance=arcConformance, IANAItuProbableCauseOrZero=IANAItuProbableCauseOrZero, arcTITimeInterval=arcTITimeInterval, arcNotificationId=arcNotificationId, arcNalmTimeRemaining=arcNalmTimeRemaining, arcGroups=arcGroups, arcSettingGroup=arcSettingGroup, arcCompliance=arcCompliance, arcQICDGroup=arcQICDGroup, arcTable=arcTable, arcTimeIntervals=arcTimeIntervals, arcState=arcState)
