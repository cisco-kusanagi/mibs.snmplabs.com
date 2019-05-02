#
# PySNMP MIB module CISCO-FABRIC-MCAST-MIB-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-FABRIC-MCAST-MIB-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:57:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
ModuleIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, ObjectIdentity, Gauge32, NotificationType, Integer32, IpAddress, MibIdentifier, Counter64, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "ObjectIdentity", "Gauge32", "NotificationType", "Integer32", "IpAddress", "MibIdentifier", "Counter64", "iso", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoFabricMcastCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 509))
ciscoFabricMcastCapability.setRevisions(('2006-06-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoFabricMcastCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoFabricMcastCapability.setLastUpdated('200606120000Z')
if mibBuilder.loadTexts: ciscoFabricMcastCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoFabricMcastCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-fabric@cisco.com')
if mibBuilder.loadTexts: ciscoFabricMcastCapability.setDescription('The capabilities description of CISCO-FABRIC-MCAST-MIB.')
cfmCapabilityIOSXRV3R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 509, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmCapabilityIOSXRV3R03 = cfmCapabilityIOSXRV3R03.setProductRelease('Cisco IOS XR 3.3 on CRS-1 ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmCapabilityIOSXRV3R03 = cfmCapabilityIOSXRV3R03.setStatus('current')
if mibBuilder.loadTexts: cfmCapabilityIOSXRV3R03.setDescription('CISCO-FABRIC-MCAST-MIB capabilities for IOS XR release 3.3')
mibBuilder.exportSymbols("CISCO-FABRIC-MCAST-MIB-CAPABILITY", cfmCapabilityIOSXRV3R03=cfmCapabilityIOSXRV3R03, PYSNMP_MODULE_ID=ciscoFabricMcastCapability, ciscoFabricMcastCapability=ciscoFabricMcastCapability)
