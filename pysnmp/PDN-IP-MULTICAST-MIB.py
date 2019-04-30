#
# PySNMP MIB module PDN-IP-MULTICAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-IP-MULTICAST-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:30:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
pdn_common, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdn-common")
SwitchState, = mibBuilder.importSymbols("PDN-TC", "SwitchState")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ObjectIdentity, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, TimeTicks, Unsigned32, Bits, ModuleIdentity, Integer32, Counter64, iso, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "TimeTicks", "Unsigned32", "Bits", "ModuleIdentity", "Integer32", "Counter64", "iso", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
pdnIpMcastMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48))
pdnIpMcastMIB.setRevisions(('2003-05-01 00:00',))
if mibBuilder.loadTexts: pdnIpMcastMIB.setLastUpdated('200305010000Z')
if mibBuilder.loadTexts: pdnIpMcastMIB.setOrganization('Paradyne Networks MIB Working Group Other information about group editing the MIB.')
pdnIpMcastNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 0))
pdnIpMcastObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 1))
pdnIpMcastAFNs = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 2))
pdnIpMcastConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 3))
pdnIgmpProxy = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 1, 1))
pdnIpMcastStats = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 1, 2))
pdnIgmpProxyEnableDisable = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 1, 1, 1), SwitchState().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnIgmpProxyEnableDisable.setStatus('current')
pdnIgmpProxyReportSummaryEnableDisable = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 1, 1, 2), SwitchState().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnIgmpProxyReportSummaryEnableDisable.setStatus('current')
pdnIpMcastCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 3, 1))
pdnIpMcastGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 3, 2))
pdnIpMcastMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 3, 1, 1)).setObjects(("PDN-IP-MULTICAST-MIB", "pdnIgmpProxyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnIpMcastMIBCompliance = pdnIpMcastMIBCompliance.setStatus('current')
pdnIpMcaseObjGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 3, 2, 1))
pdnIpMcastAfnGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 3, 2, 2))
pdnIpMcaseNtfyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 3, 2, 3))
pdnIgmpProxyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 48, 3, 2, 1, 1)).setObjects(("PDN-IP-MULTICAST-MIB", "pdnIgmpProxyEnableDisable"), ("PDN-IP-MULTICAST-MIB", "pdnIgmpProxyReportSummaryEnableDisable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnIgmpProxyGroup = pdnIgmpProxyGroup.setStatus('current')
mibBuilder.exportSymbols("PDN-IP-MULTICAST-MIB", pdnIpMcastAFNs=pdnIpMcastAFNs, pdnIpMcastCompliances=pdnIpMcastCompliances, pdnIpMcastMIBCompliance=pdnIpMcastMIBCompliance, pdnIpMcastConformance=pdnIpMcastConformance, pdnIpMcastStats=pdnIpMcastStats, pdnIpMcastGroups=pdnIpMcastGroups, PYSNMP_MODULE_ID=pdnIpMcastMIB, pdnIgmpProxyGroup=pdnIgmpProxyGroup, pdnIpMcastObjects=pdnIpMcastObjects, pdnIpMcastMIB=pdnIpMcastMIB, pdnIpMcastNotifications=pdnIpMcastNotifications, pdnIgmpProxyEnableDisable=pdnIgmpProxyEnableDisable, pdnIpMcaseObjGroups=pdnIpMcaseObjGroups, pdnIpMcastAfnGroups=pdnIpMcastAfnGroups, pdnIgmpProxyReportSummaryEnableDisable=pdnIgmpProxyReportSummaryEnableDisable, pdnIgmpProxy=pdnIgmpProxy, pdnIpMcaseNtfyGroups=pdnIpMcaseNtfyGroups)
