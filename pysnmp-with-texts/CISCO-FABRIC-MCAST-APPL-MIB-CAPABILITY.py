#
# PySNMP MIB module CISCO-FABRIC-MCAST-APPL-MIB-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-FABRIC-MCAST-APPL-MIB-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:57:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Bits, Counter64, iso, ModuleIdentity, Gauge32, Counter32, IpAddress, Integer32, ObjectIdentity, Unsigned32, TimeTicks, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "iso", "ModuleIdentity", "Gauge32", "Counter32", "IpAddress", "Integer32", "ObjectIdentity", "Unsigned32", "TimeTicks", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoFabricMcastApplCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 510))
ciscoFabricMcastApplCapability.setRevisions(('2006-06-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoFabricMcastApplCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoFabricMcastApplCapability.setLastUpdated('200606120000Z')
if mibBuilder.loadTexts: ciscoFabricMcastApplCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoFabricMcastApplCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-fabric@cisco.com')
if mibBuilder.loadTexts: ciscoFabricMcastApplCapability.setDescription('The capabilities description of CISCO-FABRIC-MCAST-APPL-MIB.')
cfmaCapabilityIOSXRV3R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 510, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmaCapabilityIOSXRV3R03 = cfmaCapabilityIOSXRV3R03.setProductRelease('Cisco IOS XR 3.3 on CRS-1 ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmaCapabilityIOSXRV3R03 = cfmaCapabilityIOSXRV3R03.setStatus('current')
if mibBuilder.loadTexts: cfmaCapabilityIOSXRV3R03.setDescription('CISCO-FABRIC-MCAST-APPL-MIB capabilities for IOS XR release 3.3')
mibBuilder.exportSymbols("CISCO-FABRIC-MCAST-APPL-MIB-CAPABILITY", cfmaCapabilityIOSXRV3R03=cfmaCapabilityIOSXRV3R03, ciscoFabricMcastApplCapability=ciscoFabricMcastApplCapability, PYSNMP_MODULE_ID=ciscoFabricMcastApplCapability)
