#
# PySNMP MIB module PDN-IP-MULTICAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-IP-MULTICAST-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:39:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
pdn_common, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdn-common")
SwitchState, = mibBuilder.importSymbols("PDN-TC", "SwitchState")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Gauge32, Unsigned32, Counter64, Counter32, MibIdentifier, IpAddress, ObjectIdentity, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Gauge32", "Unsigned32", "Counter64", "Counter32", "MibIdentifier", "IpAddress", "ObjectIdentity", "Integer32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
pdnIpMcastMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48))
pdnIpMcastMIB.setRevisions(('2003-05-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: pdnIpMcastMIB.setRevisionsDescriptions(('Initial release.',))
if mibBuilder.loadTexts: pdnIpMcastMIB.setLastUpdated('200305010000Z')
if mibBuilder.loadTexts: pdnIpMcastMIB.setOrganization('Paradyne Networks MIB Working Group Other information about group editing the MIB.')
if mibBuilder.loadTexts: pdnIpMcastMIB.setContactInfo('Paradyne Networks, Inc. 8545 126th Avenue North Largo, FL 33733 www.paradyne.com General Comments to: mibwg_team@paradyne.com Editor(s) Clay Sikes')
if mibBuilder.loadTexts: pdnIpMcastMIB.setDescription('This MIB contains the objects pertaining to the configuration and maintenance of the Internet Group Management Protocol (IGMP) and IP Multicast related operation in Paradyne devices.')
pdnIpMcastNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 0))
pdnIpMcastObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 1))
pdnIpMcastAFNs = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 2))
pdnIpMcastConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 3))
pdnIgmpProxy = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 1, 1))
pdnIpMcastStats = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 1, 2))
pdnIgmpProxyEnableDisable = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 1, 1, 1), SwitchState().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnIgmpProxyEnableDisable.setStatus('current')
if mibBuilder.loadTexts: pdnIgmpProxyEnableDisable.setDescription('This object enables or disables IGMP Proxy.')
pdnIgmpProxyReportSummaryEnableDisable = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 1, 1, 2), SwitchState().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnIgmpProxyReportSummaryEnableDisable.setStatus('current')
if mibBuilder.loadTexts: pdnIgmpProxyReportSummaryEnableDisable.setDescription('This object enables or disables the summarization of all report messages into a single report message.')
pdnIpMcastCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 3, 1))
pdnIpMcastGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 3, 2))
pdnIpMcastMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 3, 1, 1)).setObjects(("PDN-IP-MULTICAST-MIB", "pdnIgmpProxyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnIpMcastMIBCompliance = pdnIpMcastMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: pdnIpMcastMIBCompliance.setDescription('The compliance statement for IP Multicast products which implement the pdnIpMcaseMIB.')
pdnIpMcaseObjGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 3, 2, 1))
pdnIpMcastAfnGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 3, 2, 2))
pdnIpMcaseNtfyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 3, 2, 3))
pdnIgmpProxyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 3, 2, 1, 1)).setObjects(("PDN-IP-MULTICAST-MIB", "pdnIgmpProxyEnableDisable"), ("PDN-IP-MULTICAST-MIB", "pdnIgmpProxyReportSummaryEnableDisable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnIgmpProxyGroup = pdnIgmpProxyGroup.setStatus('current')
if mibBuilder.loadTexts: pdnIgmpProxyGroup.setDescription('Objects grouped for IGMP Proxy.')
mibBuilder.exportSymbols("PDN-IP-MULTICAST-MIB", pdnIgmpProxy=pdnIgmpProxy, PYSNMP_MODULE_ID=pdnIpMcastMIB, pdnIpMcastCompliances=pdnIpMcastCompliances, pdnIpMcastGroups=pdnIpMcastGroups, pdnIpMcastMIBCompliance=pdnIpMcastMIBCompliance, pdnIpMcastObjects=pdnIpMcastObjects, pdnIgmpProxyReportSummaryEnableDisable=pdnIgmpProxyReportSummaryEnableDisable, pdnIpMcaseObjGroups=pdnIpMcaseObjGroups, pdnIpMcastMIB=pdnIpMcastMIB, pdnIpMcastAfnGroups=pdnIpMcastAfnGroups, pdnIpMcaseNtfyGroups=pdnIpMcaseNtfyGroups, pdnIpMcastAFNs=pdnIpMcastAFNs, pdnIpMcastConformance=pdnIpMcastConformance, pdnIpMcastNotifications=pdnIpMcastNotifications, pdnIpMcastStats=pdnIpMcastStats, pdnIgmpProxyGroup=pdnIgmpProxyGroup, pdnIgmpProxyEnableDisable=pdnIgmpProxyEnableDisable)
