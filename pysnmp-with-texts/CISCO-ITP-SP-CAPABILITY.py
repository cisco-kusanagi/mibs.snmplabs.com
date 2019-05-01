#
# PySNMP MIB module CISCO-ITP-SP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ITP-SP-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:03:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, Unsigned32, NotificationType, iso, Gauge32, ObjectIdentity, MibIdentifier, Integer32, TimeTicks, Bits, Counter32, ModuleIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Unsigned32", "NotificationType", "iso", "Gauge32", "ObjectIdentity", "MibIdentifier", "Integer32", "TimeTicks", "Bits", "Counter32", "ModuleIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoItpSpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 217))
ciscoItpSpCapability.setRevisions(('2002-01-21 00:00', '2001-10-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoItpSpCapability.setRevisionsDescriptions(('Updated capabilities MIB as required for new group. cItpSpStatsGroup', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoItpSpCapability.setLastUpdated('200201210000Z')
if mibBuilder.loadTexts: ciscoItpSpCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoItpSpCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-ss7@cisco.com')
if mibBuilder.loadTexts: ciscoItpSpCapability.setDescription('Agent capabilities for the CISCO-ITP-SP-MIB.')
ciscoItpSpCapabilityV12R024MB1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 217, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpSpCapabilityV12R024MB1 = ciscoItpSpCapabilityV12R024MB1.setProductRelease('Cisco IOS 12.2(4)MB1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpSpCapabilityV12R024MB1 = ciscoItpSpCapabilityV12R024MB1.setStatus('current')
if mibBuilder.loadTexts: ciscoItpSpCapabilityV12R024MB1.setDescription('IOS 12.2(4)MB1 Cisco CISCO-ITP-SP-MIB.my User Agent MIB capabilities.')
ciscoItpSpCapabilityV12R0204MB3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 217, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpSpCapabilityV12R0204MB3 = ciscoItpSpCapabilityV12R0204MB3.setProductRelease('Cisco IOS 12.2(4)MB3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpSpCapabilityV12R0204MB3 = ciscoItpSpCapabilityV12R0204MB3.setStatus('current')
if mibBuilder.loadTexts: ciscoItpSpCapabilityV12R0204MB3.setDescription('IOS 12.2(4)MB3 Cisco CISCO-ITP-SP-MIB.my User Agent MIB capabilities.')
mibBuilder.exportSymbols("CISCO-ITP-SP-CAPABILITY", ciscoItpSpCapabilityV12R0204MB3=ciscoItpSpCapabilityV12R0204MB3, ciscoItpSpCapabilityV12R024MB1=ciscoItpSpCapabilityV12R024MB1, ciscoItpSpCapability=ciscoItpSpCapability, PYSNMP_MODULE_ID=ciscoItpSpCapability)
