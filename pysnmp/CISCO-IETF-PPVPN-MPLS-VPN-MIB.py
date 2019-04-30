#
# PySNMP MIB module CISCO-IETF-PPVPN-MPLS-VPN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IETF-PPVPN-MPLS-VPN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:43:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
mplsVpnVrfConfHighRouteThreshold, mplsVpnVrfPerfCurrNumRoutes = mibBuilder.importSymbols("MPLS-VPN-MIB", "mplsVpnVrfConfHighRouteThreshold", "mplsVpnVrfPerfCurrNumRoutes")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Unsigned32, Counter64, Gauge32, Counter32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, IpAddress, NotificationType, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Unsigned32", "Counter64", "Gauge32", "Counter32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "IpAddress", "NotificationType", "Bits", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMplsVpnMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 999))
ciscoMplsVpnMIB.setRevisions(('2003-04-17 12:00',))
if mibBuilder.loadTexts: ciscoMplsVpnMIB.setLastUpdated('200304171200Z')
if mibBuilder.loadTexts: ciscoMplsVpnMIB.setOrganization('Cisco Systems, Inc.')
cMplsVpnNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 999, 0))
cMplsVpnObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 999, 1))
cMplsVpnConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 999, 2))
cMplsNumVrfRouteMaxThreshCleared = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 999, 0, 1)).setObjects(("MPLS-VPN-MIB", "mplsVpnVrfPerfCurrNumRoutes"), ("MPLS-VPN-MIB", "mplsVpnVrfConfHighRouteThreshold"))
if mibBuilder.loadTexts: cMplsNumVrfRouteMaxThreshCleared.setStatus('current')
cMplsVpnCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 1))
cMplsVpnGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 2))
cMplsVpnCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 1, 1)).setObjects(("CISCO-IETF-PPVPN-MPLS-VPN-MIB", "cMplsVpnNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cMplsVpnCompliance = cMplsVpnCompliance.setStatus('current')
cMplsVpnNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 2, 1)).setObjects(("CISCO-IETF-PPVPN-MPLS-VPN-MIB", "cMplsNumVrfRouteMaxThreshCleared"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cMplsVpnNotificationGroup = cMplsVpnNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-IETF-PPVPN-MPLS-VPN-MIB", PYSNMP_MODULE_ID=ciscoMplsVpnMIB, cMplsVpnCompliances=cMplsVpnCompliances, cMplsVpnCompliance=cMplsVpnCompliance, cMplsNumVrfRouteMaxThreshCleared=cMplsNumVrfRouteMaxThreshCleared, cMplsVpnObjects=cMplsVpnObjects, cMplsVpnNotifs=cMplsVpnNotifs, cMplsVpnNotificationGroup=cMplsVpnNotificationGroup, cMplsVpnConform=cMplsVpnConform, cMplsVpnGroups=cMplsVpnGroups, ciscoMplsVpnMIB=ciscoMplsVpnMIB)
