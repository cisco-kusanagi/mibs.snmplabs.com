#
# PySNMP MIB module TIMETRA-ALARM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TIMETRA-ALARM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:16:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Integer32, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter64, IpAddress, Counter32, ObjectIdentity, MibIdentifier, Bits, iso, Unsigned32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter64", "IpAddress", "Counter32", "ObjectIdentity", "MibIdentifier", "Bits", "iso", "Unsigned32", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
timetraSRMIBModules, tmnxSRObjs, tmnxSRConfs, tmnxSRNotifyPrefix = mibBuilder.importSymbols("TIMETRA-GLOBAL-MIB", "timetraSRMIBModules", "tmnxSRObjs", "tmnxSRConfs", "tmnxSRNotifyPrefix")
TmnxEnabledDisabled, = mibBuilder.importSymbols("TIMETRA-TC-MIB", "TmnxEnabledDisabled")
timetraAlarmMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 77))
timetraAlarmMIBModule.setRevisions(('2011-02-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: timetraAlarmMIBModule.setRevisionsDescriptions(('Rev 1.0 1 Feb 2011 00:00 1.0 release of the TIMETRA-ALARM-MIB.',))
if mibBuilder.loadTexts: timetraAlarmMIBModule.setLastUpdated('201102010000Z')
if mibBuilder.loadTexts: timetraAlarmMIBModule.setOrganization('Alcatel-Lucent')
if mibBuilder.loadTexts: timetraAlarmMIBModule.setContactInfo('Alcatel-Lucent SROS Support Web: http://support.alcatel-lucent.com ')
if mibBuilder.loadTexts: timetraAlarmMIBModule.setDescription("This document, an extension of ALARM-MIB defined in RFC 3877, is the SNMP MIB module to manage and provision the alarm management components of the Alcatel-Lucent SROS device. Copyright (c) 2010-2011 Alcatel-Lucent. All rights reserved. Reproduction of this document is authorized on the condition that the foregoing copyright notice is included. This SNMP MIB module (Specification) embodies Alcatel-Lucent's proprietary intellectual property. Alcatel-Lucent retains all title and ownership in the Specification, including any revisions. Alcatel-Lucent grants all interested parties a non-exclusive license to use and distribute an unmodified copy of this Specification in connection with management of Alcatel-Lucent products, and without fee, provided this copyright notice and license appear on all copies. This Specification is supplied 'as is', and Alcatel-Lucent makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
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
if mibBuilder.loadTexts: tmnxAlarmAdminState.setDescription("The value of tmnxAlarmAdminState specifies whether or not alarm management is enabled on the system. As a result of setting tmnxAlarmAdminState to 'disabled(2)', all alarms present in MIB table ALARM-MIB::alarmActiveTable will be cleared, all rows in MIB table ALARM-MIB::alarmClearTable will be destroyed, and no new alarms will be raised.")
tmnxAlarmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 77, 1, 1)).setObjects(("TIMETRA-ALARM-MIB", "tmnxAlarmSystemConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxAlarmCompliance = tmnxAlarmCompliance.setStatus('current')
if mibBuilder.loadTexts: tmnxAlarmCompliance.setDescription('The compliance statement for the management of alarms for Release 9.0 on SROS series systems.')
tmnxAlarmV9v0Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 77, 2, 1))
tmnxAlarmSystemConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 77, 2, 1, 1)).setObjects(("TIMETRA-ALARM-MIB", "tmnxAlarmAdminState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxAlarmSystemConfigGroup = tmnxAlarmSystemConfigGroup.setStatus('current')
if mibBuilder.loadTexts: tmnxAlarmSystemConfigGroup.setDescription('The group of objects maintaining system configuration for alarm management on SROS series systems.')
mibBuilder.exportSymbols("TIMETRA-ALARM-MIB", tmnxAlarmConformance=tmnxAlarmConformance, timetraAlarmMIBModule=timetraAlarmMIBModule, tmnxAlarmObjs=tmnxAlarmObjs, tmnxAlarmConfigTimeStamps=tmnxAlarmConfigTimeStamps, tmnxAlarmConfigurations=tmnxAlarmConfigurations, tmnxAlarmGroups=tmnxAlarmGroups, PYSNMP_MODULE_ID=timetraAlarmMIBModule, tmnxAlarmAdminState=tmnxAlarmAdminState, tmnxAlarmNotifyPrefix=tmnxAlarmNotifyPrefix, tmnxAlarmNotifications=tmnxAlarmNotifications, tmnxAlarmSystemConfig=tmnxAlarmSystemConfig, tmnxAlarmCompliance=tmnxAlarmCompliance, tmnxAlarmCompliances=tmnxAlarmCompliances, tmnxAlarmSystemConfigGroup=tmnxAlarmSystemConfigGroup, tmnxAlarmV9v0Groups=tmnxAlarmV9v0Groups)
