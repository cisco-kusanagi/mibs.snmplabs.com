#
# PySNMP MIB module CISCO-BRIDGE-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-BRIDGE-EXT-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:34:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
iso, Unsigned32, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, NotificationType, IpAddress, Counter32, Counter64, TimeTicks, ObjectIdentity, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Unsigned32", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "NotificationType", "IpAddress", "Counter32", "Counter64", "TimeTicks", "ObjectIdentity", "Bits", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoBridgeExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 459))
ciscoBridgeExtCapability.setRevisions(('2013-07-26 00:00', '2010-11-18 00:00', '2009-07-24 00:00', '2007-07-03 00:00', '2005-10-20 00:00',))
if mibBuilder.loadTexts: ciscoBridgeExtCapability.setLastUpdated('201307260000Z')
if mibBuilder.loadTexts: ciscoBridgeExtCapability.setOrganization('Cisco Systems, Inc.')
cbeCapV12R0218SXEPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 459, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbeCapV12R0218SXEPCat6K = cbeCapV12R0218SXEPCat6K.setProductRelease('Cisco IOS 12.2(18)SXE on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbeCapV12R0218SXEPCat6K = cbeCapV12R0218SXEPCat6K.setStatus('current')
cbeCapV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 459, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbeCapV12R0233SXHPCat6K = cbeCapV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbeCapV12R0233SXHPCat6K = cbeCapV12R0233SXHPCat6K.setStatus('current')
cbeCapV12R0250SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 459, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbeCapV12R0250SYPCat6K = cbeCapV12R0250SYPCat6K.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbeCapV12R0250SYPCat6K = cbeCapV12R0250SYPCat6K.setStatus('current')
cbeCapNxOSV06R0202PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 459, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbeCapNxOSV06R0202PN7k = cbeCapNxOSV06R0202PN7k.setProductRelease('Cisco NX-OS 6.2(2) on Nexus 7000 \n                        series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbeCapNxOSV06R0202PN7k = cbeCapNxOSV06R0202PN7k.setStatus('current')
mibBuilder.exportSymbols("CISCO-BRIDGE-EXT-CAPABILITY", cbeCapNxOSV06R0202PN7k=cbeCapNxOSV06R0202PN7k, cbeCapV12R0250SYPCat6K=cbeCapV12R0250SYPCat6K, ciscoBridgeExtCapability=ciscoBridgeExtCapability, PYSNMP_MODULE_ID=ciscoBridgeExtCapability, cbeCapV12R0218SXEPCat6K=cbeCapV12R0218SXEPCat6K, cbeCapV12R0233SXHPCat6K=cbeCapV12R0233SXHPCat6K)
