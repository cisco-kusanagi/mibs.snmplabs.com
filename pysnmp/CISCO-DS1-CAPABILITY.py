#
# PySNMP MIB module CISCO-DS1-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DS1-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:38:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Integer32, Counter32, ObjectIdentity, Unsigned32, Gauge32, IpAddress, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ModuleIdentity, TimeTicks, Bits, iso, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "ObjectIdentity", "Unsigned32", "Gauge32", "IpAddress", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ModuleIdentity", "TimeTicks", "Bits", "iso", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDs1Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 273))
ciscoDs1Capability.setRevisions(('2007-10-31 00:00', '2007-09-10 00:00', '2007-05-11 00:00', '2006-06-16 00:00', '2005-07-11 00:00', '2003-12-22 00:00', '2002-04-28 00:00',))
if mibBuilder.loadTexts: ciscoDs1Capability.setLastUpdated('200710310000Z')
if mibBuilder.loadTexts: ciscoDs1Capability.setOrganization('Cisco Systems, Inc.')
ciscoDs1AxsmeCapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 273, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1AxsmeCapabilityV3R00 = ciscoDs1AxsmeCapabilityV3R00.setProductRelease('MGX8850 Release 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1AxsmeCapabilityV3R00 = ciscoDs1AxsmeCapabilityV3R00.setStatus('current')
ciscoDs1CapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 273, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityV5R00 = ciscoDs1CapabilityV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityV5R00 = ciscoDs1CapabilityV5R00.setStatus('current')
ciscoDs1CapabilityV5R100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 273, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityV5R100 = ciscoDs1CapabilityV5R100.setProductRelease('MGX8880 Release 5.1.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityV5R100 = ciscoDs1CapabilityV5R100.setStatus('current')
ciscoDs1CapabilityV5R310 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 273, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityV5R310 = ciscoDs1CapabilityV5R310.setProductRelease('MGX8880 Release 5.3.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityV5R310 = ciscoDs1CapabilityV5R310.setStatus('current')
ciscoDs1CapabilityMARsV12R5T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 273, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityMARsV12R5T = ciscoDs1CapabilityMARsV12R5T.setProductRelease('IOS 12.5T for Cisco Access Routers and ISRs')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityMARsV12R5T = ciscoDs1CapabilityMARsV12R5T.setStatus('current')
ciscoDs1CapabilityAS5xxxV12R5T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 273, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityAS5xxxV12R5T = ciscoDs1CapabilityAS5xxxV12R5T.setProductRelease('IOS 12.5T for Cisco Access Servers')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityAS5xxxV12R5T = ciscoDs1CapabilityAS5xxxV12R5T.setStatus('current')
ciscoDs1CapabilityV5R500 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 273, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityV5R500 = ciscoDs1CapabilityV5R500.setProductRelease('MGX8880 Release 5.5.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityV5R500 = ciscoDs1CapabilityV5R500.setStatus('current')
mibBuilder.exportSymbols("CISCO-DS1-CAPABILITY", ciscoDs1CapabilityV5R310=ciscoDs1CapabilityV5R310, ciscoDs1CapabilityMARsV12R5T=ciscoDs1CapabilityMARsV12R5T, ciscoDs1Capability=ciscoDs1Capability, ciscoDs1CapabilityV5R100=ciscoDs1CapabilityV5R100, ciscoDs1AxsmeCapabilityV3R00=ciscoDs1AxsmeCapabilityV3R00, ciscoDs1CapabilityV5R500=ciscoDs1CapabilityV5R500, ciscoDs1CapabilityAS5xxxV12R5T=ciscoDs1CapabilityAS5xxxV12R5T, PYSNMP_MODULE_ID=ciscoDs1Capability, ciscoDs1CapabilityV5R00=ciscoDs1CapabilityV5R00)
