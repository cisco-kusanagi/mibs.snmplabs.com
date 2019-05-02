#
# PySNMP MIB module PDN-MPE-DSLAM-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-MPE-DSLAM-SYSTEM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:39:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
entPhysicalEntry, entPhysicalIndex = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalEntry", "entPhysicalIndex")
pdn_mpe, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdn-mpe")
mpeSysObjectID, = mibBuilder.importSymbols("PDN-MPE-MIB2-MIB", "mpeSysObjectID")
ContactState, = mibBuilder.importSymbols("PDN-TC", "ContactState")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Integer32, Counter64, Unsigned32, MibIdentifier, iso, IpAddress, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, Gauge32, ObjectIdentity, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "Unsigned32", "MibIdentifier", "iso", "IpAddress", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "Gauge32", "ObjectIdentity", "ModuleIdentity", "Bits")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
mpe_dslam = ModuleIdentity((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24)).setLabel("mpe-dslam")
mpe_dslam.setRevisions(('2004-05-13 14:00', '2005-04-08 14:00', '2003-06-06 00:00', '2003-04-25 00:00', '2003-04-18 00:00', '2003-03-20 15:00', '2003-03-07 00:00', '2002-10-25 00:00', '2002-08-15 00:00', '2002-02-21 00:00', '2002-01-28 00:00', '2000-01-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mpe_dslam.setRevisionsDescriptions(('Jesus Pinto Added two traps for fan failure: mpeFanEntityModuleFailure, mpeFanEntityModuleOperational', 'Jesus Pinto Added four new traps for PowerSupply failure: mpePowerSourceAFailure mpePowerSourceBFailure mpePowerSourceAOperational mpePowerSourceBOperational', "Jesus Pinto and Clay Sikes Removed the entPhysicalIndex as an object in the mpeAlarmRelayInputStateChanged notification. This object was redundant in that it's the instance part of the mpeAlarmRelayState object.", 'Jesus Pinto and Clay Sikes Change mpeAlarmRelayInputState to mpeAlarmRelayState and changed it from a read-only object to a read- write object. This should give ultimate flexibility.', 'Jesus Pinto and Clay Sikes Needed objects to read Alarm Relay Input State. The addition of mpeEntPhysicalExtAlarmRelayInputContactState below was not a good idea as it implied a dense augments. mpeEntPhysicalExtAlarmRelayInputContactState was deprecated. Added a new table, mpeAlarmRelayTable to hold alarm relay objects where the table implies a sparse augments. Deprecated mpeAlarmRrelayEquipmentIndex, mpeAlarmRelayInputContactState, and the mpeAlarmRelayInputcontactStateChanged trap they were designed for to discourage use in new projects. Added a new trap, mpeAlarmRelayInputStateChanged, as a replacement that uses objects defined in or related to the mpeAlarmRelayTable. The mpeAlarmRelayTable allows Alarm Relay Input state to be read and has a direct relationship with the objects defined for the mpeAlarmRelayInputStateChanged trap. Since this table is indexed the entPhysicalIndex, it is extremely flexible in that it can apply to a Single Management Entity / Single Logical Entity, a chassis, or what ever level of granularity is desired in the implementation.', 'Added new notifications to complement the entConfigChange notification defined in RFC2737.', 'Added mpeEntPhysicalExtAlarmRelayInputContactState.', 'Added mpeEntPhysicalExtTable and cleaned up some MIB compiler warnings.', 'Added mpeAlarmRelayEquipIndex, Added mpeAlarmRelayInputContactState, Added mpeAlarmRelayInputContactStateChanged trap.', 'Added mpeDeviceFailureCleared Trap.', 'Added table to extend entityPhysicalTable by one object that would specify state of the alarm.', 'Initial Release',))
if mibBuilder.loadTexts: mpe_dslam.setLastUpdated('200405131400Z')
if mibBuilder.loadTexts: mpe_dslam.setOrganization('Paradyne Corporation MIB Working Group')
if mibBuilder.loadTexts: mpe_dslam.setContactInfo('Paradyne Corporation 8545 126th Avenue North Largo, FL 33733 www.paradyne.com General Comments to: mibwg_team@paradyne.com Editors Prakash Easwar Jesus Pinto Dragana Gough Clay Sikes')
if mibBuilder.loadTexts: mpe_dslam.setDescription('The mpe dslam MIB. This MIB is written specifically to extend entPhysicalTable.')
mpeSysDevDslamMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 1))
mpeSysDevDslamMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 2))
mpeEntExtAlarms = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 1, 1))
mpeAlarmRelay = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 1, 2))
mpeEntExtMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 1, 3))
mpeSysDevDslamMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 2, 0))
class MpeEntExtAdminStatus(TextualConvention, Integer32):
    description = 'Values to support the desired state of the entity. These values were selected to correspond to the syntax of the ifAdminStatus in the IF-MIB.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("up", 1), ("down", 2), ("testing", 3))

