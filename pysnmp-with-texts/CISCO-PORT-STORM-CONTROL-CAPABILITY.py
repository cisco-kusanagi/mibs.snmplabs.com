#
# PySNMP MIB module CISCO-PORT-STORM-CONTROL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-PORT-STORM-CONTROL-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:09:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
iso, Bits, ModuleIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, Counter32, ObjectIdentity, MibIdentifier, NotificationType, TimeTicks, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "ModuleIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "Counter32", "ObjectIdentity", "MibIdentifier", "NotificationType", "TimeTicks", "Counter64", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoPortStormControlCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 542))
ciscoPortStormControlCapability.setRevisions(('2014-04-04 00:00', '2012-09-07 00:00', '2011-03-24 00:00', '2007-07-03 00:00', '2007-07-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoPortStormControlCapability.setRevisionsDescriptions(('Added capability statement cpscCapabilityV06R0002U0301PN3K.', 'Added capability statement cpscCapabilityV15R0101SYPCat6k.', 'Added capability statement cpscCapabilityV12R0233SXJPCat6k.', 'Added capability statement cpscCapabilityV12R0233SXHPCat6K.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoPortStormControlCapability.setLastUpdated('201404040000Z')
if mibBuilder.loadTexts: ciscoPortStormControlCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoPortStormControlCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoPortStormControlCapability.setDescription('Agent capabilities for CISCO-PORT-STORM-CONTROL-MIB.')
cpscCapabilityV12R0240SGCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 542, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscCapabilityV12R0240SGCat4K = cpscCapabilityV12R0240SGCat4K.setProductRelease('Cisco IOS 12.2(40)SG on Cat4K platform')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscCapabilityV12R0240SGCat4K = cpscCapabilityV12R0240SGCat4K.setStatus('current')
if mibBuilder.loadTexts: cpscCapabilityV12R0240SGCat4K.setDescription('CISCO-PORT-STORM-CONTROL-MIB capabilities')
cpscCapabilityV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 542, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscCapabilityV12R0233SXHPCat6K = cpscCapabilityV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscCapabilityV12R0233SXHPCat6K = cpscCapabilityV12R0233SXHPCat6K.setStatus('current')
if mibBuilder.loadTexts: cpscCapabilityV12R0233SXHPCat6K.setDescription('CISCO-PORT-STORM-CONTROL-MIB capabilities.')
cpscCapabilityV12R0233SXJPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 542, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscCapabilityV12R0233SXJPCat6k = cpscCapabilityV12R0233SXJPCat6k.setProductRelease('Cisco IOS 12.2(33)SXJ on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscCapabilityV12R0233SXJPCat6k = cpscCapabilityV12R0233SXJPCat6k.setStatus('current')
if mibBuilder.loadTexts: cpscCapabilityV12R0233SXJPCat6k.setDescription('CISCO-PORT-STORM-CONTROL-MIB capabilities.')
cpscCapabilityV15R0101SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 542, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscCapabilityV15R0101SYPCat6k = cpscCapabilityV15R0101SYPCat6k.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscCapabilityV15R0101SYPCat6k = cpscCapabilityV15R0101SYPCat6k.setStatus('current')
if mibBuilder.loadTexts: cpscCapabilityV15R0101SYPCat6k.setDescription('CISCO-PORT-STORM-CONTROL-MIB capabilities.')
cpscCapabilityV06R0002U0301PN3K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 542, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscCapabilityV06R0002U0301PN3K = cpscCapabilityV06R0002U0301PN3K.setProductRelease('Cisco NX-OS 6.0(2)U3(1) on Nexus 3000.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpscCapabilityV06R0002U0301PN3K = cpscCapabilityV06R0002U0301PN3K.setStatus('current')
if mibBuilder.loadTexts: cpscCapabilityV06R0002U0301PN3K.setDescription('CISCO-PORT-STORM-CONTROL-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-PORT-STORM-CONTROL-CAPABILITY", cpscCapabilityV12R0240SGCat4K=cpscCapabilityV12R0240SGCat4K, cpscCapabilityV06R0002U0301PN3K=cpscCapabilityV06R0002U0301PN3K, cpscCapabilityV15R0101SYPCat6k=cpscCapabilityV15R0101SYPCat6k, PYSNMP_MODULE_ID=ciscoPortStormControlCapability, ciscoPortStormControlCapability=ciscoPortStormControlCapability, cpscCapabilityV12R0233SXJPCat6k=cpscCapabilityV12R0233SXJPCat6k, cpscCapabilityV12R0233SXHPCat6K=cpscCapabilityV12R0233SXHPCat6K)
