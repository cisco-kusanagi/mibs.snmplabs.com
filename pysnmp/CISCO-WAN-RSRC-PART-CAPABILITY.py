#
# PySNMP MIB module CISCO-WAN-RSRC-PART-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-RSRC-PART-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 18:04:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Counter32, NotificationType, ObjectIdentity, MibIdentifier, Unsigned32, Integer32, IpAddress, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Gauge32, ModuleIdentity, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "ObjectIdentity", "MibIdentifier", "Unsigned32", "Integer32", "IpAddress", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Gauge32", "ModuleIdentity", "iso", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoWanRsrcPartCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 260))
ciscoWanRsrcPartCapability.setRevisions(('2005-04-26 00:00', '2004-09-29 00:00', '2003-11-13 00:00', '2002-11-11 00:00', '2002-03-13 00:00',))
if mibBuilder.loadTexts: ciscoWanRsrcPartCapability.setLastUpdated('200504260000Z')
if mibBuilder.loadTexts: ciscoWanRsrcPartCapability.setOrganization('Cisco Systems, Inc.')
cwRsrcPartCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 260, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityV2R00 = cwRsrcPartCapabilityV2R00.setProductRelease('MGX8850 Release 2.0.00\n                          and Release 2.1.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityV2R00 = cwRsrcPartCapabilityV2R00.setStatus('current')
cwRsrcPartCapabilityRpmV2R0160 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 260, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityRpmV2R0160 = cwRsrcPartCapabilityRpmV2R0160.setProductRelease('MGX8850 Release 2.1.60')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityRpmV2R0160 = cwRsrcPartCapabilityRpmV2R0160.setStatus('current')
cwRsrcPartCapabilityRpmxfV12R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 260, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityRpmxfV12R02 = cwRsrcPartCapabilityRpmxfV12R02.setProductRelease('IOS Release 12.2.\n                          MGX8850 Release 3.0.00.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityRpmxfV12R02 = cwRsrcPartCapabilityRpmxfV12R02.setStatus('current')
cwRsrcPartCapabilityV4R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 260, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityV4R00 = cwRsrcPartCapabilityV4R00.setProductRelease('MGX8850 Release 4.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityV4R00 = cwRsrcPartCapabilityV4R00.setStatus('current')
cwRsrcPartCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 260, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityV5R00 = cwRsrcPartCapabilityV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityV5R00 = cwRsrcPartCapabilityV5R00.setStatus('current')
cwRsrcPartCapabilityAxsmeV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 260, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityAxsmeV2R00 = cwRsrcPartCapabilityAxsmeV2R00.setProductRelease('MGX8850 Release 2.0.00\n                          and Release 2.1.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityAxsmeV2R00 = cwRsrcPartCapabilityAxsmeV2R00.setStatus('current')
cwRsrcPartCapabilityAxsmeV4R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 260, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityAxsmeV4R00 = cwRsrcPartCapabilityAxsmeV4R00.setProductRelease('MGX8850 Release 4.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityAxsmeV4R00 = cwRsrcPartCapabilityAxsmeV4R00.setStatus('current')
cwRsrcPartCapabilityAxsmeV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 260, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityAxsmeV5R00 = cwRsrcPartCapabilityAxsmeV5R00.setProductRelease('MGX8850 Release 5.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityAxsmeV5R00 = cwRsrcPartCapabilityAxsmeV5R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-RSRC-PART-CAPABILITY", cwRsrcPartCapabilityV4R00=cwRsrcPartCapabilityV4R00, cwRsrcPartCapabilityRpmxfV12R02=cwRsrcPartCapabilityRpmxfV12R02, cwRsrcPartCapabilityAxsmeV2R00=cwRsrcPartCapabilityAxsmeV2R00, PYSNMP_MODULE_ID=ciscoWanRsrcPartCapability, cwRsrcPartCapabilityRpmV2R0160=cwRsrcPartCapabilityRpmV2R0160, cwRsrcPartCapabilityV2R00=cwRsrcPartCapabilityV2R00, cwRsrcPartCapabilityAxsmeV4R00=cwRsrcPartCapabilityAxsmeV4R00, cwRsrcPartCapabilityAxsmeV5R00=cwRsrcPartCapabilityAxsmeV5R00, cwRsrcPartCapabilityV5R00=cwRsrcPartCapabilityV5R00, ciscoWanRsrcPartCapability=ciscoWanRsrcPartCapability)
