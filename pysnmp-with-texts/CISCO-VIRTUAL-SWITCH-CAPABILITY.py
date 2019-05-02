#
# PySNMP MIB module CISCO-VIRTUAL-SWITCH-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VIRTUAL-SWITCH-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:18:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, Unsigned32, ObjectIdentity, Integer32, Counter32, TimeTicks, Counter64, NotificationType, ModuleIdentity, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "Unsigned32", "ObjectIdentity", "Integer32", "Counter32", "TimeTicks", "Counter64", "NotificationType", "ModuleIdentity", "Gauge32", "iso")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
ciscoVirtualSwitchCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 563))
ciscoVirtualSwitchCapability.setRevisions(('2012-09-07 00:00', '2011-09-26 00:00', '2010-03-29 00:00', '2008-01-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVirtualSwitchCapability.setRevisionsDescriptions(('Added capability statement cvsCapV15R0101SYPCat6K.', 'Added capability statement cvsCapV15R0001SYPCat6K.', 'Added capability statement cvsCapV12R0233SXI4PCat6K.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoVirtualSwitchCapability.setLastUpdated('201209070000Z')
if mibBuilder.loadTexts: ciscoVirtualSwitchCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVirtualSwitchCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoVirtualSwitchCapability.setDescription('The Agent capabilities for CISCO-VIRTUAL-SWITCH-MIB.')
cvsCapV12R0233SXH01PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 563, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsCapV12R0233SXH01PCat6K = cvsCapV12R0233SXH01PCat6K.setProductRelease('Cisco IOS 12.2(33)SXH1 on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsCapV12R0233SXH01PCat6K = cvsCapV12R0233SXH01PCat6K.setStatus('current')
if mibBuilder.loadTexts: cvsCapV12R0233SXH01PCat6K.setDescription('CISCO-VIRTUAL-SWITCH-MIB capabilities.')
cvsCapV12R0233SXI4PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 563, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsCapV12R0233SXI4PCat6K = cvsCapV12R0233SXI4PCat6K.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsCapV12R0233SXI4PCat6K = cvsCapV12R0233SXI4PCat6K.setStatus('current')
if mibBuilder.loadTexts: cvsCapV12R0233SXI4PCat6K.setDescription('CISCO-VIRTUAL-SWITCH-MIB capabilities.')
cvsCapV15R0001SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 563, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsCapV15R0001SYPCat6K = cvsCapV15R0001SYPCat6K.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsCapV15R0001SYPCat6K = cvsCapV15R0001SYPCat6K.setStatus('current')
if mibBuilder.loadTexts: cvsCapV15R0001SYPCat6K.setDescription('CISCO-VIRTUAL-SWITCH-MIB capabilities.')
cvsCapV15R0101SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 563, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsCapV15R0101SYPCat6K = cvsCapV15R0101SYPCat6K.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvsCapV15R0101SYPCat6K = cvsCapV15R0101SYPCat6K.setStatus('current')
if mibBuilder.loadTexts: cvsCapV15R0101SYPCat6K.setDescription('CISCO-VIRTUAL-SWITCH-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-VIRTUAL-SWITCH-CAPABILITY", cvsCapV15R0001SYPCat6K=cvsCapV15R0001SYPCat6K, ciscoVirtualSwitchCapability=ciscoVirtualSwitchCapability, cvsCapV15R0101SYPCat6K=cvsCapV15R0101SYPCat6K, PYSNMP_MODULE_ID=ciscoVirtualSwitchCapability, cvsCapV12R0233SXI4PCat6K=cvsCapV12R0233SXI4PCat6K, cvsCapV12R0233SXH01PCat6K=cvsCapV12R0233SXH01PCat6K)
