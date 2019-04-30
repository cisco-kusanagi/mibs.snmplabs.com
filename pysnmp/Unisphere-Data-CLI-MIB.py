#
# PySNMP MIB module Unisphere-Data-CLI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-CLI-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:23:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter64, Gauge32, Bits, Integer32, MibIdentifier, iso, Unsigned32, ObjectIdentity, ModuleIdentity, TimeTicks, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "Bits", "Integer32", "MibIdentifier", "iso", "Unsigned32", "ObjectIdentity", "ModuleIdentity", "TimeTicks", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "IpAddress")
DisplayString, TextualConvention, TruthValue, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue", "DateAndTime")
usDataMibs, = mibBuilder.importSymbols("Unisphere-Data-MIBs", "usDataMibs")
UsdLogSeverity, = mibBuilder.importSymbols("Unisphere-Data-TC", "UsdLogSeverity")
usdCliMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30))
usdCliMIB.setRevisions(('2000-09-26 13:50', '1999-12-01 00:00',))
if mibBuilder.loadTexts: usdCliMIB.setLastUpdated('200009261350Z')
if mibBuilder.loadTexts: usdCliMIB.setOrganization('Unisphere Networks, Inc.')
usdCliTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 0))
usdCliObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1))
usdCliConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2))
usdCliGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 1))
usdCliSecurity = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 2))
usdCliSecurityTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdCliSecurityTrapEnable.setStatus('current')
usdCliSecurityAlertPriority = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 2, 1), UsdLogSeverity()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: usdCliSecurityAlertPriority.setStatus('current')
usdCliSecurityAlertMessage = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 2, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: usdCliSecurityAlertMessage.setStatus('current')
usdCliSecurityAlertTime = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 2, 3), DateAndTime()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: usdCliSecurityAlertTime.setStatus('current')
usdCliSecurityAlert = NotificationType((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 0, 1)).setObjects(("Unisphere-Data-CLI-MIB", "usdCliSecurityAlertPriority"), ("Unisphere-Data-CLI-MIB", "usdCliSecurityAlertMessage"), ("Unisphere-Data-CLI-MIB", "usdCliSecurityAlertTime"))
if mibBuilder.loadTexts: usdCliSecurityAlert.setStatus('current')
usdCliCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2, 1))
usdCliGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2, 2))
usdCliCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2, 1, 1)).setObjects(("Unisphere-Data-CLI-MIB", "usdCliGroup"), ("Unisphere-Data-CLI-MIB", "usdCliSecurityAlertGroup"), ("Unisphere-Data-CLI-MIB", "usdCliSecurityTrapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdCliCompliance = usdCliCompliance.setStatus('current')
usdCliGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2, 2, 1)).setObjects(("Unisphere-Data-CLI-MIB", "usdCliSecurityTrapEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdCliGroup = usdCliGroup.setStatus('current')
usdCliSecurityAlertGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2, 2, 2)).setObjects(("Unisphere-Data-CLI-MIB", "usdCliSecurityAlertPriority"), ("Unisphere-Data-CLI-MIB", "usdCliSecurityAlertMessage"), ("Unisphere-Data-CLI-MIB", "usdCliSecurityAlertTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdCliSecurityAlertGroup = usdCliSecurityAlertGroup.setStatus('current')
usdCliSecurityTrapGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2, 2, 3)).setObjects(("Unisphere-Data-CLI-MIB", "usdCliSecurityAlert"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdCliSecurityTrapGroup = usdCliSecurityTrapGroup.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-CLI-MIB", usdCliTrap=usdCliTrap, usdCliGroups=usdCliGroups, usdCliSecurityTrapEnable=usdCliSecurityTrapEnable, usdCliSecurityAlertMessage=usdCliSecurityAlertMessage, usdCliCompliance=usdCliCompliance, usdCliSecurityAlertGroup=usdCliSecurityAlertGroup, usdCliSecurityAlert=usdCliSecurityAlert, usdCliMIB=usdCliMIB, usdCliGroup=usdCliGroup, usdCliObjects=usdCliObjects, PYSNMP_MODULE_ID=usdCliMIB, usdCliSecurityAlertPriority=usdCliSecurityAlertPriority, usdCliSecurity=usdCliSecurity, usdCliSecurityAlertTime=usdCliSecurityAlertTime, usdCliSecurityTrapGroup=usdCliSecurityTrapGroup, usdCliConformance=usdCliConformance, usdCliGeneral=usdCliGeneral, usdCliCompliances=usdCliCompliances)
