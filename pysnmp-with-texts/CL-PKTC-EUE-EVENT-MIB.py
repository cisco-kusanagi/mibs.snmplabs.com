#
# PySNMP MIB module CL-PKTC-EUE-EVENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CL-PKTC-EUE-EVENT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:24:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
pktcEUEMibs, = mibBuilder.importSymbols("CLAB-DEF-MIB", "pktcEUEMibs")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress, ObjectIdentity, Integer32, ModuleIdentity, Gauge32, iso, NotificationType, TimeTicks, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress", "ObjectIdentity", "Integer32", "ModuleIdentity", "Gauge32", "iso", "NotificationType", "TimeTicks", "MibIdentifier", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
pktcEUEEventMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 5))
if mibBuilder.loadTexts: pktcEUEEventMIB.setLastUpdated('200708130000Z')
if mibBuilder.loadTexts: pktcEUEEventMIB.setOrganization('Cable Television Laboratories, Inc.')
if mibBuilder.loadTexts: pktcEUEEventMIB.setContactInfo('Sumanth Channabasappa Postal: Cable Television Laboratories, Inc 858 Coal Creek Circle Louisville, CO 80027 U.S.A. Phone: +1 303 661 9100 Fax: +1 303 661 9199 E-mail:mibs@cablelabs.com Acknowledgements: Thomas Clack, Broadcom - Primary author , and members of the PacketCable PACM Focus Team.')
if mibBuilder.loadTexts: pktcEUEEventMIB.setDescription('This MIB module provides the management objects for the Management Event mechanism as specified by the PacketCable E-UE Provisioning Framework.')
pktcEUEEventNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 5, 0))
pktcEUEEventObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 5, 1))
pktcEUEEventConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 5, 2))
pktcEUEMEMVersion = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 5, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pktcEUEMEMVersion.setStatus('current')
if mibBuilder.loadTexts: pktcEUEMEMVersion.setDescription(" This MIB Object represents the Management Event Reporting Module version. The eUE MUST set this MIB Object to value of '1.0'.")
pktcEUEEventCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 5, 2, 1))
pktcEUEEventGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 5, 2, 2))
pktcEUEEventCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 5, 2, 1, 1)).setObjects(("PKTC-EVENT-MIB", "pktcEventGroup"), ("PKTC-EVENT-MIB", "pktcEventNotificationGroup"), ("CL-PKTC-EUE-EVENT-MIB", "pktcEUEMEMGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pktcEUEEventCompliance = pktcEUEEventCompliance.setStatus('current')
if mibBuilder.loadTexts: pktcEUEEventCompliance.setDescription('The compliance statement for CableLabs compliant eUE devices that implement the PacketCable E-UE Provisioning Framework. This compliance statement specifies, for PacketCable E-UE Provisioning, the required objects from the PKTC-EVENT-MIB defined in the PacketCable 1.5 Specifications Management Event MIB Specification, PKT-SP-EVEMIB1.5-I02-050812. Some objects from RFC4682 have been enhanced for applicability to eUEs. Similarly, inapplicable objects are clearly indicated.')
if mibBuilder.loadTexts: pktcEUEEventCompliance.setReference('PacketCable Embedded UE Provisioning Framework Specification')
pktcEUEMEMGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 5, 2, 2, 1)).setObjects(("CL-PKTC-EUE-EVENT-MIB", "pktcEUEMEMVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pktcEUEMEMGroup = pktcEUEMEMGroup.setStatus('current')
if mibBuilder.loadTexts: pktcEUEMEMGroup.setDescription('The eUE Operator Group.')
mibBuilder.exportSymbols("CL-PKTC-EUE-EVENT-MIB", PYSNMP_MODULE_ID=pktcEUEEventMIB, pktcEUEEventCompliances=pktcEUEEventCompliances, pktcEUEEventMIB=pktcEUEEventMIB, pktcEUEEventConformance=pktcEUEEventConformance, pktcEUEEventCompliance=pktcEUEEventCompliance, pktcEUEMEMGroup=pktcEUEMEMGroup, pktcEUEEventObjects=pktcEUEEventObjects, pktcEUEMEMVersion=pktcEUEMEMVersion, pktcEUEEventGroups=pktcEUEEventGroups, pktcEUEEventNotifications=pktcEUEEventNotifications)
