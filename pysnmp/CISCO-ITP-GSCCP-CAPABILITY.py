#
# PySNMP MIB module CISCO-ITP-GSCCP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ITP-GSCCP-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:46:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
ModuleIdentity, Counter32, Bits, ObjectIdentity, IpAddress, NotificationType, Counter64, TimeTicks, Unsigned32, MibIdentifier, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "Bits", "ObjectIdentity", "IpAddress", "NotificationType", "Counter64", "TimeTicks", "Unsigned32", "MibIdentifier", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoGsccpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 539))
ciscoGsccpCapability.setRevisions(('2007-05-17 00:00', '2005-01-14 00:00', '2004-10-07 00:00', '2003-12-08 00:00', '2003-10-28 00:00', '2003-05-20 00:00',))
if mibBuilder.loadTexts: ciscoGsccpCapability.setLastUpdated('200705170000Z')
if mibBuilder.loadTexts: ciscoGsccpCapability.setOrganization('Cisco Systems, Inc.')
ciscoGsccpCapabilityV12R0204MB10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 539, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R0204MB10 = ciscoGsccpCapabilityV12R0204MB10.setProductRelease('Cisco IOS 12.2(4)MB10')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R0204MB10 = ciscoGsccpCapabilityV12R0204MB10.setStatus('current')
ciscoGsccpCapabilityV12R0204MB13 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 539, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R0204MB13 = ciscoGsccpCapabilityV12R0204MB13.setProductRelease('Cisco IOS 12.2(4)MB13')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R0204MB13 = ciscoGsccpCapabilityV12R0204MB13.setStatus('current')
ciscoGsccpCapabilityV12R022004SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 539, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R022004SW = ciscoGsccpCapabilityV12R022004SW.setProductRelease('Cisco IOS 12.2(20.4)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R022004SW = ciscoGsccpCapabilityV12R022004SW.setStatus('current')
ciscoGsccpCapabilityV12R023000SW1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 539, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R023000SW1 = ciscoGsccpCapabilityV12R023000SW1.setProductRelease('Cisco IOS 12.2(23)SW1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R023000SW1 = ciscoGsccpCapabilityV12R023000SW1.setStatus('current')
ciscoGsccpCapabilityV12R025000SW1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 539, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R025000SW1 = ciscoGsccpCapabilityV12R025000SW1.setProductRelease('Cisco IOS 12.2(25)SW1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R025000SW1 = ciscoGsccpCapabilityV12R025000SW1.setStatus('current')
ciscoGsccpCapabilityV12R0218IXA = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 539, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R0218IXA = ciscoGsccpCapabilityV12R0218IXA.setProductRelease('Cisco IOS 12.2(18)IXA')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R0218IXA = ciscoGsccpCapabilityV12R0218IXA.setStatus('current')
ciscoGsccpCapabilityV12R0411SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 539, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R0411SW = ciscoGsccpCapabilityV12R0411SW.setProductRelease('Cisco IOS IOS 12.4(11)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R0411SW = ciscoGsccpCapabilityV12R0411SW.setStatus('current')
mibBuilder.exportSymbols("CISCO-ITP-GSCCP-CAPABILITY", ciscoGsccpCapabilityV12R023000SW1=ciscoGsccpCapabilityV12R023000SW1, ciscoGsccpCapabilityV12R022004SW=ciscoGsccpCapabilityV12R022004SW, ciscoGsccpCapabilityV12R0204MB13=ciscoGsccpCapabilityV12R0204MB13, ciscoGsccpCapability=ciscoGsccpCapability, ciscoGsccpCapabilityV12R0204MB10=ciscoGsccpCapabilityV12R0204MB10, ciscoGsccpCapabilityV12R0411SW=ciscoGsccpCapabilityV12R0411SW, PYSNMP_MODULE_ID=ciscoGsccpCapability, ciscoGsccpCapabilityV12R0218IXA=ciscoGsccpCapabilityV12R0218IXA, ciscoGsccpCapabilityV12R025000SW1=ciscoGsccpCapabilityV12R025000SW1)
