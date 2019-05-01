#
# PySNMP MIB module Unisphere-Data-CLI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-CLI-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:30:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter64, Integer32, IpAddress, ModuleIdentity, MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Unsigned32, Bits, ObjectIdentity, Gauge32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Unsigned32", "Bits", "ObjectIdentity", "Gauge32", "TimeTicks")
TruthValue, DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DateAndTime", "DisplayString", "TextualConvention")
usDataMibs, = mibBuilder.importSymbols("Unisphere-Data-MIBs", "usDataMibs")
UsdLogSeverity, = mibBuilder.importSymbols("Unisphere-Data-TC", "UsdLogSeverity")
usdCliMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30))
usdCliMIB.setRevisions(('2000-09-26 13:50', '1999-12-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdCliMIB.setRevisionsDescriptions(('Make it SMIv2 conformant.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: usdCliMIB.setLastUpdated('200009261350Z')
if mibBuilder.loadTexts: usdCliMIB.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdCliMIB.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford MA 01886 USA Tel: +1 978 589 5800 Email: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdCliMIB.setDescription('The Command Line Interface (CLI) security MIB for the Unisphere Networks Inc. enterprise.')
usdCliTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 0))
usdCliObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1))
usdCliConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2))
usdCliGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 1))
usdCliSecurity = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 2))
usdCliSecurityTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdCliSecurityTrapEnable.setStatus('current')
if mibBuilder.loadTexts: usdCliSecurityTrapEnable.setDescription('An indication of whether the usdCliSecurityAlert notifications are enabled.')
usdCliSecurityAlertPriority = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 2, 1), UsdLogSeverity()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: usdCliSecurityAlertPriority.setStatus('current')
if mibBuilder.loadTexts: usdCliSecurityAlertPriority.setDescription('The priority level of the cli security alert')
usdCliSecurityAlertMessage = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 2, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: usdCliSecurityAlertMessage.setStatus('current')
if mibBuilder.loadTexts: usdCliSecurityAlertMessage.setDescription('The cli security alert message.')
usdCliSecurityAlertTime = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 1, 2, 3), DateAndTime()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: usdCliSecurityAlertTime.setStatus('current')
if mibBuilder.loadTexts: usdCliSecurityAlertTime.setDescription('The date and time of this cliSecurityAlert.')
usdCliSecurityAlert = NotificationType((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 0, 1)).setObjects(("Unisphere-Data-CLI-MIB", "usdCliSecurityAlertPriority"), ("Unisphere-Data-CLI-MIB", "usdCliSecurityAlertMessage"), ("Unisphere-Data-CLI-MIB", "usdCliSecurityAlertTime"))
if mibBuilder.loadTexts: usdCliSecurityAlert.setStatus('current')
if mibBuilder.loadTexts: usdCliSecurityAlert.setDescription('Reports a cli security alert. Events such as the following generate this notification when it is enabled: - Logins/logouts from telnet or console access - Logins/logout from SSH - Access from unknown IP addreses - Access list accept or failures - Successful and unsuccessful authentications')
usdCliCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2, 1))
usdCliGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2, 2))
usdCliCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2, 1, 1)).setObjects(("Unisphere-Data-CLI-MIB", "usdCliGroup"), ("Unisphere-Data-CLI-MIB", "usdCliSecurityAlertGroup"), ("Unisphere-Data-CLI-MIB", "usdCliSecurityTrapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdCliCompliance = usdCliCompliance.setStatus('current')
if mibBuilder.loadTexts: usdCliCompliance.setDescription('The compliance statement for entities that implement the Unisphere CLI MIB.')
usdCliGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2, 2, 1)).setObjects(("Unisphere-Data-CLI-MIB", "usdCliSecurityTrapEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdCliGroup = usdCliGroup.setStatus('current')
if mibBuilder.loadTexts: usdCliGroup.setDescription('A management object pertaining to CLI security configuration.')
usdCliSecurityAlertGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2, 2, 2)).setObjects(("Unisphere-Data-CLI-MIB", "usdCliSecurityAlertPriority"), ("Unisphere-Data-CLI-MIB", "usdCliSecurityAlertMessage"), ("Unisphere-Data-CLI-MIB", "usdCliSecurityAlertTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdCliSecurityAlertGroup = usdCliSecurityAlertGroup.setStatus('current')
if mibBuilder.loadTexts: usdCliSecurityAlertGroup.setDescription('A collection of management objects pertaining to CLI security alert notification.')
usdCliSecurityTrapGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 30, 2, 2, 3)).setObjects(("Unisphere-Data-CLI-MIB", "usdCliSecurityAlert"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdCliSecurityTrapGroup = usdCliSecurityTrapGroup.setStatus('current')
if mibBuilder.loadTexts: usdCliSecurityTrapGroup.setDescription('A management notification pertaining to CLI security operations.')
mibBuilder.exportSymbols("Unisphere-Data-CLI-MIB", usdCliSecurityTrapEnable=usdCliSecurityTrapEnable, usdCliMIB=usdCliMIB, usdCliObjects=usdCliObjects, usdCliSecurity=usdCliSecurity, usdCliSecurityAlertPriority=usdCliSecurityAlertPriority, usdCliCompliances=usdCliCompliances, usdCliConformance=usdCliConformance, usdCliSecurityAlertMessage=usdCliSecurityAlertMessage, usdCliSecurityAlert=usdCliSecurityAlert, usdCliTrap=usdCliTrap, usdCliGroup=usdCliGroup, usdCliCompliance=usdCliCompliance, usdCliSecurityAlertGroup=usdCliSecurityAlertGroup, usdCliSecurityTrapGroup=usdCliSecurityTrapGroup, usdCliSecurityAlertTime=usdCliSecurityAlertTime, usdCliGroups=usdCliGroups, PYSNMP_MODULE_ID=usdCliMIB, usdCliGeneral=usdCliGeneral)
