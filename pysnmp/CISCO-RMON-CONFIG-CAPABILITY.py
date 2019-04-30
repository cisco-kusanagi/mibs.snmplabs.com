#
# PySNMP MIB module CISCO-RMON-CONFIG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-RMON-CONFIG-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:54:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
IpAddress, Counter32, Gauge32, iso, ModuleIdentity, ObjectIdentity, TimeTicks, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter32", "Gauge32", "iso", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "MibIdentifier", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoRmonConfigCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 346))
ciscoRmonConfigCapability.setRevisions(('2008-10-28 00:00', '2008-05-09 00:00', '2007-06-28 00:00', '2006-01-18 00:00', '2005-08-24 10:00', '2004-03-30 00:00',))
if mibBuilder.loadTexts: ciscoRmonConfigCapability.setLastUpdated('200810280000Z')
if mibBuilder.loadTexts: ciscoRmonConfigCapability.setOrganization('Cisco Systems, Inc.')
ciscoRmonConfigCapV12R0111ECat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 346, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmonConfigCapV12R0111ECat6K = ciscoRmonConfigCapV12R0111ECat6K.setProductRelease('Cisco IOS 12.1(11E) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmonConfigCapV12R0111ECat6K = ciscoRmonConfigCapV12R0111ECat6K.setStatus('current')
ciscoRmonConfigCapCatOSV6R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 346, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmonConfigCapCatOSV6R0301 = ciscoRmonConfigCapCatOSV6R0301.setProductRelease('Cisco CatOS 6.3(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmonConfigCapCatOSV6R0301 = ciscoRmonConfigCapCatOSV6R0301.setStatus('current')
ciscoRmonConfigCapCatOSV08R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 346, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmonConfigCapCatOSV08R0501 = ciscoRmonConfigCapCatOSV08R0501.setProductRelease('Cisco CatOS 8.5(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmonConfigCapCatOSV08R0501 = ciscoRmonConfigCapCatOSV08R0501.setStatus('current')
crcCapV12R0218SXDPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 346, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    crcCapV12R0218SXDPCat6k = crcCapV12R0218SXDPCat6k.setProductRelease('Cisco IOS 12.2(18)SXD on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    crcCapV12R0218SXDPCat6k = crcCapV12R0218SXDPCat6k.setStatus('current')
crcCapV12R0218SXEPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 346, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    crcCapV12R0218SXEPCat6k = crcCapV12R0218SXEPCat6k.setProductRelease('Cisco IOS 12.2(18)SXE on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    crcCapV12R0218SXEPCat6k = crcCapV12R0218SXEPCat6k.setStatus('current')
crcCapV12R0233SXHPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 346, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    crcCapV12R0233SXHPCat6k = crcCapV12R0233SXHPCat6k.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    crcCapV12R0233SXHPCat6k = crcCapV12R0233SXHPCat6k.setStatus('current')
ciscoRmonConfigCapSanOSV34R1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 346, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmonConfigCapSanOSV34R1 = ciscoRmonConfigCapSanOSV34R1.setProductRelease('Cisco SanOS 3.4(1) on MDS9000 Storage Switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmonConfigCapSanOSV34R1 = ciscoRmonConfigCapSanOSV34R1.setStatus('current')
crcCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 346, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    crcCapV12R0233SXIPCat6K = crcCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    crcCapV12R0233SXIPCat6K = crcCapV12R0233SXIPCat6K.setStatus('current')
mibBuilder.exportSymbols("CISCO-RMON-CONFIG-CAPABILITY", crcCapV12R0218SXEPCat6k=crcCapV12R0218SXEPCat6k, ciscoRmonConfigCapCatOSV6R0301=ciscoRmonConfigCapCatOSV6R0301, PYSNMP_MODULE_ID=ciscoRmonConfigCapability, ciscoRmonConfigCapV12R0111ECat6K=ciscoRmonConfigCapV12R0111ECat6K, ciscoRmonConfigCapability=ciscoRmonConfigCapability, ciscoRmonConfigCapSanOSV34R1=ciscoRmonConfigCapSanOSV34R1, crcCapV12R0218SXDPCat6k=crcCapV12R0218SXDPCat6k, crcCapV12R0233SXHPCat6k=crcCapV12R0233SXHPCat6k, crcCapV12R0233SXIPCat6K=crcCapV12R0233SXIPCat6K, ciscoRmonConfigCapCatOSV08R0501=ciscoRmonConfigCapCatOSV08R0501)
