#
# PySNMP MIB module CISCO-SWITCH-FABRIC-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SWITCH-FABRIC-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:56:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier, TimeTicks, ModuleIdentity, ObjectIdentity, Gauge32, iso, Counter32, Unsigned32, Integer32, NotificationType, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "Gauge32", "iso", "Counter32", "Unsigned32", "Integer32", "NotificationType", "Bits", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoSwitchFabricCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 618))
ciscoSwitchFabricCapability.setRevisions(('2014-09-16 00:00', '2013-07-17 00:00', '2013-07-10 00:00',))
if mibBuilder.loadTexts: ciscoSwitchFabricCapability.setLastUpdated('201409160000Z')
if mibBuilder.loadTexts: ciscoSwitchFabricCapability.setOrganization('Cisco Systems, Inc.')
ciscoSwitchFabricCapNxOSV06R0104PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 618, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchFabricCapNxOSV06R0104PN7k = ciscoSwitchFabricCapNxOSV06R0104PN7k.setProductRelease('Cisco NX-OS 6.1(4) on Nexus 7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchFabricCapNxOSV06R0104PN7k = ciscoSwitchFabricCapNxOSV06R0104PN7k.setStatus('current')
ciscoSwitchFabricCapNxOSV06R0201PMds = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 618, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchFabricCapNxOSV06R0201PMds = ciscoSwitchFabricCapNxOSV06R0201PMds.setProductRelease('Cisco NX-OS 6.2(1) on MDS series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchFabricCapNxOSV06R0201PMds = ciscoSwitchFabricCapNxOSV06R0201PMds.setStatus('current')
ciscoSwitchFabricCapV15R0102SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 618, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchFabricCapV15R0102SYPCat6K = ciscoSwitchFabricCapV15R0102SYPCat6K.setProductRelease('Cisco IOS 15.1(2)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchFabricCapV15R0102SYPCat6K = ciscoSwitchFabricCapV15R0102SYPCat6K.setStatus('current')
ciscoSwitchFabricCapNxOSV06R0210PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 618, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchFabricCapNxOSV06R0210PN7k = ciscoSwitchFabricCapNxOSV06R0210PN7k.setProductRelease('Cisco NX-OS 6.2(10) on Nexus 7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchFabricCapNxOSV06R0210PN7k = ciscoSwitchFabricCapNxOSV06R0210PN7k.setStatus('current')
mibBuilder.exportSymbols("CISCO-SWITCH-FABRIC-CAPABILITY", ciscoSwitchFabricCapNxOSV06R0210PN7k=ciscoSwitchFabricCapNxOSV06R0210PN7k, ciscoSwitchFabricCapV15R0102SYPCat6K=ciscoSwitchFabricCapV15R0102SYPCat6K, PYSNMP_MODULE_ID=ciscoSwitchFabricCapability, ciscoSwitchFabricCapability=ciscoSwitchFabricCapability, ciscoSwitchFabricCapNxOSV06R0104PN7k=ciscoSwitchFabricCapNxOSV06R0104PN7k, ciscoSwitchFabricCapNxOSV06R0201PMds=ciscoSwitchFabricCapNxOSV06R0201PMds)
