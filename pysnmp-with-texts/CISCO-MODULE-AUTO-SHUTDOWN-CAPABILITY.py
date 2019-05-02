#
# PySNMP MIB module CISCO-MODULE-AUTO-SHUTDOWN-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MODULE-AUTO-SHUTDOWN-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:07:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, Integer32, Gauge32, IpAddress, Unsigned32, ModuleIdentity, NotificationType, Counter32, Bits, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "Gauge32", "IpAddress", "Unsigned32", "ModuleIdentity", "NotificationType", "Counter32", "Bits", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "iso", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cmAutoShutdownCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 386))
cmAutoShutdownCapability.setRevisions(('2008-10-29 00:00', '2004-01-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cmAutoShutdownCapability.setRevisionsDescriptions(('Add the capability statements cmAutoShutdownCapV12R0233SXH3PCat6K and cmAutoShutdownCapV12R0233SXIPCat6K.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: cmAutoShutdownCapability.setLastUpdated('200810290000Z')
if mibBuilder.loadTexts: cmAutoShutdownCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cmAutoShutdownCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: cmAutoShutdownCapability.setDescription('The capabilities description of CISCO-MODULE-AUTO-SHUTDOWN-MIB.')
cmAutoShutdownCapCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 386, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmAutoShutdownCapCatOSV08R0301 = cmAutoShutdownCapCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                    and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmAutoShutdownCapCatOSV08R0301 = cmAutoShutdownCapCatOSV08R0301.setStatus('current')
if mibBuilder.loadTexts: cmAutoShutdownCapCatOSV08R0301.setDescription('CISCO-MODULE-AUTO-SHUTDOWN-MIB capabilities.')
cmAutoShutdownCapV12R0233SXH3PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 386, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmAutoShutdownCapV12R0233SXH3PCat6K = cmAutoShutdownCapV12R0233SXH3PCat6K.setProductRelease('Cisco IOS 12.2(33)SXH3 on Catalyst 6000/6500\n                        series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmAutoShutdownCapV12R0233SXH3PCat6K = cmAutoShutdownCapV12R0233SXH3PCat6K.setStatus('current')
if mibBuilder.loadTexts: cmAutoShutdownCapV12R0233SXH3PCat6K.setDescription('CISCO-MODULE-AUTO-SHUTDOWN-MIB capabilities.')
cmAutoShutdownCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 386, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmAutoShutdownCapV12R0233SXIPCat6K = cmAutoShutdownCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                        series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmAutoShutdownCapV12R0233SXIPCat6K = cmAutoShutdownCapV12R0233SXIPCat6K.setStatus('current')
if mibBuilder.loadTexts: cmAutoShutdownCapV12R0233SXIPCat6K.setDescription('CISCO-MODULE-AUTO-SHUTDOWN-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-MODULE-AUTO-SHUTDOWN-CAPABILITY", cmAutoShutdownCapCatOSV08R0301=cmAutoShutdownCapCatOSV08R0301, cmAutoShutdownCapability=cmAutoShutdownCapability, cmAutoShutdownCapV12R0233SXH3PCat6K=cmAutoShutdownCapV12R0233SXH3PCat6K, PYSNMP_MODULE_ID=cmAutoShutdownCapability, cmAutoShutdownCapV12R0233SXIPCat6K=cmAutoShutdownCapV12R0233SXIPCat6K)
