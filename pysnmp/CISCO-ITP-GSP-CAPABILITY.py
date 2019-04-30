#
# PySNMP MIB module CISCO-ITP-GSP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ITP-GSP-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:46:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Gauge32, Counter64, Unsigned32, Integer32, iso, Bits, ObjectIdentity, IpAddress, Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter64", "Unsigned32", "Integer32", "iso", "Bits", "ObjectIdentity", "IpAddress", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoGspCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 306))
ciscoGspCapability.setRevisions(('2007-07-16 00:00', '2006-01-06 00:00', '2003-10-15 00:00', '2003-07-17 00:00',))
if mibBuilder.loadTexts: ciscoGspCapability.setLastUpdated('200707160000Z')
if mibBuilder.loadTexts: ciscoGspCapability.setOrganization('Cisco Systems, Inc.')
ciscoGspCapabilityV12R0204MB10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 306, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGspCapabilityV12R0204MB10 = ciscoGspCapabilityV12R0204MB10.setProductRelease('Cisco IOS 12.2(4)MB10')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGspCapabilityV12R0204MB10 = ciscoGspCapabilityV12R0204MB10.setStatus('current')
ciscoGspCapabilityV12R0219SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 306, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGspCapabilityV12R0219SW = ciscoGspCapabilityV12R0219SW.setProductRelease('Cisco IOS 12.2(19)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGspCapabilityV12R0219SW = ciscoGspCapabilityV12R0219SW.setStatus('current')
ciscoGspCapabilityV12R0225SW3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 306, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGspCapabilityV12R0225SW3 = ciscoGspCapabilityV12R0225SW3.setProductRelease('Cisco IOS 12.2(25)SW3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGspCapabilityV12R0225SW3 = ciscoGspCapabilityV12R0225SW3.setStatus('current')
ciscoGspCapabilityV12R0218IXA = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 306, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGspCapabilityV12R0218IXA = ciscoGspCapabilityV12R0218IXA.setProductRelease('Cisco IOS 12.2(18)IXA')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGspCapabilityV12R0218IXA = ciscoGspCapabilityV12R0218IXA.setStatus('current')
ciscoGspCapabilityV12R0411SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 306, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGspCapabilityV12R0411SW = ciscoGspCapabilityV12R0411SW.setProductRelease('Cisco IOS 12.4(11)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGspCapabilityV12R0411SW = ciscoGspCapabilityV12R0411SW.setStatus('current')
mibBuilder.exportSymbols("CISCO-ITP-GSP-CAPABILITY", ciscoGspCapabilityV12R0204MB10=ciscoGspCapabilityV12R0204MB10, ciscoGspCapabilityV12R0218IXA=ciscoGspCapabilityV12R0218IXA, ciscoGspCapabilityV12R0411SW=ciscoGspCapabilityV12R0411SW, PYSNMP_MODULE_ID=ciscoGspCapability, ciscoGspCapability=ciscoGspCapability, ciscoGspCapabilityV12R0219SW=ciscoGspCapabilityV12R0219SW, ciscoGspCapabilityV12R0225SW3=ciscoGspCapabilityV12R0225SW3)
