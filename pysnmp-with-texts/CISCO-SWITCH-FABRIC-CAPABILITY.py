#
# PySNMP MIB module CISCO-SWITCH-FABRIC-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SWITCH-FABRIC-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:13:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Bits, TimeTicks, ObjectIdentity, MibIdentifier, Gauge32, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Unsigned32, Counter32, IpAddress, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "ObjectIdentity", "MibIdentifier", "Gauge32", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Unsigned32", "Counter32", "IpAddress", "Integer32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoSwitchFabricCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 618))
ciscoSwitchFabricCapability.setRevisions(('2014-09-16 00:00', '2013-07-17 00:00', '2013-07-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSwitchFabricCapability.setRevisionsDescriptions(('Added capability statement ciscoSwitchFabricCapNxOSV06R0210PN7k.', 'Added capability statement ciscoSwitchFabricCapV15R0102SYPCat6K.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSwitchFabricCapability.setLastUpdated('201409160000Z')
if mibBuilder.loadTexts: ciscoSwitchFabricCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSwitchFabricCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSwitchFabricCapability.setDescription('The capabilities description of CISCO-SWITCH-FABRIC-MIB.')
ciscoSwitchFabricCapNxOSV06R0104PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 618, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchFabricCapNxOSV06R0104PN7k = ciscoSwitchFabricCapNxOSV06R0104PN7k.setProductRelease('Cisco NX-OS 6.1(4) on Nexus 7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchFabricCapNxOSV06R0104PN7k = ciscoSwitchFabricCapNxOSV06R0104PN7k.setStatus('current')
if mibBuilder.loadTexts: ciscoSwitchFabricCapNxOSV06R0104PN7k.setDescription('CISCO-SWITCH-FABRIC-MIB capabilities.')
ciscoSwitchFabricCapNxOSV06R0201PMds = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 618, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchFabricCapNxOSV06R0201PMds = ciscoSwitchFabricCapNxOSV06R0201PMds.setProductRelease('Cisco NX-OS 6.2(1) on MDS series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchFabricCapNxOSV06R0201PMds = ciscoSwitchFabricCapNxOSV06R0201PMds.setStatus('current')
if mibBuilder.loadTexts: ciscoSwitchFabricCapNxOSV06R0201PMds.setDescription('CISCO-SWITCH-FABRIC-MIB capabilities.')
ciscoSwitchFabricCapV15R0102SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 618, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchFabricCapV15R0102SYPCat6K = ciscoSwitchFabricCapV15R0102SYPCat6K.setProductRelease('Cisco IOS 15.1(2)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchFabricCapV15R0102SYPCat6K = ciscoSwitchFabricCapV15R0102SYPCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoSwitchFabricCapV15R0102SYPCat6K.setDescription('CISCO-SWITCH-FABRIC-MIB capabilities.')
ciscoSwitchFabricCapNxOSV06R0210PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 618, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchFabricCapNxOSV06R0210PN7k = ciscoSwitchFabricCapNxOSV06R0210PN7k.setProductRelease('Cisco NX-OS 6.2(10) on Nexus 7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchFabricCapNxOSV06R0210PN7k = ciscoSwitchFabricCapNxOSV06R0210PN7k.setStatus('current')
if mibBuilder.loadTexts: ciscoSwitchFabricCapNxOSV06R0210PN7k.setDescription('CISCO-SWITCH-FABRIC-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SWITCH-FABRIC-CAPABILITY", ciscoSwitchFabricCapability=ciscoSwitchFabricCapability, PYSNMP_MODULE_ID=ciscoSwitchFabricCapability, ciscoSwitchFabricCapNxOSV06R0210PN7k=ciscoSwitchFabricCapNxOSV06R0210PN7k, ciscoSwitchFabricCapNxOSV06R0104PN7k=ciscoSwitchFabricCapNxOSV06R0104PN7k, ciscoSwitchFabricCapV15R0102SYPCat6K=ciscoSwitchFabricCapV15R0102SYPCat6K, ciscoSwitchFabricCapNxOSV06R0201PMds=ciscoSwitchFabricCapNxOSV06R0201PMds)
