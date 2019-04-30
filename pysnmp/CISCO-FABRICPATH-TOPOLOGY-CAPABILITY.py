#
# PySNMP MIB module CISCO-FABRICPATH-TOPOLOGY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-FABRICPATH-TOPOLOGY-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:40:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
iso, Gauge32, ObjectIdentity, TimeTicks, MibIdentifier, IpAddress, Bits, Counter32, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Integer32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Gauge32", "ObjectIdentity", "TimeTicks", "MibIdentifier", "IpAddress", "Bits", "Counter32", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Integer32", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoFabricPathTopologyCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 620))
ciscoFabricPathTopologyCapability.setRevisions(('2013-07-16 12:00',))
if mibBuilder.loadTexts: ciscoFabricPathTopologyCapability.setLastUpdated('201307161200Z')
if mibBuilder.loadTexts: ciscoFabricPathTopologyCapability.setOrganization('Cisco Systems, Inc.')
ciscoFabricPathTopologyCapNxOSV06R0202PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 620, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFabricPathTopologyCapNxOSV06R0202PN7k = ciscoFabricPathTopologyCapNxOSV06R0202PN7k.setProductRelease('Cisco NX-OS 6.2(2) on Nexus 7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFabricPathTopologyCapNxOSV06R0202PN7k = ciscoFabricPathTopologyCapNxOSV06R0202PN7k.setStatus('current')
mibBuilder.exportSymbols("CISCO-FABRICPATH-TOPOLOGY-CAPABILITY", ciscoFabricPathTopologyCapNxOSV06R0202PN7k=ciscoFabricPathTopologyCapNxOSV06R0202PN7k, ciscoFabricPathTopologyCapability=ciscoFabricPathTopologyCapability, PYSNMP_MODULE_ID=ciscoFabricPathTopologyCapability)
