#
# PySNMP MIB module CISCO-SIP-UA-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SIP-UA-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:12:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier, ObjectIdentity, iso, Counter32, Gauge32, Unsigned32, NotificationType, IpAddress, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier", "ObjectIdentity", "iso", "Counter32", "Gauge32", "Unsigned32", "NotificationType", "IpAddress", "Integer32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSipUaCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 172))
ciscoSipUaCapability.setRevisions(('2005-06-22 00:00', '2003-07-30 00:00', '2003-03-21 00:00', '2001-09-26 00:00', '2001-06-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSipUaCapability.setRevisionsDescriptions(('Adding AGENT-CAPABILITIES clause for IOS 12.4(2)T.', 'Adding AGENT-CAPABILITIES clauses for IOS 12.3(2).', 'Adding AGENT-CAPABILITIES clauses for IOS 12.2(8), 12.2(11) & 12.2(15).', 'Adding AGENT-CAPABILITIES clause for IOS 12.2(2).', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSipUaCapability.setLastUpdated('200506220000Z')
if mibBuilder.loadTexts: ciscoSipUaCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSipUaCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-sip@cisco.com')
if mibBuilder.loadTexts: ciscoSipUaCapability.setDescription('Agent capabilities for the CISCO-SIP-UA-MIB.')
ciscoSipUaCapabilityV12R0202 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 172, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0202 = ciscoSipUaCapabilityV12R0202.setProductRelease('Cisco IOS 12.2(2).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0202 = ciscoSipUaCapabilityV12R0202.setStatus('current')
if mibBuilder.loadTexts: ciscoSipUaCapabilityV12R0202.setDescription('IOS 12.2 Cisco SIP User Agent MIB capabilities.')
ciscoSipUaCapabilityV12R0208 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 172, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0208 = ciscoSipUaCapabilityV12R0208.setProductRelease('Cisco IOS 12.2(8).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0208 = ciscoSipUaCapabilityV12R0208.setStatus('current')
if mibBuilder.loadTexts: ciscoSipUaCapabilityV12R0208.setDescription('IOS 12.2 Cisco SIP User Agent MIB capabilities.')
ciscoSipUaCapabilityV12R0211 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 172, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0211 = ciscoSipUaCapabilityV12R0211.setProductRelease('Cisco IOS 12.2(11).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0211 = ciscoSipUaCapabilityV12R0211.setStatus('current')
if mibBuilder.loadTexts: ciscoSipUaCapabilityV12R0211.setDescription('IOS 12.2 Cisco SIP User Agent MIB capabilities.')
ciscoSipUaCapabilityV12R0215 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 172, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0215 = ciscoSipUaCapabilityV12R0215.setProductRelease('Cisco IOS 12.2(15).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0215 = ciscoSipUaCapabilityV12R0215.setStatus('current')
if mibBuilder.loadTexts: ciscoSipUaCapabilityV12R0215.setDescription('IOS 12.2 Cisco SIP User Agent MIB capabilities.')
ciscoSipUaCapabilityV12R0302 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 172, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0302 = ciscoSipUaCapabilityV12R0302.setProductRelease('Cisco IOS 12.3(2).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0302 = ciscoSipUaCapabilityV12R0302.setStatus('current')
if mibBuilder.loadTexts: ciscoSipUaCapabilityV12R0302.setDescription('IOS 12.3 Cisco SIP User Agent MIB capabilities.')
ciscoSipUaCapabilityV12R0402T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 172, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0402T = ciscoSipUaCapabilityV12R0402T.setProductRelease('Cisco IOS 12.4(2)T.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0402T = ciscoSipUaCapabilityV12R0402T.setStatus('current')
if mibBuilder.loadTexts: ciscoSipUaCapabilityV12R0402T.setDescription('IOS 12.4(2)T Cisco SIP User Agent MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SIP-UA-CAPABILITY", ciscoSipUaCapabilityV12R0215=ciscoSipUaCapabilityV12R0215, ciscoSipUaCapabilityV12R0208=ciscoSipUaCapabilityV12R0208, ciscoSipUaCapabilityV12R0302=ciscoSipUaCapabilityV12R0302, ciscoSipUaCapabilityV12R0211=ciscoSipUaCapabilityV12R0211, ciscoSipUaCapabilityV12R0202=ciscoSipUaCapabilityV12R0202, PYSNMP_MODULE_ID=ciscoSipUaCapability, ciscoSipUaCapabilityV12R0402T=ciscoSipUaCapabilityV12R0402T, ciscoSipUaCapability=ciscoSipUaCapability)
