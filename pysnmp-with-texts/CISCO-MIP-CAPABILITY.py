#
# PySNMP MIB module CISCO-MIP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MIP-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:07:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, Bits, Integer32, ModuleIdentity, Counter32, TimeTicks, Unsigned32, MibIdentifier, IpAddress, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "Bits", "Integer32", "ModuleIdentity", "Counter32", "TimeTicks", "Unsigned32", "MibIdentifier", "IpAddress", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMIPCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 203))
ciscoMIPCapability.setRevisions(('2003-12-24 00:00', '2002-10-08 00:00', '2000-11-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoMIPCapability.setRevisionsDescriptions(('Added ciscoMIPCapabilityV12R0304T : - faVJCompressionUnavailable not supported', 'Added ciscoMIPCapabilityV12R0204T : - mnSystem, mnDiscovery and mnRegistration added to groups supported. - mnRegRequestsWithDirectedBroadcast is not implemented.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoMIPCapability.setLastUpdated('200312240000Z')
if mibBuilder.loadTexts: ciscoMIPCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoMIPCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-mobileip@cisco.com')
if mibBuilder.loadTexts: ciscoMIPCapability.setDescription('Agent capabilities for MIP-MIB (MobileIP MIB).')
ciscoMIPCapabilityV12R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 203, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMIPCapabilityV12R02 = ciscoMIPCapabilityV12R02.setProductRelease('Cisco IOS 12.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMIPCapabilityV12R02 = ciscoMIPCapabilityV12R02.setStatus('current')
if mibBuilder.loadTexts: ciscoMIPCapabilityV12R02.setDescription('MobileIP mib capabilities')
ciscoMIPCapabilityV12R0204T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 203, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMIPCapabilityV12R0204T = ciscoMIPCapabilityV12R0204T.setProductRelease('Cisco IOS 12.2(4)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMIPCapabilityV12R0204T = ciscoMIPCapabilityV12R0204T.setStatus('current')
if mibBuilder.loadTexts: ciscoMIPCapabilityV12R0204T.setDescription('MobileIP mib capabilities')
ciscoMIPCapabilityV12R0304T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 203, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMIPCapabilityV12R0304T = ciscoMIPCapabilityV12R0304T.setProductRelease('Cisco IOS 12.3(4)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMIPCapabilityV12R0304T = ciscoMIPCapabilityV12R0304T.setStatus('current')
if mibBuilder.loadTexts: ciscoMIPCapabilityV12R0304T.setDescription('MobileIP mib capabilities')
mibBuilder.exportSymbols("CISCO-MIP-CAPABILITY", ciscoMIPCapability=ciscoMIPCapability, ciscoMIPCapabilityV12R0304T=ciscoMIPCapabilityV12R0304T, ciscoMIPCapabilityV12R0204T=ciscoMIPCapabilityV12R0204T, ciscoMIPCapabilityV12R02=ciscoMIPCapabilityV12R02, PYSNMP_MODULE_ID=ciscoMIPCapability)
