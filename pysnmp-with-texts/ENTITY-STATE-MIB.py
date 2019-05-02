#
# PySNMP MIB module ENTITY-STATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTITY-STATE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:25:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Integer32, Bits, mib_2, Counter64, ModuleIdentity, TimeTicks, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, MibIdentifier, Gauge32, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Bits", "mib-2", "Counter64", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "MibIdentifier", "Gauge32", "iso", "Unsigned32")
DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention")
entityStateMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 131))
entityStateMIB.setRevisions(('2006-09-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: entityStateMIB.setRevisionsDescriptions(('Initial version, published as RFC 4268.',))
if mibBuilder.loadTexts: entityStateMIB.setLastUpdated('200609060000Z')
if mibBuilder.loadTexts: entityStateMIB.setOrganization('IETF Entity MIB Working Group')
if mibBuilder.loadTexts: entityStateMIB.setContactInfo(' General Discussion: entmib@ietf.org To Subscribe: http://www.ietf.org/mailman/listinfo/entmib http://www.ietf.org/html.charters/entmib-charter.html Sharon Chisholm Nortel Networks PO Box 3511 Station C Ottawa, Ont. K1Y 4H7 Canada schishol@nortel.com David T. Perkins 548 Qualbrook Ct San Jose, CA 95110 USA Phone: 408 394-8702 dperkins@snmpinfo.com ')
if mibBuilder.loadTexts: entityStateMIB.setDescription('This MIB defines a state extension to the Entity MIB. Copyright at The Internet Society 2005. This version of this MIB module is part of RFC 4268; see the RFC itself for full legal notices.')
entStateObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 131, 1))
class EntityAdminState(TextualConvention, Integer32):
    description = " Represents the various possible administrative states. A value of 'locked' means the resource is administratively prohibited from use. A value of 'shuttingDown' means that usage is administratively limited to current instances of use. A value of 'unlocked' means the resource is not administratively prohibited from use. A value of 'unknown' means that this resource is unable to report administrative state."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("locked", 2), ("shuttingDown", 3), ("unlocked", 4))

class EntityOperState(TextualConvention, Integer32):
    description = " Represents the possible values of operational states. A value of 'disabled' means the resource is totally inoperable. A value of 'enabled' means the resource is partially or fully operable. A value of 'testing' means the resource is currently being tested and cannot therefore report whether it is operational or not. A value of 'unknown' means that this resource is unable to report operational state."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("disabled", 2), ("enabled", 3), ("testing", 4))

class EntityUsageState(TextualConvention, Integer32):
    description = " Represents the possible values of usage states. A value of 'idle' means the resource is servicing no users. A value of 'active' means the resource is currently in use and it has sufficient spare capacity to provide for additional users. A value of 'busy' means the resource is currently in use, but it currently has no spare capacity to provide for additional users. A value of 'unknown' means that this resource is unable to report usage state."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("idle", 2), ("active", 3), ("busy", 4))

class EntityAlarmStatus(TextualConvention, Bits):
    description = " Represents the possible values of alarm status. An Alarm [RFC 3877] is a persistent indication of an error or warning condition. When no bits of this attribute are set, then no active alarms are known against this entity and it is not under repair. When the 'value of underRepair' is set, the resource is currently being repaired, which, depending on the implementation, may make the other values in this bit string not meaningful. When the value of 'critical' is set, one or more critical alarms are active against the resource. When the value of 'major' is set, one or more major alarms are active against the resource. When the value of 'minor' is set, one or more minor alarms are active against the resource. When the value of 'warning' is set, one or more warning alarms are active against the resource. When the value of 'indeterminate' is set, one or more alarms of whose perceived severity cannot be determined are active against this resource. A value of 'unknown' means that this resource is unable to report alarm state."
    status = 'current'
    namedValues = NamedValues(("unknown", 0), ("underRepair", 1), ("critical", 2), ("major", 3), ("minor", 4), ("warning", 5), ("indeterminate", 6))

class EntityStandbyStatus(TextualConvention, Integer32):
    description = " Represents the possible values of standby status. A value of 'hotStandby' means the resource is not providing service, but it will be immediately able to take over the role of the resource to be backed up, without the need for initialization activity, and will contain the same information as the resource to be backed up. A value of 'coldStandy' means that the resource is to back up another resource, but will not be immediately able to take over the role of a resource to be backed up, and will require some initialization activity. A value of 'providingService' means the resource is providing service. A value of 'unknown' means that this resource is unable to report standby state."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("hotStandby", 2), ("coldStandby", 3), ("providingService", 4))

