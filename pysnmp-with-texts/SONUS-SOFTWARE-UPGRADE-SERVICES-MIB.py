#
# PySNMP MIB module SONUS-SOFTWARE-UPGRADE-SERVICES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SONUS-SOFTWARE-UPGRADE-SERVICES-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:10:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Counter64, Integer32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Bits, ModuleIdentity, TimeTicks, NotificationType, Unsigned32, IpAddress, iso, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter64", "Integer32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Bits", "ModuleIdentity", "TimeTicks", "NotificationType", "Unsigned32", "IpAddress", "iso", "MibIdentifier")
DisplayString, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "DateAndTime")
sonusEventClass, sonusEventLevel, sonusEventDescription, sonusShelfIndex = mibBuilder.importSymbols("SONUS-COMMON-MIB", "sonusEventClass", "sonusEventLevel", "sonusEventDescription", "sonusShelfIndex")
sonusServicesMIBs, = mibBuilder.importSymbols("SONUS-SMI", "sonusServicesMIBs")
sonusSoftwareUpgradeServicesMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2879, 2, 5, 11))
if mibBuilder.loadTexts: sonusSoftwareUpgradeServicesMIB.setLastUpdated('200104180000Z')
if mibBuilder.loadTexts: sonusSoftwareUpgradeServicesMIB.setOrganization('Sonus Networks, Inc.')
if mibBuilder.loadTexts: sonusSoftwareUpgradeServicesMIB.setContactInfo(' Customer Support Sonus Networks, Inc, 5 carlisle Road Westford, MA 01886 USA Tel: 978-692-8999 Fax: 978-392-9118 E-mail: cs.snmp@sonusnet.com')
if mibBuilder.loadTexts: sonusSoftwareUpgradeServicesMIB.setDescription('The MIB Module for Software Upgrade Configuration.')
class SonusSoftwareUpgradeState(TextualConvention, Integer32):
    description = 'Represents the different states in LSWU FSM. (Internal use only)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))
    namedValues = NamedValues(("idle", 0), ("query", 1), ("init", 2), ("delay1", 3), ("start", 4), ("sxOne", 5), ("waitSync", 6), ("sxTwoTx", 7), ("sxTwoRx", 8), ("sxTwoWait", 9), ("variant", 10), ("prepare", 11), ("stopCalls", 12), ("firstPns", 13), ("cnsReset", 14), ("spsReset", 15), ("pnsReset", 16), ("sxDelay", 17), ("done", 18))

sonusSoftwareUpgradeServicesMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1))
sonusSwUpgradeShelfAdmnTable = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 1), )
if mibBuilder.loadTexts: sonusSwUpgradeShelfAdmnTable.setStatus('current')
if mibBuilder.loadTexts: sonusSwUpgradeShelfAdmnTable.setDescription('This table specifies the software upgrade configuration.')
sonusSwUpgradeShelfAdmnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 1, 1), ).setIndexNames((0, "SONUS-SOFTWARE-UPGRADE-SERVICES-MIB", "sonusSwUpgradeShelfAdmnShelfIndex"))
if mibBuilder.loadTexts: sonusSwUpgradeShelfAdmnEntry.setStatus('current')
if mibBuilder.loadTexts: sonusSwUpgradeShelfAdmnEntry.setDescription('')
sonusSwUpgradeShelfAdmnShelfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusSwUpgradeShelfAdmnShelfIndex.setStatus('current')
if mibBuilder.loadTexts: sonusSwUpgradeShelfAdmnShelfIndex.setDescription('The shelf index of this software upgrade entry.')
sonusSwUpgradeShelfAdmnInit = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ready", 1), ("initialize", 2))).clone('ready')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusSwUpgradeShelfAdmnInit.setStatus('current')
if mibBuilder.loadTexts: sonusSwUpgradeShelfAdmnInit.setDescription('Initialize the software upgrade, verify software image availability, check for unsupported features. The feature check can be disabled by setting sonusSwUpgradeShelfAdmnOverrideFeatureCheck in the same request. This MIB object can only be set through the CLI, and only by a user with admin privileges; it always reads as ready(1).')
sonusSwUpgradeShelfAdmnUpgradeNow = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ready", 1), ("upgrade", 2))).clone('ready')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusSwUpgradeShelfAdmnUpgradeNow.setStatus('current')
if mibBuilder.loadTexts: sonusSwUpgradeShelfAdmnUpgradeNow.setDescription('Initiate the software upgrade of the specified shelf now. This MIB object can only be set through the CLI, and only by a user with admin privileges; it always reads as ready(1).')
sonusSwUpgradeShelfAdmnHalt = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ready", 1), ("halt", 2))).clone('ready')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusSwUpgradeShelfAdmnHalt.setStatus('current')
if mibBuilder.loadTexts: sonusSwUpgradeShelfAdmnHalt.setDescription('Halt the software upgrade in progress. This MIB object can only be set through the CLI, and only by a user with admin privileges; it always reads as ready(1).')
sonusSwUpgradeShelfAdmnCommitDirectory = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ready", 1), ("commit", 2))).clone('ready')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusSwUpgradeShelfAdmnCommitDirectory.setStatus('current')
if mibBuilder.loadTexts: sonusSwUpgradeShelfAdmnCommitDirectory.setDescription('Commit the new software distribution directory name into NVS. This MIB object can only be set by a user with admin privileges; it always reads as ready(1).')
sonusSwUpgradeShelfAdmnDirectory = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusSwUpgradeShelfAdmnDirectory.setStatus('current')
if mibBuilder.loadTexts: sonusSwUpgradeShelfAdmnDirectory.setDescription('The new software distribution directory name. This MIB object can only be set by a user with admin privileges.')
sonusSwUpgradeShelfAdmnOverrideFeatureCheck = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ready", 1), ("override", 2))).clone('ready')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusSwUpgradeShelfAdmnOverrideFeatureCheck.setStatus('current')
if mibBuilder.loadTexts: sonusSwUpgradeShelfAdmnOverrideFeatureCheck.setDescription('Ignore the check for unsupported features (i.e. features that would prevent a software upgrade from occurring) during initialization. This MIB object must be set with sonusSwUpgradeShelfAdmnInit in the same request. This MIB object can only be set through the CLI, and only by a user with admin privileges; it always reads as ready(1).')
sonusSwUpgradeShelfStatTable = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 2), )
if mibBuilder.loadTexts: sonusSwUpgradeShelfStatTable.setStatus('current')
if mibBuilder.loadTexts: sonusSwUpgradeShelfStatTable.setDescription('This table contains status information about the software upgrade on a shelf.')
sonusSwUpgradeShelfStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 2, 1), ).setIndexNames((0, "SONUS-SOFTWARE-UPGRADE-SERVICES-MIB", "sonusSwUpgradeShelfStatShelfIndex"))
if mibBuilder.loadTexts: sonusSwUpgradeShelfStatEntry.setStatus('current')
if mibBuilder.loadTexts: sonusSwUpgradeShelfStatEntry.setDescription('')
sonusSwUpgradeShelfStatShelfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusSwUpgradeShelfStatShelfIndex.setStatus('current')
if mibBuilder.loadTexts: sonusSwUpgradeShelfStatShelfIndex.setDescription('Identifies the target shelf within the node.')
sonusSwUpgradeShelfStatStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("idle", 1), ("busy", 2), ("complete", 3), ("incomplete", 4), ("commitRequired", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusSwUpgradeShelfStatStatus.setStatus('current')
if mibBuilder.loadTexts: sonusSwUpgradeShelfStatStatus.setDescription('Indicates the software upgrade status of the shelf.')
sonusSwUpgradeShelfStatCurSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusSwUpgradeShelfStatCurSlot.setStatus('current')
if mibBuilder.loadTexts: sonusSwUpgradeShelfStatCurSlot.setDescription('Identifies the slot currently being upgraded with new software.')
sonusSwUpgradeShelfStatSlotRemain = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusSwUpgradeShelfStatSlotRemain.setStatus('current')
if mibBuilder.loadTexts: sonusSwUpgradeShelfStatSlotRemain.setDescription('Identifies number of slots within the shelf remained to be upgraded.')
sonusSwUpgradeShelfStatGroupRemain = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusSwUpgradeShelfStatGroupRemain.setStatus('current')
if mibBuilder.loadTexts: sonusSwUpgradeShelfStatGroupRemain.setDescription('')
sonusSwUpgradeShelfStatDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusSwUpgradeShelfStatDuration.setStatus('current')
if mibBuilder.loadTexts: sonusSwUpgradeShelfStatDuration.setDescription('Indicates the duration of the software upgrade in seconds.')
sonusSwUpgradeShelfStatStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 2, 1, 7), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusSwUpgradeShelfStatStartTime.setStatus('current')
if mibBuilder.loadTexts: sonusSwUpgradeShelfStatStartTime.setDescription('Indicates the start time of the software upgrade')
sonusSwUpgradeShelfStatLastReason = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))).clone(namedValues=NamedValues(("none", 0), ("successfulCompletion", 1), ("initTimeout", 2), ("manualHalt", 3), ("upgradeNotRequired", 4), ("fileUnavailable", 5), ("parametersNotSaved", 6), ("flashUpdateInProgress", 7), ("redundSlotActive", 8), ("switchover1Timeout", 9), ("sync1Timeout", 10), ("switchover2Timeout", 11), ("sync2Timeout", 12), ("rebootTimeout", 13), ("mnsNotSynced", 14), ("notActive", 15), ("internalTimerUnavailable", 16), ("internalQueryTimeout", 17), ("internalResourceUnavailable", 18), ("internalRtmError", 19), ("mnsSwitchover", 20)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusSwUpgradeShelfStatLastReason.setStatus('current')
if mibBuilder.loadTexts: sonusSwUpgradeShelfStatLastReason.setDescription('Indicates the exit reason of the last live software upgrade.')
sonusSwUpgradeShelfStatLastState = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 2, 1, 9), SonusSoftwareUpgradeState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusSwUpgradeShelfStatLastState.setStatus('current')
if mibBuilder.loadTexts: sonusSwUpgradeShelfStatLastState.setDescription('Indicates the last state of the LSWU FSM. (Internal use only)')
sonusSwUpgradeShelfStatState = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 2, 1, 10), SonusSoftwareUpgradeState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusSwUpgradeShelfStatState.setStatus('current')
if mibBuilder.loadTexts: sonusSwUpgradeShelfStatState.setDescription('Indicates the current state of the LSWU FSM. (Internal use only)')
sonusSwUpgradeSlotStatTable = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 3), )
if mibBuilder.loadTexts: sonusSwUpgradeSlotStatTable.setStatus('current')
if mibBuilder.loadTexts: sonusSwUpgradeSlotStatTable.setDescription('This table contains status information about the software upgrade on a shelf.')
sonusSwUpgradeSlotStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 3, 1), ).setIndexNames((0, "SONUS-SOFTWARE-UPGRADE-SERVICES-MIB", "sonusSwUpgradeSlotStatShelfIndex"), (0, "SONUS-SOFTWARE-UPGRADE-SERVICES-MIB", "sonusSwUpgradeSlotStatSlotIndex"))
if mibBuilder.loadTexts: sonusSwUpgradeSlotStatEntry.setStatus('current')
if mibBuilder.loadTexts: sonusSwUpgradeSlotStatEntry.setDescription('')
sonusSwUpgradeSlotStatShelfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusSwUpgradeSlotStatShelfIndex.setStatus('current')
if mibBuilder.loadTexts: sonusSwUpgradeSlotStatShelfIndex.setDescription('Identifies the target shelf within the node.')
sonusSwUpgradeSlotStatSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusSwUpgradeSlotStatSlotIndex.setStatus('current')
if mibBuilder.loadTexts: sonusSwUpgradeSlotStatSlotIndex.setDescription('Identifies the target slot within the shelf.')
sonusSwUpgradeSlotStatStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("idle", 1), ("busy", 2), ("complete", 3), ("unknown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusSwUpgradeSlotStatStatus.setStatus('current')
if mibBuilder.loadTexts: sonusSwUpgradeSlotStatStatus.setDescription('Identifies the software upgrade status of a slot.')
sonusSwUpgradeSlotStatUpgrade = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("smooth", 2), ("disrupt", 3), ("unavailable", 4), ("unknown", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusSwUpgradeSlotStatUpgrade.setStatus('current')
if mibBuilder.loadTexts: sonusSwUpgradeSlotStatUpgrade.setDescription('')
sonusSwUpgradeSlotStatVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 1, 3, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusSwUpgradeSlotStatVersion.setStatus('current')
if mibBuilder.loadTexts: sonusSwUpgradeSlotStatVersion.setDescription('The software version available for upgrade on the slot.')
sonusSoftwareUpgradeServicesMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 2))
sonusSoftwareUpgradeServicesMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 2, 0))
sonusSoftwareUpgradeServicesMIBNotificationsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 2, 1))
sonusSoftwareUpgradeInitiatedNotification = NotificationType((1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 2, 0, 1)).setObjects(("SONUS-COMMON-MIB", "sonusShelfIndex"), ("SONUS-SOFTWARE-UPGRADE-SERVICES-MIB", "sonusSwUpgradeShelfAdmnDirectory"), ("SONUS-COMMON-MIB", "sonusEventDescription"), ("SONUS-COMMON-MIB", "sonusEventClass"), ("SONUS-COMMON-MIB", "sonusEventLevel"))
if mibBuilder.loadTexts: sonusSoftwareUpgradeInitiatedNotification.setStatus('current')
if mibBuilder.loadTexts: sonusSoftwareUpgradeInitiatedNotification.setDescription('This trap indicates that a software upgrade to the specified Software Path directory has been initiated by the user for this shelf.')
sonusSoftwareUpgradeTerminatedNotification = NotificationType((1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 2, 0, 2)).setObjects(("SONUS-COMMON-MIB", "sonusShelfIndex"), ("SONUS-SOFTWARE-UPGRADE-SERVICES-MIB", "sonusSwUpgradeShelfAdmnDirectory"), ("SONUS-SOFTWARE-UPGRADE-SERVICES-MIB", "sonusSwUpgradeShelfStatLastReason"), ("SONUS-COMMON-MIB", "sonusEventDescription"), ("SONUS-COMMON-MIB", "sonusEventClass"), ("SONUS-COMMON-MIB", "sonusEventLevel"))
if mibBuilder.loadTexts: sonusSoftwareUpgradeTerminatedNotification.setStatus('current')
if mibBuilder.loadTexts: sonusSoftwareUpgradeTerminatedNotification.setDescription('This trap indicates that a software upgrade to the specified Software Path directory has terminated in this shelf for the specified reason.')
sonusSoftwareUpgradeSucceededNotification = NotificationType((1, 3, 6, 1, 4, 1, 2879, 2, 5, 11, 2, 0, 3)).setObjects(("SONUS-COMMON-MIB", "sonusShelfIndex"), ("SONUS-SOFTWARE-UPGRADE-SERVICES-MIB", "sonusSwUpgradeShelfAdmnDirectory"), ("SONUS-SOFTWARE-UPGRADE-SERVICES-MIB", "sonusSwUpgradeShelfStatLastReason"), ("SONUS-COMMON-MIB", "sonusEventDescription"), ("SONUS-COMMON-MIB", "sonusEventClass"), ("SONUS-COMMON-MIB", "sonusEventLevel"))
if mibBuilder.loadTexts: sonusSoftwareUpgradeSucceededNotification.setStatus('current')
if mibBuilder.loadTexts: sonusSoftwareUpgradeSucceededNotification.setDescription('This trap indicates that a software upgrade to the specified Software Path directory has succeeded in this shelf for the specified reason.')
mibBuilder.exportSymbols("SONUS-SOFTWARE-UPGRADE-SERVICES-MIB", sonusSwUpgradeShelfStatStatus=sonusSwUpgradeShelfStatStatus, sonusSwUpgradeShelfStatEntry=sonusSwUpgradeShelfStatEntry, PYSNMP_MODULE_ID=sonusSoftwareUpgradeServicesMIB, sonusSwUpgradeShelfStatLastState=sonusSwUpgradeShelfStatLastState, sonusSwUpgradeShelfAdmnHalt=sonusSwUpgradeShelfAdmnHalt, sonusSwUpgradeSlotStatShelfIndex=sonusSwUpgradeSlotStatShelfIndex, sonusSwUpgradeSlotStatStatus=sonusSwUpgradeSlotStatStatus, sonusSwUpgradeShelfStatDuration=sonusSwUpgradeShelfStatDuration, sonusSoftwareUpgradeServicesMIBNotifications=sonusSoftwareUpgradeServicesMIBNotifications, sonusSwUpgradeShelfStatSlotRemain=sonusSwUpgradeShelfStatSlotRemain, sonusSwUpgradeShelfAdmnDirectory=sonusSwUpgradeShelfAdmnDirectory, sonusSwUpgradeSlotStatEntry=sonusSwUpgradeSlotStatEntry, sonusSoftwareUpgradeSucceededNotification=sonusSoftwareUpgradeSucceededNotification, sonusSwUpgradeSlotStatTable=sonusSwUpgradeSlotStatTable, sonusSwUpgradeShelfAdmnUpgradeNow=sonusSwUpgradeShelfAdmnUpgradeNow, sonusSwUpgradeShelfStatTable=sonusSwUpgradeShelfStatTable, sonusSwUpgradeSlotStatVersion=sonusSwUpgradeSlotStatVersion, sonusSwUpgradeShelfAdmnOverrideFeatureCheck=sonusSwUpgradeShelfAdmnOverrideFeatureCheck, sonusSwUpgradeShelfAdmnInit=sonusSwUpgradeShelfAdmnInit, sonusSwUpgradeShelfAdmnEntry=sonusSwUpgradeShelfAdmnEntry, sonusSwUpgradeSlotStatUpgrade=sonusSwUpgradeSlotStatUpgrade, sonusSoftwareUpgradeServicesMIB=sonusSoftwareUpgradeServicesMIB, sonusSwUpgradeShelfStatStartTime=sonusSwUpgradeShelfStatStartTime, sonusSwUpgradeShelfStatCurSlot=sonusSwUpgradeShelfStatCurSlot, sonusSwUpgradeShelfStatState=sonusSwUpgradeShelfStatState, sonusSwUpgradeShelfStatShelfIndex=sonusSwUpgradeShelfStatShelfIndex, sonusSwUpgradeSlotStatSlotIndex=sonusSwUpgradeSlotStatSlotIndex, sonusSoftwareUpgradeTerminatedNotification=sonusSoftwareUpgradeTerminatedNotification, SonusSoftwareUpgradeState=SonusSoftwareUpgradeState, sonusSwUpgradeShelfStatGroupRemain=sonusSwUpgradeShelfStatGroupRemain, sonusSwUpgradeShelfAdmnCommitDirectory=sonusSwUpgradeShelfAdmnCommitDirectory, sonusSwUpgradeShelfAdmnTable=sonusSwUpgradeShelfAdmnTable, sonusSwUpgradeShelfAdmnShelfIndex=sonusSwUpgradeShelfAdmnShelfIndex, sonusSoftwareUpgradeServicesMIBNotificationsObjects=sonusSoftwareUpgradeServicesMIBNotificationsObjects, sonusSoftwareUpgradeServicesMIBObjects=sonusSoftwareUpgradeServicesMIBObjects, sonusSwUpgradeShelfStatLastReason=sonusSwUpgradeShelfStatLastReason, sonusSoftwareUpgradeInitiatedNotification=sonusSoftwareUpgradeInitiatedNotification, sonusSoftwareUpgradeServicesMIBNotificationsPrefix=sonusSoftwareUpgradeServicesMIBNotificationsPrefix)