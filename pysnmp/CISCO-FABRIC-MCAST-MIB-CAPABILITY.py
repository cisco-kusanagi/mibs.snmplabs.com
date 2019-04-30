#
# PySNMP MIB module CISCO-FABRIC-MCAST-MIB-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-FABRIC-MCAST-MIB-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:40:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
TimeTicks, Integer32, iso, Unsigned32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter64, ModuleIdentity, Gauge32, Bits, IpAddress, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "iso", "Unsigned32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter64", "ModuleIdentity", "Gauge32", "Bits", "IpAddress", "ObjectIdentity", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoFabricMcastCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 509))
ciscoFabricMcastCapability.setRevisions(('2006-06-12 00:00',))
if mibBuilder.loadTexts: ciscoFabricMcastCapability.setLastUpdated('200606120000Z')
if mibBuilder.loadTexts: ciscoFabricMcastCapability.setOrganization('Cisco Systems, Inc.')
cfmCapabilityIOSXRV3R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 509, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmCapabilityIOSXRV3R03 = cfmCapabilityIOSXRV3R03.setProductRelease('Cisco IOS XR 3.3 on CRS-1 ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmCapabilityIOSXRV3R03 = cfmCapabilityIOSXRV3R03.setStatus('current')
mibBuilder.exportSymbols("CISCO-FABRIC-MCAST-MIB-CAPABILITY", cfmCapabilityIOSXRV3R03=cfmCapabilityIOSXRV3R03, PYSNMP_MODULE_ID=ciscoFabricMcastCapability, ciscoFabricMcastCapability=ciscoFabricMcastCapability)
