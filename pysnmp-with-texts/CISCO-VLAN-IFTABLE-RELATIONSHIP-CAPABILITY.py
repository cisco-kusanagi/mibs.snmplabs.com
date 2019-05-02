#
# PySNMP MIB module CISCO-VLAN-IFTABLE-RELATIONSHIP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VLAN-IFTABLE-RELATIONSHIP-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:18:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, Counter32, Integer32, Bits, MibIdentifier, ModuleIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, ObjectIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "Counter32", "Integer32", "Bits", "MibIdentifier", "ModuleIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "ObjectIdentity", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVlanIfTableRelCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 369))
ciscoVlanIfTableRelCapability.setRevisions(('2013-08-08 00:00', '2006-01-18 00:00', '2004-02-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVlanIfTableRelCapability.setRevisionsDescriptions(('Added ciscoVlanIfTableRelCapNxOSV6R0202PN7K.', 'Added ciscoVlanIfTableRelCapIOSXRV3R2CRS1 Agent Capabilities for IOS XR 3.2.0', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoVlanIfTableRelCapability.setLastUpdated('201308080000Z')
if mibBuilder.loadTexts: ciscoVlanIfTableRelCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVlanIfTableRelCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoVlanIfTableRelCapability.setDescription('The agent capabilities description of CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB.')
ciscoVlanIfTableRelCapV12R0119E = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 369, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanIfTableRelCapV12R0119E = ciscoVlanIfTableRelCapV12R0119E.setProductRelease('Cisco IOS 12.1(19E) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanIfTableRelCapV12R0119E = ciscoVlanIfTableRelCapV12R0119E.setStatus('current')
if mibBuilder.loadTexts: ciscoVlanIfTableRelCapV12R0119E.setDescription('CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB agent capabilities.')
ciscoVlanIfTableRelCapIOSXRV3R2CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 369, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanIfTableRelCapIOSXRV3R2CRS1 = ciscoVlanIfTableRelCapIOSXRV3R2CRS1.setProductRelease('Cisco IOS XR 3.2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanIfTableRelCapIOSXRV3R2CRS1 = ciscoVlanIfTableRelCapIOSXRV3R2CRS1.setStatus('current')
if mibBuilder.loadTexts: ciscoVlanIfTableRelCapIOSXRV3R2CRS1.setDescription('CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB capabilities for IOS XR release 3.2.0')
ciscoVlanIfTableRelCapNxOSV6R0202PN7K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 369, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanIfTableRelCapNxOSV6R0202PN7K = ciscoVlanIfTableRelCapNxOSV6R0202PN7K.setProductRelease('Cisco NX-OS 6.2(2) on Nexus 7000\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanIfTableRelCapNxOSV6R0202PN7K = ciscoVlanIfTableRelCapNxOSV6R0202PN7K.setStatus('current')
if mibBuilder.loadTexts: ciscoVlanIfTableRelCapNxOSV6R0202PN7K.setDescription('CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB agent capabilities.')
mibBuilder.exportSymbols("CISCO-VLAN-IFTABLE-RELATIONSHIP-CAPABILITY", ciscoVlanIfTableRelCapV12R0119E=ciscoVlanIfTableRelCapV12R0119E, ciscoVlanIfTableRelCapIOSXRV3R2CRS1=ciscoVlanIfTableRelCapIOSXRV3R2CRS1, ciscoVlanIfTableRelCapNxOSV6R0202PN7K=ciscoVlanIfTableRelCapNxOSV6R0202PN7K, ciscoVlanIfTableRelCapability=ciscoVlanIfTableRelCapability, PYSNMP_MODULE_ID=ciscoVlanIfTableRelCapability)
