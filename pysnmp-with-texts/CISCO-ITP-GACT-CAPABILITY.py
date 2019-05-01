#
# PySNMP MIB module CISCO-ITP-GACT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ITP-GACT-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:03:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, Gauge32, TimeTicks, ModuleIdentity, NotificationType, Counter64, Integer32, Counter32, ObjectIdentity, Bits, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "Gauge32", "TimeTicks", "ModuleIdentity", "NotificationType", "Counter64", "Integer32", "Counter32", "ObjectIdentity", "Bits", "Unsigned32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoGactCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 304))
ciscoGactCapability.setRevisions(('2007-04-26 00:00', '2003-12-08 00:00', '2003-07-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoGactCapability.setRevisionsDescriptions(('Added ciscoGactCapabilityV12R0218IXA and ciscoGactCapabilityV12R0411SW capability statements.', 'Support for cross instance global title translation. Added agent capability ciscoGactCapabilityV12R022004SW statement for IOS 12.2(20.4) and replaced ciscoGactGttGroup object group with ciscoGactGttGroupRev1.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoGactCapability.setLastUpdated('200704260000Z')
if mibBuilder.loadTexts: ciscoGactCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoGactCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-ss7@cisco.com')
if mibBuilder.loadTexts: ciscoGactCapability.setDescription('Agent capabilities for the CISCO-ITP-GACT-MIB.')
ciscoGactCapabilityV12R0204MB10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 304, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGactCapabilityV12R0204MB10 = ciscoGactCapabilityV12R0204MB10.setProductRelease('Cisco IOS 12.2(4)MB10')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGactCapabilityV12R0204MB10 = ciscoGactCapabilityV12R0204MB10.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoGactCapabilityV12R0204MB10.setDescription('CISCO-ITP-GACT-MIB.my agent capabilities.')
ciscoGactCapabilityV12R022004SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 304, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGactCapabilityV12R022004SW = ciscoGactCapabilityV12R022004SW.setProductRelease('Cisco IOS 12.2(20.4)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGactCapabilityV12R022004SW = ciscoGactCapabilityV12R022004SW.setStatus('current')
if mibBuilder.loadTexts: ciscoGactCapabilityV12R022004SW.setDescription('CISCO-ITP-GACT-MIB.my agent capabilities.')
ciscoGactCapabilityV12R0218IXA = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 304, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGactCapabilityV12R0218IXA = ciscoGactCapabilityV12R0218IXA.setProductRelease('Cisco IOS 12.2(18)IXA')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGactCapabilityV12R0218IXA = ciscoGactCapabilityV12R0218IXA.setStatus('current')
if mibBuilder.loadTexts: ciscoGactCapabilityV12R0218IXA.setDescription('CISCO-ITP-GACT-MIB.my agent capabilities.')
ciscoGactCapabilityV12R0411SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 304, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGactCapabilityV12R0411SW = ciscoGactCapabilityV12R0411SW.setProductRelease('Cisco IOS 12.4(11)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGactCapabilityV12R0411SW = ciscoGactCapabilityV12R0411SW.setStatus('current')
if mibBuilder.loadTexts: ciscoGactCapabilityV12R0411SW.setDescription('CISCO-ITP-GACT-MIB.my agent capabilities.')
mibBuilder.exportSymbols("CISCO-ITP-GACT-CAPABILITY", ciscoGactCapabilityV12R0218IXA=ciscoGactCapabilityV12R0218IXA, ciscoGactCapabilityV12R0204MB10=ciscoGactCapabilityV12R0204MB10, PYSNMP_MODULE_ID=ciscoGactCapability, ciscoGactCapabilityV12R022004SW=ciscoGactCapabilityV12R022004SW, ciscoGactCapabilityV12R0411SW=ciscoGactCapabilityV12R0411SW, ciscoGactCapability=ciscoGactCapability)
