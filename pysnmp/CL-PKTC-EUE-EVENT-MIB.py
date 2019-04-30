#
# PySNMP MIB module CL-PKTC-EUE-EVENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CL-PKTC-EUE-EVENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:08:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
pktcEUEMibs, = mibBuilder.importSymbols("CLAB-DEF-MIB", "pktcEUEMibs")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter64, ModuleIdentity, Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, Gauge32, NotificationType, Integer32, Unsigned32, ObjectIdentity, Bits, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "Gauge32", "NotificationType", "Integer32", "Unsigned32", "ObjectIdentity", "Bits", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pktcEUEEventMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 5))
if mibBuilder.loadTexts: pktcEUEEventMIB.setLastUpdated('200708130000Z')
if mibBuilder.loadTexts: pktcEUEEventMIB.setOrganization('Cable Television Laboratories, Inc.')
pktcEUEEventNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 5, 0))
pktcEUEEventObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 5, 1))
pktcEUEEventConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 5, 2))
pktcEUEMEMVersion = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 5, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pktcEUEMEMVersion.setStatus('current')
pktcEUEEventCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 5, 2, 1))
pktcEUEEventGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 5, 2, 2))
pktcEUEEventCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 5, 2, 1, 1)).setObjects(("PKTC-EVENT-MIB", "pktcEventGroup"), ("PKTC-EVENT-MIB", "pktcEventNotificationGroup"), ("CL-PKTC-EUE-EVENT-MIB", "pktcEUEMEMGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pktcEUEEventCompliance = pktcEUEEventCompliance.setStatus('current')
pktcEUEMEMGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 5, 2, 2, 1)).setObjects(("CL-PKTC-EUE-EVENT-MIB", "pktcEUEMEMVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pktcEUEMEMGroup = pktcEUEMEMGroup.setStatus('current')
mibBuilder.exportSymbols("CL-PKTC-EUE-EVENT-MIB", pktcEUEEventConformance=pktcEUEEventConformance, pktcEUEEventGroups=pktcEUEEventGroups, pktcEUEEventNotifications=pktcEUEEventNotifications, pktcEUEEventCompliances=pktcEUEEventCompliances, pktcEUEMEMGroup=pktcEUEMEMGroup, PYSNMP_MODULE_ID=pktcEUEEventMIB, pktcEUEEventObjects=pktcEUEEventObjects, pktcEUEEventCompliance=pktcEUEEventCompliance, pktcEUEMEMVersion=pktcEUEMEMVersion, pktcEUEEventMIB=pktcEUEEventMIB)
