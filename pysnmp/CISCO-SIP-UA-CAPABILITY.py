#
# PySNMP MIB module CISCO-SIP-UA-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SIP-UA-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:55:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
NotificationType, ModuleIdentity, Integer32, iso, Counter64, MibIdentifier, IpAddress, Gauge32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Bits, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "Integer32", "iso", "Counter64", "MibIdentifier", "IpAddress", "Gauge32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Bits", "Unsigned32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSipUaCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 172))
ciscoSipUaCapability.setRevisions(('2005-06-22 00:00', '2003-07-30 00:00', '2003-03-21 00:00', '2001-09-26 00:00', '2001-06-11 00:00',))
if mibBuilder.loadTexts: ciscoSipUaCapability.setLastUpdated('200506220000Z')
if mibBuilder.loadTexts: ciscoSipUaCapability.setOrganization('Cisco Systems, Inc.')
ciscoSipUaCapabilityV12R0202 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 172, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0202 = ciscoSipUaCapabilityV12R0202.setProductRelease('Cisco IOS 12.2(2).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0202 = ciscoSipUaCapabilityV12R0202.setStatus('current')
ciscoSipUaCapabilityV12R0208 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 172, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0208 = ciscoSipUaCapabilityV12R0208.setProductRelease('Cisco IOS 12.2(8).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0208 = ciscoSipUaCapabilityV12R0208.setStatus('current')
ciscoSipUaCapabilityV12R0211 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 172, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0211 = ciscoSipUaCapabilityV12R0211.setProductRelease('Cisco IOS 12.2(11).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0211 = ciscoSipUaCapabilityV12R0211.setStatus('current')
ciscoSipUaCapabilityV12R0215 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 172, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0215 = ciscoSipUaCapabilityV12R0215.setProductRelease('Cisco IOS 12.2(15).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0215 = ciscoSipUaCapabilityV12R0215.setStatus('current')
ciscoSipUaCapabilityV12R0302 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 172, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0302 = ciscoSipUaCapabilityV12R0302.setProductRelease('Cisco IOS 12.3(2).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0302 = ciscoSipUaCapabilityV12R0302.setStatus('current')
ciscoSipUaCapabilityV12R0402T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 172, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0402T = ciscoSipUaCapabilityV12R0402T.setProductRelease('Cisco IOS 12.4(2)T.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0402T = ciscoSipUaCapabilityV12R0402T.setStatus('current')
mibBuilder.exportSymbols("CISCO-SIP-UA-CAPABILITY", ciscoSipUaCapabilityV12R0402T=ciscoSipUaCapabilityV12R0402T, ciscoSipUaCapabilityV12R0215=ciscoSipUaCapabilityV12R0215, ciscoSipUaCapabilityV12R0202=ciscoSipUaCapabilityV12R0202, ciscoSipUaCapabilityV12R0302=ciscoSipUaCapabilityV12R0302, ciscoSipUaCapability=ciscoSipUaCapability, ciscoSipUaCapabilityV12R0211=ciscoSipUaCapabilityV12R0211, PYSNMP_MODULE_ID=ciscoSipUaCapability, ciscoSipUaCapabilityV12R0208=ciscoSipUaCapabilityV12R0208)
