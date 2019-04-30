#
# PySNMP MIB module CISCO-BRIDGE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-BRIDGE-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:34:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Bits, iso, Gauge32, TimeTicks, NotificationType, MibIdentifier, ModuleIdentity, IpAddress, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "Gauge32", "TimeTicks", "NotificationType", "MibIdentifier", "ModuleIdentity", "IpAddress", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoBridgeCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 106))
ciscoBridgeCapability.setRevisions(('2014-09-18 00:00', '2013-07-16 00:00', '2011-07-26 00:00', '2010-12-01 00:00', '2010-11-18 00:00', '2010-09-09 00:00', '2010-06-10 00:00', '2010-03-02 00:00', '2007-03-28 00:00', '2006-06-12 00:00', '1994-08-18 00:00',))
if mibBuilder.loadTexts: ciscoBridgeCapability.setLastUpdated('201409180000Z')
if mibBuilder.loadTexts: ciscoBridgeCapability.setOrganization('Cisco Systems, Inc.')
ciscoBridgeCapCatOSV08R0601 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 106, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBridgeCapCatOSV08R0601 = ciscoBridgeCapCatOSV08R0601.setProductRelease('Cisco CatOS 8.6(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBridgeCapCatOSV08R0601 = ciscoBridgeCapCatOSV08R0601.setStatus('current')
ciscoBridgeCapV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 106, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBridgeCapV12R0233SXHPCat6K = ciscoBridgeCapV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBridgeCapV12R0233SXHPCat6K = ciscoBridgeCapV12R0233SXHPCat6K.setStatus('current')
ciscoBridgeCapNxOSV04R0201N0101PN5k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 106, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBridgeCapNxOSV04R0201N0101PN5k = ciscoBridgeCapNxOSV04R0201N0101PN5k.setProductRelease('Cisco NX-OS 4.2(1)N1(1) on Nexus 5000\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBridgeCapNxOSV04R0201N0101PN5k = ciscoBridgeCapNxOSV04R0201N0101PN5k.setStatus('current')
ciscoBridgeCapNxOSV05R0002PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 106, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBridgeCapNxOSV05R0002PN7k = ciscoBridgeCapNxOSV05R0002PN7k.setProductRelease('Cisco NX-OS 5.0(2) on Nexus 7000\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBridgeCapNxOSV05R0002PN7k = ciscoBridgeCapNxOSV05R0002PN7k.setStatus('current')
ciscoBridgeCapV12R2SEPCat3K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 106, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBridgeCapV12R2SEPCat3K = ciscoBridgeCapV12R2SEPCat3K.setProductRelease('Cisco IOS 12.2SE on Catalyst 3K\n                        series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBridgeCapV12R2SEPCat3K = ciscoBridgeCapV12R2SEPCat3K.setStatus('current')
ciscoBridgeCapNxOSV05R0101PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 106, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBridgeCapNxOSV05R0101PN7k = ciscoBridgeCapNxOSV05R0101PN7k.setProductRelease('Cisco NX-OS 5.1(1) on Nexus 7000\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBridgeCapNxOSV05R0101PN7k = ciscoBridgeCapNxOSV05R0101PN7k.setStatus('current')
ciscoBridgeCapV12R4SEPC1861 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 106, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBridgeCapV12R4SEPC1861 = ciscoBridgeCapV12R4SEPC1861.setProductRelease('OS=IOS\n                     OSVERSION=Cisco IOS 12.4,15.1T\n                     PLATFORM=c1861')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBridgeCapV12R4SEPC1861 = ciscoBridgeCapV12R4SEPC1861.setStatus('current')
ciscoBridgeCapNxOSV05R0201PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 106, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBridgeCapNxOSV05R0201PN7k = ciscoBridgeCapNxOSV05R0201PN7k.setProductRelease('Cisco NX-OS 5.2(1) on Nexus 7000\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBridgeCapNxOSV05R0201PN7k = ciscoBridgeCapNxOSV05R0201PN7k.setStatus('current')
ciscoBridgeCapNxOSV06R0201PMds = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 106, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBridgeCapNxOSV06R0201PMds = ciscoBridgeCapNxOSV06R0201PMds.setProductRelease('Cisco NX-OS 6.2(1) on MDS 9700\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBridgeCapNxOSV06R0201PMds = ciscoBridgeCapNxOSV06R0201PMds.setStatus('current')
mibBuilder.exportSymbols("CISCO-BRIDGE-CAPABILITY", ciscoBridgeCapNxOSV04R0201N0101PN5k=ciscoBridgeCapNxOSV04R0201N0101PN5k, ciscoBridgeCapNxOSV05R0101PN7k=ciscoBridgeCapNxOSV05R0101PN7k, ciscoBridgeCapV12R0233SXHPCat6K=ciscoBridgeCapV12R0233SXHPCat6K, PYSNMP_MODULE_ID=ciscoBridgeCapability, ciscoBridgeCapV12R4SEPC1861=ciscoBridgeCapV12R4SEPC1861, ciscoBridgeCapV12R2SEPCat3K=ciscoBridgeCapV12R2SEPCat3K, ciscoBridgeCapCatOSV08R0601=ciscoBridgeCapCatOSV08R0601, ciscoBridgeCapNxOSV06R0201PMds=ciscoBridgeCapNxOSV06R0201PMds, ciscoBridgeCapNxOSV05R0201PN7k=ciscoBridgeCapNxOSV05R0201PN7k, ciscoBridgeCapNxOSV05R0002PN7k=ciscoBridgeCapNxOSV05R0002PN7k, ciscoBridgeCapability=ciscoBridgeCapability)