entStateTable = MibTable((1, 3, 6, 1, 2, 1, 131, 1, 1), )
if mibBuilder.loadTexts: entStateTable.setStatus('current')
if mibBuilder.loadTexts: entStateTable.setDescription('A table of information about state/status of entities. This is a sparse augment of the entPhysicalTable. Entries appear in this table for values of entPhysicalClass [RFC 4133] that in this implementation are able to report any of the state or status stored in this table. ')
entStateEntry = MibTableRow((1, 3, 6, 1, 2, 1, 131, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: entStateEntry.setStatus('current')
if mibBuilder.loadTexts: entStateEntry.setDescription('State information about this physical entity.')
entStateLastChanged = MibTableColumn((1, 3, 6, 1, 2, 1, 131, 1, 1, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entStateLastChanged.setStatus('current')
if mibBuilder.loadTexts: entStateLastChanged.setDescription('The value of this object is the date and time when the value of any of entStateAdmin, entStateOper, entStateUsage, entStateAlarm, or entStateStandby changed for this entity. If there has been no change since the last re-initialization of the local system, this object contains the date and time of local system initialization. If there has been no change since the entity was added to the local system, this object contains the date and time of the insertion.')
entStateAdmin = MibTableColumn((1, 3, 6, 1, 2, 1, 131, 1, 1, 1, 2), EntityAdminState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entStateAdmin.setStatus('current')
if mibBuilder.loadTexts: entStateAdmin.setDescription("The administrative state for this entity. This object refers to an entities administrative permission to service both other entities within its containment hierarchy as well other users of its services defined by means outside the scope of this MIB. Setting this object to 'notSupported' will result in an 'inconsistentValue' error. For entities that do not support administrative state, all set operations will result in an 'inconsistentValue' error. Some physical entities exhibit only a subset of the remaining administrative state values. Some entities cannot be locked, and hence this object exhibits only the 'unlocked' state. Other entities cannot be shutdown gracefully, and hence this object does not exhibit the 'shuttingDown' state. A value of 'inconsistentValue' will be returned if attempts are made to set this object to values not supported by its administrative model.")
entStateOper = MibTableColumn((1, 3, 6, 1, 2, 1, 131, 1, 1, 1, 3), EntityOperState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entStateOper.setStatus('current')
if mibBuilder.loadTexts: entStateOper.setDescription("The operational state for this entity. Note that unlike the state model used within the Interfaces MIB [RFC 2863], this object does not follow the administrative state. An administrative state of down does not predict an operational state of disabled. A value of 'testing' means that entity currently being tested and cannot therefore report whether it is operational or not. A value of 'disabled' means that an entity is totally inoperable and unable to provide service both to entities within its containment hierarchy, or to other receivers of its service as defined in ways outside the scope of this MIB. A value of 'enabled' means that an entity is fully or partially operable and able to provide service both to entities within its containment hierarchy, or to other receivers of its service as defined in ways outside the scope of this MIB. Note that some implementations may not be able to accurately report entStateOper while the entStateAdmin object has a value other than 'unlocked'. In these cases, this object MUST have a value of 'unknown'.")
entStateUsage = MibTableColumn((1, 3, 6, 1, 2, 1, 131, 1, 1, 1, 4), EntityUsageState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entStateUsage.setStatus('current')
if mibBuilder.loadTexts: entStateUsage.setDescription("The usage state for this entity. This object refers to an entity's ability to service more physical entities in a containment hierarchy. A value of 'idle' means this entity is able to contain other entities but that no other entity is currently contained within this entity. A value of 'active' means that at least one entity is contained within this entity, but that it could handle more. A value of 'busy' means that the entity is unable to handle any additional entities being contained in it. Some entities will exhibit only a subset of the usage state values. Entities that are unable to ever service any entities within a containment hierarchy will always have a usage state of 'busy'. Some entities will only ever be able to support one entity within its containment hierarchy and will therefore only exhibit values of 'idle' and 'busy'.")
entStateAlarm = MibTableColumn((1, 3, 6, 1, 2, 1, 131, 1, 1, 1, 5), EntityAlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entStateAlarm.setStatus('current')
if mibBuilder.loadTexts: entStateAlarm.setDescription("The alarm status for this entity. It does not include the alarms raised on child components within its containment hierarchy. A value of 'unknown' means that this entity is unable to report alarm state. Note that this differs from 'indeterminate', which means that alarm state is supported and there are alarms against this entity, but the severity of some of the alarms is not known. If no bits are set, then this entity supports reporting of alarms, but there are currently no active alarms against this entity.")
entStateStandby = MibTableColumn((1, 3, 6, 1, 2, 1, 131, 1, 1, 1, 6), EntityStandbyStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entStateStandby.setStatus('current')
if mibBuilder.loadTexts: entStateStandby.setDescription("The standby status for this entity. Some entities will exhibit only a subset of the remaining standby state values. If this entity cannot operate in a standby role, the value of this object will always be 'providingService'.")
entStateNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 131, 0))
entStateOperEnabled = NotificationType((1, 3, 6, 1, 2, 1, 131, 0, 1)).setObjects(("ENTITY-STATE-MIB", "entStateAdmin"), ("ENTITY-STATE-MIB", "entStateAlarm"))
if mibBuilder.loadTexts: entStateOperEnabled.setStatus('current')
if mibBuilder.loadTexts: entStateOperEnabled.setDescription("An entStateOperEnabled notification signifies that the SNMP entity, acting in an agent role, has detected that the entStateOper object for one of its entities has transitioned into the 'enabled' state. The entity this notification refers can be identified by extracting the entPhysicalIndex from one of the variable bindings. The entStateAdmin and entStateAlarm varbinds may be examined to find out additional information on the administrative state at the time of the operation state change as well as to find out whether there were any known alarms against the entity at that time that may explain why the physical entity has become operationally disabled.")
entStateOperDisabled = NotificationType((1, 3, 6, 1, 2, 1, 131, 0, 2)).setObjects(("ENTITY-STATE-MIB", "entStateAdmin"), ("ENTITY-STATE-MIB", "entStateAlarm"))
if mibBuilder.loadTexts: entStateOperDisabled.setStatus('current')
if mibBuilder.loadTexts: entStateOperDisabled.setDescription("An entStateOperDisabled notification signifies that the SNMP entity, acting in an agent role, has detected that the entStateOper object for one of its entities has transitioned into the 'disabled' state. The entity this notification refers can be identified by extracting the entPhysicalIndex from one of the variable bindings. The entStateAdmin and entStateAlarm varbinds may be examined to find out additional information on the administrative state at the time of the operation state change as well as to find out whether there were any known alarms against the entity at that time that may affect the physical entity's ability to stay operationally enabled.")
entStateConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 131, 2))
entStateCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 131, 2, 1))
entStateCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 131, 2, 1, 1)).setObjects(("ENTITY-STATE-MIB", "entStateGroup"), ("ENTITY-STATE-MIB", "entStateNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entStateCompliance = entStateCompliance.setStatus('current')
if mibBuilder.loadTexts: entStateCompliance.setDescription('The compliance statement for systems supporting the Entity State MIB.')
entStateGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 131, 2, 2))
entStateGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 131, 2, 2, 1)).setObjects(("ENTITY-STATE-MIB", "entStateLastChanged"), ("ENTITY-STATE-MIB", "entStateAdmin"), ("ENTITY-STATE-MIB", "entStateOper"), ("ENTITY-STATE-MIB", "entStateUsage"), ("ENTITY-STATE-MIB", "entStateAlarm"), ("ENTITY-STATE-MIB", "entStateStandby"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entStateGroup = entStateGroup.setStatus('current')
if mibBuilder.loadTexts: entStateGroup.setDescription('Standard Entity State group.')
entStateNotificationsGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 131, 2, 2, 2)).setObjects(("ENTITY-STATE-MIB", "entStateOperEnabled"), ("ENTITY-STATE-MIB", "entStateOperDisabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entStateNotificationsGroup = entStateNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: entStateNotificationsGroup.setDescription('Standard Entity State Notification group.')
mibBuilder.exportSymbols("ENTITY-STATE-MIB", entStateNotifications=entStateNotifications, entStateAdmin=entStateAdmin, entStateGroup=entStateGroup, EntityOperState=EntityOperState, entStateNotificationsGroup=entStateNotificationsGroup, EntityAdminState=EntityAdminState, entityStateMIB=entityStateMIB, EntityUsageState=EntityUsageState, entStateTable=entStateTable, entStateOperEnabled=entStateOperEnabled, entStateAlarm=entStateAlarm, entStateCompliances=entStateCompliances, entStateLastChanged=entStateLastChanged, entStateOperDisabled=entStateOperDisabled, PYSNMP_MODULE_ID=entityStateMIB, EntityStandbyStatus=EntityStandbyStatus, entStateCompliance=entStateCompliance, entStateStandby=entStateStandby, entStateUsage=entStateUsage, entStateConformance=entStateConformance, entStateObjects=entStateObjects, entStateOper=entStateOper, EntityAlarmStatus=EntityAlarmStatus, entStateGroups=entStateGroups, entStateEntry=entStateEntry)
