#
# PySNMP MIB module CISCO-VLAN-IFTABLE-RELATIONSHIP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VLAN-IFTABLE-RELATIONSHIP-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 18:02:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Unsigned32, NotificationType, Gauge32, Counter64, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, iso, Counter32, TimeTicks, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "Gauge32", "Counter64", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "iso", "Counter32", "TimeTicks", "Integer32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoVlanIfTableRelCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 369))
ciscoVlanIfTableRelCapability.setRevisions(('2013-08-08 00:00', '2006-01-18 00:00', '2004-02-03 00:00',))
if mibBuilder.loadTexts: ciscoVlanIfTableRelCapability.setLastUpdated('201308080000Z')
if mibBuilder.loadTexts: ciscoVlanIfTableRelCapability.setOrganization('Cisco Systems, Inc.')
ciscoVlanIfTableRelCapV12R0119E = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 369, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanIfTableRelCapV12R0119E = ciscoVlanIfTableRelCapV12R0119E.setProductRelease('Cisco IOS 12.1(19E) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanIfTableRelCapV12R0119E = ciscoVlanIfTableRelCapV12R0119E.setStatus('current')
ciscoVlanIfTableRelCapIOSXRV3R2CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 369, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanIfTableRelCapIOSXRV3R2CRS1 = ciscoVlanIfTableRelCapIOSXRV3R2CRS1.setProductRelease('Cisco IOS XR 3.2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanIfTableRelCapIOSXRV3R2CRS1 = ciscoVlanIfTableRelCapIOSXRV3R2CRS1.setStatus('current')
ciscoVlanIfTableRelCapNxOSV6R0202PN7K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 369, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanIfTableRelCapNxOSV6R0202PN7K = ciscoVlanIfTableRelCapNxOSV6R0202PN7K.setProductRelease('Cisco NX-OS 6.2(2) on Nexus 7000\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanIfTableRelCapNxOSV6R0202PN7K = ciscoVlanIfTableRelCapNxOSV6R0202PN7K.setStatus('current')
mibBuilder.exportSymbols("CISCO-VLAN-IFTABLE-RELATIONSHIP-CAPABILITY", ciscoVlanIfTableRelCapIOSXRV3R2CRS1=ciscoVlanIfTableRelCapIOSXRV3R2CRS1, ciscoVlanIfTableRelCapability=ciscoVlanIfTableRelCapability, ciscoVlanIfTableRelCapNxOSV6R0202PN7K=ciscoVlanIfTableRelCapNxOSV6R0202PN7K, PYSNMP_MODULE_ID=ciscoVlanIfTableRelCapability, ciscoVlanIfTableRelCapV12R0119E=ciscoVlanIfTableRelCapV12R0119E)
