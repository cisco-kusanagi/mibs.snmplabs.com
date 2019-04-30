#
# PySNMP MIB module TIMETRA-ALARM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TIMETRA-ALARM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:09:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ModuleIdentity, Counter64, Gauge32, NotificationType, IpAddress, TimeTicks, ObjectIdentity, iso, Unsigned32, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ModuleIdentity", "Counter64", "Gauge32", "NotificationType", "IpAddress", "TimeTicks", "ObjectIdentity", "iso", "Unsigned32", "Integer32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
timetraSRMIBModules, tmnxSRNotifyPrefix, tmnxSRObjs, tmnxSRConfs = mibBuilder.importSymbols("TIMETRA-GLOBAL-MIB", "timetraSRMIBModules", "tmnxSRNotifyPrefix", "tmnxSRObjs", "tmnxSRConfs")
TmnxEnabledDisabled, = mibBuilder.importSymbols("TIMETRA-TC-MIB", "TmnxEnabledDisabled")
timetraAlarmMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 77))
timetraAlarmMIBModule.setRevisions(('2011-02-01 00:00',))
if mibBuilder.loadTexts: timetraAlarmMIBModule.setLastUpdated('201102010000Z')
if mibBuilder.loadTexts: timetraAlarmMIBModule.setOrganization('Alcatel-Lucent')
tmnxAlarmObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 77))
tmnxAlarmNotifyPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 77))
tmnxAlarmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 77))
tmnxAlarmConfigTimeStamps = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 77, 1))
tmnxAlarmConfigurations = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 77, 2))
tmnxAlarmNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 77, 0))
tmnxAlarmCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 77, 1))
tmnxAlarmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 77, 2))
tmnxAlarmSystemConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 77, 2, 1))
tmnxAlarmAdminState = MibScalar((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 77, 2, 1, 1), TmnxEnabledDisabled().clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmnxAlarmAdminState.setStatus('current')
tmnxAlarmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 77, 1, 1)).setObjects(("TIMETRA-ALARM-MIB", "tmnxAlarmSystemConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxAlarmCompliance = tmnxAlarmCompliance.setStatus('current')
tmnxAlarmV9v0Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 77, 2, 1))
tmnxAlarmSystemConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 77, 2, 1, 1)).setObjects(("TIMETRA-ALARM-MIB", "tmnxAlarmAdminState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxAlarmSystemConfigGroup = tmnxAlarmSystemConfigGroup.setStatus('current')
mibBuilder.exportSymbols("TIMETRA-ALARM-MIB", tmnxAlarmAdminState=tmnxAlarmAdminState, tmnxAlarmNotifyPrefix=tmnxAlarmNotifyPrefix, tmnxAlarmSystemConfig=tmnxAlarmSystemConfig, tmnxAlarmConfigurations=tmnxAlarmConfigurations, tmnxAlarmConfigTimeStamps=tmnxAlarmConfigTimeStamps, tmnxAlarmCompliance=tmnxAlarmCompliance, tmnxAlarmSystemConfigGroup=tmnxAlarmSystemConfigGroup, timetraAlarmMIBModule=timetraAlarmMIBModule, tmnxAlarmV9v0Groups=tmnxAlarmV9v0Groups, tmnxAlarmObjs=tmnxAlarmObjs, tmnxAlarmGroups=tmnxAlarmGroups, tmnxAlarmConformance=tmnxAlarmConformance, PYSNMP_MODULE_ID=timetraAlarmMIBModule, tmnxAlarmNotifications=tmnxAlarmNotifications, tmnxAlarmCompliances=tmnxAlarmCompliances)
