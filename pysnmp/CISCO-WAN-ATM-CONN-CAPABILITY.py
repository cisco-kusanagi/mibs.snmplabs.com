#
# PySNMP MIB module CISCO-WAN-ATM-CONN-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-ATM-CONN-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 18:03:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
iso, IpAddress, Integer32, ObjectIdentity, Bits, ModuleIdentity, NotificationType, Counter64, Unsigned32, TimeTicks, Counter32, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "IpAddress", "Integer32", "ObjectIdentity", "Bits", "ModuleIdentity", "NotificationType", "Counter64", "Unsigned32", "TimeTicks", "Counter32", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoWanAtmConnCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 380))
ciscoWanAtmConnCapability.setRevisions(('2004-02-07 00:00', '2002-03-26 00:00',))
if mibBuilder.loadTexts: ciscoWanAtmConnCapability.setLastUpdated('200402070000Z')
if mibBuilder.loadTexts: ciscoWanAtmConnCapability.setOrganization('Cisco Systems, Inc.')
cwAtmConnCapabilityAxsmV2R0160 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 380, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityAxsmV2R0160 = cwAtmConnCapabilityAxsmV2R0160.setProductRelease('MGX8850 Release 2.1.60.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityAxsmV2R0160 = cwAtmConnCapabilityAxsmV2R0160.setStatus('current')
cwAtmConnCapabilityAxsmeV2R0160 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 380, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityAxsmeV2R0160 = cwAtmConnCapabilityAxsmeV2R0160.setProductRelease('MGX8850 Release 2.1.60')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityAxsmeV2R0160 = cwAtmConnCapabilityAxsmeV2R0160.setStatus('current')
cwAtmConnCapabilityRpmprV2R0160 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 380, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityRpmprV2R0160 = cwAtmConnCapabilityRpmprV2R0160.setProductRelease('MGX8850 Release 2.1.60')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityRpmprV2R0160 = cwAtmConnCapabilityRpmprV2R0160.setStatus('current')
cwAtmConnCapabilityBpxsesV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 380, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityBpxsesV3R00 = cwAtmConnCapabilityBpxsesV3R00.setProductRelease('BPX SES Release 3.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityBpxsesV3R00 = cwAtmConnCapabilityBpxsesV3R00.setStatus('current')
cwAtmConnCapabilityAxsmV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 380, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityAxsmV3R00 = cwAtmConnCapabilityAxsmV3R00.setProductRelease('MGX8850 Release 3.0.00.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityAxsmV3R00 = cwAtmConnCapabilityAxsmV3R00.setStatus('current')
cwAtmConnCapabilityAxsmeV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 380, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityAxsmeV3R00 = cwAtmConnCapabilityAxsmeV3R00.setProductRelease('MGX8850 Release 3.0.00.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityAxsmeV3R00 = cwAtmConnCapabilityAxsmeV3R00.setStatus('current')
cwAtmConnCapabilityPxm1eV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 380, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityPxm1eV3R00 = cwAtmConnCapabilityPxm1eV3R00.setProductRelease('MGX8850 Release 3.0.00.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityPxm1eV3R00 = cwAtmConnCapabilityPxm1eV3R00.setStatus('current')
cwAtmConnCapabilityRpmprV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 380, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityRpmprV3R00 = cwAtmConnCapabilityRpmprV3R00.setProductRelease('MGX8850 Release 3.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityRpmprV3R00 = cwAtmConnCapabilityRpmprV3R00.setStatus('current')
cwAtmConnCapabilityRpmxfV12R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 380, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityRpmxfV12R02 = cwAtmConnCapabilityRpmxfV12R02.setProductRelease('IOS Release 12.2\n                          in MGX8850 Release 3.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityRpmxfV12R02 = cwAtmConnCapabilityRpmxfV12R02.setStatus('current')
cwAtmConnCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 380, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityV5R00 = cwAtmConnCapabilityV5R00.setProductRelease('MGX8850 Release 5.0.00.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityV5R00 = cwAtmConnCapabilityV5R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-ATM-CONN-CAPABILITY", PYSNMP_MODULE_ID=ciscoWanAtmConnCapability, cwAtmConnCapabilityRpmprV2R0160=cwAtmConnCapabilityRpmprV2R0160, cwAtmConnCapabilityAxsmeV3R00=cwAtmConnCapabilityAxsmeV3R00, cwAtmConnCapabilityAxsmV3R00=cwAtmConnCapabilityAxsmV3R00, cwAtmConnCapabilityPxm1eV3R00=cwAtmConnCapabilityPxm1eV3R00, cwAtmConnCapabilityBpxsesV3R00=cwAtmConnCapabilityBpxsesV3R00, cwAtmConnCapabilityRpmxfV12R02=cwAtmConnCapabilityRpmxfV12R02, cwAtmConnCapabilityV5R00=cwAtmConnCapabilityV5R00, ciscoWanAtmConnCapability=ciscoWanAtmConnCapability, cwAtmConnCapabilityAxsmV2R0160=cwAtmConnCapabilityAxsmV2R0160, cwAtmConnCapabilityRpmprV3R00=cwAtmConnCapabilityRpmprV3R00, cwAtmConnCapabilityAxsmeV2R0160=cwAtmConnCapabilityAxsmeV2R0160)
