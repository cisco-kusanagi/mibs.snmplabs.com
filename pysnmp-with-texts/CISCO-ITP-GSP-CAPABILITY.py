#
# PySNMP MIB module CISCO-ITP-GSP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ITP-GSP-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:03:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
ObjectIdentity, ModuleIdentity, MibIdentifier, TimeTicks, Integer32, Counter32, NotificationType, iso, Bits, Counter64, Unsigned32, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "ModuleIdentity", "MibIdentifier", "TimeTicks", "Integer32", "Counter32", "NotificationType", "iso", "Bits", "Counter64", "Unsigned32", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoGspCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 306))
ciscoGspCapability.setRevisions(('2007-07-16 00:00', '2006-01-06 00:00', '2003-10-15 00:00', '2003-07-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoGspCapability.setRevisionsDescriptions(('Added ciscoGspCapabilityV12R0218IXA and ciscoGspCapabilityV12R0411SW capability statements. Corrected all statements to remove support for ciscoGspProfileGroup and removed variation associated with following objects. cgspProfileVariant cgspProfileMtp2BundleTimer cgspProfileMtp2SendQueueDepth cgspProfileRowStatus cgspProfileTimerValue cgspProfileTimerRowStatus', 'Added support for new isolation notifcation. Added capability statement ciscoGspCapabilityV12R0225SW3.', 'Deprecate cgspLinkSctpAssociation and replace with cgspLinkSctpAssociationId to allow larger range for association identifiers.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoGspCapability.setLastUpdated('200707160000Z')
if mibBuilder.loadTexts: ciscoGspCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoGspCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-ss7@cisco.com')
if mibBuilder.loadTexts: ciscoGspCapability.setDescription('Agent capabilities for the CISCO-ITP-GSP-MIB.')
ciscoGspCapabilityV12R0204MB10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 306, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGspCapabilityV12R0204MB10 = ciscoGspCapabilityV12R0204MB10.setProductRelease('Cisco IOS 12.2(4)MB10')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGspCapabilityV12R0204MB10 = ciscoGspCapabilityV12R0204MB10.setStatus('current')
if mibBuilder.loadTexts: ciscoGspCapabilityV12R0204MB10.setDescription('IOS 12.2(4)MB1 Cisco CISCO-ITP-GSP-MIB.my User Agent MIB capabilities.')
ciscoGspCapabilityV12R0219SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 306, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGspCapabilityV12R0219SW = ciscoGspCapabilityV12R0219SW.setProductRelease('Cisco IOS 12.2(19)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGspCapabilityV12R0219SW = ciscoGspCapabilityV12R0219SW.setStatus('current')
if mibBuilder.loadTexts: ciscoGspCapabilityV12R0219SW.setDescription('IOS 12.2(19)SW Cisco CISCO-ITP-GSP-MIB.my User Agent MIB capabilities.')
ciscoGspCapabilityV12R0225SW3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 306, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGspCapabilityV12R0225SW3 = ciscoGspCapabilityV12R0225SW3.setProductRelease('Cisco IOS 12.2(25)SW3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGspCapabilityV12R0225SW3 = ciscoGspCapabilityV12R0225SW3.setStatus('current')
if mibBuilder.loadTexts: ciscoGspCapabilityV12R0225SW3.setDescription('IOS 12.2(25)SW3 Cisco CISCO-ITP-GSP-MIB.my User Agent MIB capabilities.')
ciscoGspCapabilityV12R0218IXA = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 306, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGspCapabilityV12R0218IXA = ciscoGspCapabilityV12R0218IXA.setProductRelease('Cisco IOS 12.2(18)IXA')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGspCapabilityV12R0218IXA = ciscoGspCapabilityV12R0218IXA.setStatus('current')
if mibBuilder.loadTexts: ciscoGspCapabilityV12R0218IXA.setDescription('IOS 12.2(18)IXA Cisco CISCO-ITP-GSP-MIB.my User Agent MIB capabilities.')
ciscoGspCapabilityV12R0411SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 306, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGspCapabilityV12R0411SW = ciscoGspCapabilityV12R0411SW.setProductRelease('Cisco IOS 12.4(11)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGspCapabilityV12R0411SW = ciscoGspCapabilityV12R0411SW.setStatus('current')
if mibBuilder.loadTexts: ciscoGspCapabilityV12R0411SW.setDescription('Cisco IOS 12.4(11)SW CISCO-ITP-GSP-MIB.my User Agent MIB capabilities.')
mibBuilder.exportSymbols("CISCO-ITP-GSP-CAPABILITY", ciscoGspCapabilityV12R0411SW=ciscoGspCapabilityV12R0411SW, ciscoGspCapability=ciscoGspCapability, ciscoGspCapabilityV12R0219SW=ciscoGspCapabilityV12R0219SW, PYSNMP_MODULE_ID=ciscoGspCapability, ciscoGspCapabilityV12R0218IXA=ciscoGspCapabilityV12R0218IXA, ciscoGspCapabilityV12R0204MB10=ciscoGspCapabilityV12R0204MB10, ciscoGspCapabilityV12R0225SW3=ciscoGspCapabilityV12R0225SW3)
