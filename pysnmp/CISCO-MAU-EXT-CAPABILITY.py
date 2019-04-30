#
# PySNMP MIB module CISCO-MAU-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MAU-EXT-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:49:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity, Counter32, iso, MibIdentifier, ModuleIdentity, NotificationType, Bits, TimeTicks, Unsigned32, IpAddress, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity", "Counter32", "iso", "MibIdentifier", "ModuleIdentity", "NotificationType", "Bits", "TimeTicks", "Unsigned32", "IpAddress", "Integer32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMauExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 404))
ciscoMauExtCapability.setRevisions(('2008-10-28 00:00', '2004-12-31 00:00',))
if mibBuilder.loadTexts: ciscoMauExtCapability.setLastUpdated('200810280000Z')
if mibBuilder.loadTexts: ciscoMauExtCapability.setOrganization('Cisco Systems, Inc.')
ciscoMauExtCapCatOSV08R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 404, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauExtCapCatOSV08R0401 = ciscoMauExtCapCatOSV08R0401.setProductRelease('Cisco CatOS 8.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauExtCapCatOSV08R0401 = ciscoMauExtCapCatOSV08R0401.setStatus('current')
ciscoMauExtCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 404, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauExtCapV12R0233SXIPCat6K = ciscoMauExtCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauExtCapV12R0233SXIPCat6K = ciscoMauExtCapV12R0233SXIPCat6K.setStatus('current')
mibBuilder.exportSymbols("CISCO-MAU-EXT-CAPABILITY", PYSNMP_MODULE_ID=ciscoMauExtCapability, ciscoMauExtCapability=ciscoMauExtCapability, ciscoMauExtCapCatOSV08R0401=ciscoMauExtCapCatOSV08R0401, ciscoMauExtCapV12R0233SXIPCat6K=ciscoMauExtCapV12R0233SXIPCat6K)
