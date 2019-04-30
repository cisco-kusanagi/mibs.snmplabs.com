#
# PySNMP MIB module Juniper-CLI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-CLI-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:51:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
JuniLogSeverity, = mibBuilder.importSymbols("Juniper-TC", "JuniLogSeverity")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Unsigned32, ModuleIdentity, MibIdentifier, Integer32, Gauge32, Bits, IpAddress, Counter32, ObjectIdentity, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ModuleIdentity", "MibIdentifier", "Integer32", "Gauge32", "Bits", "IpAddress", "Counter32", "ObjectIdentity", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso")
TextualConvention, TruthValue, DisplayString, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString", "DateAndTime")
juniCliMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30))
juniCliMIB.setRevisions(('2007-12-10 13:25', '2002-09-16 21:44', '2000-09-26 13:50', '1999-12-01 00:00',))
if mibBuilder.loadTexts: juniCliMIB.setLastUpdated('200712101325Z')
if mibBuilder.loadTexts: juniCliMIB.setOrganization('Juniper Networks, Inc.')
juniCliTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 0))
juniCliObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1))
juniCliConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2))
juniCliGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 1))
juniCliSecurity = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 2))
juniCliSecurityTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniCliSecurityTrapEnable.setStatus('current')
juniCliConfigurationTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 3), )
if mibBuilder.loadTexts: juniCliConfigurationTable.setStatus('current')
juniCliConfigurationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 3, 1), ).setIndexNames((0, "Juniper-CLI-MIB", "juniCliConfigurationIndex"))
if mibBuilder.loadTexts: juniCliConfigurationEntry.setStatus('current')
juniCliConfigurationIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: juniCliConfigurationIndex.setStatus('current')
juniCliConfigurationFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniCliConfigurationFileName.setStatus('current')
juniCliConfigurationApply = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("juniCliConfigurationReadyToApply", 0), ("juniCliConfigurationApplyNow", 1))).clone('juniCliConfigurationReadyToApply')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniCliConfigurationApply.setStatus('current')
juniCliConfigurationOpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("juniCliConfigurationOpNoOp", 0), ("juniCliConfigurationOpSuccessful", 1), ("juniCliConfigurationOpInProgress", 2), ("juniCliConfigurationFileNotFound", 3), ("juniCliConfigurationFileIncompatible", 4), ("juniCliConfigurationOperationFailed", 5))).clone('juniCliConfigurationOpNoOp')).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniCliConfigurationOpStatus.setStatus('current')
juniCliSecurityAlertPriority = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 2, 1), JuniLogSeverity()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: juniCliSecurityAlertPriority.setStatus('current')
juniCliSecurityAlertMessage = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 2, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: juniCliSecurityAlertMessage.setStatus('current')
juniCliSecurityAlertTime = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 2, 3), DateAndTime()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: juniCliSecurityAlertTime.setStatus('current')
juniCliSecurityAlert = NotificationType((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 0, 1)).setObjects(("Juniper-CLI-MIB", "juniCliSecurityAlertPriority"), ("Juniper-CLI-MIB", "juniCliSecurityAlertMessage"), ("Juniper-CLI-MIB", "juniCliSecurityAlertTime"))
if mibBuilder.loadTexts: juniCliSecurityAlert.setStatus('current')
juniCliCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2, 1))
juniCliGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2, 2))
juniCliCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2, 1, 1)).setObjects(("Juniper-CLI-MIB", "juniCliGroup"), ("Juniper-CLI-MIB", "juniCliSecurityAlertGroup"), ("Juniper-CLI-MIB", "juniCliSecurityTrapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniCliCompliance = juniCliCompliance.setStatus('obsolete')
juniCliCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2, 1, 2)).setObjects(("Juniper-CLI-MIB", "juniCliGroup"), ("Juniper-CLI-MIB", "juniCliSecurityAlertGroup"), ("Juniper-CLI-MIB", "juniCliSecurityTrapGroup"), ("Juniper-CLI-MIB", "juniCliConfigurationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniCliCompliance2 = juniCliCompliance2.setStatus('current')
juniCliGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2, 2, 1)).setObjects(("Juniper-CLI-MIB", "juniCliSecurityTrapEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniCliGroup = juniCliGroup.setStatus('current')
juniCliSecurityAlertGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2, 2, 2)).setObjects(("Juniper-CLI-MIB", "juniCliSecurityAlertPriority"), ("Juniper-CLI-MIB", "juniCliSecurityAlertMessage"), ("Juniper-CLI-MIB", "juniCliSecurityAlertTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniCliSecurityAlertGroup = juniCliSecurityAlertGroup.setStatus('current')
juniCliSecurityTrapGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2, 2, 3)).setObjects(("Juniper-CLI-MIB", "juniCliSecurityAlert"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniCliSecurityTrapGroup = juniCliSecurityTrapGroup.setStatus('current')
juniCliConfigurationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2, 2, 4)).setObjects(("Juniper-CLI-MIB", "juniCliConfigurationFileName"), ("Juniper-CLI-MIB", "juniCliConfigurationApply"), ("Juniper-CLI-MIB", "juniCliConfigurationOpStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniCliConfigurationGroup = juniCliConfigurationGroup.setStatus('current')
mibBuilder.exportSymbols("Juniper-CLI-MIB", juniCliConfigurationIndex=juniCliConfigurationIndex, juniCliSecurityAlert=juniCliSecurityAlert, juniCliConfigurationTable=juniCliConfigurationTable, juniCliSecurityAlertMessage=juniCliSecurityAlertMessage, juniCliSecurity=juniCliSecurity, juniCliConfigurationGroup=juniCliConfigurationGroup, juniCliGroups=juniCliGroups, juniCliObjects=juniCliObjects, juniCliSecurityAlertTime=juniCliSecurityAlertTime, juniCliSecurityAlertGroup=juniCliSecurityAlertGroup, juniCliCompliance=juniCliCompliance, juniCliMIB=juniCliMIB, juniCliGeneral=juniCliGeneral, juniCliConfigurationOpStatus=juniCliConfigurationOpStatus, juniCliCompliances=juniCliCompliances, juniCliSecurityAlertPriority=juniCliSecurityAlertPriority, juniCliConfigurationEntry=juniCliConfigurationEntry, juniCliCompliance2=juniCliCompliance2, juniCliGroup=juniCliGroup, juniCliSecurityTrapEnable=juniCliSecurityTrapEnable, juniCliConformance=juniCliConformance, juniCliConfigurationApply=juniCliConfigurationApply, PYSNMP_MODULE_ID=juniCliMIB, juniCliConfigurationFileName=juniCliConfigurationFileName, juniCliSecurityTrapGroup=juniCliSecurityTrapGroup, juniCliTrap=juniCliTrap)
