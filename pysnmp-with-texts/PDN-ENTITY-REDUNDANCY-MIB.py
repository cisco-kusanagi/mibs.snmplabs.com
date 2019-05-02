#
# PySNMP MIB module PDN-ENTITY-REDUNDANCY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-ENTITY-REDUNDANCY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:38:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
pdnEntityRedundancy, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdnEntityRedundancy")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Bits, iso, NotificationType, TimeTicks, Unsigned32, IpAddress, MibIdentifier, Integer32, Gauge32, Counter32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "NotificationType", "TimeTicks", "Unsigned32", "IpAddress", "MibIdentifier", "Integer32", "Gauge32", "Counter32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pdnEntRedunMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1))
pdnEntRedunMIB.setRevisions(('2003-07-25 13:00', '2003-05-22 10:00', '2003-05-04 17:00', '2003-03-03 15:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: pdnEntRedunMIB.setRevisionsDescriptions(('J. Pinto - Added pdnRedunGeneralNotificationEnable. - Modified DESCRIPTION for pdnRedunNotificationEnable. ', 'J. Pinto - Fixed spelling name of this mib in line#1 ', 'J. Pinto - Removed the word non-critical from the PdnRedunStates. - Added pdnYCableSelection scalar object. - Added pdnRedunGeneralStatusAlarm scalar object. - Modified PdnRedunAlarmStatus TEXTUAL-CONVENTION. - Added traps for new alarm conditions. ', 'J. Pinto - Modified PdnRedunCmd Textual Convention to add a new forceswitch command.',))
if mibBuilder.loadTexts: pdnEntRedunMIB.setLastUpdated('200301121100Z')
if mibBuilder.loadTexts: pdnEntRedunMIB.setOrganization('Paradyne Corporation MIB Working Group')
if mibBuilder.loadTexts: pdnEntRedunMIB.setContactInfo(' Paradyne Networks Inc. Postal: 8545, 126th Ave. N. Largo, FL 33779 US Editor: Jesus Pinto Email: mibwg_team@eng.paradyne.com')
if mibBuilder.loadTexts: pdnEntRedunMIB.setDescription('This management information module supports the objects to be used for redundancy of entities.')
class PdnRedunStates(TextualConvention, Integer32):
    description = 'This textual Convention describes the valid states relevant to the redundancy feature that an entity module can be. The possibles states are: activeState ----------- the module is currently performing its main functions in the system, including communicating with other modules, monitoring the operation of itself and other standby modules. activeAlarmState ---------------- the same as an activeState except an Alarm condition has been detected on the module. standbyState ------------ the module is primarily in a dormant state until an event is triggered that requires its activation. While in this state, the module only performs background tests to verify that its hardware is operating properly and monitor the active module for proper operation. standbyAlarmState ---------------- the same as an standbyState except a Alarm condition has been detected on the module.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("activeState", 1), ("activeAlarmState", 2), ("standbyState", 3), ("standbyAlarmState", 4))

class PdnRedunCmd(TextualConvention, Integer32):
    description = 'This list of commands allows an user to perform actions on the redundancy entities. The commands are: noCmd ----- This value should be returned by a read request when no previous command has been issue. This value may not be used in a write operation. A wrongValue error shall be returned in this case. switch ------ This is the *Normal* switch. shall be directed to an entity in the Active, Active/Alarm, Standby or Standby/Alarm state. Will cause an entity and its redundant mate to switch roles unless the Standby entity is in a failed state or redundancy is disabled. A switch shall result in the Active or Active/Alarm entity going into a Standby or Standby/Alarm state and the Standby or Standby/Alarm entity going into the Active or Active/Alarm state. forceswitch ----------- This is the *Forced* switch. shall be directed to an entity in the Active, Active/Alarm, Standby or Standby/Alarm state. Will cause an entity and its redundant mate to switch roles regardless of the state of the entities or if redundancy is enabled. A switch shall result in the Active or Active/Alarm entity going into a Standby or Standby/Alarm state and the Standby or Standby/Alarm entity going into the Active or Active/Alarm state.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("noCmd", 1), ("switch", 2), ("forcedswitch", 3))

class PdnRedunAlarmStatus(TextualConvention, Bits):
    description = 'This textual convention lists the possibles alarm status. The status are: noAlarm --------------------------- This is the normal status when there is no alarm condition. linkDefect ---------------------------- This alarm is detected when there is an abnormal condition in the link (e.g., LOS, LOF, etc.) of this redundant unit. hwFailure ---------------------------- This alarm is detected when there is a hardware failure on this redundant unit. hwMissing ---------------------------- This alarm is detected when there is an expected piece of hw that is missing on this redundant unit. hwIncompatible ---------------------------- This alarm is detected when the modules in a redundancy configuration present hardware incompatibilities. fwIncompatible ---------------------------- This alarm is detected when the modules in a redundancy configuration present firmware incompatibilities. cfgIncompatible ----------------------------- This alarm is detected when the modules in a redundancy configuration present configuration incompatibilities.'
    status = 'current'
    namedValues = NamedValues(("noAlarm", 0), ("linkDefect", 1), ("hwFailure", 2), ("hwMissing", 3), ("hwIncompatible", 4), ("fwIncompatible", 5), ("cfgIncompatible", 6))

class PdnRedunGeneralAlarmStatus(TextualConvention, Bits):
    description = 'This textual convention lists the possibles alarm status that are general to the redundancy feature; which are not associated to a particular redundant module. The status are: noAlarm --------------------------- This is the Normal status with no General alarm condition. noActiveModule --------------------------- This alarm is detected when no module is in the Active State. standbyAlarmOrReset ---------------------------- This alarm is detected when on of the modules configured for redundancy is either in the Standby-Alarm or Reset Test state. '
    status = 'current'
    namedValues = NamedValues(("noAlarm", 0), ("noActiveModule", 1), ("standbyAlarmOrReset", 2))

pdnEntityRedundancyMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 1))
pdnEntityRedundancyNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 2))
pdnEntityRedundancyConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 3))
pdnEntityRedundancySelection = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnEntityRedundancySelection.setStatus('current')
if mibBuilder.loadTexts: pdnEntityRedundancySelection.setDescription('This object is used to enable or disable the redundancy feature on this device.')
pdnYCableSelection = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnYCableSelection.setStatus('current')
if mibBuilder.loadTexts: pdnYCableSelection.setDescription('This object is used to configure the Y-cable presence used for tx and rx of data between the redundant units. When the selection is enabled (1), it indicates that the tx and rx signals of each redundant unit are sharing a single common pair to tx and rx data to the network. When the selection is disable (2), it indicates that the tx and rx signals of each redundant unit has a separate (independant) pair to tx and rx data to the network. ')
pdnRedunGeneralAlarmStatus = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 1, 3), PdnRedunGeneralAlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnRedunGeneralAlarmStatus.setStatus('current')
if mibBuilder.loadTexts: pdnRedunGeneralAlarmStatus.setDescription('This object provides status of any General Alarm detected by the redundancy feature. ')
pdnRedunGeneralNotificationEnable = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 1, 6), PdnRedunGeneralAlarmStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnRedunGeneralNotificationEnable.setStatus('current')
if mibBuilder.loadTexts: pdnRedunGeneralNotificationEnable.setDescription('This object provides the ability to enable and disable the following general notifications: o pdnRedunEventNoActiveModule o pdnRedunEventStandbyAlarmOrReset ')
pdnRedunCmdTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 1, 4), )
if mibBuilder.loadTexts: pdnRedunCmdTable.setStatus('current')
if mibBuilder.loadTexts: pdnRedunCmdTable.setDescription('This table contains one row per entity module being used for redundancy.')
pdnRedunCmdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 1, 4, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: pdnRedunCmdEntry.setStatus('current')
if mibBuilder.loadTexts: pdnRedunCmdEntry.setDescription('Commands that can be performed on a particular entity module used for redundancy.')
pdnRedunCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 1, 4, 1, 1), PdnRedunCmd()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnRedunCommand.setStatus('current')
if mibBuilder.loadTexts: pdnRedunCommand.setDescription('This object allows users to command an entity module, configured for redundancy to perform an action such as switch (2). Reading this object should return the last command issued on this interface or noCmd (1) if no command has been issued since last reset.')
pdnRedunStatusTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 1, 5), )
if mibBuilder.loadTexts: pdnRedunStatusTable.setStatus('current')
if mibBuilder.loadTexts: pdnRedunStatusTable.setDescription('This table contains configuration and status information related to events in entity modules used for redundancy.')
pdnRedunStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 1, 5, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: pdnRedunStatusEntry.setStatus('current')
if mibBuilder.loadTexts: pdnRedunStatusEntry.setDescription('Configuration and Status information for a particular entity module used for redundancy.')
pdnRedunEntityState = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 1, 5, 1, 1), PdnRedunStates()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnRedunEntityState.setStatus('current')
if mibBuilder.loadTexts: pdnRedunEntityState.setDescription('This object is used to display the current state on an entity that is used for redundancy.')
pdnRedunAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 1, 5, 1, 2), PdnRedunAlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnRedunAlarmStatus.setStatus('current')
if mibBuilder.loadTexts: pdnRedunAlarmStatus.setDescription('This object provides status of any Alarm detected in a redundant entity.')
pdnRedunNotificationEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 1, 5, 1, 3), PdnRedunAlarmStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnRedunNotificationEnable.setStatus('current')
if mibBuilder.loadTexts: pdnRedunNotificationEnable.setDescription('This object provides the ability to enable and disable the following notifications: o pdnRedunEventHwIncompatible o pdnRedunEventFwIncompatible o pdnRedunEventCfgIncompatible o pdnRedunEventLinkDefect o pdnRedunEventHwFailure o pdnRedunEventHwMissingHwFailure ')
pdnRedunNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 2, 0))
pdnRedunEventNoActiveModule = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 2, 0, 1)).setObjects(("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunGeneralAlarmStatus"))
if mibBuilder.loadTexts: pdnRedunEventNoActiveModule.setStatus('current')
if mibBuilder.loadTexts: pdnRedunEventNoActiveModule.setDescription('This notification will be issued when no module is in the Active State.')
pdnRedunEventHwIncompatible = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 2, 0, 2)).setObjects(("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunAlarmStatus"))
if mibBuilder.loadTexts: pdnRedunEventHwIncompatible.setStatus('current')
if mibBuilder.loadTexts: pdnRedunEventHwIncompatible.setDescription('This notification will be issued when the modules in a redundancy configuration present hardware incompatibilities.')
pdnRedunEventStandbyAlarmOrReset = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 2, 0, 3)).setObjects(("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunGeneralAlarmStatus"))
if mibBuilder.loadTexts: pdnRedunEventStandbyAlarmOrReset.setStatus('current')
if mibBuilder.loadTexts: pdnRedunEventStandbyAlarmOrReset.setDescription('This notification will be issued when one of the modules configured for redundancy is either in the Standby/Alarm or Reset Test state.')
pdnRedunEventFwIncompatible = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 2, 0, 4)).setObjects(("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunAlarmStatus"))
if mibBuilder.loadTexts: pdnRedunEventFwIncompatible.setStatus('current')
if mibBuilder.loadTexts: pdnRedunEventFwIncompatible.setDescription('This notification will be issued when the modules in a redundancy configuration present firmware incompatibilities.')
pdnRedunEventCfgIncompatible = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 2, 0, 5)).setObjects(("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunAlarmStatus"))
if mibBuilder.loadTexts: pdnRedunEventCfgIncompatible.setStatus('current')
if mibBuilder.loadTexts: pdnRedunEventCfgIncompatible.setDescription('This notification will be issued when the modules in a redundancy configuration present configuration incompatibilities.')
pdnRedunEventLinkDefect = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 2, 0, 6)).setObjects(("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunAlarmStatus"))
if mibBuilder.loadTexts: pdnRedunEventLinkDefect.setStatus('current')
if mibBuilder.loadTexts: pdnRedunEventLinkDefect.setDescription('This notification will be issued when a module in a redundancy configuration has a link condition.')
pdnRedunEventHwFailure = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 2, 0, 7)).setObjects(("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunAlarmStatus"))
if mibBuilder.loadTexts: pdnRedunEventHwFailure.setStatus('current')
if mibBuilder.loadTexts: pdnRedunEventHwFailure.setDescription('This notification will be issued when a module in a redundancy configuration has a hardware failure condition.')
pdnRedunEventHwMissingHwFailure = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 2, 0, 8)).setObjects(("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunAlarmStatus"))
if mibBuilder.loadTexts: pdnRedunEventHwMissingHwFailure.setStatus('current')
if mibBuilder.loadTexts: pdnRedunEventHwMissingHwFailure.setDescription('This notification will be issued when a module in a redundancy configuration is expecting a piece of hw to be used for redundancy which can not be found or is not operational. ')
pdnEntityRedundancyCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 3, 1))
pdnEntityRedundancyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 3, 2))
pdnEntityRedundancyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 3, 1, 1)).setObjects(("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedundancyGeneralGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnEntityRedundancyCompliance = pdnEntityRedundancyCompliance.setStatus('current')
if mibBuilder.loadTexts: pdnEntityRedundancyCompliance.setDescription('The compliance statement for SNMP entities which manage the configuration parameters on entities used for redundancy.')
pdnRedundancyGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 3, 2, 1)).setObjects(("PDN-ENTITY-REDUNDANCY-MIB", "pdnEntityRedundancySelection"), ("PDN-ENTITY-REDUNDANCY-MIB", "pdnYCableSelection"), ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunGeneralAlarmStatus"), ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunGeneralNotificationEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnRedundancyGeneralGroup = pdnRedundancyGeneralGroup.setStatus('current')
if mibBuilder.loadTexts: pdnRedundancyGeneralGroup.setDescription('A collection of general configuration objects for the entity redundancy implementation.')
pdnEntityRedundancyOptGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 3, 2, 2)).setObjects(("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunCommand"), ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunNotificationEnable"), ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunEntityState"), ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunAlarmStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnEntityRedundancyOptGroup = pdnEntityRedundancyOptGroup.setStatus('current')
if mibBuilder.loadTexts: pdnEntityRedundancyOptGroup.setDescription(' A collection of configuration objects applicable to redundancy implementations.')
pdnEntityRedundancyEventGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 41, 1, 3, 2, 3)).setObjects(("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunEventNoActiveModule"), ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunEventHwIncompatible"), ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunEventStandbyAlarmOrReset"), ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunEventFwIncompatible"), ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunEventCfgIncompatible"), ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunEventLinkDefect"), ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunEventHwFailure"), ("PDN-ENTITY-REDUNDANCY-MIB", "pdnRedunEventHwMissingHwFailure"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnEntityRedundancyEventGroup = pdnEntityRedundancyEventGroup.setStatus('current')
if mibBuilder.loadTexts: pdnEntityRedundancyEventGroup.setDescription('A collection of redundancy notifications.')
mibBuilder.exportSymbols("PDN-ENTITY-REDUNDANCY-MIB", PdnRedunStates=PdnRedunStates, pdnEntityRedundancyCompliance=pdnEntityRedundancyCompliance, pdnRedunGeneralNotificationEnable=pdnRedunGeneralNotificationEnable, PdnRedunAlarmStatus=PdnRedunAlarmStatus, pdnRedunCmdEntry=pdnRedunCmdEntry, PdnRedunCmd=PdnRedunCmd, pdnYCableSelection=pdnYCableSelection, pdnEntityRedundancyCompliances=pdnEntityRedundancyCompliances, pdnRedunCommand=pdnRedunCommand, pdnEntityRedundancyMIBObjects=pdnEntityRedundancyMIBObjects, pdnRedunStatusTable=pdnRedunStatusTable, pdnEntityRedundancyGroups=pdnEntityRedundancyGroups, pdnRedunEventStandbyAlarmOrReset=pdnRedunEventStandbyAlarmOrReset, pdnEntRedunMIB=pdnEntRedunMIB, pdnRedunEventHwIncompatible=pdnRedunEventHwIncompatible, PdnRedunGeneralAlarmStatus=PdnRedunGeneralAlarmStatus, pdnEntityRedundancyNotifications=pdnEntityRedundancyNotifications, pdnEntityRedundancyConformance=pdnEntityRedundancyConformance, pdnRedunNotificationEnable=pdnRedunNotificationEnable, pdnEntityRedundancyEventGroup=pdnEntityRedundancyEventGroup, pdnRedunCmdTable=pdnRedunCmdTable, pdnRedunAlarmStatus=pdnRedunAlarmStatus, pdnRedunEventCfgIncompatible=pdnRedunEventCfgIncompatible, pdnRedunEventHwMissingHwFailure=pdnRedunEventHwMissingHwFailure, PYSNMP_MODULE_ID=pdnEntRedunMIB, pdnEntityRedundancyOptGroup=pdnEntityRedundancyOptGroup, pdnRedunStatusEntry=pdnRedunStatusEntry, pdnRedunEventHwFailure=pdnRedunEventHwFailure, pdnEntityRedundancySelection=pdnEntityRedundancySelection, pdnRedunEventNoActiveModule=pdnRedunEventNoActiveModule, pdnRedundancyGeneralGroup=pdnRedundancyGeneralGroup, pdnRedunGeneralAlarmStatus=pdnRedunGeneralAlarmStatus, pdnRedunEventLinkDefect=pdnRedunEventLinkDefect, pdnRedunEventFwIncompatible=pdnRedunEventFwIncompatible, pdnRedunEntityState=pdnRedunEntityState, pdnRedunNotificationsPrefix=pdnRedunNotificationsPrefix)
