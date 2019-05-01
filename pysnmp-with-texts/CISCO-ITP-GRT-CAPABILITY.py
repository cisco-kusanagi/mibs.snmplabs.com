#
# PySNMP MIB module CISCO-ITP-GRT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ITP-GRT-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:03:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Bits, Integer32, Counter32, NotificationType, MibIdentifier, Unsigned32, TimeTicks, Counter64, Gauge32, ObjectIdentity, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Counter32", "NotificationType", "MibIdentifier", "Unsigned32", "TimeTicks", "Counter64", "Gauge32", "ObjectIdentity", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoItpGrtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 309))
ciscoItpGrtCapability.setRevisions(('2007-04-25 00:00', '2006-10-13 00:00', '2003-07-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoItpGrtCapability.setRevisionsDescriptions(('Added ciscoGrtCapabilityV12R0411SW capability statements.', 'Added ciscoGrtCapabilityV12R0218IXA capability statement. Added cosmetic changes to MIB sections.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoItpGrtCapability.setLastUpdated('200704250000Z')
if mibBuilder.loadTexts: ciscoItpGrtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoItpGrtCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-ss7@cisco.com')
if mibBuilder.loadTexts: ciscoItpGrtCapability.setDescription('Agent capabilities for the CISCO-ITP-GRT-MIB.')
ciscoGrtCapabilityV12R0204MB10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 309, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGrtCapabilityV12R0204MB10 = ciscoGrtCapabilityV12R0204MB10.setProductRelease('Cisco IOS 12.2(4)MB10')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGrtCapabilityV12R0204MB10 = ciscoGrtCapabilityV12R0204MB10.setStatus('current')
if mibBuilder.loadTexts: ciscoGrtCapabilityV12R0204MB10.setDescription('IOS 12.2(4)MB10 Cisco CISCO-ITP-GRT-MIB.my User Agent MIB capabilities.')
ciscoGrtCapabilityV12R0218IXA = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 309, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGrtCapabilityV12R0218IXA = ciscoGrtCapabilityV12R0218IXA.setProductRelease('Cisco IOS 12.2(18)IXA')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGrtCapabilityV12R0218IXA = ciscoGrtCapabilityV12R0218IXA.setStatus('current')
if mibBuilder.loadTexts: ciscoGrtCapabilityV12R0218IXA.setDescription('IOS 12.2(18)IXA Cisco CISCO-ITP-GRT-MIB.my User Agent MIB capabilities.')
ciscoGrtCapabilityV12R0411SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 309, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGrtCapabilityV12R0411SW = ciscoGrtCapabilityV12R0411SW.setProductRelease('Cisco IOS 12.4(11)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGrtCapabilityV12R0411SW = ciscoGrtCapabilityV12R0411SW.setStatus('current')
if mibBuilder.loadTexts: ciscoGrtCapabilityV12R0411SW.setDescription('Cisco IOS 12.4(11)SW Cisco CISCO-ITP-GRT-MIB.my User Agent MIB capabilities.')
mibBuilder.exportSymbols("CISCO-ITP-GRT-CAPABILITY", ciscoGrtCapabilityV12R0204MB10=ciscoGrtCapabilityV12R0204MB10, ciscoItpGrtCapability=ciscoItpGrtCapability, ciscoGrtCapabilityV12R0218IXA=ciscoGrtCapabilityV12R0218IXA, ciscoGrtCapabilityV12R0411SW=ciscoGrtCapabilityV12R0411SW, PYSNMP_MODULE_ID=ciscoItpGrtCapability)
