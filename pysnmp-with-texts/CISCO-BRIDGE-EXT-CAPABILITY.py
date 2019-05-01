#
# PySNMP MIB module CISCO-BRIDGE-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-BRIDGE-EXT-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:51:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Integer32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, IpAddress, iso, ModuleIdentity, Unsigned32, MibIdentifier, ObjectIdentity, TimeTicks, Gauge32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "IpAddress", "iso", "ModuleIdentity", "Unsigned32", "MibIdentifier", "ObjectIdentity", "TimeTicks", "Gauge32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoBridgeExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 459))
ciscoBridgeExtCapability.setRevisions(('2013-07-26 00:00', '2010-11-18 00:00', '2009-07-24 00:00', '2007-07-03 00:00', '2005-10-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoBridgeExtCapability.setRevisionsDescriptions(('Added capability statement cbeCapNxOSV06R0202PN7k.', 'Added capability statement cbeCapV12R0250SYPCat6K.', 'Added VARIATION for cbeDot1dTpGlobalAgingTime and cbeDot1dTpVlanAgingTime in cbeCapV12R0233SXHPCat6K statement.', 'Added cbeCapV12R0233SXHPCat6K for Cisco IOS 12.2(33)SXH.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoBridgeExtCapability.setLastUpdated('201307260000Z')
if mibBuilder.loadTexts: ciscoBridgeExtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoBridgeExtCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoBridgeExtCapability.setDescription('Agent capabilities for CISCO-BRIDGE-EXT-MIB.')
cbeCapV12R0218SXEPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 459, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbeCapV12R0218SXEPCat6K = cbeCapV12R0218SXEPCat6K.setProductRelease('Cisco IOS 12.2(18)SXE on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbeCapV12R0218SXEPCat6K = cbeCapV12R0218SXEPCat6K.setStatus('current')
if mibBuilder.loadTexts: cbeCapV12R0218SXEPCat6K.setDescription('CISCO-BRIDGE-EXT-MIB agent capabilities.')
cbeCapV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 459, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbeCapV12R0233SXHPCat6K = cbeCapV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbeCapV12R0233SXHPCat6K = cbeCapV12R0233SXHPCat6K.setStatus('current')
if mibBuilder.loadTexts: cbeCapV12R0233SXHPCat6K.setDescription('CISCO-BRIDGE-EXT-MIB agent capabilities.')
cbeCapV12R0250SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 459, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbeCapV12R0250SYPCat6K = cbeCapV12R0250SYPCat6K.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbeCapV12R0250SYPCat6K = cbeCapV12R0250SYPCat6K.setStatus('current')
if mibBuilder.loadTexts: cbeCapV12R0250SYPCat6K.setDescription('CISCO-BRIDGE-EXT-MIB agent capabilities.')
cbeCapNxOSV06R0202PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 459, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbeCapNxOSV06R0202PN7k = cbeCapNxOSV06R0202PN7k.setProductRelease('Cisco NX-OS 6.2(2) on Nexus 7000 \n                        series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbeCapNxOSV06R0202PN7k = cbeCapNxOSV06R0202PN7k.setStatus('current')
if mibBuilder.loadTexts: cbeCapNxOSV06R0202PN7k.setDescription('CISCO-BRIDGE-EXT-MIB agent capabilities.')
mibBuilder.exportSymbols("CISCO-BRIDGE-EXT-CAPABILITY", cbeCapNxOSV06R0202PN7k=cbeCapNxOSV06R0202PN7k, cbeCapV12R0250SYPCat6K=cbeCapV12R0250SYPCat6K, cbeCapV12R0233SXHPCat6K=cbeCapV12R0233SXHPCat6K, ciscoBridgeExtCapability=ciscoBridgeExtCapability, cbeCapV12R0218SXEPCat6K=cbeCapV12R0218SXEPCat6K, PYSNMP_MODULE_ID=ciscoBridgeExtCapability)