class MpeEntExtOperStatus(TextualConvention, Integer32):
    description = 'Values to support the current operational state of the entity. These values were selected to correspond to the syntax of the ifOperStatus in the IF-MIB.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("up", 1), ("down", 2), ("testing", 3), ("unknown", 4), ("dormant", 5), ("notPresent", 6), ("reserved1", 7))

mpeEntExtAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 1, 1, 1), )
if mibBuilder.loadTexts: mpeEntExtAlarmTable.setStatus('current')
if mibBuilder.loadTexts: mpeEntExtAlarmTable.setDescription('This table lists the alarm states of the objects listed in the entity-MIB entPhysicalTable.')
mpeEntExtAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 1, 1, 1, 1), )
entPhysicalEntry.registerAugmentions(("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeEntExtAlarmEntry"))
mpeEntExtAlarmEntry.setIndexNames(*entPhysicalEntry.getIndexNames())
if mibBuilder.loadTexts: mpeEntExtAlarmEntry.setStatus('current')
if mibBuilder.loadTexts: mpeEntExtAlarmEntry.setDescription('An mpeEntExtAlarmTable entry indicates the alarm state of the physical entity.')
mpeEntExtAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 1, 1, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpeEntExtAlarm.setStatus('current')
if mibBuilder.loadTexts: mpeEntExtAlarm.setDescription('This variable indicates the alarm state of the physical entity.')
mpeAlarmRelayEquipIndex = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 1, 2, 1), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: mpeAlarmRelayEquipIndex.setStatus('deprecated')
if mibBuilder.loadTexts: mpeAlarmRelayEquipIndex.setDescription('This variable is the index of the equipment whose alarms are being relayed. It is a integer number starting from 1 until the max number of physical connectors the DSLAM device has to support relay. NOTE: This object has been deprecated. Please consider using the mpeAlarmRelayTable and mpeAlarmRelayInputStateChanged objects.')
mpeAlarmRelayInputContactState = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 1, 2, 2), ContactState()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: mpeAlarmRelayInputContactState.setStatus('deprecated')
if mibBuilder.loadTexts: mpeAlarmRelayInputContactState.setDescription('This variable indicates the alarm state of the Input Contact (open/closed). NOTE: This object has been deprecated. Please consider using the mpeAlarmRelayTable and mpeAlarmRelayInputStateChanged objects.')
mpeAlarmRelayTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 1, 2, 3), )
if mibBuilder.loadTexts: mpeAlarmRelayTable.setStatus('current')
if mibBuilder.loadTexts: mpeAlarmRelayTable.setDescription('This table holds objects that relate to Alarm Relay input or output.')
mpeAlarmRelayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 1, 2, 3, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: mpeAlarmRelayEntry.setStatus('current')
if mibBuilder.loadTexts: mpeAlarmRelayEntry.setDescription('An entry in this table is a sparse augmentation of the entPhysicalEntry. As such, it is indexed by the entPhysicalIndex and not an augmentation of the entPhysicalTable.')
mpeAlarmRelayState = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 1, 2, 3, 1, 1), ContactState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpeAlarmRelayState.setStatus('current')
if mibBuilder.loadTexts: mpeAlarmRelayState.setDescription('This object is used to read or write the state an alarm relay input or output.')
mpeEntPhysicalExtTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 1, 3, 1), )
if mibBuilder.loadTexts: mpeEntPhysicalExtTable.setStatus('current')
if mibBuilder.loadTexts: mpeEntPhysicalExtTable.setDescription('This table contains entity information that is not defined in the standard ENTITY-MIB.')
mpeEntPhysicalExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 1, 3, 1, 1), )
entPhysicalEntry.registerAugmentions(("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeEntPhysicalExtEntry"))
mpeEntPhysicalExtEntry.setIndexNames(*entPhysicalEntry.getIndexNames())
if mibBuilder.loadTexts: mpeEntPhysicalExtEntry.setStatus('current')
if mibBuilder.loadTexts: mpeEntPhysicalExtEntry.setDescription('An entry extends the entPhysicalEntry defined in the ENTITY-MIB.')
mpeEntPhysicalExtUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 1, 3, 1, 1, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpeEntPhysicalExtUpTime.setStatus('current')
if mibBuilder.loadTexts: mpeEntPhysicalExtUpTime.setDescription('The time (in hundredths of a second --just like the sysUpTime) since the entity was last re-initialized.')
mpeEntPhysicalExtLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 1, 3, 1, 1, 2), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpeEntPhysicalExtLocation.setStatus('current')
if mibBuilder.loadTexts: mpeEntPhysicalExtLocation.setDescription("This object allows the manager to enter the location of the physical entity where applicable. For example, in a stack, chassis or units may be in different locations. In this case, it would be logical for the manager to set this object to the location of the associated chassis. Where the location doesn't make sense, it is recommended that the object return a zero-length string.")
mpeEntPhysicalExtAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 1, 3, 1, 1, 3), MpeEntExtAdminStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpeEntPhysicalExtAdminStatus.setStatus('current')
if mibBuilder.loadTexts: mpeEntPhysicalExtAdminStatus.setDescription('The desired state of the entity.')
mpeEntPhysicalExtOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 1, 3, 1, 1, 4), MpeEntExtOperStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpeEntPhysicalExtOperStatus.setStatus('current')
if mibBuilder.loadTexts: mpeEntPhysicalExtOperStatus.setDescription('The current operational state of the entity.')
mpeCcn = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 2, 7)).setObjects(("ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: mpeCcn.setStatus('current')
if mibBuilder.loadTexts: mpeCcn.setDescription("This trap signifies a Configuration change or software upgrade in the xDSL card. This trap is of 'warning' class")
mpeDeviceFailure = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 2, 15)).setObjects(("ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: mpeDeviceFailure.setStatus('current')
if mibBuilder.loadTexts: mpeDeviceFailure.setDescription("This trap signifies that the sending protocol's device has failed and the failure was not a result of a device test. Note there are no variable bindings for this trap")
mpeDeviceFailureCleared = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 2, 16)).setObjects(("ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: mpeDeviceFailureCleared.setStatus('current')
if mibBuilder.loadTexts: mpeDeviceFailureCleared.setDescription("This trap signifies that the sending protocol's device has failed but now it is operational. Failure was not a result of a device test.")
mpeNonSupportedMCC = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 2, 20)).setObjects(("PDN-MPE-MIB2-MIB", "mpeSysObjectID"))
if mibBuilder.loadTexts: mpeNonSupportedMCC.setStatus('current')
if mibBuilder.loadTexts: mpeNonSupportedMCC.setDescription('AN has detected MCC firmware release too low to support this device')
mpeNonSupportedChassis = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 2, 21)).setObjects(("PDN-MPE-MIB2-MIB", "mpeSysObjectID"))
if mibBuilder.loadTexts: mpeNonSupportedChassis.setStatus('current')
if mibBuilder.loadTexts: mpeNonSupportedChassis.setDescription('AN in slot xx has been installed in a chassis that cannot support one or more of its features. ')
mpeAlarmRelayInputContactStateChanged = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 2, 22)).setObjects(("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeAlarmRelayEquipIndex"), ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeAlarmRelayInputContactState"))
if mibBuilder.loadTexts: mpeAlarmRelayInputContactStateChanged.setStatus('deprecated')
if mibBuilder.loadTexts: mpeAlarmRelayInputContactStateChanged.setDescription('This trap signifies that the state of the InputContact Alarm has changed since last time. NOTE: This object has been deprecated. Please consider using the mpeAlarmRelayInputStateChanged notification.')
mpeEntPhysicalExtEntityCreated = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 2, 23)).setObjects(("ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: mpeEntPhysicalExtEntityCreated.setStatus('current')
if mibBuilder.loadTexts: mpeEntPhysicalExtEntityCreated.setDescription(' This trap signifies that an instance of this entity has been created in the entPhysicalTable. This trap is generated in addition to the entConfigChange notification defined in RFC2737.')
mpeEntPhysicalExtEntityDeleted = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 2, 24)).setObjects(("ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: mpeEntPhysicalExtEntityDeleted.setStatus('current')
if mibBuilder.loadTexts: mpeEntPhysicalExtEntityDeleted.setDescription(' This trap signifies that an instance of this entity has been deleted from the entPhysicalTable. This trap is generated in addition to the entConfigChange notification defined in RFC2737.')
mpeEntPhysicalExtEntityChanged = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 2, 25)).setObjects(("ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: mpeEntPhysicalExtEntityChanged.setStatus('current')
if mibBuilder.loadTexts: mpeEntPhysicalExtEntityChanged.setDescription(' This trap signifies that an instance of this entity has been modified in the entPhysicalTable as a result of a change in any of the objects in that table. This trap is generated in addition to the entConfigChange notification defined in RFC2737.')
mpeAlarmRelayInputStateChanged = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 2, 0, 26)).setObjects(("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeAlarmRelayState"))
if mibBuilder.loadTexts: mpeAlarmRelayInputStateChanged.setStatus('current')
if mibBuilder.loadTexts: mpeAlarmRelayInputStateChanged.setDescription('This trap signifies that the state of the Alarm Relay Input has changed.')
mpeFanEntityModuleFailure = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 2, 0, 27)).setObjects(("ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: mpeFanEntityModuleFailure.setStatus('current')
if mibBuilder.loadTexts: mpeFanEntityModuleFailure.setDescription('This trap indicates the failure of the fan module on the device.')
mpeFanEntityModuleOperational = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 2, 0, 28)).setObjects(("ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: mpeFanEntityModuleOperational.setStatus('current')
if mibBuilder.loadTexts: mpeFanEntityModuleOperational.setDescription('This trap indicates the indicates the fan module on the device is back to operational.')
mpePowerSourceAFailure = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 2, 0, 29)).setObjects(("ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: mpePowerSourceAFailure.setStatus('current')
if mibBuilder.loadTexts: mpePowerSourceAFailure.setDescription('This trap indicates that power source A has failed.')
mpePowerSourceBFailure = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 2, 0, 30)).setObjects(("ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: mpePowerSourceBFailure.setStatus('current')
if mibBuilder.loadTexts: mpePowerSourceBFailure.setDescription('This trap indicates that power source B has failed.')
mpePowerSourceAOperational = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 2, 0, 31)).setObjects(("ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: mpePowerSourceAOperational.setStatus('current')
if mibBuilder.loadTexts: mpePowerSourceAOperational.setDescription('This trap indicates that the power source A is operational. This trap compliments powerSourceAFailure trap.')
mpePowerSourceBOperational = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 2, 0, 32)).setObjects(("ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: mpePowerSourceBOperational.setStatus('current')
if mibBuilder.loadTexts: mpePowerSourceBOperational.setDescription('This trap indicates that the power source B is operational. This trap compliments powerSourceBFailure trap.')
mpeSysDevDslamConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 3))
mpeSysDevDslamGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 3, 1))
mpeSysDevDslamCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 3, 2))
mpeSysDevDslamDeprecatedGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 3, 3))
mpeSysDevDslamAlarmCompliances = ModuleCompliance((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 3, 2, 1)).setObjects(("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeSysDevDslamAlarmStateGroup"), ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeEntityExtNotificationGroup"), ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeSysDevDslamAlarmRelayGroup"), ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeEntPhysicalExtGroup"), ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeEntPhysicalExtNotificationObjectGroup"), ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeEntityExtPowerFailureNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mpeSysDevDslamAlarmCompliances = mpeSysDevDslamAlarmCompliances.setStatus('current')
if mibBuilder.loadTexts: mpeSysDevDslamAlarmCompliances.setDescription('The compliance statement for entities and their alarms states.')
mpeSysDevDslamAlarmDeprecatedCompliances = ModuleCompliance((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 3, 2, 2)).setObjects(("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeDslamDeprecatedObjectsGroup"), ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeDslamDeprecatedNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mpeSysDevDslamAlarmDeprecatedCompliances = mpeSysDevDslamAlarmDeprecatedCompliances.setStatus('deprecated')
if mibBuilder.loadTexts: mpeSysDevDslamAlarmDeprecatedCompliances.setDescription('The compliance statement for deprecated groups')
mpeSysDevDslamAlarmStateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 3, 1, 1)).setObjects(("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeEntExtAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mpeSysDevDslamAlarmStateGroup = mpeSysDevDslamAlarmStateGroup.setStatus('current')
if mibBuilder.loadTexts: mpeSysDevDslamAlarmStateGroup.setDescription('The collection of objects which are used to describe alarm states for equipments physically connected to a DSLAM device.')
mpeEntityExtNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 3, 1, 2)).setObjects(("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeCcn"), ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeDeviceFailure"), ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeDeviceFailureCleared"), ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeNonSupportedMCC"), ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeNonSupportedChassis"), ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeEntPhysicalExtEntityCreated"), ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeEntPhysicalExtEntityDeleted"), ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeEntPhysicalExtEntityChanged"), ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeAlarmRelayInputStateChanged"), ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeFanEntityModuleFailure"), ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeFanEntityModuleOperational"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mpeEntityExtNotificationGroup = mpeEntityExtNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: mpeEntityExtNotificationGroup.setDescription('The collection of objects which are used to notify that trap conditions are met.')
mpeSysDevDslamAlarmRelayGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 3, 1, 3)).setObjects(("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeAlarmRelayState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mpeSysDevDslamAlarmRelayGroup = mpeSysDevDslamAlarmRelayGroup.setStatus('current')
if mibBuilder.loadTexts: mpeSysDevDslamAlarmRelayGroup.setDescription('The collection of objects which are used for Alarm Relay objects.')
mpeEntPhysicalExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 3, 1, 4)).setObjects(("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeEntPhysicalExtUpTime"), ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeEntPhysicalExtLocation"), ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeEntPhysicalExtAdminStatus"), ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeEntPhysicalExtOperStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mpeEntPhysicalExtGroup = mpeEntPhysicalExtGroup.setStatus('current')
if mibBuilder.loadTexts: mpeEntPhysicalExtGroup.setDescription('The collection of objects which are used in extending the entPhysicalTable.')
mpeEntPhysicalExtNotificationObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 3, 1, 5)).setObjects(("ENTITY-MIB", "entPhysicalIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mpeEntPhysicalExtNotificationObjectGroup = mpeEntPhysicalExtNotificationObjectGroup.setStatus('current')
if mibBuilder.loadTexts: mpeEntPhysicalExtNotificationObjectGroup.setDescription(' A collection of objects that are included in the OBJECTS clause of notifications.')
mpeEntityExtPowerFailureNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 3, 1, 6)).setObjects(("PDN-MPE-DSLAM-SYSTEM-MIB", "mpePowerSourceAFailure"), ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpePowerSourceBFailure"), ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpePowerSourceAOperational"), ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpePowerSourceBOperational"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mpeEntityExtPowerFailureNotificationGroup = mpeEntityExtPowerFailureNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: mpeEntityExtPowerFailureNotificationGroup.setDescription('The collection of objects which are used to notify that trap conditions are met.')
mpeDslamDeprecatedObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 3, 3, 1)).setObjects(("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeAlarmRelayEquipIndex"), ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeAlarmRelayInputContactState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mpeDslamDeprecatedObjectsGroup = mpeDslamDeprecatedObjectsGroup.setStatus('deprecated')
if mibBuilder.loadTexts: mpeDslamDeprecatedObjectsGroup.setDescription('The collection of objects that have been deprecated.')
mpeDslamDeprecatedNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 3, 3, 2)).setObjects(("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeAlarmRelayInputContactStateChanged"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mpeDslamDeprecatedNotificationsGroup = mpeDslamDeprecatedNotificationsGroup.setStatus('deprecated')
if mibBuilder.loadTexts: mpeDslamDeprecatedNotificationsGroup.setDescription('The collection of traps/notifications that have been deprecated.')
mibBuilder.exportSymbols("PDN-MPE-DSLAM-SYSTEM-MIB", mpeAlarmRelayState=mpeAlarmRelayState, mpeAlarmRelay=mpeAlarmRelay, mpeEntPhysicalExtGroup=mpeEntPhysicalExtGroup, mpeEntPhysicalExtTable=mpeEntPhysicalExtTable, mpeEntExtMibObjects=mpeEntExtMibObjects, mpeSysDevDslamMIBNotifications=mpeSysDevDslamMIBNotifications, mpeEntPhysicalExtOperStatus=mpeEntPhysicalExtOperStatus, mpeEntPhysicalExtEntityCreated=mpeEntPhysicalExtEntityCreated, mpeAlarmRelayInputContactState=mpeAlarmRelayInputContactState, mpeCcn=mpeCcn, mpeAlarmRelayEntry=mpeAlarmRelayEntry, mpeEntPhysicalExtEntry=mpeEntPhysicalExtEntry, mpeAlarmRelayInputContactStateChanged=mpeAlarmRelayInputContactStateChanged, mpeAlarmRelayInputStateChanged=mpeAlarmRelayInputStateChanged, mpeFanEntityModuleOperational=mpeFanEntityModuleOperational, mpeSysDevDslamDeprecatedGroup=mpeSysDevDslamDeprecatedGroup, MpeEntExtAdminStatus=MpeEntExtAdminStatus, MpeEntExtOperStatus=MpeEntExtOperStatus, PYSNMP_MODULE_ID=mpe_dslam, mpeSysDevDslamAlarmDeprecatedCompliances=mpeSysDevDslamAlarmDeprecatedCompliances, mpeEntPhysicalExtUpTime=mpeEntPhysicalExtUpTime, mpeEntityExtNotificationGroup=mpeEntityExtNotificationGroup, mpe_dslam=mpe_dslam, mpeEntExtAlarms=mpeEntExtAlarms, mpeAlarmRelayEquipIndex=mpeAlarmRelayEquipIndex, mpeDslamDeprecatedObjectsGroup=mpeDslamDeprecatedObjectsGroup, mpeSysDevDslamAlarmStateGroup=mpeSysDevDslamAlarmStateGroup, mpePowerSourceAOperational=mpePowerSourceAOperational, mpeEntityExtPowerFailureNotificationGroup=mpeEntityExtPowerFailureNotificationGroup, mpeSysDevDslamAlarmCompliances=mpeSysDevDslamAlarmCompliances, mpeEntExtAlarmEntry=mpeEntExtAlarmEntry, mpeSysDevDslamCompliances=mpeSysDevDslamCompliances, mpeNonSupportedMCC=mpeNonSupportedMCC, mpeNonSupportedChassis=mpeNonSupportedChassis, mpeSysDevDslamGroups=mpeSysDevDslamGroups, mpeEntPhysicalExtNotificationObjectGroup=mpeEntPhysicalExtNotificationObjectGroup, mpeFanEntityModuleFailure=mpeFanEntityModuleFailure, mpeEntExtAlarm=mpeEntExtAlarm, mpeEntPhysicalExtAdminStatus=mpeEntPhysicalExtAdminStatus, mpeDeviceFailureCleared=mpeDeviceFailureCleared, mpeEntExtAlarmTable=mpeEntExtAlarmTable, mpePowerSourceBOperational=mpePowerSourceBOperational, mpeSysDevDslamMIBObjects=mpeSysDevDslamMIBObjects, mpeEntPhysicalExtLocation=mpeEntPhysicalExtLocation, mpeDeviceFailure=mpeDeviceFailure, mpePowerSourceAFailure=mpePowerSourceAFailure, mpeAlarmRelayTable=mpeAlarmRelayTable, mpeSysDevDslamAlarmRelayGroup=mpeSysDevDslamAlarmRelayGroup, mpePowerSourceBFailure=mpePowerSourceBFailure, mpeEntPhysicalExtEntityChanged=mpeEntPhysicalExtEntityChanged, mpeDslamDeprecatedNotificationsGroup=mpeDslamDeprecatedNotificationsGroup, mpeSysDevDslamMIBTraps=mpeSysDevDslamMIBTraps, mpeSysDevDslamConformance=mpeSysDevDslamConformance, mpeEntPhysicalExtEntityDeleted=mpeEntPhysicalExtEntityDeleted)
