#
# PySNMP MIB module CISCO-IETF-PPVPN-MPLS-VPN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IETF-PPVPN-MPLS-VPN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:00:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
mplsVpnVrfPerfCurrNumRoutes, mplsVpnVrfConfHighRouteThreshold = mibBuilder.importSymbols("MPLS-VPN-MIB", "mplsVpnVrfPerfCurrNumRoutes", "mplsVpnVrfConfHighRouteThreshold")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Counter64, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ObjectIdentity, NotificationType, Integer32, IpAddress, Bits, ModuleIdentity, MibIdentifier, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter64", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ObjectIdentity", "NotificationType", "Integer32", "IpAddress", "Bits", "ModuleIdentity", "MibIdentifier", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoMplsVpnMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 999))
ciscoMplsVpnMIB.setRevisions(('2003-04-17 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoMplsVpnMIB.setRevisionsDescriptions(('Shorten names of identifiers and change name of the mib to from CISCO-MPLS-VPN-MIB to CISCO-IETF-PPVPN-MPLS-VPN-MIB.',))
if mibBuilder.loadTexts: ciscoMplsVpnMIB.setLastUpdated('200304171200Z')
if mibBuilder.loadTexts: ciscoMplsVpnMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoMplsVpnMIB.setContactInfo(' Cisco Systems, Inc. Postal: Customer Service 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS Email: cs-snmp@cisco.com ch-mpls-mib-team@cisco.com ')
if mibBuilder.loadTexts: ciscoMplsVpnMIB.setDescription('This MIB is an extension of the MPLS-VPN-MIB. It contains a new notification, mplsNumVrfRouteMaxThreshCleared, which was added with MPLS-VPN-MIB-DRAFT-05.')
cMplsVpnNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 999, 0))
cMplsVpnObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 999, 1))
cMplsVpnConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 999, 2))
cMplsNumVrfRouteMaxThreshCleared = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 999, 0, 1)).setObjects(("MPLS-VPN-MIB", "mplsVpnVrfPerfCurrNumRoutes"), ("MPLS-VPN-MIB", "mplsVpnVrfConfHighRouteThreshold"))
if mibBuilder.loadTexts: cMplsNumVrfRouteMaxThreshCleared.setStatus('current')
if mibBuilder.loadTexts: cMplsNumVrfRouteMaxThreshCleared.setDescription('This notification is generated only after the number of routes contained by the specified VRF reaches or attempts to exceed the maximum allowed value as indicated by mplsVrfMaxRouteThreshold, and then falls below this value. The emission of this notification informs the operator that the error condition has been cleared without the operator having to query the device.')
cMplsVpnCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 1))
cMplsVpnGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 2))
cMplsVpnCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 1, 1)).setObjects(("CISCO-IETF-PPVPN-MPLS-VPN-MIB", "cMplsVpnNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cMplsVpnCompliance = cMplsVpnCompliance.setStatus('current')
if mibBuilder.loadTexts: cMplsVpnCompliance.setDescription('Compliance statement for agents that support the CISCO MPLS VPN MIB.')
cMplsVpnNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 2, 1)).setObjects(("CISCO-IETF-PPVPN-MPLS-VPN-MIB", "cMplsNumVrfRouteMaxThreshCleared"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cMplsVpnNotificationGroup = cMplsVpnNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: cMplsVpnNotificationGroup.setDescription('Objects required for CISCO MPLS VPN notifications.')
mibBuilder.exportSymbols("CISCO-IETF-PPVPN-MPLS-VPN-MIB", cMplsVpnGroups=cMplsVpnGroups, cMplsVpnNotificationGroup=cMplsVpnNotificationGroup, cMplsVpnNotifs=cMplsVpnNotifs, cMplsVpnConform=cMplsVpnConform, cMplsNumVrfRouteMaxThreshCleared=cMplsNumVrfRouteMaxThreshCleared, PYSNMP_MODULE_ID=ciscoMplsVpnMIB, cMplsVpnObjects=cMplsVpnObjects, cMplsVpnCompliances=cMplsVpnCompliances, ciscoMplsVpnMIB=ciscoMplsVpnMIB, cMplsVpnCompliance=cMplsVpnCompliance)
